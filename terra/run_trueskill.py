from collections import defaultdict
import json
import trueskill.trueskill as ts

class Player(object):
    pass

def make_player():
    p = Player()
    p.skill = (25.0, 25.0/3.0)
    p.num_games = 0
    p.num_wins = 0
    p.num_last = 0
    return p


def load_all_games():
    wat = open('all_games.json')
    jd = json.load(wat)
    return jd

def calc_faction_ts(jd):
    rankees = defaultdict(make_player)
    i = 0
    early_break = False

    for game_id in jd:
        game = jd[game_id]
        current_facs = []
        print 'game'
        num_players = len(game['players'])

        for player in game['players']:
            fac = "p" + str(num_players) + "," + player['faction']

            rnk = player['rank']
            rankees[fac].rank = rnk
            rankees[fac].num_games = rankees[fac].num_games + 1
            if rnk == 1:
                rankees[fac].num_wins = rankees[fac].num_wins + 1
            if rnk == num_players:
                rankees[fac].num_last = rankees[fac].num_last + 1
        
            current_facs.append(fac)
            print fac
            print rankees[fac].num_games
            print player['rank']
            print rankees[fac].skill

            # ts.AdjustPlayers has divide by 0 error if there's only one player.
            # TODO: look at games with one player to see how they exist. Could be a bug in this code?
            if len(current_facs) > 1:
                ts.AdjustPlayers([rankees[x] for x in current_facs])

        if early_break:
            if i > 100:
                break
            i = i + 1
    return rankees


def sort_ranks(rankees):
    detail_ranks = defaultdict(dict)
    for tsitem in rankees:
        num_players, fac = tsitem.split(",")
        detail_ranks[num_players][fac] = rankees[tsitem]
        # print tsitem
        # print float(rankees[tsitem].num_wins)
        # print float(rankees[tsitem].num_games)
        # print float(rankees[tsitem].num_wins) / float(rankees[tsitem].num_games)
        # print rankees[tsitem].skill

    for num_players in detail_ranks:
        print num_players
        sortme = []
        for fac in detail_ranks[num_players]:
            sortme.append((fac,
                           detail_ranks[num_players][fac].skill,
                           float(detail_ranks[num_players][fac].num_wins) / detail_ranks[num_players][fac].num_games,
                           float(detail_ranks[num_players][fac].num_last) / detail_ranks[num_players][fac].num_games
                       ))
            # print fac
            # print detail_ranks[num_players][fac].skill
        for wat in sorted(sortme, key=lambda x: -(x[1][0] - 3*x[1][1])):
            print wat

jd = load_all_games()
rankees = calc_faction_ts(jd)
sort_ranks(rankees)
