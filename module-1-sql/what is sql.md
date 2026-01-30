# What is SQL?

1. SQL stands for Structured Query Language
2. SQL is case-insensitive language
   - Examples: `INSERT`, `insert`, or `Insert`
3. SQL is used to create database and table structures
4. SQL is fast and creates structure
5. SQL is a non-procedural based language
6. SQL joins tables
7. SQL creates stored procedures
8. SQL creates views
9. SQL creates and manages structured data types

# Types of SQL Commands or Queries

1. **DDL** (Data Definition Language)
2. **DML** (Data Manipulation Language)
3. **DQL** (Data Query Language)
4. **TCL** (Transactional Control Language)

## DDL (Data Definition Language)

DDL stands for Data Definition Language. It is used to create databases and table structures. DDL provides the following operations:

1. **CREATE** - Create database and tables
2. **ALTER** - Modify table structure
3. **RENAME** - Rename tables
4. **TRUNCATE** - Delete all records
5. **DROP** - Delete table
6. **CHANGE** - Change column properties

## What is Database?

A database is used to store user information in the form of tables.

## What is Table?

A table contains columns and rows, providing a structured data format.

## How to Create a Database

**Syntax:**
```sql
CREATE DATABASE database_name;
```

**Examples:**
```sql
CREATE DATABASE flipkart_db;
CREATE DATABASE amazondb;
```

## How to Create a Table in Database

**Syntax:**
```sql
CREATE TABLE tablename (
    id DATATYPE(size) PRIMARY KEY AUTO_INCREMENT,
    name DATATYPE(size),
    email DATATYPE(size),
    password DATATYPE(size)
);
```

**Example 1 - Users Table:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(155),
    email VARCHAR(255),
    password VARCHAR(200)
);
```

**Example 2 - Feedback Table:**
```sql
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(155),
    email VARCHAR(255),
    subject VARCHAR(255),
    phone BIGINT,
    comment TEXT
);
```

## Data Types in SQL

| Data Type | Description |
|-----------|-------------|
| CHAR | Fixed-length character string |
| VARCHAR | Variable-length character string |
| INT | Integer |
| BIGINT | Large integer |
| FLOAT | Floating-point number |
| BLOB | Binary large object |
| DATE | Date |
| DATETIME | Date and time |
| TEXT | Text data |
| ENUM | Enumerated list |

## Table Column Guidelines

| Column Name | Data Type | Size | Notes |
|-------------|-----------|------|-------|
| id | INT | (11) | Default size with AUTO_INCREMENT |
| name | CHAR, VARCHAR | (0-255) | For names |
| password | VARCHAR | (0-255) | For passwords |
| age | INT | - | For age values |
| price | INT, FLOAT | - | For prices |
| date & time | VARCHAR, DATE, DATETIME | - | For temporal data |
| status | VARCHAR | - | For status information |
| address | TEXT | - | For longer text |
| comment | TEXT | - | For comments |
| photo, image | VARCHAR, BLOB | - | For file references or binary data |
| multiple selection | ENUM, VARCHAR | - | For enumerated or comma-separated values |
| mobile, phone | BIGINT | (20) | Default size for phone numbers |

**Example - Employee Table:**
```sql
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    empname VARCHAR(255),
    password VARCHAR(255),
    age INT,
    mobile BIGINT,
    salary FLOAT,
    department VARCHAR(255),
    country VARCHAR(255),
    state VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);
