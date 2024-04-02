import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

# website = input("Enter Website")
# ip_address = socket.gethostbyname(website)


# def printDetails(ip):
#     res = DbIpCity.get(ip, api_key="free")
#     print(f"IP Address: {res.ip_address}")
#     print(f"Location: {res.city}, {res.region}, {res.country}")
#     print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


# printDetails(ip_address)

print("Socket Module", dir(socket))
print("Request Module", dir(requests))