from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

MY_CITY_CODE = "VNO"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_destonation_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
print(tomorrow)
print(six_month_from_today)
hour =  datetime.now().hour
minute = datetime.now().minute
# You can set here which hour of the day should check for flights and send sms if find any.
if hour == hour and minute == minute:

    for destination in sheet_data:
        flight = flight_search.check_flights(
            MY_CITY_CODE,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight.price < destination["lowestPrice"]:
            msg = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            print(msg)
            NotificationManager(messages=msg)

