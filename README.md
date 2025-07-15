# Halogenase Data Base

This database contains information for the halogenase annotation package.
The repository offers two solutions for browsing the data.

## Simple solution
If you don't have PgSQL set up, just run the app.py in the **read_in_database** folder:

**python3 read_in_database/app.py**

## You are a pgAdmin user
If you would like to use the database to add your own notes as well and you have PostgreSQL set up, then your path leads through the **connection_database** path.

* Import the database file into your local DB
* Create a **.env** file and add it to **.gitignore**
    * This file should contain two variables: **SECRET_KEY** and **DATABASE_URL**
    * **SECRET_KEY** is the password to your DB
    * **DATABASE_URL** is the route to your DB
* Run **python3 connection_database/app.py**
* If you want to use the json solution with your own data, you can use the **db_to_json** script in the **read_in_database** folder to export the data into one json file

_The author of this repository was trying to avoid vibe-coding, but occasionally general ChatGPT and Claude Sonnet 4 was used to figure out the infrastructure of the app._