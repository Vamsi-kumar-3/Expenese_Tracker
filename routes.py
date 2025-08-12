from flask import render_template, request, redirect, url_for, flash, jsonify, make_response, session
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from models import User, Expense, Category
from forms import LoginForm, RegisterForm, ExpenseForm, CategoryForm, FilterForm
from utils import generate_csv_response, get_expense_data, get_monthly_summary
from datetime import datetime, date
from sqlalchemy import extract, func
import calendar

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists', 'danger')
            return render_template('register.html', form=form)
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered', 'danger')
            return render_template('register.html', form=form)
        
        # Create new user
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard with expense overview and charts"""
    # Get total expenses
    total_expenses = db.session.query(func.sum(Expense.amount)).filter_by(user_id=current_user.id).scalar() or 0
    
    # Get recent expenses
    recent_expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).limit(5).all()
    
    # Get current month expenses
    current_month = datetime.now().month
    current_year = datetime.now().year
    month_expenses = db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        extract('month', Expense.date) == current_month,
        extract('year', Expense.date) == current_year
    ).scalar() or 0
    
    # Get expense data for charts
    expense_data = get_expense_data(current_user.id)
    
    return render_template('dashboard.html', 
                         total_expenses=total_expenses,
                         month_expenses=month_expenses,
                         recent_expenses=recent_expenses,
                         expense_data=expense_data)

@app.route('/expenses')
@login_required
def expenses():
    """List all expenses with filtering"""
    form = FilterForm()
    query = Expense.query.filter_by(user_id=current_user.id)
    
    # Apply filters
    category_id = request.args.get('category_id')
    if category_id and int(category_id) > 0:
        query = query.filter_by(category_id=int(category_id))
    
    start_date_str = request.args.get('start_date')
    if start_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        query = query.filter(Expense.date >= start_date)
    
    end_date_str = request.args.get('end_date')
    if end_date_str:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        query = query.filter(Expense.date <= end_date)
    
    page = request.args.get('page', 1, type=int)
    expenses = query.order_by(Expense.date.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    
    return render_template('expenses.html', expenses=expenses, form=form)

@app.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    """Add new expense"""
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense()
        expense.amount = form.amount.data
        expense.description = form.description.data
        expense.date = form.date.data
        expense.category_id = form.category_id.data
        expense.user_id = current_user.id
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('expenses'))
    return render_template('add_expense.html', form=form)

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    """Edit existing expense"""
    expense = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    form = ExpenseForm(obj=expense)
    
    if form.validate_on_submit():
        expense.amount = form.amount.data
        expense.description = form.description.data
        expense.date = form.date.data
        expense.category_id = form.category_id.data
        db.session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('expenses'))
    
    return render_template('edit_expense.html', form=form, expense=expense)

@app.route('/delete_expense/<int:id>')
@login_required
def delete_expense(id):
    """Delete expense"""
    expense = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('expenses'))

@app.route('/categories')
@login_required
def categories():
    """List all categories"""
    categories = Category.query.order_by(Category.name).all()
    return render_template('categories.html', categories=categories)

@app.route('/add_category', methods=['POST'])
@login_required
def add_category():
    """Add new category"""
    form = CategoryForm()
    if form.validate_on_submit():
        # Check if category already exists
        if Category.query.filter_by(name=form.name.data).first():
            flash('Category already exists', 'warning')
        else:
            category = Category()
            category.name = form.name.data
            db.session.add(category)
            db.session.commit()
            flash('Category added successfully!', 'success')
    return redirect(url_for('categories'))

@app.route('/reports')
@login_required
def reports():
    """Monthly expense reports"""
    year = request.args.get('year', datetime.now().year, type=int)
    monthly_data = get_monthly_summary(current_user.id, year)
    
    return render_template('reports.html', monthly_data=monthly_data, year=year)

@app.route('/export_csv')
@login_required
def export_csv():
    """Export expenses to CSV"""
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    return generate_csv_response(expenses)

@app.route('/api/expense_data')
@login_required
def api_expense_data():
    """API endpoint for expense data (for charts)"""
    data = get_expense_data(current_user.id)
    return jsonify(data)
