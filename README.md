# Todo App - Flask Application

A simple, elegant todo application built with Flask and SQLAlchemy. Features a modern UI with full CRUD operations for managing tasks.

## Features

- ✅ **Create** - Add new todos with title, description, and due date
- ✅ **Read** - View all todos with statistics
- ✅ **Update** - Edit existing todos
- ✅ **Delete** - Remove completed or unwanted todos
- ✅ **Complete/Incomplete** - Mark todos as done with real-time updates
- 📊 **Statistics** - View total and completed task counts
- 🎨 **Responsive Design** - Works on desktop, tablet, and mobile
- 🗄️ **Database** - SQLite database for persistent storage

## Project Structure

```
ExampleApp/
├── ExampleApp.py          # Main Flask application
├── requirements.txt       # Python dependencies
├── todo.db               # SQLite database (auto-created)
├── templates/            # HTML templates
│   ├── index.html        # Main page with todo list
│   ├── add_todo.html     # Add new todo form
│   ├── edit_todo.html    # Edit todo form
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── static/               # Static files
    └── style.css         # CSS styling
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd ExampleApp
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python ExampleApp.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Add a Todo**
   - Click the "+ Add New Todo" button
   - Enter a title (required), description (optional), and due date (optional)
   - Click "Add Todo"

2. **View Todos**
   - All todos are displayed on the main page
   - Statistics show total and completed tasks

3. **Complete a Todo**
   - Click the checkbox next to a todo to mark it as complete/incomplete
   - The update happens in real-time

4. **Edit a Todo**
   - Click the "Edit" button on any todo
   - Modify the title, description, or due date
   - Click "Update Todo"

5. **Delete a Todo**
   - Click the "Delete" button on any todo
   - Confirm the deletion

## API Endpoints

- `GET /` - Display all todos
- `GET /add` - Show add todo form
- `POST /add` - Create a new todo
- `GET /edit/<todo_id>` - Show edit todo form
- `POST /edit/<todo_id>` - Update a todo
- `POST /delete/<todo_id>` - Delete a todo
- `POST /toggle/<todo_id>` - Toggle todo completion status (returns JSON)
- `GET /api/todos` - Get all todos as JSON

## Database Schema

### Todo Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| title | String(200) | Todo title (required) |
| description | Text | Todo description (optional) |
| completed | Boolean | Completion status (default: False) |
| created_at | DateTime | Creation timestamp |
| due_date | Date | Due date (optional) |

## Customization

### Change Port
Edit the last line in `ExampleApp.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port to desired number
```

### Modify Styling
Edit `static/style.css` to customize colors, fonts, and layout.

### Change Database
By default, SQLite (`todo.db`) is used. To use a different database, modify the configuration in `ExampleApp.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
python ExampleApp.py --port 5001
```

Or change the port in the code.

### Database Reset
To reset the database, simply delete the `todo.db` file and restart the application.

### Module Not Found
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Technologies Used

- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **HTML/CSS** - Frontend
- **JavaScript** - Interactive features

## Development

To enable debug mode with auto-reload on file changes:
```bash
export FLASK_ENV=development
export FLASK_APP=ExampleApp.py
flask run
```

## License

This project is open source and available for personal and educational use.

## Author

Created as a simple Todo App example using Flask.
