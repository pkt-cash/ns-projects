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

# Ben
votes.append({
  'gridfinity': {
    # It's been clear some support is essential to operating a functional network at all
    # so this work is a necessity in the short term. The scope is clearly-defined and
    # there is a history of the same people doing this work, so risk is low and not
    # spending on this project pretty much asks gridfinity to do this for free.
    'short': 0.9,
    'long': 0.8,
    'scope': 0.8,
    'risk': 0.9,
    'hazard': 0.7
  },

  'community': {
    # The network has reached a stage where there is enough software, infrastructure, and
    # communication materials to engage with a wider audience. It is important to do this
    # broad engagement in order to identify gaps and start receiving wider input, so this
    # proposal seems timely. There are clear asset deliverables, which this project team
    # seems capable as they have completed previous projects. The "10x growth" goals are
    # inherently risky, but there are clear metrics defined, so to the NS the risk is bound
    # by respective milestones. There is additional "hazard" risk around this leading to
    # PKT price speculation, and the team has made a statement on how to address this risk.
    # Since assets are published openly, the NS will have an opportunity to evaluate whether
    # the community building efforts are focused on driving price speculation or promoting
    # the NS's vision of a decentralized bandwidth marketplace. If accepted, I encourage the
    # project team to stick to this statement and present plenty of evidence in their reports.
    'short': 0.8,
    'long': 0.7,
    'scope': 0.6,
    'risk': 0.5,
    'hazard': 0.6
  },

  'doublewallet': {
    # Important to have a second wallet implementation for the near term, but long term
    # value is limited. A bit expensive for the outcome in relation to what is most needed
    # for the network at this time. High confidence the project team can deliver this.
    'short': 0.7,
    'long': 0.5,
    'scope': 0.6,
    'risk': 0.7,
    'hazard': 0.6
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
