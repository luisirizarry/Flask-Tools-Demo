from flask import Flask, request, render_template,  redirect, flash
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

MOVIES = [ 'The Dark Knight', 'The Departed', 'The Godfather', 'Goodfellas', 
          'Inception', 'Jaws', 'Jurassic Park', 'The Matrix', 'Rocky', 
          'Saving Private Ryan', 'The Shawshank Redemption', 'The Shining',
          'Star Wars', 'The Terminator', 'Titanic', 'Toy Story']

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    """Redirects to home page"""
    flash("That page has moved! This is our new home!")
    return redirect('/')

@app.route('/movies')
def show_all_movies():
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    if title in MOVIES:
        flash("That movie is already in the list!", "error")
    else:
        MOVIES.append(title)
        flash(f"Added {title}", "success")
    return redirect('/movies')