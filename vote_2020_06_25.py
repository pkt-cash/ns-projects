#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 90.0  # million?
costs = {
  'runewallet': 80.0,
  'techsupport': 12.0,  # for the next 6 months
  'tokenstrike': 40.0,
}
votes = []

# Adonis
votes.append({
  # Three projects have been submitted this round and I believe
  # each of them are led by highly competant teams and are 
  # requesting reasonable compensation for their proposed efforts
  # 
  # Interestingly, each one addresses benefits PKT in a different way:
  # - immediate bug fixes and incremental improvements
  # - short-term usability improvements
  # - long-term technology/feature improvements
  'runewallet': {
    # Feels to me like pushing a second wallet with different functionality in the
    # early stages of the project may result in some confusion and fragmentation,
    # although I do definitely understand the appetite for some diversity long-term
    # and certainly lightning-like transactions will be beneficial in the future. 
    'short': 0.2,   #
    'long': 0.6,    #
    'scope': 0.7,   # 
    'risk': 0.5,    # 
    'hazard': 0.5   # 
  },

  'techsupport': {
    # Gridfinity right now is pretty central to the network functioning and overall
    # their input and support has been critical, even if it's just in the form of
    # fixing bugs and providing technical know-how. This is the kind of support that
    # the project needs at this stage, although it should be noted that the NS can
    # not continue to fund projects like this indefinitely without clearer end goals 
    'short': 0.8,   # 
    'long': 0.6,    # 
    'scope': 0.7,   # 
    'risk': 0.9,    # 
    'hazard': 0.5   #
  },

  'tokenstrike': {
    # Tokenstrike seems to be important to me as a long-term goal and I am reasonably
    # happy with the proposal. Aware that there is the possibility of lack of funding
    # this time to satisfy all projects, I would be very interested in seeing this
    # funded at some point, even if not straight away.
    'short': 0.1,   # 
    'long': 0.9,    # 
    'scope': 0.6,   # 
    'risk': 0.9,    # 
    'hazard': 0.5   # 
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
