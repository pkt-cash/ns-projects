#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 40.0  # million
costs = {
  'lobbying': 3.5,
  'wallet': 21.0,
  'UOI_1': 10.0,
  'UOI_2': 10.0,
  'UOI_3': 10.0,
  'UOI_4': 10.0,
}
votes = []

# Votes will go here...

print "WINNING PROJECTS: %s" % getApprovedProjects(budget, costs, votes)

projects = {}
for x in votes[0]:
    projects[x] = { 'short': 0., 'long': 0., 'scope': 0., 'risk': 0., 'hazard': 0. }
for r in votes:
    for x in r:
        ## x = repo, price_display, etc
        for y in projects[x]:
          projects[x][y] += r[x][y]
trans = {
    'short':  "Short term impact         ",
    'long':   "Long term impact          ",
    'scope':  "Scope and use of resources",
    'risk':   "Risk control              ",
    'hazard': "Hazard control            "
}
for p in projects:
    print p
    for q in projects[p]:
        print "  ", trans[q], projects[p][q]
