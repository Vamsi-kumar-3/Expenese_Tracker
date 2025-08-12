# Flask Expense Tracker - VS Code Setup Guide

This guide will help you set up and run the Flask Expense Tracker application in VS Code.

## 🚀 Quick Start

### 1. Extract and Open in VS Code
```bash
# Extract the zip file
unzip expense_tracker_vscode.zip
cd expense_tracker

# Open in VS Code
code .
```

### 2. Set Up Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements-dev.txt
```

### 4. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings (optional for development)
```

### 5. Run the Application

**Option A: Using the VS Code debugger**
- Press `F5` or go to Run → Start Debugging
- Select "Flask App" configuration

**Option B: Using the development runner**
```bash
python run.py
```

**Option C: Using Flask directly**
```bash
flask --app main run --debug
```

**Option D: Using Gunicorn (production-like)**
```bash
gunicorn --bind 127.0.0.1:5000 --reload main:app
```

### 6. Access the Application
Open your browser and go to: `http://127.0.0.1:5000`

## 🛠️ VS Code Configuration

### Recommended Extensions
Install these VS Code extensions for the best development experience:

1. **Python** - Python language support
2. **Pylance** - Advanced Python language features
3. **Jinja** - Jinja2 template syntax highlighting
4. **Thunder Client** - API testing (optional)
5. **SQLite Viewer** - View SQLite database files
6. **GitLens** - Git integration (if using version control)

### Configured Features
- **Debug Configuration**: Pre-configured Flask debugging
- **Python Linting**: Flake8 for code quality
- **File Associations**: HTML templates recognized as Jinja2
- **Auto-formatting**: Black formatter configured
- **Environment**: Automatic virtual environment activation

## 📁 Project Structure

```
expense_tracker/
├── .vscode/                 # VS Code configuration
│   ├── settings.json       # Editor settings
│   └── launch.json         # Debug configurations
├── static/                 # Static files (CSS, JS, images)
├── templates/              # Jinja2 HTML templates
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── app.py                 # Flask application setup
├── main.py                # Application entry point
├── run.py                 # Development runner
├── models.py              # Database models
├── routes.py              # Application routes
├── forms.py               # WTForms definitions
├── utils.py               # Utility functions
├── requirements-dev.txt   # Python dependencies
├── README.md              # Project documentation
└── SETUP_GUIDE.md         # This file
```

## 🗃️ Database Setup

### Default (SQLite)
The application will automatically create a SQLite database file (`expense_tracker.db`) on first run.

### PostgreSQL (Optional)
1. Install PostgreSQL
2. Create a database: `createdb expense_tracker`
3. Update `.env` file:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/expense_tracker
   ```

## 🔧 Development Workflow

### 1. Making Changes
- Edit Python files: Changes are automatically reloaded in debug mode
- Edit templates: Refresh browser to see changes
- Edit static files: Refresh browser (may need hard refresh)

### 2. Debugging
- Set breakpoints in VS Code by clicking line numbers
- Use `F5` to start debugging
- Variables and call stack are shown in the debug panel

### 3. Database Operations
- View SQLite database: Use SQLite Viewer extension
- Reset database: Delete `expense_tracker.db` and restart app

### 4. Testing Features
1. Register a new user account
2. Log in with credentials
3. Add expense categories
4. Create expenses
5. View dashboard with charts
6. Filter and export data

## 🚨 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
# Or change port in .env file
```

**Module not found**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements-dev.txt
```

**Database errors**
```bash
# Reset database
rm expense_tracker.db
python run.py
```

**VS Code not recognizing Python**
- Press `Ctrl+Shift+P`
- Type "Python: Select Interpreter"
- Choose the interpreter from your virtual environment

### Environment Variables
Create a `.env` file with these variables:
```
FLASK_APP=main.py
FLASK_ENV=development
FLASK_DEBUG=True
SESSION_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///expense_tracker.db
HOST=127.0.0.1
PORT=5000
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)

## 🎯 Next Steps

1. **Customize the application**: Modify templates, add features, change styling
2. **Add tests**: Create unit tests for your routes and models
3. **Deploy**: Deploy to platforms like Heroku, AWS, or DigitalOcean
4. **Version control**: Initialize git repository and commit your changes

Happy coding! 🚀