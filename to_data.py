import csv
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

from createdb import connection,mycursor,df
df_colums = df.columns
# print(type(df_colums))
def csv_to_db():
    my_conn = create_engine("mysql+mysqldb://root:mysql1234@localhost/matches_history")
    df.to_sql(con = my_conn,name = "eplmatches",if_exists="append",index=False)

def addMatch(list):
    sql = "INSERT INTO eplmatches(Season_End_Year,Wk,Date,\
        Home,HomeGoals,AwayGoals,Away,FTR)\
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (list)
    mycursor.execute(sql,values)
    try:
        connection.commit()
        print("Your record has been saved {}".format(mycursor.rowcount))  #cursor.rowcount ile kaç tane kayıt eklendiğini görüyorum
        print(f"last row id is :{mycursor.lastrowid}")

    except mysql.connector.Error as err:
        print("Error",err)
    finally:
        connection.close()
        print("Database Closed..")



