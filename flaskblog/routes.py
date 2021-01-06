from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Arun Narayanan',
        'title': 'Beginning Python',
        'content': 'My first content',
        'date_posted': 'Dec 30, 2020'
    },
    {
        'author': 'Tom Hanks',
        'title': 'GTD',
        'content': 'GTD is cool',
        'date_posted': 'Dec 28, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='My Title')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flaskblog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check username & password', 'danger')

    return render_template('login.html', title='Login', form=form)