```

## ALTER Command

ALTER is used to add, modify, and update column names after creating a table.

### 1. Add New Column to Existing Table

**Syntax:**
```sql
ALTER TABLE tablename ADD columnname DATATYPE(size);
```

**Example:**
```sql
ALTER TABLE employee ADD pin INT;
```

### 2. Add Column After Specific Column

**Example:**
```sql
ALTER TABLE employee ADD photo VARCHAR(255) AFTER empname;
```

### 3. Modify or Change Column Properties

**Example:**
```sql
ALTER TABLE employee CHANGE mobile phone BIGINT;
```

## RENAME Command

RENAME is used to rename or change an existing table name.

**Syntax:**
```sql
RENAME TABLE old_table_name TO new_table_name;
```

**Examples:**
```sql
RENAME TABLE employee TO tbl_employee;
RENAME TABLE users TO tbl_users;
```


## 6) TRUNCATE - Removing Table Data or clear all data from tables

Used to remove or empty all data from tables.

### Syntax
```sql
TRUNCATE TABLE tbl_country;
```
**Note:** After truncate, data cannot be rolled back.

## 7) DROP - Delete Database and Tables structure after drop can not be rollback

Used to delete database and table structures.

### Syntax

**a) Drop a database:**
```sql
DROP DATABASE flipkart_db;
```

**b) Drop a table:**
```sql
DROP TABLE tbl_country;
``` 

## DML (data manipulation language)
   
   DML is used to manipulate data meanse insert | delete | update data in a table   

   examples : insert | delete | update

  1. insert a data  in tables 

     ## single data insert 
      ``` 
      insert into tablename (columnname) values('value')
      ```
      **query**
      ```
      insert into tbl_feedback(name,email,subject,phone,comment) values('paree','paree@gmail.com','24x7 customer care support',9121212158,'help me to return products')

      ```

    ## multiple data insert 
      ``` 
      insert into tablename (columnname) values('value1'),('value2'),('value3')
      ```
      **query**
      ```
      insert into tbl_feedback(name,email,subject,phone,comment) values('punit','punit@gmail.com','24x7 customer care support',983845654,'help me to return products'),('brijesh','brijesh@gmail.com','24x7 customer care support',989845654,'help me to return products'),('kumar','kumar@gmail.com','24x7 customer care support',983845659,'help me to return products')

      ```
 2. delete a data  in tables
    
    delete is used to delete a data from tables 
    
    **delete all data**
    ```
    delete from tablename
    ```
    examples:
    ```
    delete from tbl_feedback
    ```
    **delete particular data**
    ```
    delete from tbl_feedback where id=3;
    ```
    **delete between data**
    ```
     delete from tbl_feedback where id between 3 and 20;
     ```
    **delete alternate data**
    ```
     delete from tbl_feedback where id in(3,5,7,9);
    ```
3. update data : update is used to update any data from tables
   **update data**
   ```
   update tbl_feedback set name='mukesh',email='mukesh@gmail.com',subject='hi customers',comment='hi i am mukesh' where id=4;
   ```    

## 3. DQL (data query  language)
   
    DQL stands for data query language it is used to fetch data or select data from tables.

**select**

**select all data**
```
select * from tbl_feedback

```
**select particular with column name**
```
select id,name,email from tbl_feedback

```
**select particular with id**
```
select  * from tbl_feedback where id=1;
```
**select particular between data**
```
select  * from tbl_feedback where between 1 and 100;
```

**select particular in operator data**
```
select * from tbl_feedback where id in(1,2);
```

**select particular data using limit**
```
select * from tbl_feedback where id limit 0,2;

```

**select particular data using order by(filter data) in ASC or DESC order**
```
select * from tbl_feedback order by name ASC;
or
select * from tbl_feedback order by name DESC;
or
select * from tbl_feedback order by name;

```


**searching data using like operator**

```
searching data start name of 'a' character

1. select * from tbl_feedback where name like 'a%';
or
2. select * from tbl_feedback where name like 'p%';

searching data end name of 'e' character

3. select * from tbl_feedback where name like '%e';

searching data start or end anywhere name of 'a' character

4. select * from tbl_feedback where name like '%a%';

```


**sql function**
sql function are two types 

1. aggrigate function 
   
   **query**
   **examples**
   1. count
   2. sum
   3. max
   4. min 
   5. avg

2. scalar function 
   **query**
   **examples**
   1. first (first is not supported in mysql it support in oracle)
   2. last  (last is not supported in mysql it support in oracle)
   3. lcase
   4. ucase
   

 **all query of function**

 ```
  1. select max(salary) as highest_salary from tbl_employee;
  
  2. select min(salary) as minimum_salary from tbl_employee;
  
  3. select count(employee_id) as total_number_employee from tbl_employee;

  4. select sum(salary) as total_sum_salary from tbl_employee;
 
  5. select avg(salary) as total_average_salary from tbl_employee;

  6. select first(empname)  from tbl_employee;

  7. select last(empname)  from tbl_employee;

  8. select ucase(empname)  from tbl_employee;

  9. select lcase(empname)  from tbl_employee;

 ```   

**subquery in sql**

subquery meanse query within another query 

**examples of subquery**

```
 select max(salary) as second_highest_salary from tbl_employee where salary < (select max(salary) from tbl_employee);

```

## TCL : transactional query language 
 
     1) commit
        commit will be used to save any data after delete 
    
      **query**
 
      ```
      start TRANSACTION;
      delete from tbl_feedback where id=4;
      commit;
      
      ```

     2) rollback 

        after delete we rollback our data using rollback

        **query**

        ```
        start TRANSACTION;
        select * from tbl_feedback where id=4;
        rollback;

        ```

        **Note**
         rollback only support in oracle mysql is not supported



## normalisation in SQL ...

1.  Normalization is used to removed redundancy(dublicate data formate) data formate from tables
2.  Normalization is used to provide relationship between one tables to another table
3.  Normalization is used to create a Normalized formate of any tables 

## types of normalization...

1. 1-NF (Normalized form) 
2. 2-NF (Normalized form)
3. 3-NF (Normalized form) 
4. 4-NF (Normalized form)
5. 5-NF (Normalized form)  


1. create a 1-NF (basic information about table with primary key)

   **users**

| user_id(pk) | email | age     | salary | department|
|-------------|-------|----|-----|--------------------|    
|1            |b@gmail.com| 34  | Rs.89500|IT        |   




