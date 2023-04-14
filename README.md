#Strava and GCal sync

The idea of the project is to syncronise Strava activity log with Google calendar.
--------------------
#Strava API

0. Create app.
To get started create your app following the link:
https://www.strava.com/settings/api

1. Authorize the user and get code.
Strava will provide you with client id, client secret and client token that will give you general information such as user name or his id. To get access to user activity log, you need to authorize via OAuth. To manually get token use the link:
https://www.strava.com/oauth/authorize?client_id=[your_client_id]&response_type=code&redirect_uri=http://localhost:5000/exchange_token&approval_prompt=force&scope=activity:read_all

As soon as you push the "Authorize" button it will redirect you to
http://localhost:5000/exchange_token?state=&code=[code]&scope=read,activity:read_all

You need to get code from this link and use it to generate new access and refresh tokens for exact user.

2. Get Access token for the user.
Use the following post method in Postman to get json respond:
https://www.strava.com/oauth/token?client_id=[client id]&client_secret=[client secret]&code=[code from previous step]&grant_type=authorization_code

3. Create .env file in root repository:
```
CLIENT_ID=your_id
CLIENT_SECRET=your_secret
REF_USER_TOKEN=users_auth_token_from_last_lson_response
```
