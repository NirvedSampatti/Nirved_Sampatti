import requests

url = "https://nirvedsampatti.onrender.com/login"

data = {
    "client_code": "9021115667",
    "password": "Nirved@2025",
    "api_key": "6R2647876651#k*JK859036`Nn464937"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)
