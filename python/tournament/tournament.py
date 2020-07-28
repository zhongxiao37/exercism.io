import re

def tally(rows):
    header = 'Team                           | MP |  W |  D |  L |  P'
    ranks = [header]
    teams = {}
    for row in rows:
        teams = add_match_result(teams, row)
    
    ranks += calculate_ranks(teams)
    return ranks

def calculate_ranks(teams):
    formatter = '{:<31s}|{:>3d} |{:>3d} |{:>3d} |{:>3d} |{:3d}'
    ranks = []
    for t in sorted(teams.items(), key=lambda v: (-v[1]['P'], v[0])):
        ranks.append(formatter.format(t[0], t[1]['MP'], t[1]['W'], t[1]['D'], t[1]['L'], t[1]['P']))
    return ranks

def add_match_result(teams, row):
    m = re.match('(.*?);(.*?);(.*)$', row)
    home_team_result = 'win' if m.group(3) == 'loss' else ('loss' if m.group(3) == 'win' else m.group(3))
    teams = add_team_result(m.group(1), m.group(3), teams)
    teams = add_team_result(m.group(2), home_team_result, teams)
    return teams

def add_team_result(team, result, teams):
    if team in teams.keys():
        teams[team]['MP'] += 1
        teams[team]['W'] += 1 if result == 'win' else 0
        teams[team]['D'] += 1 if result == 'draw' else 0
        teams[team]['L'] += 1 if result == 'loss' else 0
        teams[team]['P'] += 3 if result == 'win' else (1 if result == 'draw' else 0)
    else:
        teams[team] = {'MP': 1}
        teams[team]['W'] = 1 if result == 'win' else 0
        teams[team]['D'] = 1 if result == 'draw' else 0
        teams[team]['L'] = 1 if result == 'loss' else 0
        teams[team]['P'] = 3 if result == 'win' else (1 if result == 'draw' else 0)
    return teams
