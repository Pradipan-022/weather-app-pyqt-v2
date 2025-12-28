import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

API_keys = ["ENTER API KEY 1",
            "ENTER API KEY 2",
            "ENTER API KEY 3"
            ]

BASE_URL_CURRENT = "https://api.weatherapi.com/v1/current.json"
BASE_URL_HISTORY = "https://api.weatherapi.com/v1/history.json"

# COORDINATES WAS WRITTEN FOR OPENWEATHER. GREEDY COMPANY DEMANDS MONEY FOR SIMPLE 1 WEEK HISTORICAL DATA API CALL
# def get_coordinates(city):
#     for key in API_keys:
#         try:
#             parameters ={"key": key, "q":city}
        
#             response = requests.get(BASE_URL_CURRENT, params=parameters)
#             if response.status_code != 200: # to try next API key if 1st doesnt work
#                 continue
            
#             data = response.json()
#             if "coord" not in data:
#                 raise ValueError(f"City '{city}' not found.") #error raised for city name not found
            
#             lat = data["coord"]["lat"]
#             lon = data["coord"]["lon"]
#             return lat, lon, key
#         except requests.exceptions.RequestException: #if network timeout happens(slow ass internet)
#             continue
    
#     raise Exception("All API keys failed or API limit reached")

def get_current_weather(city):
    
    if city.lower() == "simulation":
        return get_simulated_current_weather()
    for key in API_keys:
        try:
            parameters = {
                "key": key,
                "q": city
            }

            response = requests.get(BASE_URL_CURRENT, params=parameters)

            if response.status_code != 200: 
                continue

            data = response.json()

            weather_dict = {
                "city": city,
                "temperature": data["current"]["temp_c"],
                "humidity": data["current"]["humidity"],
                "pressure": data["current"]["pressure_mb"],
                "wind_speed": data["current"]["wind_kph"],
                "description": data["current"]["condition"]["text"]
            }

            return pd.DataFrame([weather_dict])

        except requests.exceptions.RequestException: #NETWORK
            continue

    raise Exception("All API keys failed")

def get_historical_weather(city, days=7):
    if city.lower() == "simulation":
        return get_simulated_historical_weather()
    
    historical_data = []

    for i in range(1, days + 1):
        date_obj = datetime.now() - timedelta(days=i)
        date_str = date_obj.strftime("%Y-%m-%d")

        for key in API_keys:
            try:
                params = {
                    "key": key,
                    "q": city,
                    "dt": date_str
                }

                response = requests.get(BASE_URL_HISTORY, params=params)

                if response.status_code != 200:
                    continue

                data = response.json()
                day = data["forecast"]["forecastday"][0]["day"]
                astro = data["forecast"]["forecastday"][0]["astro"]

                historical_data.append({
                    "date_iso": date_obj,
                    "date": date_obj.strftime("%Y-%m-%d"),
                    "avg_temp": day["avgtemp_c"],
                    "min_temp": day["mintemp_c"],
                    "max_temp": day["maxtemp_c"],
                    "humidity": day["avghumidity"],
                    "max_wind": day["maxwind_kph"],
                    "precipitation": day.get("totalprecip_mm", 0),
                    "chance_of_rain": day.get("daily_chance_of_rain", 0),
                    "uv": day.get("uv", 0),
                    "condition": day["condition"]["text"],
                    "sunrise": astro.get("sunrise", ""),
                    "sunset": astro.get("sunset", ""),
                    "moonrise": astro.get("moonrise", ""),
                    "moonset": astro.get("moonset", ""),
                    "moon_phase": astro.get("moon_phase", ""),
                    "moon_illumination": astro.get("moon_illumination", "")
                })
                break

            except requests.exceptions.RequestException: #NETWORK
                continue

    return pd.DataFrame(historical_data)

def get_simulated_current_weather(): #SIMULATED CURRENT WTHR
    data = {
        "city": ["Simulation"],
        "temperature": [27.0],
        "humidity": [65],
        "pressure": [1008.0],
        "wind_speed": [14.2],
        "description": ["Partly cloudy"]
    }
    return pd.DataFrame(data)

