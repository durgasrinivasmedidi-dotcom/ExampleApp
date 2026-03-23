# Quick Start Guide - Todo App

## Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python ExampleApp.py
```

### Step 3: Open in Browser
Navigate to `http://localhost:5000`

### Step 4: Start Using!
- Click "+ Add New Todo" to create your first task
- Check off tasks as you complete them
- Edit or delete tasks as needed

## Features at a Glance

| Feature | How to Use |
|---------|-----------|
| Add Todo | Click "+ Add New Todo" button |
| Mark Complete | Click the checkbox on a todo |
| Edit | Click the "Edit" button |
| Delete | Click the "Delete" button |
| View Stats | Check the stat cards at the top |

## Common Tasks

### Add a Todo
1. Click "+ Add New Todo"
2. Enter a title (required)
3. Add description (optional)
4. Set due date (optional)
5. Click "Add Todo"

### Check Off a Completed Task
1. Find the todo in the list
2. Click the checkbox
3. Task will immediately mark as complete

### Edit a Todo
1. Find the todo you want to edit
2. Click the "Edit" button
3. Modify the information
4. Click "Update Todo"

### Delete a Todo
1. Find the todo to delete
2. Click the "Delete" button
3. Confirm the deletion

## Tips

- **Organized Lists**: Add clear, specific descriptions to help you remember what each task is about
- **Due Dates**: Set due dates to prioritize your tasks
- **Quick Completion**: Use the checkbox to quickly mark tasks as complete without opening the edit page
- **Statistics**: Keep an eye on the stat cards to track your productivity

## Keyboard Shortcuts

- **Auto-focus**: The title field is auto-focused when adding/editing todos
- **Tab Navigation**: Use Tab to move between form fields

## Troubleshooting

### App won't start?
- Make sure Python 3.7+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`

### Can't access the app?
- Check if port 5000 is free
- Look for error messages in the terminal
- Make sure the Flask server is running

### Lost my todos?
- Check if `todo.db` file exists in the project folder
- Delete `todo.db` to start fresh (warning: this clears all todos)

## Next Steps

- Customize colors in `static/style.css`
- Add more fields to todos in `ExampleApp.py`
- Deploy to the cloud (Heroku, AWS, etc.)
- Add user authentication
