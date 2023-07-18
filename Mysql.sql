Microsoft Windows [Version 10.0.19045.3086]
(c) Microsoft Corporation. All rights reserved.

C:\Users\ANIL KUMAR>cd\

C:\>cd xampp

C:\xampp>cd mysql

C:\xampp\mysql>cd bin

C:\xampp\mysql\bin>mysql -h localhost -u root -p
Enter password:
ERROR 2002 (HY000): Can't connect to MySQL server on 'localhost' (10061)

C:\xampp\mysql\bin>mysql -u root -h localhost -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.4.27-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| employee           |
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| test               |
+--------------------+
6 rows in set (0.032 sec)

MariaDB [(none)]> use test;
Database changed
MariaDB [test]> show test;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'test' at line 1
MariaDB [test]> shows tables;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'shows tables' at line 1
MariaDB [test]> show tables;
Empty set (0.001 sec)

MariaDB [test]> show tables;
Empty set (0.001 sec)

MariaDB [test]> use employee;
Database changed
MariaDB [employee]> show tables;
+--------------------+
| Tables_in_employee |
+--------------------+
| emp                |
| test               |
+--------------------+
2 rows in set (0.001 sec)

MariaDB [employee]> desc emp
    -> ;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(10)     | NO   | PRI | NULL    | auto_increment |
| firstname | varchar(30) | NO   |     | NULL    |                |
| lastname  | varchar(30) | NO   |     | NULL    |                |
| salary    | int(7)      | NO   |     | NULL    |                |
| mob       | bigint(10)  | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
5 rows in set (0.079 sec)

MariaDB [employee]> desc test;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(3)      | NO   | PRI | NULL    |       |
| name  | varchar(30) | YES  |     | NULL    |       |
| age   | int(2)      | YES  |     | NULL    |       |
| city  | varchar(30) | YES  |     | Noida   |       |
| mob   | bigint(10)  | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.081 sec)

MariaDB [employee]> select * from emp;
+----+-----------+----------+--------+------------+
| id | firstname | lastname | salary | mob        |
+----+-----------+----------+--------+------------+
|  1 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+-----------+----------+--------+------------+
7 rows in set (0.236 sec)

MariaDB [employee]> select * from test;
+----+--------------+------+-----------+------------+
| id | name         | age  | city      | mob        |
+----+--------------+------+-----------+------------+
|  1 | Ramesh Kumar |   35 | Ghaziabad | 8956895269 |
|  2 | Alock Maurya |   40 | Mahoba    | 8978545645 |
|  3 | Jyuti Maurya |   40 | Lucknow   | 9999999999 |
|  4 | Alok Maurya  |   45 | Mahoba    | 7708545645 |
|  5 | Jyuti Rani   |   41 | Rampur    | 5645342311 |
+----+--------------+------+-----------+------------+
5 rows in set (0.001 sec)

MariaDB [employee]> insert into test values(6,"Ravindra",37,Sirathu,8965714569),(7,"Ravi",41,"Latur",7845874589),(8,"Tarun",34,"Aligarh",5689523651);
ERROR 1054 (42S22): Unknown column 'Sirathu' in 'field list'
MariaDB [employee]> insert into test values(6,"Ravindra",37,'Sirathu',8965714569),(7,"Ravi",41,"Latur",7845874589),(8,"Tarun",34,"Aligarh",5689523651);
Query OK, 3 rows affected (0.080 sec)
Records: 3  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from test;
+----+--------------+------+-----------+------------+
| id | name         | age  | city      | mob        |
+----+--------------+------+-----------+------------+
|  1 | Ramesh Kumar |   35 | Ghaziabad | 8956895269 |
|  2 | Alock Maurya |   40 | Mahoba    | 8978545645 |
|  3 | Jyuti Maurya |   40 | Lucknow   | 9999999999 |
|  4 | Alok Maurya  |   45 | Mahoba    | 7708545645 |
|  5 | Jyuti Rani   |   41 | Rampur    | 5645342311 |
|  6 | Ravindra     |   37 | Sirathu   | 8965714569 |
|  7 | Ravi         |   41 | Latur     | 7845874589 |
|  8 | Tarun        |   34 | Aligarh   | 5689523651 |
+----+--------------+------+-----------+------------+
8 rows in set (0.000 sec)

