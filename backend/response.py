import requests

response = requests.get(
    "https://api.weatherapi.com/v1/current.json",
    params={"key": "ENTER API KEY HERE", "q": "Chennai"}
)

print(response.status_code)
print(response.text)