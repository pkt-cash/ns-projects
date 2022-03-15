#!/usr/bin/env python2.7

# budget = max budget available to allocate
# costs = dict of project name -> project cost
# votes = list or set, one vote (dict) per person
#   vote dict is name -> scores (dict)
#   scores dict is category name -> category's score
def getApprovedProjects(budget, costs, votes):
  votes = getCombinedVotes(votes) # combine scores per category, and throw out projects with fewer than 3 non-zero supporters
  cost = 0
  approved = []
  while cost < 0.9 * budget:
    costs = getAffordable(budget, cost, costs)
    if len(costs) == 0: break # no remaining projects that fit under budget
    best = getBest(approved, votes, costs) # lower cost used as tiebreaker
    if best == None: break # all filtered project are approved
    cost += costs[best]
    del costs[best]
    approved.append(best)
  return approved

# expects a list (or set) of votes, as a dict with scores per category
# returns a list of votes as dicts that map name onto a single combined score
# filters the list to only include projects where at least 3 votes give a non-zero score
def getCombinedVotes(votes):
  ret = []
  approvals = dict()
  for vote in votes:
    v = dict()
    for project,scores in vote.iteritems():
      v[project] = combine(scores)
      if project not in approvals: approvals[project] = 0
      if v[project] > 0: approvals[project] += 1
    ret.append(v)
  for project,count in approvals.iteritems():
    if count < 3:
      # too many 0 scores to be considered
      for a in ret:
        del a[project] 
    else:
      # make sure every project appears on every ballot
      # so fill in anything missing with a 0 score on that ballot
      for a in ret:
        if project not in a: a[project] = 0.
  return ret

# expects a dict of scores per category
# returns a combined score
def combine(cats):
  return 0.5*(cats['short'] + cats['long'])*cats['scope']*cats['risk']*cats['hazard']

# expects a the total budget, cost so far, and a dict of names -> costs per project
# returns a dict of names -> costs per project, filtered to only include the projects
#   which are still affordable given the remaining budget
def getAffordable(budget, cost, costs):
  ret = dict()
  for name,req in costs.iteritems():
    if cost+req > budget: continue # too expensive to afford anymore
    ret[name] = req
  return ret

# expects an iterable (e.g. list, set) container of projects approved so far,
#   and an iterable container of votes (with scores already combined)
# returns the best unapproved project remaining in votes
def getBest(approved, votes, costs):
  scores = dict()
  approved = set(approved)
  for vote in votes:
    s = sum([vote[a] for a in approved])
    w = 1./(1. + s) # weight of this vote in the current round
    for project,score in vote.iteritems():
      if project in approved: continue # already approved
      if project not in scores: scores[project] = 0.
      scores[project] += w*vote[project]
    s = 0. # sum of scores given to candidates approved so far
  best, bestScore, bestCost = None, 0., 0
  for project,score in scores.iteritems():
    if project in costs and (score > bestScore or (score == bestScore and costs[project] < bestCost)):
      best = project
      bestScore = score
      bestCost = costs[project]
    # TODO if scores and cost both tie, select a winner based on some other sensible metric
    #   e.g. the earlier submission wins
    #   currently it's just arbitrarily broken based on whatever order the iterator follows
  return best

# End