MariaDB [employee]> update test set name=(if name='Ramesh Kumar',"Pooja","XXXXX");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'name='Ramesh Kumar',"Pooja","XXXXX")' at line 1
MariaDB [employee]> update test set name=(if id=1,"Pooja","XXXXX");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'id=1,"Pooja","XXXXX")' at line 1
MariaDB [employee]> update test set city=(if name="Ramesh Kumar","Agra","Pune");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'name="Ramesh Kumar","Agra","Pune")' at line 1
MariaDB [employee]> update test set city=if (name="Ramesh Kumar","Agra","Pune");
Query OK, 8 rows affected (0.092 sec)
Rows matched: 8  Changed: 8  Warnings: 0

MariaDB [employee]> select * fromtest;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'fromtest' at line 1
MariaDB [employee]> select * from test;
+----+--------------+------+------+------------+
| id | name         | age  | city | mob        |
+----+--------------+------+------+------------+
|  1 | Ramesh Kumar |   35 | Agra | 8956895269 |
|  2 | Alock Maurya |   40 | Pune | 8978545645 |
|  3 | Jyuti Maurya |   40 | Pune | 9999999999 |
|  4 | Alok Maurya  |   45 | Pune | 7708545645 |
|  5 | Jyuti Rani   |   41 | Pune | 5645342311 |
|  6 | Ravindra     |   37 | Pune | 8965714569 |
|  7 | Ravi         |   41 | Pune | 7845874589 |
|  8 | Tarun        |   34 | Pune | 5689523651 |
+----+--------------+------+------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> begin;
Query OK, 0 rows affected (0.000 sec)

MariaDB [employee]> update test set name=if(name="Ramesh Kumar","Pooja","Ram Bharose");
Query OK, 8 rows affected (0.039 sec)
Rows matched: 8  Changed: 8  Warnings: 0

MariaDB [employee]> select * from test;
+----+-------------+------+------+------------+
| id | name        | age  | city | mob        |
+----+-------------+------+------+------------+
|  1 | Pooja       |   35 | Agra | 8956895269 |
|  2 | Ram Bharose |   40 | Pune | 8978545645 |
|  3 | Ram Bharose |   40 | Pune | 9999999999 |
|  4 | Ram Bharose |   45 | Pune | 7708545645 |
|  5 | Ram Bharose |   41 | Pune | 5645342311 |
|  6 | Ram Bharose |   37 | Pune | 8965714569 |
|  7 | Ram Bharose |   41 | Pune | 7845874589 |
|  8 | Ram Bharose |   34 | Pune | 5689523651 |
+----+-------------+------+------+------------+
8 rows in set (0.000 sec)

MariaDB [employee]> rollback;
Query OK, 0 rows affected (0.102 sec)

MariaDB [employee]> select * from test;
+----+--------------+------+------+------------+
| id | name         | age  | city | mob        |
+----+--------------+------+------+------------+
|  1 | Ramesh Kumar |   35 | Agra | 8956895269 |
|  2 | Alock Maurya |   40 | Pune | 8978545645 |
|  3 | Jyuti Maurya |   40 | Pune | 9999999999 |
|  4 | Alok Maurya  |   45 | Pune | 7708545645 |
|  5 | Jyuti Rani   |   41 | Pune | 5645342311 |
|  6 | Ravindra     |   37 | Pune | 8965714569 |
|  7 | Ravi         |   41 | Pune | 7845874589 |
|  8 | Tarun        |   34 | Pune | 5689523651 |
+----+--------------+------+------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> select name,city,if(age>40,"You are senior","Junior") as result from test;
+--------------+------+----------------+
| name         | city | result         |
+--------------+------+----------------+
| Ramesh Kumar | Agra | Junior         |
| Alock Maurya | Pune | Junior         |
| Jyuti Maurya | Pune | Junior         |
| Alok Maurya  | Pune | You are senior |
| Jyuti Rani   | Pune | You are senior |
| Ravindra     | Pune | Junior         |
| Ravi         | Pune | You are senior |
| Tarun        | Pune | Junior         |
+--------------+------+----------------+
8 rows in set (0.001 sec)

