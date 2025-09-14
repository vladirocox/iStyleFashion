import requests

url = "http://raspberrypi.local:25565/get_code"
payload = {"code_type": "Arcade"}
response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("Redemption URL:", data["redemption_url"])
    print("Code:", data["code"])
else:
    print("Failed to retrieve code:", response.text)
