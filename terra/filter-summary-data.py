import json

# filter for:
# 4p
# original map (base_map => 126fe960806d587c78546b30f1a90853b1ada468)
# No drop
# No exclude_from_stats
# id_hash not null
# No "fire-and-ice-final-scoring"

def keep_game(game):
    if game["base_map"] != "126fe960806d587c78546b30f1a90853b1ada468":
        return False
    if game["player_count"] != 4:
        return False
    for player in game["players"]:
        if player["exclude_from_stats"] == 1 or player["dropped"] == 1:
            return False
        if player["id_hash"] == None:
            return False
    for option in game["options"]:
        if option == "fire-and-ice-final-scoring":
            return False
    return True
    
filtered_games = {}

with open('all_games.json', 'r') as f:
    parsed = json.load(f)
    for game_name in parsed:        
        game = parsed[game_name]
        if keep_game(game):
            filtered_games[game_name] = game

with open('filtered_games.json', 'w') as outfile:
    json.dump(filtered_games, outfile) 
            
        

