# lamp_0

# Setup
```
install mysql

create database tutorial;
create table users (id int, Name varchar(255), Birthday varchar(255), KG varchar(255));
INSERT INTO users (Name, Birthday, KG) = VALUES (“tommy”,"2000/02/26", “d-hacks");
```

#Result
* send get request to [http://localhost:5000/](http://localhost:5000/) then you'll get
```
{"Name": "tommy", "Birthday": "2000/02/26", "KG": "d-hacks"}
```
