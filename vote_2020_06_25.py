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
    # I think this project is very interesting because it is both a near-term need (UI wallet) and has some interesting technological improvements to PKT that would increase PKT's usability.
    'short': 0.8,   # I believe that having a desktop UI is critical for widespread consumer adoption of PKT
    'long': 0.4,    # Though a UI walletw will be a long-lasting part PKT, I believe the off-chain and decentralized nature of the wallet has important utility for PKT future
    'scope': 0.8,   # The timeline and budget seem reasonable for this project, given my understanding of the scope and talent involved.
    'risk': 0.95,   # The team seems to have excellent pedigree, including having developed the BIP-47 protocol
    'hazard': 0.8   # There is already a traditional wallet being developed, but without BIP-47 support.  I would prefer that these two projects collaborate, to prevent segmentation of users and hopefully to leverage existing and new tech into a faster shipping time and for the developers involved to all benefit from understanding the latest tech.
  },

  'techsupport': {
    # I believe this project will result in dramatically improved reliability, speed, and usability of the  PKT blockchain in the near term.
    'short': 0.9,     # I gurantee this project will result in immediate, tangible improvements to PKT and the chain. As party to discussions with the Gridfinity team on existing issues, I know they are already commited to improving and stabilizing PKT and have already put in considerable successful effort to do so at their own expense.
    'long': 0.1,      # The improvements Gridfinity seeks to make are incremental and not revolutionary.  They will improve the stability and speed of the chain but are unlikely to revolutionize how PKT works.
    'scope': 0.7,     # Gridfinity is asking for 25000 PKT/hour, which at it's current estimated value is around $83/hour, and about 2 days per week dedicated to PKT improvements both sounds reasonable and in line with what I believe to be the time they have put into PKT in the past. In thir proposal, they estimate 2m PKT/month but without an end date. Understandibly, this is a maintenance proposal and therefore it is difficult to estimate the timeline. Bugs are squashed as they are found. But a major limitation of this proposal is  that there is no difinitive end and therefore no way to calculate the total cost in accordance to our budget.
    'risk': 0.9,      # Gridfinity has been working with Caleb to improve PKT for over a year. They rely on PKT for their business model. Their developer, Jeff has make specific improvements and bug fixes to PKT in the past and knows the code-base. Therefore I believe they have the capability to do this work and are motivated to do so.
    'hazard': 0.3     # I am involved with one of Gridfinity's partners, Jon in another venture, Anode. This puts me in a conflict of interest in voting for this team, but I believe that fact is mitigated by the pedigree of their past work regarding PKT.
  },

  'tokenstrike': {
    # I believe this project will deliver fascitating improvements to PKT, including opening token swapping and lightning payments, which are directly in line with PKT's objectives.
    'short': 0.1,   # I believe there is little short-term gain from implementing this project
    'long': 0.9,    # I believe an advanced token issuance protocol that is Lightning compatible would enable PKT Cash liquidity and ultimately be a building block in the creation of both a PKT trading market and in a bandwidth leasing market that is ultimately goals of the PKT network.
    'scope': 0.5,   # At the current estimated value of PKT, each milestone costs about $30k. At 4 milestones this is  $133,333, but no timeline is given and no team is yet speculated. My experience with Caleb is that he is fair and honest,  but it is difficult to know for certain what the value of the project is without those elements.
    'risk': 0.9,    # Caleb has laid out the protocol's states and messaging, and as the inventor of PKT he knows what he's working with. I believe he has everything he needs to execute this project.
    'hazard': 0.3   # I am involved with Caleb a venture, Anode, which puts me in a conflict of interest in voting for him. However, he is the brilliant inventor of PKT and cjdns. I believe his pedigree and follow-through are self evident. No one knows these technologies better than him.
  },

})


