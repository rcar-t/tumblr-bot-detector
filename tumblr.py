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

print(urllib.parse.parse_qsl())
config = config.load_config()
request_conf = config["requests"]
api.request_token(config["requests"][""])


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
