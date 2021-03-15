import requests
import json
import queries

URL = "https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql"

def pretty_print(data):
    ret = ""
    for e in data.keys():
        if data[e] is None:
            continue
        if isinstance(data[e], list):
            if isinstance(data[e][0], dict):
              li = []
              for x in data[e]:
                li.append(x["name"])
              data[e] = li
            ret += "**" + e.title() + "**:" + "\n\t" + "\n\t".join(data[e]) + "\n"
            continue
        ret += "**" + e.title() + "**:" + "\n\t" + str(data[e]) + "\n"
    return ret

def get_spells():
    request = requests.post(URL, json={'query': queries.Spells_query})
    if request.status_code == 200:
        return request.json()["data"]["spells"]
    else:
        print(request.status_code)

def get_spell(s: str):
    spells = get_spells()
    spell = []
    for e in spells:
        if s.lower() in e["name"].lower():
            spell = e
            break
    return pretty_print(spell)

def get_conditions():
    request = requests.post(URL, json={'query': queries.cond_query})
    if request.status_code == 200:
        return request.json()["data"]["conditions"]
    else:
        print(request.status_code)

def get_traits():
    request = requests.post(URL, json={'query': queries.trait_query})
    if request.status_code == 200:
        return request.json()["data"]["traits"]
    else:
        print(request.status_code)

def get_condition(s: str):
    conds = get_conditions()
    cond = []
    for e in conds:
        if s.lower() in e["name"].lower():
            cond = e
            break
    return pretty_print(cond)


def get_trait(s: str):
    traits = get_traits()
    trait = []
    for e in traits:
        if s.lower() in e["name"].lower():
            trait = e
            break
    return pretty_print(trait)



