import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
key = os.getenv('API_KEY')

# Input the phone number
number = input("Please give your number (with country code, e.g., +14155552671): ")

# Parse the number (the region can be set based on the expected phone numbers)
new_number = phonenumbers.parse(number)

# Get location description
location = geocoder.description_for_number(new_number, "en")
print(f"Location: {location}")

# Get carrier name
service_name = carrier.name_for_number(new_number, "en")
print(f"Carrier: {service_name}")

# Use both the description and the phone number as context for geocoding
query = f"{location} {number}"
geocoder = OpenCageGeocode(key)
result = geocoder.geocode(query)

if result and len(result) > 0:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    components = result[0]['components']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Extract detailed location information
    city = components.get('city', components.get('town', 'N/A'))
    state = components.get('state', 'N/A')
    country = components.get('country', 'N/A')
    road = components.get('road', 'N/A')
    suburb = components.get('suburb', 'N/A')
    postcode = components.get('postcode', 'N/A')
    landmark = components.get('landmark', 'N/A')

    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Country: {country}")
    print(f"Road: {road}")
    print(f"Suburb: {suburb}")
    print(f"Postcode: {postcode}")
    print(f"Landmark: {landmark}")

    # Create a map with folium
    my_map = folium.Map(location=[lat, lng], zoom_start=15)
    folium.Marker([lat, lng], popup=f"{road}, {suburb}, {city}, {state}, {country}").add_to(my_map)
    my_map.save("location.html")

    print("Location tracking completed. Map saved as location.html")
else:
    print("Geocoding failed. Please check the API key and try again.")

print("Thank you")
