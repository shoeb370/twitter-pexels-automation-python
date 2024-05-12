import requests
import json
import os
from post_tweet_v2 import post_tweet
import pandas as pd

# This function retrieves data from the specified URL using the provided Pexels API key.
# It constructs the request with necessary headers for authorization and returns the response.
def get_data(url, pexel_api_key):
    headers = {
      'Authorization': pexel_api_key
    }
    response = requests.request("GET", url, headers=headers)
    return response

# This function fetches details of images based on the provided query using the Pexels API.
# It prints the response text containing image details.
def get_image_details(query, pexel_api_key):
    # Constructing the URL for image query
    url = f"https://api.pexels.com/v1/search?query={query}"
    response = get_data(url, pexel_api_key)
    print(response.text)

# This function fetches details of videos based on the provided query using the Pexels API.
# It prints the response text containing video details.
def get_video_details(query,pexel_api_key):
    # Constructing the URL for video query
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"
    response = get_data(url, pexel_api_key)
    print(response.text)

# This function retrieves a curated photo from Pexels in real-time.
# It selects a photo that is not already posted, downloads it, and posts it on Twitter.
def get_curated_photo(pexel_api_key):
    '''This endpoint enables you to receive real-time photos curated by the Pexels team.
    We add at least one new photo per hour to our curated list so that you always get a changing selection of trending photos.'''
    url = "https://api.pexels.com/v1/curated?per_page=1"
    response = get_data(url, pexel_api_key)
    json_data = json.loads(response.text)
    # Fetching photo details
    photo_id = json_data['photos'][0]['id']
    prev_id_df = pd.read_csv('already_posted_link.csv')
    prev_photo = prev_id_df['Photo_id'].tolist()
    
    # Selecting a non-posted photo
    while True:
        if photo_id in prev_photo:
           url = json_data['next_page']
           response = get_data(url, pexel_api_key)
           json_data = json.loads(response.text)
           photo_id = json_data['photos'][0]['id']
        else:
            photo_id = json_data['photos'][0]['id']
            df = pd.DataFrame({'Photo_id':[photo_id]})
            prev_id_df = pd.concat([prev_id_df, df], ignore_index=True)
            prev_id_df.to_csv('already_posted_link.csv', index=False)
            break
              
    # Extracting photo details              
    photographer_name = json_data['photos'][0]['photographer']
    photographer_url = json_data['photos'][0]['photographer_url']
    image_url = json_data['photos'][0]['src']['original']
    hashtag_list = ["#PexelsCurated", "#TrendingSelection", "#PexelsTeam", "#PhotoCuration", "#PhotoTrends",
                    '#Pexels', '#photography']
    file_name = image_url.split("/")[-1]  # Extracting the file name from the URL
    # Downloading the image
    response = requests.get(image_url, stream=True)
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'wb') as out_file:
        for chunk in response.iter_content(chunk_size=128):
            out_file.write(chunk)
    
    # Creating Twitter post content
    twitter_post = f'''
    📸 Photo by {photographer_name} on Pexels
    {photographer_url}    
    {' '.join(hashtag_list)}
    '''
    # Posting the tweet with the image
    print(twitter_post)
    post_tweet(twitter_post, file_path)
    # Delete the downloaded file
    os.remove(file_path)
    return True

# This function retrieves a popular video from Pexels.
# It selects a video that is not already posted, downloads it, and posts it on Twitter.
def get_popular_video(pexel_api_key):
    url = "https://api.pexels.com/videos/popular?per_page=1"
    response = get_data(url, pexel_api_key)
    json_data = json.loads(response.text)
    # Fetching video details
    video_id = json_data['videos'][0]['id']
    prev_id_df = pd.read_csv('already_posted_video.csv')
    prev_video = prev_id_df['Video_id'].tolist()
    
    # Selecting a non-posted video
    while True:
        if video_id in prev_video:
           url = json_data['next_page']
           response = get_data(url, pexel_api_key)
           json_data = json.loads(response.text)
           video_id = json_data['videos'][0]['id']
        else:
            video_id = json_data['videos'][0]['id']
            df = pd.DataFrame({'Video_id':[video_id]})
            prev_id_df = pd.concat([prev_id_df, df], ignore_index=True)
            prev_id_df.to_csv('already_posted_video.csv', index=False)
            break
    
    # Extracting video details
    photographer_name = json_data['videos'][0]['user']['name']
    photographer_url = json_data['videos'][0]['user']['url']
    video_url = json_data['videos'][0]['video_files'][0]['link']
    hashtag_list = ["#PexelsCurated", "#TrendingSelection", "#PexelsTeam", "#PopularVideo", "#VideoTrends", "#VideoCategory"]
    file_name = video_url.split("/")[-1]  # Extracting the file name from the URL
    file_path = os.path.join(os.getcwd(), file_name)
    
    # Downloading the video
    with requests.get(video_url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=128):
                out_file.write(chunk)

    # Creating Twitter post content
    twitter_post = f'''
    🎥 Video by {photographer_name} on Pexels
    {photographer_url}
    
    {' '.join(hashtag_list)}
    '''
    print(twitter_post)
    post_tweet(twitter_post, file_path)
    # Delete the downloaded file
    os.remove(file_path)
    return True
    
    

# Main function to fetch a curated photo and a popular video based on the specified query.
if __name__ == "__main__":
    query = 'seashore'
    pexel_api_key = r'QxLl9CpTT7Op1kmOUTiRxoqro57YykqIXRXkJsKBM3zNbZompzoEPkFB'
    get_curated_photo(pexel_api_key)
    get_popular_video(pexel_api_key)
    
    # get_video_details(query,pexel_api_key) # If you a video with respect to query based data please uncomment it
    # get_image_details(query, pexel_api_key) # Same for images also
    


