#!/usr/bin/python

import pymongo
import collections
import random
import trueskill

PLAYER_SKILLS = (15, 10, 8, 6, 4)
(GOOD_P, DECENT_P, OKAY_P, BAD_P, TERRIBLE_P) = PLAYER_SKILLS

OPENING_STRENGTHS = (3, 2, 1, 0, -2)
(GREAT_O, GOOD_O, DECENT_O, OKAY_O, BAD_O) = OPENING_STRENGTHS

def choose_from_dist(labels, weights):
    r = random.random()
    for l, w in zip(labels, weights):
        if w > r:
            return l
        r -= w

def sample_player_opening():
    p = random.choice(PLAYER_SKILLS)
    if p == GOOD_P:
        o = choose_from_dist(OPENING_STRENGTHS, [.05, .05, .05, .05, .8])
    else:
        o = choose_from_dist(OPENING_STRENGTHS, [.2, .2, .2, .2, .2])
    return p, o

def sim_team(t):
    return random.random() * (t[0] + t[1])

def sim_game(teams):
    results = [(-sim_team(t), t)  for t in teams]
    return [t[1] for t in sorted(results)]

def encode_team(t):
    return 'player' + str(t[0]),  'open:' + str(t[1])

def encode_player(t):
    return ('player' + str(t[0]), )

def sim_games(credit_assignment, blame):
    w, l = collections.defaultdict(int), collections.defaultdict(int)
    skill_table = trueskill.SkillTable()

    players_per_game = 3
    for i in range(1000):
        sample_teams = [sample_player_opening() for i in xrange(
                players_per_game)]
        players = set(t[0] for t in sample_teams)
        if len(players) != players_per_game:
            continue
        openings = set(t[1] for t in sample_teams)
        if len(players) != players_per_game:
            continue

        output_order = sim_game(sample_teams)
        for ind, t in enumerate(output_order):
            if ind == 0:
                d = w
            else:
                d = l
            creds = credit_assignment(t)
            if len(creds) > 1:
                d[creds[0] + '-' + creds[1]] += 1
            for cred in creds:
                d[cred] += 1

        trueskill.update_trueskill_team(
            [(credit_assignment(t), blame, ind) for 
             ind, t in enumerate(output_order)], skill_table)

        def print_t_record(t):
            print w[t[0]], w[t[1]], '-', l[t[0]], l[t[1]]

        for t in output_order:
            pass
            #print_t_record(t)

    for name, skill in skill_table.ordered_skills():
        print name, skill.mu, w[name], l[name]
    print
    for k in sorted(w.keys()):
        print k, w[k], l[k]

def main():
    print 'just players'
    sim_games(encode_player, [1.0])
    print 'players with teams'
    sim_games(encode_team, [.5, .5])

if __name__ == '__main__':
    main()
