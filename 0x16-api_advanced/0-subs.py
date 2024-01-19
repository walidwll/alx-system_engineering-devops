#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Reddit API URL for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the number of subscribers
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            # Subreddit not found, return 0
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            # Other error, return 0
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
