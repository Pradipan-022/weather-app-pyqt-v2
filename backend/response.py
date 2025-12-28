import requests

response = requests.get(
    "https://api.weatherapi.com/v1/current.json",
    params={"key": "00d37d147fde4cbfb0d170238251512", "q": "Durgapur"}
)

print(response.status_code)
print(response.text)