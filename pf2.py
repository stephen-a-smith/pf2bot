import api

conds = api.get_conditions()
spells = api.get_spells()
traits = api.get_traits()

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
            ret += "**" + e.title() + "**:" + "\n\t" + "\n\t".join(data[e]) + "\n"
            continue
        ret += "**" + e.title() + "**:" + "\n\t" + str(data[e]) + "\n"
    return ret

# Finds requested spell, and returns the pretty_printed string
def get_spell(s: str):
    spell = []
    for e in spells:
        if s.lower() in e["name"].lower():
            spell = e
            break
    return pretty_print(spell)

# Finds requested condition, and returns the pretty_printed string
def get_condition(s: str):
    cond = []
    for e in conds:
        if s.lower() in e["name"].lower():
            cond = e
            break
    return pretty_print(cond)

# Finds requested trait, and returns the pretty_printed string
def get_trait(s: str):
    trait = []
    for e in traits:
        if s.lower() in e["name"].lower():
            trait = e
            break
    return pretty_print(trait)



