# what is SQL ?
 1. sql stands for structured query language 
 2. sql is case-insenstive language 
    examples :
    ```    
     insert or INSERT  or Insert
 
    ``` 
 3. sql is used to create database | table structure 
 4. sql is fast and create structure
 5. sql is no-procedural based language  
 6. sql is join a tables 
 7. sql create store proceedures 
 8. sql create a view 
 9. sql is create  and manage a structures type of data

# types of sql commands or query 

 1. DDL (data definition language)
 2. DML (data manupulation language) 
 3. DQL (data query language)
 4. TCL (transactional control language)
  
 
 ## DDL (data query language) 
  ```
  DDL stands for data definition language 
  DDL create database and tables structures 
  DDL are used to provides some query 
  examples : 1) create 2)  alter 3) rename 4) truncate 5) drop 6) change
  ```


## what is database

  ``` 
  A database is used to stored an information of user in form of tables i.e called database.

  ```

## what is table   

 ```
  A table can contain column and rows and give us a structure data formate 

 ```


1. how to create a database   
    **syntax**

    ```
    create database database name;

    **examples**
     
     create database flipkart_db;
     or 
     create database amazondb;

    ```             

    
1. how to create a table in  database   
    **syntax**

    ```
      create table tablename
      (
         id datatype(size) primary key auto_increment,
         name datatype(size),
         email datatype(size),
         password datatype(size)

      )    
    **examples**

    create table users
    (
     id int AUTO_INCREMENT PRIMARY key,
     name varchar(155),
     email varchar(255),    
     password varchar(200)
    
    )


    or


    create table feedback
    (
    id int AUTO_INCREMENT PRIMARY key,
    name varchar(155),
    email varchar(255),    
    subject varchar(255),
    phone bigInt,
    comment text       
    )
     
    ```             


## chart of tables of data types 

 1.  char 
 2.  varchar
 3.  int 
 4.  bigInt
 5.  float
 6.  blob 
 7.  date 
 8.  datetime
 9.  text 
 10. enum    
