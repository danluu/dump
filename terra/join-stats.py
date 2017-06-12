import json

def append_game_hash(all_games, filepath):
    with open(filepath) as json_file:
        json_data = json.load(json_file)
        if 'games' in json_data:
            all_games.update(json_data['games'])
    

# First month: http://terra.snellman.net/app/results/v2/2013/02
all_games = {}
for year in range(2013, 2018):
    for month in range(1, 13):
        if (year > 2013 or month >= 2):
            filepath = "summary-data/{0}.{1}.json".format(year, month)
            print(filepath)
            append_game_hash(all_games, filepath)
            print(len(all_games))

with open('all_games.json', 'w') as outfile:
    json.dump(all_games, outfile) 

# j = json.load(data)
# print j
# l = json.dumps(j)
# print l
