# Infinity

# 创建测试用的 MySQL 数据库

```MySQL
$ sudo mysql -u root -p

> create database test;

> create user 'test'@localhost identified by 'test';

> user test;

> grant all on r.*TO 'test'@'localhost';

> quit;
```
