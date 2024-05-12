import tweepy
import configparser
config=configparser.RawConfigParser()
config.read('config_tweet.ini') # Load credential files


def auth_cred():
    #creating a variables
    ACCESS_TOKEN = config['Twitter']['acess_token']
    ACCESS_TOKEN_SECRET = config['Twitter']['acess_secret_token']
    CONSUMER_KEY = config['Twitter']['api_key']
    CONSUMER_SECRET = config['Twitter']['api_secret']
    bearer_token = config['Twitter']['bearer_token']
    
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )
    auth = tweepy.OAuth1UserHandler(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
    )
    return client, auth
# Initialize the Twitter Session
client, auth = auth_cred()

def post_tweet(tweet, file_name):
    
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # api.verify_credentials()

    
    # Create tweet
    message = tweet
    
    if file_name != "Not Available":
        # Upload an Image or Video File
        media = api.media_upload(file_name)
        # Attach tweet + media
        client.create_tweet(text=message, media_ids=[media.media_id])
    else:
        # Post a tweet without media
        client.create_tweet(text=message)
    print("Tweeted!")
    
    # Function to post a tweet with optional media file

    
