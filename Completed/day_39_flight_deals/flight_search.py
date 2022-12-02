import requests
from flight_data import FlightData

KIWI_ENDPOINT = "KIWI TEQUILA END POINT"      # KIWI TEQUILA END POINT
KIWI_API_KEY = "KIWI TEQUILA API KEY"   # KIWI TEQUILA API KEY


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        SEARCH_END_POINT = f"{KIWI_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=SEARCH_END_POINT, headers=headers, params=query)
        results = response.json()
        print(results)
        code = results["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "GBP"
        }
        response = requests.get(
            url=f"{KIWI_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        print(f"{flight_data.out_date} - {flight_data.return_date}")
        return flight_data