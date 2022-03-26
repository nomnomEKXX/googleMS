import requests
from flask import Flask, request, jsonify
import json
import os

from dotenv import load_dotenv
load_dotenv('./.env')

key = os.getenv('GOOGLE_MAPS_API_KEY')
app = Flask(__name__)

@app.route("/stores/getDistance/<storeEmail>")
def getDistance():
    #{
    #   "userLocation": Take from browser, 
    #   "storeLocation": Take from frontend
    # }
    locations = request.get_json()
    userLocation = locations["userLocation"]
    storeAddress = locations["address"]

    url = (
        "https://maps.googleapis.com/maps/api/distancematrix/json"
        + "?origins={}".format(userLocation)
        + "&destinations={}".format(storeAddress)
        + "&key={}".format(key)
    )

    payload = {}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        answer = json.loads(response.text)
        distance = answer["rows"][0]["elements"][0]["distance"]["text"]
        return {"code": 200, "message": "Distance to travel: {}".format(distance)}
    

    except:
        return {"code": 401, "message": "Failed to retrieve distance from user to store"}



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

