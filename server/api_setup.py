"""This module is an API set up
SHOULD WORK WITH YELP API"""

import os
import random
import requests
import sys
from dotenv import find_dotenv, load_dotenv

print(find_dotenv())

load_dotenv(find_dotenv())

API_KEY_YELP = os.getenv("API_KEY_YELP")
BASE_URL = os.getenv("BASE_URL")


def get_data(searched_value):
    # searched_value -> name of the searched item
    _params = {
        "term":searched_value,"radius":2000,"latitude":33.75662886123124,"longitude":-84.38882273143552
    }
    _headers = {"Authorization": 'Bearer '+API_KEY_YELP}
    data = requests.get(BASE_URL + "search",params=_params,headers=_headers)
    business_data = requests.get(BASE_URL+ data.json()["businesses"][0]["id"],headers=_headers)
    
    return {
        # "all_data": data.json(),
        "business_data": business_data.json() # has all info about searched item
    }




#print(get_data("cafe lucia"))