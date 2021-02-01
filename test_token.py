import requests

JWT_TOKEN = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lk"
             "IjoxLCJ1c2VybmFtZSI6ImFjZXBpbG90MDYyMCIsImV4cCI6MTYxMTY0N"
             "jU4MSwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTYxMTY0NjI4MX0."
             "31iGioNpmNvwgo3L8xJQv8_x3ToTQXa6b9xRV0vduG8")

headers = {
    'Authorization' : f'JWT {JWT_TOKEN}',
}

res = requests.get("http://localhost:8000/post/1/",headers=headers)
print(res.json())