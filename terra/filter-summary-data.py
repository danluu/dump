import json

# filter for:
# 4p
# original map (base_map => 126fe960806d587c78546b30f1a90853b1ada468)
# No drop
# No exclude_from_stats
# id_hash not null
# No "fire-and-ice-final-scoring"
# Player has rating

def didnt_take_fav11_in_round1(faction):
    # Never took FAV11?
    if not "favor:FAV11" in faction:
        return False
    # Didn't take FAV11 in round 1?
    if not "1" in faction["favor:FAV11"]["round"]:
        return False

    return True
    

def keep_game(game_name, game, all_players):
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

    if not game_name in filtered_events:
        return False
    else:
        game_events = filtered_events[game_name]
        for faction_name,faction in game_events["events"]["faction"].items():
            # Ever went first?
            if "order:1" in faction:
                # Went first in rd1?
                if "1" in faction["order:1"]["round"]:
                    if didnt_take_fav11_in_round1(faction):
                        return False
            if "order:2" in faction:
                if "1" in faction["order:2"]["round"]:
                    if didnt_take_fav11_in_round1(faction):
                        return False
            if "order:3" in faction:
                if "1" in faction["order:3"]["round"]:
                    if didnt_take_fav11_in_round1(faction):
                        return False
    return True
    

all_players = {}
with open('all_players.json', 'r') as f:
    all_players = json.load(f)

ratings = {}
with open('ratings.json', 'r') as f:
    parsed = json.load(f)
    ratings = parsed["players"]

filtered_events = {}
with open('filtered_events.json', 'r') as f:
    filtered_events = json.load(f)

filtered_games = {}
with open('all_games.json', 'r') as f:
    parsed = json.load(f)
    for game_name in parsed:        
        game = parsed[game_name]
        if keep_game(game_name, game, all_players):
            filtered_games[game_name] = game

# with open('filtered_games.json', 'w') as outfile:
with open('filtered_games.fav11.json', 'w') as outfile:
    json.dump(filtered_games, outfile) 

            
        

