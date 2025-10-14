import json
import requests

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    "name" : "Uday",
    "classs" : 9,
    "section" :"B",
    "roll" : 45,
}
json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
data = r.json()