# Arceliar
votes.append({
  'runewallet': {
    "short": 0.95, # Not much to say, if it does what it says on the tin then I'd expect it to have a significant impact short-term
    "long": 0.5, # It helps, but wallets are the sort of thing that I expect would emerge somewhere in the community if given enough time and continue to gain features ~indefinitely, so in the grand scheme of things I would expect that accepting this proposal would have diminishing implications over time
    "scope": 0.5, # The wallet seems generally in-scope, the main issue is the opportunity cost -- this would take our entire budget for this proposal period, and we wouldn't have anything left over to let us open the next proposal period early
    "risk": 0.5, # Two potential issues. 1: I don't know the applicants (at least the ones listed on the proposal, as far as I'm aware), so there's at least a little uncertainty about how prepared they are to work on this, though their related work is generally encouraging (so this has a minor effect -- if anything it's probably good, since it means there's no nepotism hazard). 2: the more significant issue -- the "planning fallacy" -- is that the proposal aims for a 3(+) month schedule with a dozen people working. I'm happy to see the + in the initial outline, but I think *in general* people have trouble predicting how long it will take to do something (especially when other people are involved, a dozen+ in this case). The milestones do a pretty good job of outlining what the applicants want to have happen each month, but I think it would benefit a bit from documenting which components depend upon each other, which parts of the milestone(s) could reasonably be delayed without significantly altering the project timeline as a whole, and what (if anything) can be done to mitigate any issues that arise if a critical component takes longer than expected. Basically, I'd like to hear what a worst-realistic-case scenario sounds like, since (statistically speaking) timelines tend to advance a little worse than that on average
    "hazard": 1.0, # I'm not aware of any conflicts of interest or other issues that would lead to problems here
  },
  'techsupport': {
    "short": 0.95, # Tech support is useful, though I tend to think it's not quite as important as core blockchain development is (e.g. there's less there to support before things are feature complete, so better to prioritize developments first and support later, at least in my train of thought)
    "long": 0.5, # No direct benefit after the project duration, but presumably some indirect benefit from a larger and more skilled community
    "scope": 0.83, # (40/48, rounded, for lack of a better idea, since it's kind of hard to compare cost-per-person-month for focused development work in the other projects vs something as open-ended and wildly variable tech support). I think that, given the budget constraints in the current proposal period, asking for 2 years is a bit much. I think it would be inappropriate to renegotiate the duration after we've already voted, but for future reference, it probably would have made sense to update this proposal with an option to approve it for a shorter duration (1 or 1.5 years) at a lower budget. Then we'd effectively be choosing between tokens+support vs the OT wallet, instead of only getting to pick one.
    "risk": 0.95, # I can't really think of a failure mode for tech support, so it seems unlikely that there would be any problems here (at least anything unique to this proposal)
    "hazard": 0.5, # This is a little hazardous for 2 reasons. 1: The applicant(s) are known by several NS members, so there's the usual risk of some appearance of nepotism. 2: It seems like, given that Gridfinity both operates a large mining pool and sells mining hardware, they're in a position to financially benefit more from the existence of competent tech support (to increase the size of the community by both selling more hardware and likely picking up more miners through being the default pool in most documentation). So we'd basically be paying Gridfinity to do work that mostly benefits Gridfinity. On the other hand, *no* tech support doesn't really benefit anyone, so I'd begrudgingly consider this acceptable given the lack of alternatives.
  },
  'tokenstrike': {
    "short": 0.5, # Tokens themselves aren't particularly useful, it's the services built on them that matter, so by itself I think this probably doesn't have much short-term impact (but it has *some*, mostly by opening the door for other things to be built on top of it)
    "long": 1.0, # Long term this is strictly necessary for the project goals (bandwidth market, etc.)
    "scope": 1.0, # I can't think of anything out-of-scope about this. Since we only have enough budget for 1 project, all of them effectively have the same opportunity cost, but this one has the lowest real cost (e.g. we could open another submission window again sooner than if we went with another proposal)
    "risk": 0.75, # It's plausible that the loosened security requirements (that attacks can be proven to have taken place, instead of being blocked outright) and a few implementation details could mean that the result is insufficient for some intended use cases. That said, I would naively expect it to be good enough for a large enough number of cases that it's likely to still be useful, and if it was unfit for an interesting reason then at least we'd learn something from it.
    "hazard": 0.75, # The proposal was submitted by an NS member, so there's some appearance of nepotism (but realistically, this isn't something that I'd feel confident in supporting without CJD's oversight, so that partly cancels out).
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
