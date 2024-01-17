#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)

        # Check if the response contains valid JSON data
        if response.text.strip():  # Check if the response is not empty
            data = response.json().get("data")

            # Check if "subscribers" key is present in the JSON data
            if data and "subscribers" in data:
                return data["subscribers"]
            else:
                print("Error: Invalid JSON format - 'subscribers' key not found.")
                return 0
        else:
            print("Error: Empty response or invalid JSON format.")
            return 0

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            # Subreddit not found (invalid subreddit)
            return 0
        else:
            # Other HTTP error occurred
            print(f"HTTP Error: {err}")
            return 0
    except requests.exceptions.RequestException as e:
        # Other non-HTTP-related error occurred
        print(f"Error: {e}")
        return 0
