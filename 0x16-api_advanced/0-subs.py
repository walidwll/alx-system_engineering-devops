#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests,json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "PostmanRuntime/7.35.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(response.text)
    if response.status_code == 404:
        return 0
    results = response.json().get("data", {}).get("subscribers", 0)
    return results
