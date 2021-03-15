import requests
import json
import queries

URL = "https://us-central1-pf2-graphql.cloudfunctions.net/api/graphql"

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
    ret = ""
    for e in spell.keys():
        if spell[e] is None:
            continue
        if e in "traits":
            ret += "**Traits:**\n\t"
            for f in spell[e]:
                ret += "\t" + f["name"]
            ret += "\n"
            continue
        ret += "**" + e.title() + "**:" + "\n\t" + str(spell[e]) + "\n"
    return ret

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
    ret = ""
    for e in cond.keys():
        if cond[e] is None:
            continue
        if isinstance(cond[e], list):
            ret += "**" + e.title() + "**:" + "\n\t" + "\n\t".join(cond[e]) + "\n"
            continue
        ret += "**" + e.title() + "**:" + "\n\t" + str(cond[e]) + "\n"
    return ret


def get_trait(s: str):
    traits = get_traits()
    trait = []
    for e in traits:
        if s.lower() in e["name"].lower():
            trait = e
            break
    ret = ""
    for e in trait.keys():
        if trait[e] is None:
            continue
        ret += "**" + e.title() + "**:" + "\n\t" + str(trait[e]) + "\n"
    return ret



