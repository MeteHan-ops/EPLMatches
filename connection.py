import mysql.connector
connection = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "mysql1234",
    database = "matches_history"
)
mycursor = connection.cursor()
