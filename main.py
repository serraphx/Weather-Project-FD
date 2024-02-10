import json
import requests

# Global constants for API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
APPID = "Your_API_Key_Here"  # Replace with your actual API key

# Collects user input
def user_input():
    valid_inputs = ['1', '2', '3']
    user_choice = input(
        "\nTo search by city name press 1, to search by zip press 2, if you would like to exit press 3:\n "
    )

    while user_choice not in valid_inputs:
        print("\nInvalid input. Please try again.\n")
        user_choice = input(
            "To search by city name press 1, to search by zip press 2, if you would like to exit press 3: "
        )

    if user_choice == '3':
        print('Thank you for using my program!')
        return  # Exit the function instead of the program

    fetch_data(user_choice)

# Determines if the search is by city or zip
def fetch_data(choice):
    search_term = input("\nEnter the search term (city name or zip code):\n")
    if choice in ['1', '2']:
        fetch_json(choice, search_term)
    else:
        print('Thank you for using my program!')

# Fetch JSON with city name or zip code
def fetch_json(choice, search_term):
    if choice == '1':
        param = f"q={search_term}"
    elif choice == '2':
        param = f"zip={search_term},us"

    url = f"{BASE_URL}?{param}&units=imperial&APPID={APPID}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        unformatted_data = response.json()

        temp = unformatted_data["main"]["temp"]
        temp_max = unformatted_data["main"]["temp_max"]

        print("\nConnection successful!\n")
        print(f"The current temp is: {temp}")
        print(f'The max temp is: {temp_max}')
    except requests.exceptions.HTTPError as e:
        print("\nFailed to connect. HTTP Error:", e)
    except KeyError:
        print("\nFailed to retrieve the data. The search term might be incorrect.")

    repeat()

# Allows user to repeat program
def repeat():
    valid_inputs = ['1', '2']
    user_repeat = input(
        "\nWould you like to search again? Press 1 for yes, 2 for no: ")

    while user_repeat not in valid_inputs:
        print("Invalid input.")
        user_repeat = input(
            "Would you like to search again? Press 1 for yes, 2 for no: "
        )

    if user_repeat == '1':
        user_input()
    else:
        print('Thank you for using my program!')

def main():
    print(
        "Welcome to my weather program! I can look up the weather by city or zip code."
    )
    user_input()

if __name__ == "__main__":
    main()
