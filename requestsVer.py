import requests

print(requests.__version__)

print(requests.get("http://www.google.com/").text)

print(requests.get("https://raw.githubusercontent.com/Sean-Meyers/CMPUT404Lab1/main/requestsVer.py").text)