# Expense Tracker

## Overview

An expense tracking web application built with Flask that allows users to manage their personal finances by recording, categorizing, and analyzing expenses. The application provides user authentication, expense management with categories, data visualization through charts, and reporting capabilities with CSV export functionality.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5 for responsive UI
- **CSS Framework**: Bootstrap with dark theme and Font Awesome icons
- **JavaScript Libraries**: Chart.js for data visualization
- **Responsive Design**: Mobile-first approach with collapsible navigation

### Backend Architecture
- **Framework**: Flask web framework with Blueprint pattern
- **Authentication**: Flask-Login for session management with password hashing
- **Form Handling**: WTForms with CSRF protection for secure form processing
- **Database ORM**: SQLAlchemy with Flask-SQLAlchemy extension
- **Application Structure**: Modular design separating routes, models, forms, and utilities

### Data Storage Solutions
- **Primary Database**: SQLAlchemy with configurable backend (defaults to SQLite)
- **Database Models**: Three main entities - Users, Categories, and Expenses
- **Relationships**: One-to-many relationships between Users-Expenses and Categories-Expenses
- **Migration Support**: Built-in database creation with default category seeding

### Authentication and Authorization
- **User Management**: Username/email registration with password hashing using Werkzeug
- **Session Handling**: Flask-Login for user session management
- **Access Control**: Login required decorators for protected routes
- **Security Features**: CSRF protection and secure password storage

### Key Features
- **Expense Management**: CRUD operations for expenses with category assignment
- **Category System**: User-managed expense categories with default options
- **Data Visualization**: Interactive charts showing expense distribution and monthly trends
- **Filtering and Search**: Date range and category-based expense filtering
- **Reporting**: CSV export functionality for expense data
- **Dashboard Analytics**: Monthly summaries and expense totals

### Application Configuration
- **Environment Variables**: Configurable database URL and session secrets
- **Database Settings**: Connection pooling and health check configuration
- **Production Ready**: ProxyFix middleware for deployment behind proxies

## External Dependencies

### Core Framework Dependencies
- **Flask**: Main web framework
- **SQLAlchemy**: Database ORM and management
- **Flask-Login**: User session management
- **WTForms**: Form handling and validation

### Frontend Dependencies
- **Bootstrap 5**: CSS framework with dark theme
- **Chart.js**: JavaScript charting library
- **Font Awesome**: Icon library

### Database Support
- **SQLite**: Default development database
- **PostgreSQL**: Production database option (configurable via DATABASE_URL)

### Development Tools
- **Werkzeug**: WSGI utilities and password hashing
- **Jinja2**: Template engine (Flask dependency)

### Optional Integrations
- **CSV Export**: Built-in Python CSV module for data export
- **Email Validation**: WTForms email validation
- **Date Handling**: Python datetime for expense date management