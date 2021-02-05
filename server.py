"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db 
import crud 

from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 


# Replace this with routes and view functions!

@app.route('/')
def create_homepage():

    return render_template('homepage.html')

@app.route('/movies')
def show_movies():
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_me_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_users():
    users = crud.get_users()

    return render_template('users.html', users=users)


@app.route('/users/<user_id>')
def show_me_user(user_id):    
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    
    if user:
        flash("can't create account with email")
    else:
        crud.create_user(email, password)
        flash("account successfully created")

    return redirect('/')

@app.route('/users')
def login_user():
    """Create a new user."""

    email = request.args.get('email')
    password = request.args.get('password')
    user = crud.get_user_by_email(email)
    
    if user:
        flash("login unsuccessful")
    else:
        crud.create_user(email, password)
        flash("successful login!")

    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
