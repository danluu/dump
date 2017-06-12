import json

lowest_score = 300.0
highest_score = 1300.0
increment = 100.0

ratings = {}

with open('ratings.json', 'r') as f:
    parsed = json.load(f)
    ratings = parsed["players"]

games = {}

with open('all_games.json', 'r') as f:
    games = json.load(f)

def lowest_rating_in_game(game):
    lowest = 10000.0
    for player in game["players"]:
        if player["score"] < lowest:
            lowest = player["score"]
    assert(lowest != 10000.0)
    return lowest

# Already filtered to 4p, base map, no drops.
with open('filtered_games.json', 'r') as f:
    parsed = json.load(f)
    for junk, game in parsed.items():
        print(lowest_rating_in_game(game))
    
