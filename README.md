<h1>Project_1_350</h1>

This is group 2 and we are working on a PostgreSQL database about [ toxicity ], of
substances and products.

We're primarily working with this data set: https://catalog.data.gov/dataset/chemicals-in-cosmetics-2a971

This dataset tracks cosmetics products sold in California that the state has found to be toxic.

This project contains:

- A small python program that parses csv files into insert statements (insert_gen.py and compare.py)
- A sql file for creating relations in a database (createDB.sql)
- A sql file for inserting data into the created database (inserts.sql)

**We all have 1 function and 1 procedure for each task based on the tables we each did.**

The seven tables are the following:

- Brand
- Chemical
- Chemical_List
- Company
- Primary_Category
- Product
- Sub_Category

<h2>Starting the project via postgresql. </h2>

```bash
sudo -u postgres psql
CREATE DATABASE (whatever DB name you choose here);
\l (To check if Database was actually added)
\q (exit)

CREATE DATABASE northwind;


psql -U (username) -d (database) -h localhost
\i createDB.sql (creating tables, schema etc.)
\i inserts.sql (insert data)
\dt (checks if tables are actually added)
\q (exit)


# The other way of starting the project is to use the backup file that we have submitted which is an SQL file for loading up the DataBase.
```

Now load up PGadmin and you should be able to see your database.

**Note:** Don't try to load this via pgAdmin with the query tool as there will be an error stopping it with duplicate key values. This is why PostgreSQL is recommended as it will still show the error, but it will be ignored and still proceed with inserting the data unlike the query tool stopping you in pgAdmin.
