import mysql.connector
import pandas as pd
import numpy as np

connection = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "mysql1234",
    database = "matches_history"
)
mycursor = connection.cursor()
# sql = "CREATE DATABASE matches_history"
# mycursor.execute(sql)
df = pd.read_csv("eplmatches.csv")
colums = df.columns  #list
#control Enum sql datatype
sql = f"CREATE TABLE eplmatches (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
{colums[0]} VARCHAR(255),\
{colums[1]}  VARCHAR(255),\
    {colums[2]} DATETIME,\
        {colums[3]} VARCHAR(255),\
        {colums[4]} VARCHAR(255),\
        {colums[5]} VARCHAR(255),\
        {colums[6]} VARCHAR(255),\
        {colums[7]} ENUM('H','D','A')\
            )"

# mycursor.execute(sql)

