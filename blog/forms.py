from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User



class RegistrationForm(FlaskForm):
    firstname = StringField('FirstName',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address',
                          validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sing UP')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken. Please choose different one.')
        
    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already taken. Please choose different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('FirstName',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField('Upload picture', 
                        validators=[FileAllowed(['jpg', 'png'])])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address',
                          validators=[DataRequired()])
   
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:          
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already taken. Please choose different one.')
        
    def validate_email(self, email):
        if email.data != current_user.email:   
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already taken. Please choose different one.')


class PostForm(FlaskForm):
    title = StringField('Tiltle', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


