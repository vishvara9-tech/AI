import requests

r = requests.get("http://127.0.0.1:8000/studet")
print("Status code:", r.status_code)

# Only parse JSON if the response is JSON
if "application/json" in r.headers.get("Content-Type", ""):
    data = r.json()
    print(data)
else:
    print("Response is not JSON")
