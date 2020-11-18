#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 70.0  # million
costs = {
  'gridfinity': 3.0,
  'community': 26.0,
  'doublewallet': 40.0,
}
votes = []

# Neil
votes.append({
  'gridfinity': {
    # I continue to be impressed by the support that Gridfinity has shown to the PKT
    # project and their support and infrastructure has been somewhat critical to the
    # success of the project so far. In the past I have mentioned my concerns over how
    # ongoing support will be handled and funded on a long-term basis in the future,
    # but for now I am happy that this is adjacent to the success of the project.
    'short': 0.9,   #
    'long': 0.6,    #
    'scope': 0.5,   # 
    'risk': 0.7,    # 
    'hazard': 0.7   # 
  },

  'community': {
    # The pkt.cash website and promotional material so far have been very good overall
    # and further expansion in this space will be important in order to maintain any
    # external interest in the project. However, I am a little cautious about promises
    # made in the success criteria and whether the results will have longevity, hence
    # the risk.
    'short': 0.8,   # 
    'long': 0.5,    # 
    'scope': 0.6,   # 
    'risk': 0.4,    # 
    'hazard': 0.6   #
  },

  'doublewallet': {
    # I am encouraged by the idea of exploring more than one approach to off-chain
    # transactions as a way of hopefully improving chances of success, but if nothing
    # else then we will have more than one functioning PKT wallet as a result of this
    # work which is of obvious long term benefit.
    'short': 0.5,   # 
    'long': 0.8,    # 
    'scope': 0.8,   # 
    'risk': 0.7,    # 
    'hazard': 0.8   # 
  },
})

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
