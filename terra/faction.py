import collections
import json

# TODO: refactor to share code with the very similar turn-order.py.

lowest_score = 900.0
increment = 50.0
highest_score = 1300.0 + increment
num_slots = int((highest_score - lowest_score) / increment)


factions_top_base = {
    'yetis',
    'engineers',
    'alchemists',
    'darklings',
    'dragonlords',
    'acolytes',
    'halflings',
    'cultists',
    'witches',
}

faction_splits = [
    'swarmlings',
    'darklings',
    'chaosmagicians',
    'icemaidens',
    'riverwalkers',
    'auren',
    'witches',
    'mermaids',
    'alchemists',
    'acolytes',
    'halflings',
    'cultists',
    'giants',
    'engineers',
    'yetis',
    'nomads',
    'dwarves',
    'dragonlords',
    'shapeshifters',
    'fakirs',
]

faction_splits = {
    'swarmlings': 1,
    'darklings': 0,
    'chaosmagicians': 1,
    'icemaidens': 1,
    'riverwalkers': 1,
    'auren': 2,
    'witches': 0,
    'mermaids': 1,
    'alchemists': 0,
    'acolytes': 0,
    'halflings': 0,
    'cultists': 0,
    'giants': 2,
    'engineers': 0,
    'yetis': 0,
    'nomads': 1,
    'dwarves': 1,
    'dragonlords': 0,
    'shapeshifters': 1,
    'fakirs': 2,
}


# https://boardgamegeek.com/thread/1758810/new-starting-vps-base-game-map
faction_adjustment = {
    'swarmlings': 2,
    'darklings': -5,
    'chaosmagicians': -1,
    'icemaidens': 0,
    'riverwalkers': 1,
    'auren': 7,
    'witches': -1,
    'mermaids': -1,
    'alchemists': 7,
    'acolytes': 3,
    'halflings': 0,
    'cultists': -4,
    'giants': 5,
    'engineers': -4,
    'yetis': 2,
    'nomads': -1,
    'dwarves': 0,
    'dragonlords': 4,
    'shapeshifters': 2,
    'fakirs': 13,
}

neighboring_colors = {
    'darklings': ['brown', 'blue'],
    'alchemists': ['brown', 'blue'],
    'mermaids': ['black', 'green'],
    'swarmlings': ['black', 'green'],
    'witches': ['blue', 'grey'],
    'auren': ['blue', 'grey'],
    'engineers': ['green', 'red'],
    'dwarves': ['green', 'red'],
    'giants': ['grey', 'yellow'],
    'chaosmagicians': ['grey', 'yellow'],
    'nomads': ['red', 'brown'],
    'fakirs': ['red', 'brown'],
    'cultists': ['yellow', 'black'],
    'halflings': ['yellow', 'black'],
}

color_to_faction = {
    'black': {'darklings', 'alchemists'},
    'blue': {'mermaids', 'swarmlings'},
    'green': {'witches', 'auren'},
    'grey': {'engineers', 'dwarves'},
    'red': {'chaosmagicians', 'giants'},
    'yellow': {'nomads', 'fakirs'},
    'brown': {'cultists', 'halflings'},
}

def get_faction_neighbors(faction, factions_in_game):
    num_neighbors = 0
    neighbor = 'FAILED TO FIND FACTION'
    for color in neighboring_colors[faction]:
        for other_faction in factions_in_game:
            if other_faction in color_to_faction[color]:
                num_neighbors += 1
                neighbor = color
    if num_neighbors == 2:
        neighbor = 'both'

    if num_neighbors > 0:
        return '{}.{}'.format(faction, neighbor)
    else:
        # We don't need this case, but we use this so that our
        # debug sentinel value will fall through if we have a bug.
        return '{}.none'.format(faction)
    

# Input: list of factions
# Output: something like [darklings.both or darklings.blue, etc.]
def factions_with_neighbors(factions_in_game):
    return [get_faction_neighbors(faction, factions_in_game) for factions in factions_in_game]

ratings = {}
with open('ratings.json', 'r') as f:
    parsed = json.load(f)
    ratings = parsed["players"]

players = {}
with open('all_players.json', 'r') as f:
    players = json.load(f)

def lowest_rating_in_game(game):
    lowest = 10000.0
    for player in game["players"]:
        username = players[player['id_hash']]['username']
        rating = ratings[username]['score']
        if rating < lowest:
            lowest = rating
    assert(lowest != 10000.0)
    return lowest

def win_rate_vs_rating(games, do_adjustment, compute_neighbors):
    total_games = [collections.defaultdict(int) for i in range(num_slots)]
    num_wins = [collections.defaultdict(int) for i in range(num_slots)]

    for junk, game in games.items():
        lowest_rating = lowest_rating_in_game(game)
        for bucket in range(num_slots):
            bucket_rating = lowest_score + bucket * increment
            highest_vp = -1
            highest_faction = 'FAILED_TO_FIND_FACTION'
            
            factions_in_game = []
            for player in game['players']:
                faction = player['faction']
                factions_in_game.append(faction)

            if lowest_rating >= bucket_rating:
                for player in game['players']:
                    faction = player['faction']
                    vps = player['vp']
                    if (do_adjustment):
                        vps += faction_adjustment[faction]
                    if compute_neighbors:
                        faction = get_faction_neighbors(faction, factions_in_game)
                    total_games[bucket][faction] += 1
                    if vps > highest_vp:
                        highest_vp = vps
                        highest_faction = faction
                assert(highest_faction != 'FAILED_TO_FIND_FACTION')
                # print("bucket {} player {}".format(bucket, highest_start_order))
                # print(num_wins)
                num_wins[bucket][highest_faction] += 1
    return total_games, num_wins

def process_games_file(filename, do_adjustment, compute_neighbors):
    with open(filename, 'r') as f:
        parsed = json.load(f)
        return win_rate_vs_rating(parsed, do_adjustment, compute_neighbors)

# total_games, num_wins = process_games_file("filtered_games.json")
# print(total_games)
# print(num_wins)

def rank_factions():
    total_games, num_wins = process_games_file("filtered_games.json", True, True)

    
    for bucket in range(num_slots):
        factions_with_rates = []
        bucket_rating = lowest_score + bucket * increment
        for faction in num_wins[bucket]:
            win_pct = num_wins[bucket][faction] / total_games[bucket][faction]
            factions_with_rates.append((faction, win_pct))

        sorted_factions = sorted(factions_with_rates, key=lambda x: x[1])
    
        print("--------{}---------".format(bucket_rating))
        for faction, win_pct in sorted_factions:
            print("{:<24s}{:>.2f}".format(faction, win_pct))

def base_factions():
    total_games, num_wins = process_games_file("filtered_games.json", False, False)

    splits = [0,1,2]
    handles = []

    for ss in splits:
        filename = "faction.{}.csv".format(ss)
        handles.append(open(filename, 'w'))
        print("rating,faction,win rate", file=handles[ss])

    for bucket in range(num_slots):
        total_games_in_bucket_debug = 0
        for faction in num_wins[bucket]:
            # Not enough data due to recent v4 faction adjustment.
            if faction != 'riverwalkers' and faction != 'shapeshifters':
                ss = faction_splits[faction]
                bucket_rating = lowest_score + bucket * increment
                win_pct = num_wins[bucket][faction] / total_games[bucket][faction]
                print("{},{},{}".format(bucket_rating, faction, win_pct), file=handles[ss])

# base_factions()

rank_factions()


