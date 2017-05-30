create database if not exists caoliu;
use caoliu;

drop table if exists rawdata;
create table rawdata
(
    id int not null auto_increment,
    url varchar(255) not null,
    url_md5 char(32) not null,
    cat char(2),
    cat_name varchar(32),
    title varchar(1024),
    publish_time varchar(32),
    content text,
    created_at timestamp default current_timestamp,
    parsed char(1) default 'N',
    UNIQUE(url_md5),
    PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
