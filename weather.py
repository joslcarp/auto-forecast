import requests
import json
from twilio.rest import TwilioRestClient

#Dark Sky API Credentials
ds_key = "https://api.darksky.net/forecast/abf3ee4fa6193f946ba40f8ae9b3ac6f/[COORDINATES]?exclude=currently,minutely,hourly,flags"

#Twilio API Credentials
account_sid = "XXXXXXXXXX"
auth_token = "XXXXXXXXXXX"
client = TwilioRestClient(account_sid, auth_token)

#Dark Sky API get request
response = requests.get(ds_key)
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


message = client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx",
                                     body=textSMS)