MariaDB [employee]> update test set city= case id when 2 then "Alighar" when 3 then "Ghaziabad" when 4 then "Noida" when 5 then "Grugram" when 6 then "East Delhi" when 7 then "Prayagraj" else "Sikkim-Darjling" end;
Query OK, 8 rows affected (0.086 sec)
Rows matched: 8  Changed: 8  Warnings: 0

MariaDB [employee]> select * from test;
+----+--------------+------+-----------------+------------+
| id | name         | age  | city            | mob        |
+----+--------------+------+-----------------+------------+
|  1 | Ramesh Kumar |   35 | Sikkim-Darjling | 8956895269 |
|  2 | Alock Maurya |   40 | Alighar         | 8978545645 |
|  3 | Jyuti Maurya |   40 | Ghaziabad       | 9999999999 |
|  4 | Alok Maurya  |   45 | Noida           | 7708545645 |
|  5 | Jyuti Rani   |   41 | Grugram         | 5645342311 |
|  6 | Ravindra     |   37 | East Delhi      | 8965714569 |
|  7 | Ravi         |   41 | Prayagraj       | 7845874589 |
|  8 | Tarun        |   34 | Sikkim-Darjling | 5689523651 |
+----+--------------+------+-----------------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> select concat("Yahoo","Baba","Channel");
+----------------------------------+
| concat("Yahoo","Baba","Channel") |
+----------------------------------+
| YahooBabaChannel                 |
+----------------------------------+
1 row in set (0.001 sec)

MariaDB [employee]> select concat_ws("_","yahoo","Baba","chanel");
+----------------------------------------+
| concat_ws("_","yahoo","Baba","chanel") |
+----------------------------------------+
| yahoo_Baba_chanel                      |
+----------------------------------------+
1 row in set (0.000 sec)

MariaDB [employee]> select concat("_","Yahoo","Baba","Chanel");
+-------------------------------------+
| concat("_","Yahoo","Baba","Chanel") |
+-------------------------------------+
| _YahooBabaChanel                    |
+-------------------------------------+
1 row in set (0.000 sec)

MariaDB [employee]> select concat_ws("_","Yahoo","Baba","Chanel");
+----------------------------------------+
| concat_ws("_","Yahoo","Baba","Chanel") |
+----------------------------------------+
| Yahoo_Baba_Chanel                      |
+----------------------------------------+
1 row in set (0.000 sec)

MariaDB [employee]> select concat_ws(" ","Yahoo","Baba","Chanel");
+----------------------------------------+
| concat_ws(" ","Yahoo","Baba","Chanel") |
+----------------------------------------+
| Yahoo Baba Chanel                      |
+----------------------------------------+
1 row in set (0.000 sec)

MariaDB [employee]> select * from emp;
+----+-----------+----------+--------+------------+
| id | firstname | lastname | salary | mob        |
+----+-----------+----------+--------+------------+
|  1 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+-----------+----------+--------+------------+
7 rows in set (0.001 sec)

MariaDB [employee]> select * from test;
+----+--------------+------+-----------------+------------+
| id | name         | age  | city            | mob        |
+----+--------------+------+-----------------+------------+
|  1 | Ramesh Kumar |   35 | Sikkim-Darjling | 8956895269 |
|  2 | Alock Maurya |   40 | Alighar         | 8978545645 |
|  3 | Jyuti Maurya |   40 | Ghaziabad       | 9999999999 |
|  4 | Alok Maurya  |   45 | Noida           | 7708545645 |
|  5 | Jyuti Rani   |   41 | Grugram         | 5645342311 |
|  6 | Ravindra     |   37 | East Delhi      | 8965714569 |
|  7 | Ravi         |   41 | Prayagraj       | 7845874589 |
|  8 | Tarun        |   34 | Sikkim-Darjling | 5689523651 |
+----+--------------+------+-----------------+------------+
8 rows in set (0.000 sec)

