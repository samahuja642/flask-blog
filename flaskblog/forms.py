from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,FileField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit =  SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Already Taken.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Already Taken.')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit =  SubmitField('Login')

class UpdationForm(FlaskForm):
    username = StringField('UserName',validators=[DataRequired(),Length(min=2,max=10)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Update Now!')
    picture = FileField('Update Profile Photo',validators=[FileAllowed(['jpg','png'])])

    def validate_username(self,username):
        if current_user.username != username.data:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username Already Taken.')

    def validate_email(self,email):
        if current_user.email != email.data:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email Already Taken.')
            
class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),Length(max=100)])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post Now')

class UpdatePostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),Length(max=100)])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post Now')