#!/bin/bash

# insert dummy data

# insert user
curl -i -XPOST -d '{"username": "Orgil", "profile_pic": "./static/member_pic/orgil.jpg", "email": "a@a.com"}' -H "Content-Type: application/json" localhost:5000/user/1
curl -i -XPOST -d '{"username": "Bya", "profile_pic": "./static/member_pic/bya.png", "email": "b@a.com"}' -H "Content-Type: application/json" localhost:5000/user/2
curl -i -XPOST -d '{"username": "Byambaa", "profile_pic": "./static/member_pic/byambajav.jpeg", "email": "c@a.com"}' -H "Content-Type: application/json" localhost:5000/user/3
curl -i -XPOST -d '{"username": "Zoloo", "profile_pic": "./static/member_pic/zoloo.jpeg", "email": "d@a.com"}' -H "Content-Type: application/json" localhost:5000/user/4
curl -i -XPOST -d '{"username": "JPHack", "profile_pic": "./static/member_pic/jphacks.jpeg", "email": "e@a.com"}' -H "Content-Type: application/json" localhost:5000/user/5
