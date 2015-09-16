from collections import defaultdict
import json
import trueskill.trueskill as ts

class Player(object):
    pass

alice = Player()
alice.skill = (25.0, 25.0/3.0)

bob = Player()
bob.skill = (25.0, 25.0/3.0)

chris = Player()
chris.skill = (25.0, 25.0/3.0)

darren = Player()
darren.skill = (25.0, 25.0/3.0)

alice.rank = 1
bob.rank = 2
chris.rank = 2
darren.rank = 4

ts.AdjustPlayers([alice, bob, chris, darren])

print(" Alice: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(alice.skill))
print("   Bob: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(bob.skill))
print(" Chris: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(chris.skill))
print("Darren: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(darren.skill))

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
    if len(current_facs) > 1:
        ts.AdjustPlayers([rankees[x] for x in current_facs])

# ts.AdjustPlayers([rankees['alchemists'], rankees['swarmlings'], rankees['nomads'], rankees['witches'], rankees['nofaction2']])

for fac in rankees:
    print fac
    print rankees[fac].skill
                 
