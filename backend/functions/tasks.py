from datetime import datetime, timezone
import dotenv
dotenv.load_dotenv()
import os
from pyflightdata import FlightData
import requests



def get_local_time():
    return datetime.now().strftime("day/month: %d/%m clock: %H:%M:%S")

def get_flight_info(origin, destination):
    f=FlightData()
    f.login(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
    
    flights = [{'departure_time': flight['time']['scheduled']['departure_time'] + " " + flight['time']['scheduled']['departure_date']} for flight in f.get_flights_from_to(origin=origin, destination=destination) if datetime.strptime(flight['time']['scheduled']['departure_date'] + ' ' + flight['time']['scheduled']['departure_time'], "%Y%m%d %H%M").replace(tzinfo=timezone.utc) > datetime.now(timezone.utc)]

    for flight in flights:
        time = datetime.strptime(flight['departure_time'], "%H%M %Y%m%d")
        time = time.replace(tzinfo=timezone.utc).astimezone()
        flight['departure_time'] = time.strftime("%H:%M %d/%m/%y")
    
    return flights[0]["departure_time"] if flights else "No flights available"
def get_weather_info(city="Bergen"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=794b42e3bf6a12a7eeac83d5886a9294&units=metric"

    response = requests.get(url).json()

    return "Weather in " + city + ": " + response["weather"][0]["description"] + ", degrees: " + str(response["main"]["temp"]) + "C, feels like: " + str(response["main"]["feels_like"]) + "C, humidity: " + str(response["main"]["humidity"]) + "%"



def get_cheapest_flight(origin, destination):
    url = "https://skyscanner80.p.rapidapi.com/api/v1/flights/search-one-way"

    from_id = find_airport_id(origin)
    to_id = find_airport_id(destination)
    depart_date = datetime.now(UTC).strftime("%Y-%m-%d")

    querystring = {"fromId":from_id,"toId":to_id,"departDate":depart_date,"adults":"1","currency":"USD","market":"US","locale":"en-US"}

    headers = {
	    "X-RapidAPI-Key": "dcdc53af85msh365c2e7df63f3a1p1c1125jsn09a2b383ea11",
	    "X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
    }

    response =  requests.get(url, headers=headers, params=querystring).json()
    flights = response["data"]["itineraries"]
    lowest_price_flight = [flight for flight in flights if flight["price"]["raw"] == min([flight["price"]["raw"] for flight in flights])][0]

    marketing_carrier_name = lowest_price_flight['legs'][0]['carriers']['marketing'][0]['name']
    formatted_price = lowest_price_flight['price']['formatted']
    departure_time = lowest_price_flight['legs'][0]['departure']

    return marketing_carrier_name, formatted_price, departure_time



def find_airport_id(city):
    url = "https://skyscanner80.p.rapidapi.com/api/v1/flights/auto-complete"

    querystring = {"query":city,"market":"US","locale":"en-US"}

    headers = {
	    "X-RapidAPI-Key": "dcdc53af85msh365c2e7df63f3a1p1c1125jsn09a2b383ea11",
	    "X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
    }
    
    return requests.get(url, headers=headers, params=querystring).json()["data"][0]["id"]


