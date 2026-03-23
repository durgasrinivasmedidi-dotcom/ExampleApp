from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Todo {self.id}: {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None
        }

# Routes
@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    completed_count = Todo.query.filter_by(completed=True).count()
    total_count = Todo.query.count()
    return render_template('index.html', todos=todos, completed_count=completed_count, total_count=total_count)

@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date = request.form.get('due_date')

        if not title:
            return redirect(url_for('index'))

        try:
            new_todo = Todo(title=title, description=description)
            if due_date:
                from datetime import datetime
                new_todo.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            
            db.session.add(new_todo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error adding todo: {e}")

        return redirect(url_for('index'))

    return render_template('add_todo.html')

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    
    if request.method == 'POST':
        todo.title = request.form.get('title', todo.title)
        todo.description = request.form.get('description', todo.description)
        due_date = request.form.get('due_date')
        
        if due_date:
            from datetime import datetime
            todo.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error updating todo: {e}")

        return redirect(url_for('index'))

    return render_template('edit_todo.html', todo=todo)

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    
    try:
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting todo: {e}")

    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    
    try:
        todo.completed = not todo.completed
        db.session.commit()
        return jsonify({'success': True, 'completed': todo.completed})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
