from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import(
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
    )
class SignupForm(FlaskForm):
    username=StringField(
        "username",
        validators=[DataRequired(),Length(2,30)]
    )
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    dob=DateField(
        "Date of Birth",
        validators=[Optional()]
    )
    Gender=SelectField(
        "Gender",
        validators=["Male","Female","Other"]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30)]
    )
    confirm_password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30),EqualTo("password")]
    )
    submit=SubmitField("Sign Up")
class LoginForm(FlaskForm):
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Login")