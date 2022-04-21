"""
This file does the interfacing with yelp. It requests restaurants within a 2 mile radius of aderhold. 
"""

import os
from dotenv import load_dotenv, find_dotenv
import requests

# from model import Users, Restaurant, Chatroom, Ct

load_dotenv(find_dotenv())


def get_yelp():
    """This gets the json for the desired movie and then parses out and returns the movie details"""

    api_key = os.getenv("API_KEY_YELP")

    base_url = "https://api.yelp.com/v3/businesses/search"
    auth_header = {"Authorization": f"bearer {api_key}"}

    parameters = {
        "term": "restaurants",
        "limit": 50,
        "offset": 100,
        "radius": 3220,
        "latitude": 33.756633321231654,
        "longitude": -84.38884955332108,
    }

    response = requests.get(url=base_url, params=parameters, headers=auth_header)

    data = response.json()
    print(data)
    data = data["businesses"]
    attributes = ["id", "name", "display_location", "rating", "price", "image_url"]
    for biz in data:
        ls = {}
        for a in attributes:
            if a not in biz.keys():
                ls[a] = "None"
            else:
                ls[a] = biz[a]
        new_restaurant = {
            "id": ls["id"],
            "name": ls["name"],
            "address": ls["display_location"],
            "rating": ls["rating"],
            "price": ls["price"],
            "image": ls["image_url"],
        }

    return data


get_yelp()
