import requests
import os
from dotenv import load_dotenv
import json
import urllib.parse

import api 
import config


load_dotenv()

baseUrl = "https://api.tumblr.com/v2/blog/"
uri = "/info"
username = "rcarx"
apiKey = os.environ["API_KEY"]

url = f'{baseUrl}{username}{uri}'
payload={"api_key": apiKey}

conf = config.load_config()
request_url = f'{conf.requests.oauthBaseUrl}{conf.requests.oauthUri}'
token = api.request_token(request_url, os.environ["CONSUMER_ID"], os.environ["CONSUMER_SECRET"])
print(token)


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
