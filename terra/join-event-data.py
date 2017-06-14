# Event data is a list of games scattered into files by month. We want to join
# the data into a single file and create a dict from game => game data to allow
# indexing for other analysis.

import glob
import json

def keep_game(game, all_players):
    if game["base_map"] != "126fe960806d587c78546b30f1a90853b1ada468":
        return False
    if game["player_count"] != 4:
        return False
    for player in game["players"]:
        if player["exclude_from_stats"] == 1 or player["dropped"] == 1:
            return False
        if player["id_hash"] == None:
            return False

        # Player has no rating, perhaps from not having played enough games.
        username = all_players[player['id_hash']]['username']
        if not username in ratings:
            return False
        if not 'score' in ratings[username]:
            return False

    for option in game["options"]:
        if option == "fire-and-ice-final-scoring":
            return False

    return True

all_games = {}
with open('all_games.json', 'r') as f:
    all_games = json.load(f)

all_players = {}
with open('all_players.json', 'r') as f:
    all_players = json.load(f)

ratings = {}
with open('ratings.json', 'r') as f:
    parsed = json.load(f)
    ratings = parsed["players"]

filtered_events = {}
for filename in glob.iglob('game-data/*.json'):
    with open(filename) as f:
        json_data = json.load(f)
        for game in json_data:
            game_name = game['game']
            summary_game_data = all_games[game_name]
            if keep_game(summary_game_data, all_players):
                filtered_events[game_name] = game

with open('filtered_events.json', 'w') as outfile:
    json.dump(filtered_events, outfile)



