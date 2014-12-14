# upload multiple photo
photo_hash=`curl -XPOST -F "files[]=@1.jpg" -F "files[]=@2.jpg" -F "files[]=@3.jpg" -F "files[]=@4.jpg" -F "files[]=@5.jpg" -F "files[]=@6.jpg" -F "files[]=@7.jpg" -F "files[]=@8.jpg" -F "files[]=@9.jpg" localhost:5000/upload`

# create post
curl -i -XPOST -d '{"comment": "testjson", "user_id": "1"}' -H "Content-Type: application/json" localhost:5000/post/create/$photo_hash

# get posts
curl -i -XGET localhost:5000/posts