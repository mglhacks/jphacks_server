# coding=utf8
# JPhacks 2014 server side program
# Code name: Temujin
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

import urllib
import urllib2

app = Flask(__name__)
api = Api(app)

# Post
#  returns post
class Post(Resource):
    def get(self, post_id):
        return 'ok' + str(post_id), 201



##
## Actually setup the Api resource routing here
##
api.add_resource(Post, '/post/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)
