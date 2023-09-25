# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='theotms',
    password='pass_word',
    database='flight_game',
    autocommit=True
)

iso_country = input("What's the area code? ").upper()
sql = f"SELECT name, type FROM airport WHERE iso_country = '{iso_country}' order by type;"
print(sql)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
