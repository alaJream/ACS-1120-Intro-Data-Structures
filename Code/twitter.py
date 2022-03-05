from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os

load_dotenv()

class TwitterBot:
    def __init__(self):
        self.url = 'https://api.twitter.com/1.1/statuses/update.json'
        self.session = OAuth1Session(os.getenv('CONSUMER_KEY'),
                                     client_secret=os.getenv('CONSUMER_SECRET'),
                                     resource_owner_key=os.getenv('ACCESS_TOKEN'),
                                     resource_owner_secret=os.getenv('ACCESS_TOKEN_SECRET'))

    def tweet(self, status):
        resp = self.session.post(self.url, { 'status': status })
        return resp.text