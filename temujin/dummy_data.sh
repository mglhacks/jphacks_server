#!/bin/bash

# insert dummy data

# insert user
curl -i -XPOST -d '{"username": "Orgil", "profile_pic": "./static/member_pic/orgil.jpg", "email": "a@a.com"}' -H "Content-Type: application/json" localhost:5000/user/1
curl -i -XPOST -d '{"username": "Bya", "profile_pic": "./static/member_pic/bya.png", "email": "b@a.com"}' -H "Content-Type: application/json" localhost:5000/user/2
curl -i -XPOST -d '{"username": "Byambaa", "profile_pic": "./static/member_pic/byambajav.jpeg", "email": "c@a.com"}' -H "Content-Type: application/json" localhost:5000/user/3
curl -i -XPOST -d '{"username": "Zoloo", "profile_pic": "./static/member_pic/zoloo.jpeg", "email": "d@a.com"}' -H "Content-Type: application/json" localhost:5000/user/4
curl -i -XPOST -d '{"username": "JPHack", "profile_pic": "./static/member_pic/zoloo.jpeg", "email": "e@a.com"}' -H "Content-Type: application/json" localhost:5000/user/5

# upload multiple photo
#curl -XPOST -F "files[]=@1.jpg" -F "files[]=@2.jpg" -F "files[]=@3.jpg" -F "files[]=@4.jpg" -F "files[]=@5.jpg" -F "files[]=@6.jpg" -F "files[]=@7.jpg" -F "files[]=@8.jpg" -F "files[]=@9.jpg" localhost:5000/upload

# create post
#curl -i -XPOST -d '{"comment": "Orgils photo", "user_id": "1", "obj_url": "hey"}' -H "Content-Type: application/json" localhost:5000/post/create/36cd220726bdeff076f09c04a4c00f1b
#curl -i -XPOST -d '{"comment": "Bya photo", "user_id": "2"}' -H "Content-Type: application/json" localhost:5000/post/create/36cd220726bdeff076f09c04a4c00f1b
#curl -i -XPOST -d '{"comment": "Zoloogg photo", "user_id": "4"}' -H "Content-Type: application/json" localhost:5000/post/create/36cd220726bdeff076f09c04a4c00f1b


# get posts
#curl -i -XGET localhost:5000/posts
