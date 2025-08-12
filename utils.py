from flask import make_response
from models import Expense, Category
from sqlalchemy import func, extract
import csv
import io
from datetime import datetime
import calendar

def generate_csv_response(expenses):
    """Generate CSV response for expense export"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    
    # Write expense data
    for expense in expenses:
        writer.writerow([
            expense.date.strftime('%Y-%m-%d'),
            expense.category.name,
            str(expense.amount),
            expense.description or ''
        ])
    
    # Create response
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = f'attachment; filename=expenses_{datetime.now().strftime("%Y%m%d")}.csv'
    
    return response

def get_expense_data(user_id):
    """Get expense data for charts and dashboard"""
    from app import db
    
    # Get expenses by category
    category_data = db.session.query(
        Category.name,
        func.sum(Expense.amount).label('total')
    ).join(Expense).filter(
        Expense.user_id == user_id
    ).group_by(Category.name).all()
    
    # Get monthly expenses for current year
    current_year = datetime.now().year
    monthly_data = db.session.query(
        extract('month', Expense.date).label('month'),
        func.sum(Expense.amount).label('total')
    ).filter(
        Expense.user_id == user_id,
        extract('year', Expense.date) == current_year
    ).group_by(extract('month', Expense.date)).all()
    
    # Format data for charts
    categories = [item[0] for item in category_data]
    category_amounts = [float(item[1]) for item in category_data]
    
    # Create monthly data array (12 months)
    monthly_amounts = [0.0] * 12
    for month, amount in monthly_data:
        monthly_amounts[int(month) - 1] = float(amount)
    
    return {
        'categories': categories,
        'category_amounts': category_amounts,
        'monthly_amounts': monthly_amounts,
        'months': [calendar.month_name[i] for i in range(1, 13)]
    }

def get_monthly_summary(user_id, year):
    """Get monthly expense summary for reports"""
    from app import db
    
    monthly_data = db.session.query(
        extract('month', Expense.date).label('month'),
        func.sum(Expense.amount).label('total'),
        func.count(Expense.id).label('count')
    ).filter(
        Expense.user_id == user_id,
        extract('year', Expense.date) == year
    ).group_by(extract('month', Expense.date)).all()
    
    # Create summary for all 12 months
    summary = []
    for month in range(1, 13):
        month_data = next((item for item in monthly_data if item[0] == month), None)
        summary.append({
            'month': calendar.month_name[month],
            'total': float(month_data[1]) if month_data else 0,
            'count': month_data[2] if month_data else 0
        })
    
    return summary
