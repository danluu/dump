import json

lowest_score = 300.0
highest_score = 1300.0
increment = 10.0

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

# TODO: off by one?
num_slots = int((highest_score - lowest_score) / increment)
total_games = [0] * num_slots
num_wins = [[0 for i in range(4)] for j in range(num_slots)]

# Already filtered to 4p, base map, no drops.
with open('filtered_games.json', 'r') as f:
# with open('filtered_games.fav11.json', 'r') as f:
    parsed = json.load(f)
    for junk, game in parsed.items():
        lowest_rating = lowest_rating_in_game(game)
        # print("lowest", lowest_rating)
        for bucket in range(num_slots):
            bucket_rating = lowest_score + bucket * increment
            # print("bucket_rating", bucket_rating)
            highest_vp = -1
            highest_start_order = -1
            if lowest_rating >= bucket_rating:
                total_games[bucket] += 1
                # print("incrementing bucket", bucket)
                for player in game['players']:
                    if player['vp'] > highest_vp:
                        highest_vp = player['vp']
                        highest_start_order = player['start_order']
                assert(highest_start_order != -1)
                # print("bucket {} player {}".format(bucket, highest_start_order))
                # print(num_wins)
                num_wins[bucket][highest_start_order-1] += 1


print(num_wins)
print(total_games)
    
print("rating,player,win rate")
for bucket in range(num_slots):
    for i in range(len(num_wins[bucket])):
        bucket_rating = lowest_score + bucket * increment
        player_number = i+1
        win_pct = num_wins[bucket][i] / total_games[bucket]
        # print("{},{}.fav11.123,{}".format(bucket_rating, player_number, win_pct))
        print("{},{}.all,{}".format(bucket_rating, player_number, win_pct))
        # print("{},{},true,{}".format(bucket_rating, player_number, win_pct))
