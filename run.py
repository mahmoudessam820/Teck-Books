# Imports
from flask import (Flask, render_template, redirect,
                   url_for, flash, get_flashed_messages)
from flask_login import (login_user, logout_user, login_required)

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models import db, Books, User
from forms import RegisterForm, LoginForm, AddBook


#! App Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = '63cb0a4adea3bfa8078b4c7b'
db.init_app(app)
with app.app_context():
    db.create_all()

#! App Bcrypt Config
bcrypt = Bcrypt(app)

#! App Login Manager Config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ? Controllers


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/market')
@login_required
def market():
    books = Books.query.all()
    return render_template('market.html', books=books)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        create_user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=bcrypt.generate_password_hash(
                form.password1.data).decode('utf-8')
        )
        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(
            f"You were create new account successfully {create_user.username}", 'success')
        return redirect(url_for('market'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(
                f"An error occurred {error_message}  could not be created", category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        one_user = User.query.filter_by(
            username=form.username.data).first()

        if one_user and bcrypt.check_password_hash(one_user.password_hash, form.password.data):
            login_user(one_user)
            flash(
                f"You were successfully logged in! {one_user.username}", 'success')
            return redirect(url_for('market'))
        else:
            flash(f'Invalid  username or password', 'danger')

    return render_template('login.html', form=form)


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = AddBook()
    if form.validate_on_submit():
        new_book = Books(
            name=form.name.data,
            author=form.author.data,
            category=form.category.data,
            language=form.language.data,
            pages=form.pages.data,
            published=form.published.data,
            link=form.link.data
        )
        db.session.add(new_book)
        db.session.commit()
        flash(f"New Book Added successfully {new_book.name} 📕", 'success')
        return redirect(url_for('market'))

    return render_template('add-book.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logout!', 'info')
    return redirect(url_for('home'))
