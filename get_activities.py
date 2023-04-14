import requests
import urllib3
from dotenv import load_dotenv
import os
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
secret = os.environ.get('CLIENT_SECRET')
ref_token = os.environ.get('REF_USER_TOKEN')
client_id = os.environ.get('CLIENT_ID')

auth_token_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': client_id,
    'client_secret': secret,
    'refresh_token': ref_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_token_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

request_page_num = 1
all_activities = {}

param = {'per_page': 10, 'page': request_page_num}
all_activities = requests.get(activites_url, headers=header, params=param).json()

pprint(all_activities)
