# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='theotms',
    password='pass_word',
    autocommit=True
)

def showairport(icao):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The ICAO {row[0]} corresponds to {row[1]} and the municipality is {row[2]}.")
    return

icao = input("What's the ICAO of the airport? ")
showairport(icao)
