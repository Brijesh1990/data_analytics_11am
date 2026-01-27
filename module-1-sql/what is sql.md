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
