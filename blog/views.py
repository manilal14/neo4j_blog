from flask import Flask, render_template
from .models import Movie
app = Flask(__name__)

@app.route('/')
def index():
    movieList = Movie.getMovieList()
    print(movieList[0])
    return render_template('show_movie_list.html', movieList = movieList)


@app.route('/register', methods=['GET','POST'])
def register():
    pass
   
@app.route('/login', methods=['GET', 'POST'])
def login():
    pass
   
@app.route('/logout')
def logout():
    pass

@app.route('/add_post', methods=['POST'])
def add_post():
    pass
   

@app.route('/like_post/<post_id>')
def like_post(post_id):
    pass
    

@app.route('/profile/<username>')
def profile(username):
    pass

