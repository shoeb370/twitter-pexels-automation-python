# Twitter Pexels Automation with Python

Automate Twitter posts with curated content from Pexels using Python scripts.

## Overview

This repository contains Python scripts to automate the process of fetching curated photos and popular videos from Pexels and posting them on Twitter. The scripts utilize the Pexels API for fetching content and the Twitter API for posting tweets.

## Requirements

- Python 3.x
- Pexels API Key
- Twitter Developer Account
- Requests library
- Pandas library

## Twitter API Setup

1. **Create a Twitter Developer Account**: Sign up for a Twitter Developer account at [Twitter Developer](https://developer.twitter.com/).
  
2. **Create a New App**: Once logged in to the Twitter Developer Portal, create a new app and note down the following credentials:
   - API key
   - API secret key
   - Access token
   - Access token secret
   
3. **Configure config_tweet.ini**: Create a `config_tweet.ini` file in the project directory with the following format:
   ```ini
   [Twitter]
   api_key = YOUR_API_KEY
   api_secret = YOUR_API_SECRET
   access_token = YOUR_ACCESS_TOKEN
   access_secret_token = YOUR_ACCESS_SECRET_TOKEN
   bearer_token = YOUR_BEARER_TOKEN
4. Update the auth_cred() function in post_tweet_v2.py to read these credentials from config_tweet.ini

## Authentication and Tweet Posting

The `auth_cred()` function reads the Twitter API credentials from `config_tweet.ini` and authenticates the API client using `tweepy.Client` and `tweepy.OAuth1UserHandler`.

The `post_tweet(tweet, file_name)` function in `post_tweet_v2.py` posts a tweet with the provided tweet content and an optional image (`file_name`).

## Usage

1. Ensure `config_tweet.ini` is correctly configured with your Twitter API credentials.
2. Run the `pexel_automations.py` script to fetch the latest images and videos.


## Contributors

- [Shoeb Ahmed](https://github.com/shoeb370)
## Sponsorship
Thank you for considering supporting this project! Your sponsorship helps in maintaining and improving this project.

Supported Funding Platforms:
- PayPal: [Donate Now](https://www.paypal.me/shoeb370)
