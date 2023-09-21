# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new
# airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport
# information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If
# the user chooses to quit, the program execution ends. The user can choose a new option as many times they want
# until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example,
# the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

airports = {}

while True:
  need = input("Do you want to add and airport, fetch or quit? ")

  if need == "add":
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    airport_name = input("Enter the name of the airport: ")
    airports[icao_code] = airport_name
    print(f"Airport data for {icao_code} ({airport_name}) has been added.")

  elif need == "fetch":
    icao_code = input("Enter the ICAO code of the airport to fetch information: ").strip().upper()

    if icao_code in airports:
      airport_name = airports[icao_code]
      print(f"The name of the airport with ICAO code {icao_code} is: {airport_name}")

    else:
      print(f"No airport data found for ICAO code {icao_code}.")

  elif need == "quit":
    print("Exiting the program.")
    break

  else:
    print("Invalid choice. Please add, fetch or quit.")