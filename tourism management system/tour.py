from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,TextField,validators,SelectField
from flask import Flask,render_template,redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY']='fahadrahman'

@app.route('/')
def welcome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=SignUpform()
    form.firstname.data = ''
    form.lastname.data = ''
    form.email.data = ''
    form.phone.data = ''
    form.gender.data = ''
    return render_template('reg.html',form=form)


class SignUpform(FlaskForm):
    
    firstname = StringField("First Name", validators=[Required()])
    lastname = StringField('last Name', validators=[Required()])
    email = TextField('E-mail', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    con_password = PasswordField('Cofirm Password', validators=[Required()])
    phone = IntegerField('Phone Number', validators=[Required()])
    gender = SelectField("Gender", choices=[("Please Select"), ("MALE"), ("FEMALE"), ("N/A")])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = TextField('E-mail', [validators.Required("EX:myname@gmail.com")])
    password=PasswordField('Password')
    submit = SubmitField('Login')



@app.route('/login', methods=['GET', 'POST'])
def login():
    Form=LoginForm()
    Form.email.data = ''
    return render_template('login.html',form=Form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/package')
def package():
    return render_template('package.html')


if __name__ == '__main__':
    app.run()