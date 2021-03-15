# Handles the backend of making requests to the server and returning results

import requests
import queries
import json

URL = "https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql"

# Gets the full spell list from https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql
def get_spells():
    request = requests.post(URL, json={'query': queries.spells_query})
    if request.status_code == 200:
        return request.json()["data"]["spells"]
    else:
        print(request.status_code)

# Gets the full condition list from https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql
def get_conditions():
    request = requests.post(URL, json={'query': queries.conditions_query})
    if request.status_code == 200:
        return request.json()["data"]["conditions"]
    else:
        print(request.status_code)

# Gets the full trait list from https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql
def get_traits():
    request = requests.post(URL, json={'query': queries.trait_query})
    if request.status_code == 200:
        return request.json()["data"]["traits"]
    else:
        print(request.status_code)
