import json

lowest = 2000.0

with open('ratings.json', 'r') as f:
    parsed = json.load(f)
    for name, player in parsed["players"].items():
        if player["score"] < lowest:
            lowest = player["score"]

print(lowest)
        
