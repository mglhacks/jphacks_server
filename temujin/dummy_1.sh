# upload multiple photo
curl -XPOST -F "files[]=@./sample1/1.jpg" -F "files[]=@./sample1/2.jpg" -F "files[]=@./sample1/3.jpg" -F "files[]=@./sample1/4.jpg" -F "files[]=@./sample1/5.jpg" -F "files[]=@./sample1/6.jpg" -F "files[]=@./sample1/7.jpg" -F "files[]=@./sample1/8.jpg" -F "files[]=@./sample1/9.jpg" localhost:5000/upload/a
curl -XPOST -F "files[]=@./sample2/1.jpg" -F "files[]=@./sample2/2.jpg" -F "files[]=@./sample2/3.jpg" -F "files[]=@./sample2/4.jpg" -F "files[]=@./sample2/5.jpg" -F "files[]=@./sample2/6.jpg" -F "files[]=@./sample2/7.jpg" -F "files[]=@./sample2/8.jpg" -F "files[]=@./sample2/9.jpg" localhost:5000/upload/b
curl -XPOST -F "files[]=@./sample3/1.jpg" -F "files[]=@./sample3/2.jpg" -F "files[]=@./sample3/3.jpg" -F "files[]=@./sample3/4.jpg" -F "files[]=@./sample3/5.jpg" -F "files[]=@./sample3/6.jpg" -F "files[]=@./sample3/7.jpg" -F "files[]=@./sample3/8.jpg" -F "files[]=@./sample3/9.jpg" localhost:5000/upload/c
curl -XPOST -F "files[]=@./sample4/1.jpg" -F "files[]=@./sample4/2.jpg" -F "files[]=@./sample4/3.jpg" -F "files[]=@./sample4/4.jpg" -F "files[]=@./sample4/5.jpg" -F "files[]=@./sample4/6.jpg" -F "files[]=@./sample4/7.jpg" -F "files[]=@./sample4/8.jpg" -F "files[]=@./sample4/9.jpg" localhost:5000/upload/d
curl -XPOST -F "files[]=@./sample5/1.jpg" -F "files[]=@./sample5/2.jpg" -F "files[]=@./sample5/3.jpg" -F "files[]=@./sample5/4.jpg" -F "files[]=@./sample5/5.jpg" -F "files[]=@./sample5/6.jpg" -F "files[]=@./sample5/7.jpg" -F "files[]=@./sample5/8.jpg" -F "files[]=@./sample5/9.jpg" localhost:5000/upload/e

# create post
curl -i -XPOST -d '{"comment": "My JPHacks life", "user_id": "1", "obj_url": "https://zoloogg.autodesk360.com/shares/public/SHabee1QT1a327cf2b7ab5c89e238eeecdd4?mode=embed"}' -H "Content-Type: application/json" localhost:5000/post/create/a
curl -i -XPOST -d '{"comment": "Amazon Box #kawai #kawai", "user_id": "2", "obj_url": "https://zoloogg.autodesk360.com/shares/public/SHabee1QT1a327cf2b7a401d76ee18f330f7?mode=embed"}' -H "Content-Type: application/json" localhost:5000/post/create/b
curl -i -XPOST -d '{"comment": "Oooiii Ooooochaaaa", "user_id": "3", "obj_url": "https://zoloogg.autodesk360.com/shares/public/SHabee1QT1a327cf2b7a86340da45a50456f?mode=embed"}' -H "Content-Type: application/json" localhost:5000/post/create/c
curl -i -XPOST -d '{"comment": "My 2D camera, but my phone camera can take 3D #haha", "user_id": "4", "obj_url": "https://zoloogg.autodesk360.com/shares/public/SHabee1QT1a327cf2b7aff3e6a4454e7dd03?mode=embed"}' -H "Content-Type: application/json" localhost:5000/post/create/d
curl -i -XPOST -d '{"comment": "Wow, MiniMax is the app", "user_id": "5", "obj_url": "https://zoloogg.autodesk360.com/shares/public/SHabee1QT1a327cf2b7a15bfdf20720696fa?mode=embed"}' -H "Content-Type: application/json" localhost:5000/post/create/e


# get posts
curl -i -XGET localhost:5000/posts