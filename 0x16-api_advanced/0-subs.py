#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
