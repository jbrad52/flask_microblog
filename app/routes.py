from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Justin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Chicago!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Sandman series was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)