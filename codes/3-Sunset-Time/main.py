import requests
import datetime

MY_LAT = 41.008240
MY_LONG = 28.978359

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


resp = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)

data = resp.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

splitted_sunrise = sunrise.split("T")[1].split(":")[0]
splitted_sunset = sunset.split("T")[1].split(":")[0]

print(splitted_sunrise)
print(splitted_sunset)

time_now = datetime.datetime.now()
print(time_now.hour)
