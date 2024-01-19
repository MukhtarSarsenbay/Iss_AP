import requests
from datetime import datetime
import smtplib

MY_LAT = 51.160522
MY_LONG = 71.470360
my_email = "mukhtar.sarsenbay@nu.edu.kz"
password = "rbnb jxon xxxl nrqs"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json() # []
sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])
print(sunset)
print(sunrise)

time_now = datetime.now()
print(time_now.hour)

if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
    if time_now.hour >= sunset or time_now.hour <=sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="doterzadrdoter@gmail.com",
                                msg="Subject:ISS Location\n\n Iss is flying right above you!")



