import requests
import json
from twilio.rest import TwilioRestClient

import secrets

#Twilio API Credentials
client = TwilioRestClient(secrets.account_sid, secrets.auth_token)

#Dark Sky API get request
response = requests.get(secrets.ds_key)

data = response.json()

# Write JSON to file
#with open('json.txt', 'w') as outfile:
#    json.dump(data, outfile)

days = ['\nMon: ', 'Tue: ', 'Wed: ', 'Thu: ', 'Fri: ', 'Sat: ', 'Sun: ']
textSMS = ""

for i in range(0,7):
    avgTemp = str(round((data["daily"]["data"][i]["temperatureMin"] + data["daily"]["data"][i]["temperatureMax"])/2))
    precipProbability = str(round((data["daily"]["data"][i]["precipProbability"] * 100)))
    textSMS += days[i] + avgTemp + "F " + precipProbability + "%\n"


message = client.messages.create(to=secrets.target_number, from_=secrets.twilio_number,
                                     body=textSMS)
