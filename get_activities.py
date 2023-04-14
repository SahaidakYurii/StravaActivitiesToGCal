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

def refresh_auth_token():
    """
    uses refresh token to get auth token
    """
    auth_token_url = "https://www.strava.com/oauth/token"

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
    return access_token

def get_activities(access_token, page_num=1, per_page=30):
    """
    gets users activities via this users access token
    """
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + access_token}

    param = {'per_page': per_page, 'page': page_num}
    return requests.get(activites_url, headers=header, params=param).json()

if __name__ == "__main__":
    access_token = refresh_auth_token()
    pprint(get_activities(access_token))
