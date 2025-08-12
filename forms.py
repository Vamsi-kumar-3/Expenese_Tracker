from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange, Length
from models import Category
from datetime import datetime

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', 
                             validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

class ExpenseForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01, message='Amount must be positive')])
    description = TextAreaField('Description', validators=[Length(max=500)])
    date = DateField('Date', validators=[DataRequired()], default=datetime.utcnow().date)
    category_id = SelectField('Category', validators=[DataRequired()], coerce=int)
    
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(c.id, c.name) for c in Category.query.order_by(Category.name).all()]

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(min=1, max=64)])

class FilterForm(FlaskForm):
    category_id = SelectField('Category', coerce=int)
    start_date = DateField('Start Date')
    end_date = DateField('End Date')
    
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        choices = [(0, 'All Categories')]
        categories = [(c.id, c.name) for c in Category.query.order_by(Category.name).all()]
        self.category_id.choices = choices + categories  # type: ignore
