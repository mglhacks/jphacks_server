# coding=utf8
"""
# Code name: Temujin

# JPhacks 2014 server side program

"""
# flask imports
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.restful import reqparse, abort, Api, Resource

# other imports
import urllib, urllib2
import time
import json
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime

# user library
#from post_helper.py import *
#from database_helper.py import *

# configuration
DATABASE = '/tmp/temujin.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'burtechono'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    # add post1
    # add_post(1)

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

def add_post(content_json):
    """Put json post data into database
    post id is no included(autoincrement)
    """
    user_id = None
    if 'user_id' in content_json: user_id = content_json['user_id']
    pub_date = int(time.time())
    comment = None
    if 'comment' in content_json: comment = content_json['comment']
    photo_url = "photo_url"
    autodesk_url = "autodesk_url"
    # inserting into db
    db = get_db()
    db.execute('''insert into post (user_id, pub_date, comment, photo_url, autodesk_url)
        values (?,?,?,?,?)''', [user_id, pub_date, comment, photo_url, autodesk_url])
    db.commit()
    flash('Your post added to db.')
    return 201

def get_post(post_id):
    """Returns one post by post_id"""
    post = query_db('''select * from post where post.post_id = ?''', [post_id], one=True)
    return post

def post_to_json(post):
    post_as_dict = {
        'post_id' : post['post_id'],
        'user_id' : post['user_id'],
        'pub_date' : post['pub_date'],
        'comment' : post['comment'],
        'photo_url' : post['photo_url'],
        'autodesk_url' : post['autodesk_url']
    }
    return json.dumps(post_as_dict)

def posts_to_json(posts):
    post_as_dict = []

    for post in posts:
        post_as_dict = {
            'post_id' : post['post_id'],
            'user_id' : post['user_id'],
            'pub_date' : post['pub_date'],
            'comment' : post['comment'],
            'photo_url' : post['photo_url'],
            'autodesk_url' : post['autodesk_url']
            }
        posts_as_dict.append(post_as_dict)

    return json.dumps(posts_as_dict)

# Post
#  returns post
class Post(Resource):
    def get(self, post_id):
        post = get_post(post_id)
        json_dump = post_to_json(post)
        return json_dump, 201

class Upload(Resource):
    def post(self):
        # Read post body json
        content_json = json.loads(request.data)
        return add_post(content_json)




##
## Actually setup the Api resource routing here
##
api.add_resource(Post, '/post/<int:post_id>')
api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
