# coding=utf8
"""
# Code name: Temujin

# JPhacks 2014 server side program

"""
# flask imports
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack, jsonify
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.restful import reqparse, abort, Api, Resource
from werkzeug import secure_filename
import json

# other imports
import urllib, urllib2
import time
import json, os
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

# upload config
UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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

# user db functions
def add_user(content_json, user_id):
    # user_id
    username = None
    if 'username' in content_json: username = content_json['username']
    profile_pic = None
    if 'profile_pic' in content_json: profile_pic = content_json['profile_pic']    
    email = None
    if 'email' in content_json: email = content_json['email']    
    pw_hash = None
    if 'pw_hash' in content_json: pw_hash = content_json['pw_hash']    
    # inserting into db
    db = get_db()
    db.execute('''insert into user (user_id, username, profile_pic, email, pw_hash)
        values (?,?,?,?,?)''', [user_id, username, profile_pic, email, pw_hash])
    db.commit()
    flash('Your post added to db.')
    return 201

def get_user(user_id):
    user = query_db('''select * from user where user.user_id = ?''', [user_id], one=True)
    return user

def user_to_json(post):
    user_as_dict = {
        'user_id' : post['user_id'],
        'username' : post['username'],
        'profile_pic' : post['profile_pic'],
        'email' : post['email'],
        'pw_hash' : post['pw_hash']
    }
    return json.dumps(user_as_dict)


# post db functions
def add_post(content_json, photo_hash):
    """Put json post data into database
    post id is no included(autoincrement)
    """
    user_id = None
    if 'user_id' in content_json: user_id = content_json['user_id']
    pub_date = int(time.time())
    comment = None
    if 'comment' in content_json: comment = content_json['comment']
    photo_url = app.config['UPLOAD_FOLDER'] + photo_hash + '/'
    obj_url = None
    if 'obj_url' in content_json: obj_url = content_json['obj_url']
    # inserting into db
    db = get_db()
    db.execute('''insert into post (user_id, pub_date, comment, photo_url, obj_url)
        values (?,?,?,?,?)''', [user_id, pub_date, comment, photo_url, obj_url])
    db.commit()
    flash('Your post added to db.')
    return 201

def get_post(post_id):
    """Returns one post by post_id"""
    post = query_db('''select * from post where post.post_id = ?''', [post_id], one=True)
    return post

def get_posts():
    """Returns all posts"""
    posts = query_db('''select * from post order by post_id asc''')
    return posts

def post_to_json(post):
    post_as_dict = {
        'post_id' : post['post_id'],
        'user_id' : post['user_id'],
        'pub_date' : post['pub_date'],
        'comment' : post['comment'],
        'photo_url' : post['photo_url'],
        'obj_url' : post['obj_url']
    }
    return json.dumps(post_as_dict)

def posts_to_json(posts):
    posts_as_dict = []

    for post in posts:
        post_as_dict = {
            'post_id' : post['post_id'],
            'user_id' : post['user_id'],
            'pub_date' : post['pub_date'],
            'comment' : post['comment'],
            'photo_url' : post['photo_url'],
            'obj_url' : post['obj_url']
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


# Upload single file
class Upload(Resource):
    def post(self):

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            photo_hash = str(md5(str(file)).hexdigest())
            savepath = app.config['UPLOAD_FOLDER'] + photo_hash + '/'
            if not os.path.exists(os.path.dirname(savepath)):
                os.makedirs(os.path.dirname(savepath))

        file.save(os.path.join(savepath, filename))
        return photo_hash, 201

# Upload multiple files
class Upload2(Resource):
    def post(self, photo_path):
        files = request.files.getlist('files[]')
        #photo_hash = str(md5(str(files[0])).hexdigest())
        savepath = app.config['UPLOAD_FOLDER'] + photo_path + '/'
        if not os.path.exists(os.path.dirname(savepath)):
            os.makedirs(os.path.dirname(savepath))

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(savepath, filename))

        return photo_path, 201

# Create post
class PostCreate(Resource):
    def post(self, photo_hash):
        # Read post body json
        content_json = json.loads(request.data)
        add_post(content_json, photo_hash)
        return 'ok', 201

# Posts
# returns all posts
class Posts(Resource):
    def get(self):
        return posts_to_json(get_posts())

# User getter setter
class User(Resource):
    def get(self, user_id):
        return user_to_json(get_user(user_id))
    def post(self, user_id):
        content_json = json.loads(request.data)
        add_user(content_json, user_id)
        return 'ok', 201

# Feed class for android
class Feed(Resource):
    def get(self):
        posts = get_posts()
        feed_all = []
        # make feed json
        for post in posts:
            user = get_user(post['user_id'])
            feed_element = {
                'id' : post['post_id'],
                'name' : user['username'],
                'image' : post['photo_url'] + '5.jpg',
                'status' : post['comment'],
                'profilePic' : user['profile_pic'],
                'timeStamp' : post['pub_date'],
                'url' : None
            }
            feed_all.append(feed_element)
        feed = { 'feed' : feed_all }
        #return str(json.dumps(feed)).replace('\\\"', '"')
        return jsonify(feed)


@app.route('/2', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('files[]')
        photo_hash = str(md5(str(files[0])).hexdigest())
        savepath = app.config['UPLOAD_FOLDER'] + photo_hash + '/'
        if not os.path.exists(os.path.dirname(savepath)):
            os.makedirs(os.path.dirname(savepath))

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(savepath, filename))
        
        return 'ok all images' + str(os.path.join(app.config['UPLOAD_FOLDER']))

@app.route('/')
def index():
    list = json.loads(posts_to_json(get_posts()))
    return render_template('index.html', data = list)
            

##
## Actually setup the Api resource routing here
##
api.add_resource(Posts, '/posts')
api.add_resource(Post, '/post/<int:post_id>')
api.add_resource(PostCreate, '/post/create/<string:photo_hash>')
api.add_resource(Upload, '/upload_single')
api.add_resource(Upload2, '/upload/<string:photo_path>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Feed, '/feed')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host="0.0.0.0")
    # for deployment comment above
    #app.run()