def get_simulated_historical_weather(): #SIMULATED HISTORICAL WTHR
    today = datetime.today()
    
    data = [
        {
            "date_iso": today - timedelta(days=6),
            "date": (today - timedelta(days=6)).date(),
            "avg_temp": 24.0,
            "min_temp": 18.0,
            "max_temp": 30.0,
            "humidity": 72,
            "max_wind": 12.0,
            "precipitation": 2.5,
            "chance_of_rain": 40,
            "uv": 6.0,
            "condition": "Partly cloudy",
            "sunrise": "06:18 AM",
            "sunset": "05:02 PM",
            "moonrise": "03:40 AM",
            "moonset": "02:20 PM",
            "moon_phase": "Waning Crescent",
            "moon_illumination": 18,
        },
        {
            "date_iso": today - timedelta(days=5),
            "date": (today - timedelta(days=5)).date(),
            "avg_temp": 26.5,
            "min_temp": 20.0,
            "max_temp": 33.0,
            "humidity": 68,
            "max_wind": 18.0,
            "precipitation": 0.0,
            "chance_of_rain": 10,
            "uv": 9.0,
            "condition": "Sunny",
            "sunrise": "06:18 AM",
            "sunset": "05:01 PM",
            "moonrise": "04:30 AM",
            "moonset": "03:10 PM",
            "moon_phase": "Waning Crescent",
            "moon_illumination": 24,
        },
        {
            "date_iso": today - timedelta(days=4),
            "date": (today - timedelta(days=4)).date(),
            "avg_temp": 22.0,
            "min_temp": 17.0,
            "max_temp": 28.0,
            "humidity": 85,
            "max_wind": 22.0,
            "precipitation": 12.0,
            "chance_of_rain": 85,
            "uv": 4.0,
            "condition": "Rain",
            "sunrise": "06:17 AM",
            "sunset": "05:01 PM",
            "moonrise": "05:20 AM",
            "moonset": "04:05 PM",
            "moon_phase": "Waning Crescent",
            "moon_illumination": 31,
        },
        {
            "date_iso": today - timedelta(days=3),
            "date": (today - timedelta(days=3)).date(),
            "avg_temp": 21.0,
            "min_temp": 16.0,
            "max_temp": 26.0,
            "humidity": 90,
            "max_wind": 28.0,
            "precipitation": 18.0,
            "chance_of_rain": 95,
            "uv": 3.0,
            "condition": "Thunderstorm",
            "sunrise": "06:17 AM",
            "sunset": "05:00 PM",
            "moonrise": "06:10 AM",
            "moonset": "05:00 PM",
            "moon_phase": "Last Quarter",
            "moon_illumination": 39,
        },
        {
            "date_iso": today - timedelta(days=2),
            "date": (today - timedelta(days=2)).date(),
            "avg_temp": 23.5,
            "min_temp": 18.5,
            "max_temp": 29.5,
            "humidity": 70,
            "max_wind": 16.0,
            "precipitation": 4.0,
            "chance_of_rain": 35,
            "uv": 7.5,
            "condition": "Cloudy",
            "sunrise": "06:16 AM",
            "sunset": "05:00 PM",
            "moonrise": "07:00 AM",
            "moonset": "05:55 PM",
            "moon_phase": "Last Quarter",
            "moon_illumination": 47,
        },
        {
            "date_iso": today - timedelta(days=1),
            "date": (today - timedelta(days=1)).date(),
            "avg_temp": 25.8,
            "min_temp": 19.8,
            "max_temp": 32.2,
            "humidity": 60,
            "max_wind": 14.0,
            "precipitation": 0.0,
            "chance_of_rain": 5,
            "uv": 10.5,
            "condition": "Clear",
            "sunrise": "06:16 AM",
            "sunset": "04:59 PM",
            "moonrise": "07:50 AM",
            "moonset": "06:45 PM",
            "moon_phase": "Waning Gibbous",
            "moon_illumination": 55,
        },
        {
            "date_iso": today,
            "date": today.date(),
            "avg_temp": 27.0,
            "min_temp": 21.0,
            "max_temp": 34.0,
            "humidity": 65,
            "max_wind": 20.0,
            "precipitation": 6.0,
            "chance_of_rain": 50,
            "uv": 8.0,
            "condition": "Partly cloudy",
            "sunrise": "06:15 AM",
            "sunset": "04:59 PM",
            "moonrise": "08:40 AM",
            "moonset": "07:35 PM",
            "moon_phase": "Waning Gibbous",
            "moon_illumination": 62,
        },
    ]
    return pd.DataFrame(data)

if __name__ == "__main__" :
    city = "Durgapur"
    print("Current Weather: ")
    print(get_current_weather(city))
    print("\nHistorical Weather: ")
    print(get_historical_weather(city))