MariaDB [employee]> desc test;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(3)      | NO   | PRI | NULL    |       |
| name  | varchar(30) | YES  |     | NULL    |       |
| age   | int(2)      | YES  |     | NULL    |       |
| city  | varchar(30) | YES  |     | Noida   |       |
| mob   | bigint(10)  | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.020 sec)

MariaDB [employee]> alter table test id change cid int(3);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'id change cid int(3)' at line 1
MariaDB [employee]> alter table test id change cid int;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'id change cid int' at line 1
MariaDB [employee]> alter table test name change emp_name varchar(30);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'name change emp_name varchar(30)' at line 1
MariaDB [employee]> ALTER TABLE TEST CHANGE ID CID INT(3);
Query OK, 8 rows affected (0.909 sec)
Records: 8  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from test;
+------+--------------+------+-----------------+------------+
| CID  | name         | age  | city            | mob        |
+------+--------------+------+-----------------+------------+
|    1 | Ramesh Kumar |   35 | Sikkim-Darjling | 8956895269 |
|    2 | Alock Maurya |   40 | Alighar         | 8978545645 |
|    3 | Jyuti Maurya |   40 | Ghaziabad       | 9999999999 |
|    4 | Alok Maurya  |   45 | Noida           | 7708545645 |
|    5 | Jyuti Rani   |   41 | Grugram         | 5645342311 |
|    6 | Ravindra     |   37 | East Delhi      | 8965714569 |
|    7 | Ravi         |   41 | Prayagraj       | 7845874589 |
|    8 | Tarun        |   34 | Sikkim-Darjling | 5689523651 |
+------+--------------+------+-----------------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> desc test;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| CID   | int(3)      | YES  | UNI | NULL    |       |
| name  | varchar(30) | YES  |     | NULL    |       |
| age   | int(2)      | YES  |     | NULL    |       |
| city  | varchar(30) | YES  |     | Noida   |       |
| mob   | bigint(10)  | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.024 sec)

MariaDB [employee]> alter table test modify cid int(3) primary key auto_increment;
Query OK, 8 rows affected (0.970 sec)
Records: 8  Duplicates: 0  Warnings: 0

MariaDB [employee]> desc test;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| cid   | int(3)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(30) | YES  |     | NULL    |                |
| age   | int(2)      | YES  |     | NULL    |                |
| city  | varchar(30) | YES  |     | Noida   |                |
| mob   | bigint(10)  | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
5 rows in set (0.031 sec)

MariaDB [employee]> select * from emp;
+----+-----------+----------+--------+------------+
| id | firstname | lastname | salary | mob        |
+----+-----------+----------+--------+------------+
|  1 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+-----------+----------+--------+------------+
7 rows in set (0.000 sec)

