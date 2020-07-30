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
    'long': 0.0,    # I believe an advanced token issuance protocol that is Lightning compatible would enable PKT Cash liquidity and ultimately be a building block in the creation of both a PKT trading market and in a bandwidth leasing market that is ultimately goals of the PKT network.
    'scope': 0.5,   # At the current estimated value of PKT, each milestone costs about $30k. At 4 milestones this is  $133,333, but no timeline is given and no team is yet speculated. My experience with Caleb is that he is fair and honest,  but it is difficult to know for certain what the value of the project is without those elements.
    'risk': 0.9,    # Caleb has laid out the protocol's states and messaging, and as the inventor of PKT he knows what he's working with. I believe he has everything he needs to execute this project.
    'hazard': 0.3   # I am involved with Caleb a venture, Anode, which puts me in a conflict of interest in voting for him. However, he is the brilliant inventor of PKT and cjdns. I believe his pedigree and follow-through are self evident. No one knows these technologies better than him.
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