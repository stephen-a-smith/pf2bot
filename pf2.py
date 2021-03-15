import api

conds = api.get_conditions()
spells = api.get_spells()
traits = api.get_traits()
feats = api.get_feats() + api.get_archFeats()


# formats the data into a neat format for reading
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
            ret += "" + e.title() + ":" + "\n\t" + "\n\t".join(data[e]) + "\n"
            continue
        ret += "" + e.title() + ":" + "\n\t" + str(data[e]) + "\n"
    return ret

# Finds requested trait
def get(s: str, data):
    target = []
    for e in data:
        if s.lower() in e["name"].lower():
            target = e
            break
    return pretty_print(target)
