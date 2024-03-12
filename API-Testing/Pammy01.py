import requests


def main():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1337")

    # Check if the request was successful
    if response.status_code == 200:
        print("Booking details retrieved successfully.")
    else:
        print(f"Failed to retrieve booking details. Status code: {response.status_code}")

    # Here, you can handle different status codes as needed
    # For example, checking for a 404 (Not Found) or a 500 (Server Error) specifically
    # and handling those cases accordingly.


if __name__ == "__main__":
    main()