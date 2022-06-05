import requests

MY_LAT = 41.008240
MY_LONG = 28.978359

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}


resp = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)

data = resp.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sun_tuple = (sunrise, sunset)

print(sun_tuple)
