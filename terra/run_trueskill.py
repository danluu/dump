from collections import defaultdict
import json
import trueskill.trueskill as ts

def make_player():
    p = Player()
    p.skill = (25.0, 25.0/3.0)
    return p

rankees = defaultdict(make_player)

wat = open('all_games.json')
jd = json.load(wat)
i = 0
for game_id in jd:
    game = jd[game_id]
    current_facs = []
    print 'game'
    for player in game['players']:
        fac = player['faction']
        rnk = player['rank']
        rankees[fac].rank = rnk
        
        current_facs.append(fac)
        print player['faction']
        print player['rank']
        print rankees[fac].skill

    # ts.AdjustPlayers has divide by 0 error if there's only one player.
    # TODO: look at games with one player to see how they exist. Could be a bug in this code?
    if len(current_facs) > 1:
        ts.AdjustPlayers([rankees[x] for x in current_facs])

for fac in rankees:
    print fac
    print rankees[fac].skill
                 
