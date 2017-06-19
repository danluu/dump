import collections
import json

# TODO: refactor to share code with the very similar turn-order.py.

lowest_score = 900.0
highest_score = 1320.0
increment = 20.0
num_slots = int((highest_score - lowest_score) / increment)

factions = [
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

def win_rate_vs_rating(games):
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
                    if player['vp'] > highest_vp:
                        highest_vp = player['vp']
                        highest_faction = faction
                assert(highest_faction != 'FAILED_TO_FIND_FACTION')
                # print("bucket {} player {}".format(bucket, highest_start_order))
                # print(num_wins)
                num_wins[bucket][highest_faction] += 1
    return total_games, num_wins

def process_games_file(filename):
    with open(filename, 'r') as f:
        parsed = json.load(f)
        return win_rate_vs_rating(parsed)

# total_games, num_wins = process_games_file("filtered_games.json")
# print(total_games)
# print(num_wins)


def base_factions():
    print("rating,faction,win rate")
    total_games, num_wins = process_games_file("filtered_games.json")

    for bucket in range(num_slots):
        total_games_in_bucket_debug = 0
        for faction in num_wins[bucket]:
            bucket_rating = lowest_score + bucket * increment
            win_pct = num_wins[bucket][faction] / total_games[bucket][faction]
            print("{},{},{}".format(bucket_rating, faction, win_pct))

base_factions()

