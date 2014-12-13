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
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime

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

def add_post(post_id):
	user_id = 0
	pub_date = int(time.time())
	comment = "test comment"
	photo_url = "photo_url"
	autodesk_url = "autodesk_url"
	db = get_db()
	db.execute('''insert into post (post_id, user_id, pub_date, comment, photo_url, autodesk_url)
		values (?,?,?,?,?,?)''', [post_id, user_id, pub_date, comment, photo_url, autodesk_url])
	db.commit()
	flash('Your post added to db.')

	return 'post added'

def get_post(post_id):
	post = query_db('''select * from post where post.post_id = ?''', [post_id], one=True)
	return post


# Post
#  returns post
class Post(Resource):
    def get(self, post_id):
    	post = get_post(post_id)
        return 'ok' + str(post['post_id']) + post['comment'], 201

    def post(self, post_id):
    	return add_post(post_id)





##
## Actually setup the Api resource routing here
##
api.add_resource(Post, '/post/<int:post_id>')


if __name__ == '__main__':
	init_db()
	app.run(debug=True)