MariaDB [employee]> select * from test;
+-----+--------------+------+-----------------+------------+
| cid | name         | age  | city            | mob        |
+-----+--------------+------+-----------------+------------+
|   1 | Ramesh Kumar |   35 | Sikkim-Darjling | 8956895269 |
|   2 | Alock Maurya |   40 | Alighar         | 8978545645 |
|   3 | Jyuti Maurya |   40 | Ghaziabad       | 9999999999 |
|   4 | Alok Maurya  |   45 | Noida           | 7708545645 |
|   5 | Jyuti Rani   |   41 | Grugram         | 5645342311 |
|   6 | Ravindra     |   37 | East Delhi      | 8965714569 |
|   7 | Ravi         |   41 | Prayagraj       | 7845874589 |
|   8 | Tarun        |   34 | Sikkim-Darjling | 5689523651 |
+-----+--------------+------+-----------------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> alter table test drop column name varchar;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'varchar' at line 1
MariaDB [employee]> alter table test drop column name;
Query OK, 0 rows affected (0.160 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from test;
+-----+------+-----------------+------------+
| cid | age  | city            | mob        |
+-----+------+-----------------+------------+
|   1 |   35 | Sikkim-Darjling | 8956895269 |
|   2 |   40 | Alighar         | 8978545645 |
|   3 |   40 | Ghaziabad       | 9999999999 |
|   4 |   45 | Noida           | 7708545645 |
|   5 |   41 | Grugram         | 5645342311 |
|   6 |   37 | East Delhi      | 8965714569 |
|   7 |   41 | Prayagraj       | 7845874589 |
|   8 |   34 | Sikkim-Darjling | 5689523651 |
+-----+------+-----------------+------------+
8 rows in set (0.001 sec)

MariaDB [employee]> alter table test drop column mob;
Query OK, 0 rows affected (0.146 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from test;
+-----+------+-----------------+
| cid | age  | city            |
+-----+------+-----------------+
|   1 |   35 | Sikkim-Darjling |
|   2 |   40 | Alighar         |
|   3 |   40 | Ghaziabad       |
|   4 |   45 | Noida           |
|   5 |   41 | Grugram         |
|   6 |   37 | East Delhi      |
|   7 |   41 | Prayagraj       |
|   8 |   34 | Sikkim-Darjling |
+-----+------+-----------------+
8 rows in set (0.001 sec)

MariaDB [employee]> alter table test change city emp_city varchar(50);
Query OK, 0 rows affected (0.139 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from test;
+-----+------+-----------------+
| cid | age  | emp_city        |
+-----+------+-----------------+
|   1 |   35 | Sikkim-Darjling |
|   2 |   40 | Alighar         |
|   3 |   40 | Ghaziabad       |
|   4 |   45 | Noida           |
|   5 |   41 | Grugram         |
|   6 |   37 | East Delhi      |
|   7 |   41 | Prayagraj       |
|   8 |   34 | Sikkim-Darjling |
+-----+------+-----------------+
8 rows in set (0.000 sec)

MariaDB [employee]> select * from emp;
+----+-----------+----------+--------+------------+
| id | firstname | lastname | salary | mob        |
+----+-----------+----------+--------+------------+
|  1 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+-----------+----------+--------+------------+
7 rows in set (0.002 sec)

MariaDB [employee]> alter table emp add city_id int(3);
Query OK, 0 rows affected (0.127 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [employee]> select *from emp;
+----+-----------+----------+--------+------------+---------+
| id | firstname | lastname | salary | mob        | city_id |
+----+-----------+----------+--------+------------+---------+
|  1 | Ravi      | Kumar    |  50000 | 2323453735 |    NULL |
|  2 | Pooja     | Devi     | 100000 | 9856985698 |    NULL |
|  3 | Prakash   | Raj      |  55000 | 5658978546 |    NULL |
|  4 | Deepak    | Kumar    |  40000 | 1245214521 |    NULL |
|  5 | Rakhi     | Rao      |  35000 | 4512451252 |    NULL |
|  6 | Hari      | Narayan  |  60000 | 1212121210 |    NULL |
|  7 | Prakash   | Jha      |  51000 | 5652535652 |    NULL |
+----+-----------+----------+--------+------------+---------+
7 rows in set (0.001 sec)

MariaDB [employee]> alter table emp modify city_id int(3) before firstname;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'before firstname' at line 1
MariaDB [employee]> alter table emp modify city_id before firstname;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'before firstname' at line 1
MariaDB [employee]> alter table emp modify city_id int(3) after id;
Query OK, 0 rows affected (0.169 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from emp;
+----+---------+-----------+----------+--------+------------+
| id | city_id | firstname | lastname | salary | mob        |
+----+---------+-----------+----------+--------+------------+
|  1 |    NULL | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 |    NULL | Pooja     | Devi     | 100000 | 9856985698 |
|  3 |    NULL | Prakash   | Raj      |  55000 | 5658978546 |
|  4 |    NULL | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 |    NULL | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 |    NULL | Hari      | Narayan  |  60000 | 1212121210 |
|  7 |    NULL | Prakash   | Jha      |  51000 | 5652535652 |
+----+---------+-----------+----------+--------+------------+
7 rows in set (0.001 sec)

MariaDB [employee]> update emp set city_id= case id when 1 then 2 when 2 then 4 when 3 then 7 when 4 then 5 when 5 then 2 when 6 then 4 else 7 end;
Query OK, 7 rows affected (0.101 sec)
Rows matched: 7  Changed: 7  Warnings: 0

MariaDB [employee]> select *n from emp;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'n from emp' at line 1
MariaDB [employee]> select * from emp;
+----+---------+-----------+----------+--------+------------+
| id | city_id | firstname | lastname | salary | mob        |
+----+---------+-----------+----------+--------+------------+
|  1 |       2 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 |       4 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 |       7 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 |       5 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 |       2 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 |       4 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 |       7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+---------+-----------+----------+--------+------------+
7 rows in set (0.000 sec)

MariaDB [employee]> alter table emp add foreign key(city_id) references(cid);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '(cid)' at line 1
MariaDB [employee]> alter table emp add foreign key(city_id) refrences test(cid);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'refrences test(cid)' at line 1
MariaDB [employee]> select * from test;
+-----+------+-----------------+
| cid | age  | emp_city        |
+-----+------+-----------------+
|   1 |   35 | Sikkim-Darjling |
|   2 |   40 | Alighar         |
|   3 |   40 | Ghaziabad       |
|   4 |   45 | Noida           |
|   5 |   41 | Grugram         |
|   6 |   37 | East Delhi      |
|   7 |   41 | Prayagraj       |
|   8 |   34 | Sikkim-Darjling |
+-----+------+-----------------+
8 rows in set (0.001 sec)

MariaDB [employee]> alter table emp add foreign key(city_id) refrences test(cid);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'refrences test(cid)' at line 1
MariaDB [employee]> alter table emp add foreign key(city_id) references test(cid);
Query OK, 7 rows affected (1.017 sec)
Records: 7  Duplicates: 0  Warnings: 0

MariaDB [employee]> select * from emp;
+----+---------+-----------+----------+--------+------------+
| id | city_id | firstname | lastname | salary | mob        |
+----+---------+-----------+----------+--------+------------+
|  1 |       2 | Ravi      | Kumar    |  50000 | 2323453735 |
|  2 |       4 | Pooja     | Devi     | 100000 | 9856985698 |
|  3 |       7 | Prakash   | Raj      |  55000 | 5658978546 |
|  4 |       5 | Deepak    | Kumar    |  40000 | 1245214521 |
|  5 |       2 | Rakhi     | Rao      |  35000 | 4512451252 |
|  6 |       4 | Hari      | Narayan  |  60000 | 1212121210 |
|  7 |       7 | Prakash   | Jha      |  51000 | 5652535652 |
+----+---------+-----------+----------+--------+------------+
7 rows in set (0.002 sec)

MariaDB [employee]> select * from test;
+-----+------+-----------------+
| cid | age  | emp_city        |
+-----+------+-----------------+
|   1 |   35 | Sikkim-Darjling |
|   2 |   40 | Alighar         |
|   3 |   40 | Ghaziabad       |
|   4 |   45 | Noida           |
|   5 |   41 | Grugram         |
|   6 |   37 | East Delhi      |
|   7 |   41 | Prayagraj       |
|   8 |   34 | Sikkim-Darjling |
+-----+------+-----------------+
8 rows in set (0.000 sec)

MariaDB [employee]> select concat(e.firstname,e.lastname) as emp_name,t.age,e.mob,e.salary,t.emp_city from emp as e inner join test as t on e.city_id=t.cid;
+-------------+------+------------+--------+-----------+
| emp_name    | age  | mob        | salary | emp_city  |
+-------------+------+------------+--------+-----------+
| RaviKumar   |   40 | 2323453735 |  50000 | Alighar   |
| PoojaDevi   |   45 | 9856985698 | 100000 | Noida     |
| PrakashRaj  |   41 | 5658978546 |  55000 | Prayagraj |
| DeepakKumar |   41 | 1245214521 |  40000 | Grugram   |
| RakhiRao    |   40 | 4512451252 |  35000 | Alighar   |
| HariNarayan |   45 | 1212121210 |  60000 | Noida     |
| PrakashJha  |   41 | 5652535652 |  51000 | Prayagraj |
+-------------+------+------------+--------+-----------+
7 rows in set (0.001 sec)

MariaDB [employee]> ^S