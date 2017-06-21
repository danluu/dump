import argparse
import json

# filter for:
# 4p
# original map (base_map => 126fe960806d587c78546b30f1a90853b1ada468)
# No drop
# No exclude_from_stats
# id_hash not null
# No "fire-and-ice-final-scoring"
# Player has rating

# debug_fav11 = set()
# with open('fav11-games.txt') as f:
#     for line in f:
#         debug_fav11.add(line.strip())

def didnt_take_fav11_in_round1(faction):
    # Never took FAV11?
    if not "favor:FAV11" in faction:
        return True
    # Didn't take FAV11 in round 1?
    if not "1" in faction["favor:FAV11"]["round"]:
        return True

    return False
    

def keep_game(game_name, game, all_players, keep_if):
    if "base_map" in keep_if:
        if keep_if["base_map"] == True and game["base_map"] != "126fe960806d587c78546b30f1a90853b1ada468":
            return False
        elif keep_if["base_map"] == False and game["base_map"] == "126fe960806d587c78546b30f1a90853b1ada468":
            return False

    if "player_count" in keep_if:
        required_count = keep_if["player_count"]
        if game["player_count"] != required_count:
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

    # TODO: hoist game option loop to top level.

    if "fire-and-ice-final-scoring" in keep_if:
        seen_fi_scoring = False
        for option in game["options"]:
            if option == "fire-and-ice-final-scoring":
                if keep_if["fire-and-ice-final-scoring"] == False:
                    return False
                else:
                    seen_fi_scoring = True
        if keep_if["fire-and-ice-final-scoring"] == True and seen_fi_scoring == False:
            return False

    if "fire-and-ice-factions" in keep_if:
        # We look for all or none here, so we check for count == 3.
        # We also disallow original or v2 variable factions.
        fi_faction_count = 0
        for option in game["options"]:
            if option.startswith("fire-and-ice-factions"):
                if keep_if["fire-and-ice-factions"] == False:
                    return False
                if option == "fire-and-ice-factions/variable" or option == "fire-and-ice-factions/variable_v2":
                    return False
                fi_faction_count += 1
        if keep_if["fire-and-ice-factions"] == True:
            if fi_faction_count != 3:
                return False

    # Always remove old variable factions. Note that this conflicts with the above code block.
    for option in game["options"]:
        if option.startswith("fire-and-ice-factions/variable") and option != "fire-and-ice-factions/variable_v5":
            return False
        # if option == "fire-and-ice-factions/variable" or option == "fire-and-ice-factions/variable_v2":
        #     return False

    # # if "fav11-123" in keep_game and keep_game["fav11-123"] == True:
    # if not game_name in filtered_events:
    #     # if game_name in debug_fav11:
    #     #     print("Failed to find in filtered_events", game_name)
    #     # return False
    #     # 
    # else:
    #     game_events = filtered_events[game_name]
    #     for faction_name,faction in game_events["events"]["faction"].items():
    #         # Ever went first?
    #         if "order:1" in faction:
    #             # Went first in rd1?
    #             if "1" in faction["order:1"]["round"]:
    #                 if didnt_take_fav11_in_round1(faction):
    #                     # if game_name in debug_fav11:
    #                     #     print("Failed p1 check", game_name, faction_name)
    #                     return False
    #         if "order:2" in faction:
    #             if "1" in faction["order:2"]["round"]:
    #                 if didnt_take_fav11_in_round1(faction):
    #                     # if game_name in debug_fav11:
    #                     #     print("Failed p2 check", game_name, faction_name)
    #                     # return False
    #         if "order:3" in faction:
    #             if "1" in faction["order:3"]["round"]:
    #                 if didnt_take_fav11_in_round1(faction):
    #                     if game_name in debug_fav11:
    #                         print(game_name)

    #                         # print(faction)
    #                         # print(faction["favor:FAV11"])

    #                         # if not "favor:FAV11" in faction:
    #                         #     print("Fail 1")
    #                         # if not "1" in faction["favor:FAV11"]["round"]:
    #                         #     print("Fail 2")

    #                     return False
    return True

# Fire-and-ice factions here means all f&i factions enabled, shapeshifters v3 or later.
keep_params = {
    "base_map": True,
    "player_count": 4,
    "fire-and-ice-final-scoring": False,
    "fire-and-ice-factions": False,
    # "fav11-123": True, # TODO: remove from default.
}

parser = argparse.ArgumentParser()
parser.add_argument("-fis", "--fireandicescoring", help="[t/f]")
parser.add_argument("-fif", "--fireandicefactions", help="[t/f]")
parser.add_argument("-f11", "--fav11_123", help="[t/f]")
parser.add_argument("-o", "--output", help="[filename]")
args = parser.parse_args()

if args.fireandicescoring != None:
    if args.fireandicescoring.lower() == "t" or args.fireandicescoring.lower() == "true":
        keep_params["fire-and-ice-final-scoring"] = True
    elif args.fireandicescoring.lower() == 'f' or args.fireandicescoring.lower() == "false":
        keep_params["fire-and-ice-final-scoring"] = False
    else:
        print("Don't understand --fireandicescoring argument", args.fireandicescoring)
        assert(False)

if args.fireandicefactions != None:
    if args.fireandicefactions.lower() == "t" or args.fireandicefactions.lower() == "true":
        keep_params["fire-and-ice-factions"] = True
    elif args.fireandicescoring.lower() == 'f' or args.fireandicefactions.lower() == "false":
        keep_params["fire-and-ice-factions"] = False
    else:
        print("Don't understand --fireandicescoring argument", args.fireandicescoring)
        assert(False)

# TODO: handle fav11 argument.

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
        if keep_game(game_name, game, all_players, keep_params):
            filtered_games[game_name] = game

# with open('filtered_games.json', 'w') as outfile:
# with open('filtered_games.fav11.json', 'w') as outfile:
with open(args.output, 'w') as outfile:
    json.dump(filtered_games, outfile) 

