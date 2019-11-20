from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required

bp = Blueprint('blog', __name__)


now = datetime.now()
posts = [
        {'id': 1, 'title': 'First Post', 'body': 'This is my first post', 'created':  now.strftime("%m/%d/%Y")}
    ]

def get_post(id):
    for post in posts:
        if post['id'] == id:
            return post;

def update_post(id, title, body):
    for i, post in enumerate(posts):
        if post['id'] == id:
            posts[i] = {'id': id, 'title': title, 'body': body, 'created': now.strftime("%m/%d/%Y")}
            return


@bp.route('/')
def index():
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
       title = request.form['title']
       body = request.form['body']
       error = None
       
       if not title:
           error = 'Title is required'
        
       if error is not None:
            flash(error)
       else:
           newId = posts[-1]['id'] + 1
           posts.append({'id': newId, 'title': title, 'body': body, 'created': now.strftime("%m/%d/%Y")})
           return redirect(url_for('blog.index'))
        
    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
       title = request.form['title']
       body = request.form['body']
       error = None
       
       if not title:
           error = 'Title is required'
        
       if error is not None:
            flash(error)
       else:
           update_post(id, title, body)
           return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    print('id to delete', id)
    return 'delete'
