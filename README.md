# Expense Tracker - Flask Web Application

A comprehensive expense tracking web application built with Flask that allows users to manage their personal finances by recording, categorizing, and analyzing expenses.

## Features

### Core Features
- **User Authentication**: Secure signup, login, and logout with password hashing
- **Expense Management**: Add, edit, delete, and view expenses with categories
- **Category System**: Manage custom expense categories
- **Dashboard**: Overview with total expenses, monthly summaries, and visual charts
- **Data Visualization**: Interactive charts showing spending by category and monthly trends
- **Filtering**: Filter expenses by date range and category
- **Reports**: Monthly expense summaries and analytics
- **Data Export**: Export expense data to CSV format

### Technical Features
- **Responsive Design**: Mobile-first design with Bootstrap 5
- **Dark Theme**: Professional dark theme interface
- **Data Persistence**: PostgreSQL/SQLite database support
- **Form Validation**: Server-side validation with WTForms
- **Session Management**: Secure user sessions with Flask-Login
- **CSRF Protection**: Built-in security features

## Project Structure

```
expense_tracker/
├── app.py                 # Flask application setup and configuration
├── main.py               # Application entry point
├── models.py             # Database models (User, Category, Expense)
├── routes.py             # Application routes and view functions
├── forms.py              # WTForms for form handling and validation
├── utils.py              # Utility functions for data processing
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Landing page
│   ├── login.html       # User login form
│   ├── register.html    # User registration form
│   ├── dashboard.html   # Main dashboard with charts
│   ├── expenses.html    # Expense listing with filters
│   ├── add_expense.html # Add new expense form
│   ├── edit_expense.html# Edit expense form
│   ├── categories.html  # Category management
│   └── reports.html     # Monthly reports
├── static/              # Static assets
│   ├── css/
│   │   └── custom.css   # Custom styling
│   └── js/
│       └── dashboard.js # Chart.js configuration
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

## Installation and Setup

### Requirements
- Python 3.11+
- PostgreSQL (optional, SQLite works as fallback)

### Installation Steps

1. **Extract the project files**
   ```bash
   unzip expense_tracker_clean.zip
   cd expense_tracker
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using the modern approach:
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-wtf wtforms gunicorn psycopg2-binary email-validator werkzeug sqlalchemy
   ```

3. **Set environment variables**
   ```bash
   # For development (optional)
   export SESSION_SECRET="your-secret-key-here"
   export DATABASE_URL="sqlite:///expense_tracker.db"
   
   # For PostgreSQL
   export DATABASE_URL="postgresql://username:password@localhost/expense_tracker"
   ```

4. **Run the application**
   ```bash
   # Development mode
   python app.py
   
   # Production mode with Gunicorn
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Usage Instructions

### Getting Started
1. **Create an Account**: Visit the homepage and click "Sign Up" to create a new account
2. **Login**: Use your credentials to log into the application
3. **Add Categories**: Start by adding expense categories (Food, Transport, etc.)
4. **Record Expenses**: Add your first expense with amount, category, date, and description

### Using the Dashboard
- **Overview Cards**: View total expenses, monthly spending, and recent activity
- **Charts**: Visual representation of spending by category and monthly trends
- **Recent Expenses**: Quick view of your latest transactions

### Managing Expenses
- **Add Expense**: Click "Add Expense" to record new transactions
- **Edit/Delete**: Use the actions in the expense list to modify or remove entries
- **Filter**: Use date ranges and categories to find specific expenses
- **Export**: Download your expense data as CSV for external analysis

### Reports and Analytics
- **Monthly Reports**: View detailed monthly breakdowns with statistics
- **Category Analysis**: See spending distribution across different categories
- **Trends**: Track spending patterns over time with interactive charts

## Default Test Data

The application comes with default categories:
- Food
- Transport
- Utilities
- Entertainment
- Healthcare
- Shopping
- Other

## Configuration

### Database Configuration
- **SQLite** (default): Automatically creates `expense_tracker.db` file
- **PostgreSQL**: Set `DATABASE_URL` environment variable

### Security Configuration
- Set `SESSION_SECRET` environment variable for secure sessions
- CSRF protection is enabled by default
- Passwords are hashed using Werkzeug security functions

## Technology Stack

### Backend
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **WTForms**: Form handling and validation
- **Gunicorn**: WSGI HTTP Server

### Frontend
- **Bootstrap 5**: CSS framework with dark theme
- **Chart.js**: Interactive charts and data visualization
- **Font Awesome**: Icon library
- **Jinja2**: Template engine

### Database
- **PostgreSQL**: Primary database (production)
- **SQLite**: Fallback database (development)

## Deployment

### Local Development
1. Use the built-in Flask development server
2. Set `DEBUG=True` for development features

### Production Deployment
1. Use Gunicorn or similar WSGI server
2. Set up PostgreSQL database
3. Configure environment variables
4. Use reverse proxy (nginx) for static files

### Replit Deployment
The application is optimized for Replit deployment:
1. Upload the project files
2. Set environment variables in Replit secrets
3. Run with the provided configuration

## Security Features

- **Password Hashing**: Werkzeug password hashing
- **Session Management**: Flask-Login secure sessions
- **CSRF Protection**: WTForms CSRF tokens
- **Input Validation**: Server-side form validation
- **SQL Injection Protection**: SQLAlchemy ORM queries

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Contributing

This is a complete, self-contained expense tracking application. The code is well-documented and modular for easy customization and extension.

## License

This project is created for educational and personal use.