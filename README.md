Phone Number Location Tracker using Python
Are you curious about the location of a mobile number? Maybe you want to track a lost phone or keep tabs on your child's whereabouts. Whatever your reason, you can use Python to find the location of a mobile number.

In this step-by-step guide, we'll show you how to track a mobile number's location using Python. You'll need some Python coding skills and access to a few geolocation libraries. Let's get started!

To make this project only you need to follow this step:-

Installation
Install package with pip

  pip install phonenumbers
  pip install folium
  pip install geocoder
  pip install opencage
Now need to collect Geocoder API Key from https://opencagedata.com/

Step1: Need to log in or sign up

github1

Step2: Need to click Geocoding API

github2

Step3: From API Keys collect API key

github3

Deployment
To deploy this project run

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = "your key" #Geocoder API Key need to paste here "your key" 
number = input("please giver your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")

print("location tracking completed")
print("Thank you")