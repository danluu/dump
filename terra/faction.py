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
    'chaosmagicians': 2,
    'icemaidens': 1,
    'riverwalkers': 1,
    'auren': 2,
    'witches': 1,
    'mermaids': 1,
    'alchemists': 0,
    'acolytes': 0,
    'halflings': 1,
    'cultists': 1,
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

def win_rate_vs_rating(games, do_adjustment):
    total_games = [collections.defaultdict(int) for i in range(num_slots)]
    num_wins = [collections.defaultdict(int) for i in range(num_slots)]

    for junk, game in games.items():
        lowest_rating = lowest_rating_in_game(game)
        # print("lowest", lowest_rating)
        for bucket in range(num_slots):
            bucket_rating = lowest_score + bucket * increment
            # print("bucket_rating", bucket_rating)
            highest_vp = -1
            highest_faction = 'FAILED_TO_FIND_FACTION'
            if lowest_rating >= bucket_rating:
                # print("incrementing bucket", bucket)
                for player in game['players']:
                    faction = player['faction']
                    total_games[bucket][faction] += 1
                    vps = player['vp']
                    if (do_adjustment):
                        vps += faction_adjustment[faction]
                    if vps > highest_vp:
                        highest_vp = vps
                        highest_faction = faction
                assert(highest_faction != 'FAILED_TO_FIND_FACTION')
                # print("bucket {} player {}".format(bucket, highest_start_order))
                # print(num_wins)
                num_wins[bucket][highest_faction] += 1
    return total_games, num_wins

def process_games_file(filename, do_adjustment):
    with open(filename, 'r') as f:
        parsed = json.load(f)
        return win_rate_vs_rating(parsed, do_adjustment)

# total_games, num_wins = process_games_file("filtered_games.json")
# print(total_games)
# print(num_wins)


def base_factions():
    total_games, num_wins = process_games_file("filtered_games.json", False)

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

base_factions()

