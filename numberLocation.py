import phonenumbers
import folium

from myNumber import number
from phonenumbers import geocoder

key = '2861ea9bebfa4b16a08d275ad5abb53d'

RNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(RNumber, "en")
print(yourLocation)

## get service Provide

from phonenumbers import carrier

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)

results = geocoder.geocode(query)

## print(results)


lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']

print(lat, long)

myMap = folium.Map(location=[lat, long], zoom_start = 9)

folium.Marker([lat, long], popup=yourLocation).add_to(myMap)

## save map in HTML file

myMap.save("myLocation.html")
