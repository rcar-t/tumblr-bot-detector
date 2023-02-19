from dataclasses import dataclass
import requests
from requests_oauthlib import OAuth1
import urllib.parse
import config

class Api:

    @dataclass
    class TumblrOAuth():
        oauth_token: str
        oauth_token_secret: str
        oauth_callback_confirmed: bool

    conf = config.load_config()

    def get_request_token(): 
        request_url = f'{conf.requests.baseUrl}{conf.requests.oauth.requestTokenUri}'

        auth = OAuth1(os.environ["CONSUMER_ID"], os.environ["CONSUMER_SECRET"])
        response = requests.get(request_url, auth=auth)

        (oauth_token, oauth_token_secret, ouath_callback_confirmed) = urllib.parse.parse_qsl(response.content)

        return TumblrOAuth(oauth_token[1], oauth_token_secret[1], ouath_callback_confirmed[1])

    def authorise(): 
        request_url = f'{conf.requests.baseUrl}{conf.requests.oauth.authorisationUri}'
        token = request_token().oauth_token

        payload = {"oauth_token": token}

        response = requests.get(request_url, payload=payload)

    def retrieve_followers(blog: str): 
        url = f'{config.load_config().apiBaseUrl}/blog/{blog}/followers'

