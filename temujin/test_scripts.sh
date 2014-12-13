# upload multiple photo
curl -i -XPOST -F "files[]=@test1.jpg" -F "files[]=@test2.jpg" -F "files[]=@test3.jpg" -F "files[]=@test4.jpg" localhost:5000/upload

# create post
curl -i -XPOST -d '{"comment": "testjson", "user_id": "1"}' -H "Content-Type: application/json" localhost:5000/post/create/photo_hash

# get posts
curl -i -XGET localhost:5000/posts