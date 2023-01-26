from dataclasses import dataclass
import requests
from requests_oauthlib import OAuth1
import urllib.parse


@dataclass
class TumblrOAuth():
    oauth_token: str
    oauth_token_secret: str
    oauth_callback_confirmed: bool

def request_token(url: str, consumer_id: str, consumer_secret: str): 
    auth = OAuth1(consumer_id, consumer_secret)
    response = requests.get(url, auth=auth)

    (oauth_token, oauth_token_secret, ouath_callback_confirmed) = urllib.parse.parse_qsl(response.content)

    return TumblrOAuth(oauth_token[1], oauth_token_secret[1], ouath_callback_confirmed[1])