drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
  profile_pic text,
  email text,
  pw_hash text
);

drop table if exists post;
create table post (
  post_id integer primary key autoincrement,
  user_id integer,
  pub_date integer,
  comment text,
  photo_url text,
  obj_url text
);
