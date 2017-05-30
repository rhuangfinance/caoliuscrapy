### 1024 技术讨论区帖子抓取及 web 展示

包含两部分内容

- caoliu: 基于 scrapy 的爬虫部分
- web: 基于 tornado 的 web 展示

web 展示中，写死了用户名 daixiepython.com 字段值。输入即可登录。

#### 爬虫及 web 系统的安装

整个程序使用 MySQL 存储数据，依赖于 python 的 MySQL 驱动，除此之外，还需要安装一些其他依赖，
比如 tornado、scrapy 等。

#### 运行方法

首先需要创建数据库及表，表定义在 caoliu/schema.sql 中。
其次需要配置数据库用户名、密码等，分别保存在 caoliu/settings.py 及 web/settings.py 里面。

运行 web 程序，只需要 python app.py 即可，默认运行在 9876 端口。

运行爬虫程序，在 caoliu 目录下，python runspider.py 即可。

#### 效果图

![](http://wx3.sinaimg.cn/large/92f3355cgy1fg3irsclz7j20u30lf42y.jpg)


#### 其他

本人不对程序运行产生的任何结果负任何责任，仅供学习 python 和最最最最基础的 scrapy tutorial。

天若有情天亦老。

以上。