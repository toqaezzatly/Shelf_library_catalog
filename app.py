import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from models import db, User, Book, UserBook
from forms import RegistrationForm, LoginForm, BookForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelf.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        flash('Book Added successfully')
        return redirect(url_for('books'))

    all_books = Book.query.all()
    return render_template('books.html', form=form, books=all_books)


@app.route('/book/<int:book_id>')
@login_required
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)


@app.route('/user-books')
@login_required
def user_books():
    user_id = current_user.id
    user_books = UserBook.query.filter_by(user_id=user_id).all()
    return render_template('user_books.html', user_books=user_books)


@app.route('/add-user-book/<int:book_id>')
@login_required
def add_user_book(book_id):
    book = Book.query.get_or_404(book_id)
    user = current_user
    if UserBook.query.filter_by(user_id=user.id, book_id=book.id).first():
        flash('You have already recorded this book before!')
        return redirect(url_for('books'))

    user_book = UserBook(user_id=user.id, book_id=book.id)
    db.session.add(user_book)
    db.session.commit()
    flash(f'You have Recorded the book: {book.title}')

    return redirect(url_for('books'))


if __name__ == '__main__':
     with app.app_context():
        db.create_all()
     app.run(debug=True)