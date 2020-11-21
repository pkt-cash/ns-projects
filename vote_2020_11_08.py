#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 70.0  # million
costs = {
  'gridfinity': 3.0,
  'community': 26.0,
  'doublewallet': 40.0,
}
votes = []

# Adonis
votes.append({
  'gridfinity': {
    # est 1600 man-hours, 3mn PKT ~ $9.75/hour
    # Gridfinity has been and continues to put considerable effort into
    # improving the PKT blockchain. This proposal effectively describes
    # work they are already doing. I believe they have the experience,
    # commitment, and follow-through to deliver on this project.
    # They are better equipped than anyone to do it and honestly they deserve
    # it for the work they've already done.
    'short': 0.9,   #
    'long': 0.7,    #
    'scope': 0.7,   # 
    'risk': 0.7,    # 
    'hazard': 0.7   # 
  },

  'community': {
    # est 11000 man-hours, 26mn PKT ~ $11/hour
    # Josh and Jesse have done a nice job on the pkt.cash website, and having
    # worked with Josh on app design, I know he has a keen eye for design.
    # I believe this is a much bigger project than what is letting on,
    # and must be maintained and nurtured once begun.
    # instructional material can make the complex relatable.
    # Lack of such resources is hindering adoption of PKT,
    # But I fear the risk is that materials are launched and there is no
    # way to manage the potential rapid growth in questions and interest
    'short': 0.6,   # 
    'long': 0.8,    # 
    'scope': 0.4,   # 
    'risk': 0.4,    # 
    'hazard': 0.6   #
  },

  'doublewallet': {
    # est 6400 man-hours, 40mn PKT ~ $31.25/hour
    # The exisitng wallet is a challenge to use - it takes a long time to load
    # the chain and requires a lot of disk space. Obviously it is in progress
    # I like the idea of using newer technologies such as Electron to deploy
    # wallets simultaneously on multiple platforms, and it's possible that
    # having multiple wallet options for consumers can grow the community
    # faster, though I think only time can tell.
    # For these reasons I don't believe this is a critical feature
    # but one that improves the PKT project longer term.
    # As wallet functionality is more-or-less closed in scope, I believe
    # the scope and hazard are easily managed.
    'short': 0.4,   # 
    'long': 0.6,    # 
    'scope': 0.8,   # 
    'risk': 0.8,    # 
    'hazard': 0.8   # 
  },
})

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
    # seems capable as they have completed previous projects. There is "hazard" risk around
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

# Arceliar
votes.append({
  'gridfinity': {
    'short': 0.95,  # It's hard to think of something with more short-term benefit than ongoing tech support.
    'long': 0.5,    # A bug fixed now is a bug that doesn't need to be fixed later, so this has some long-term benefit, though I imagine the benefit to diminish after the proposal period ends (as people tend to stop caring about problems after they're no longer problems).
    'scope': 1.0,   # At 1.5 Mpkt per work-month, this is the most cost effective project submitted this round. While it wasn't explicitly factored in, I just want to note for the record that I appreciate how payment is requested after each PR milestone, rather than up front.
    'risk': 0.95,   # I would be very surprised if this project fails to meet its stated goals (maybe +- the exact number of PRs submitted over the period, since some can be of dramatically larger scope than others, though 20/month or ~1/work-day doesn't seem unresonably high or low given the track record). Even in scenarios where it fails to meet all of it's goals (for some unforeseen reason), in contrast with the other proposals, some progress is better than none progress for this one, and the relatively short duration keeps the range of unforeseen problems fairly tightly bound.
    'hazard': 0.75  # The applicant is known by several NS members, but there really isn't anyone else qualified to do this (outside of CJD). Additionally, it's a very short duration commitment, and the cost-per-work-month is quite low compared to other proposals (with payment after-the-fact). These factors serve to mitigate some of the usual hazard penality I would normally be inclined to assign to a proposal from an applicant known to the NS.
  },

  'community': {
    'short': 0.8,   # The documentation side of the project is of significant short-term value to my mind, though I'm not entirely convinced that the material being suggested is appropriate to the kind of users who are likely to become active participants in the community given the current state of pkt as a whole.
    'long': 0.25,   #  The sorts of documentation being proposed is likely to become obsolete / be replaced over the long run, so eventually its significance seems likely to decrease off (IMO).
    'scope': 0.8,   # ~1.86 Mpkt per work-month, normalized against the most cost-effective project (+- rounding).
    'risk': 0.75,   # There's a (relatively) large team working on (relatively) many deliverables over a short time, so compared to the other projects (submitted this proposal period), this one seems less likely to meet all of it goals (and do so on time -- which is a consideration when a large fraction of the payment is requested in advance). That said, partial completion is still worth something, so I think that mitigates some of the risk.
    'hazard': 0.5   # The applicants are known to one or more NS members, and there's nothing specific I can think of to help offset any appearance of favoritism (e.g. I don't think it's true that only these applicants would be capable of producing these resources for community building, though I do suspect they're among the best suited to do so within the existing community). On a personal note, I greatly I appreciate that the problematic 10x growth targets were removed.
  },

  'doublewallet': {
    'short': 0.75,  # A wallet is good, and two wallets does reduce the risk of complete failure, but it also means there's some duplicate effort (so the redundancy partly reduces some of the benefit).
    'long': 0.75,   # See above. Over all, having a good wallet is probably more important long-term than short term, but having *two* good wallets is probably less important (especially since at least one of them is more likely to become obsolete given the fact that, if pkt is successful enough for there to be a long term, then we're likely to see many more wallets be written over the years as new code bases emerge and platform market shares evolve).
    'scope': 0.375, # 4 Mpkt / person-month if we include pre-project effort (which seems reasonable to include), normalized against the most cost-effective proposal.
    'risk': 0.75,   # As with the community proposal, there's a relativley large amount of work to be done by a relatively large team (or two), over what seems like a relatively short duration considering the scope of the project. It seems somewhat likely that unforeseen problems will prevent at least some of the deliverables from being reached to the full satisfication of all parties by the target date, but this is partly mitigated by the pre-project effort and the fact that there are two wallets (so it's not the end of the world if some aspects of one don't pan out or take longer than expected).
    'hazard': 0.5   # The applicants are known to one or more NS members. While there are few people (if any) better positioned to write the OT/Rune wallet, I don't see the fact that it's an OT wallet being critical to fulfill the overall goal of the proposal (having one or two *good* wallet implementations, regardless of how they're implemented).
  },
})

## Caleb
votes.append({
  'doublewallet': {
    # This project is similar to the previously proposed runewallet project, but is much more attractive because there are two wallets being proposed to be developed and for half the cost.
    'short': 0.8,   # It is very important for the PKT project to have a good working wallet, it has been proven so far that while the chain backend itself is relatively stable, the wallet is lacking in features and stability which harms adoption. I'm giving this the same short term value as the Rune wallet proposal from before since two excellent wallets are not really much better than one.
    'long': 0.3,    # Both proposed wallets have plans for off-chain (micro) transactions, this is quite positive, but still there is no provision made for supporting the more niche aspects of the PKT project.
    'scope': 0.8,   # This project is highly competitive, the previous rune wallet project was given [0.8,0.7,0.5,0.83,0.6] on scope before and this project is for 2 wallets whereas the original rune wallet project was for 1, and this project is half the price, though it is to be noted that the original proposal included also a mobile version of the Rune wallet. The price is 4mn PKT per person/month. The declared effort is just under 1/5th of that of the rune project and the person-month cost is 2.35x, but this project has a reduced scope of what was in the original Rune project and some of the participants are different.
    'risk': 0.6,    # The risks involved in this project are relatively less than those of the original Rune wallet project because there are two parallel projects to be delivered, also it is observed that since the electrum wallet is available for download already - and the applicant needs to simply recoup their costs - we have a near guarantee of at least one of the two wallets being delivered.
    'hazard': 0.3,  # There is a fairly significant conflict because I am the contractor who developed the Electrum wallet for the applicant. In the event that there was contention between projects. As a result I will abstain from any vote which would be the deciding factor in choosing between this project and another. The reason I am evaluating it is to establish precedent for evaluation of future projects.
  },

  'community': {
    # This project is for helping to build the PKT community, communicating the objectives of the project to potential community members and providing documentation to help community members understand how they can participate.
    'short': 0.8,   # There were only 3 applications in this NS funding round, they all have declared conflicts (all are from a small community), and the total requested budget is less than the available budget. This should be satisfactory evidence that the project is not being properly explained to potential community members. Because what this project aims to do is something which is clearly lacking and important, I give this an 8/10 for short term need.
    'long': 0.6,    # Effectively informing critical potential participants of the project vision and providing them with ways to participate is something which can lead to significant long term value for the community. This application appears to community outreach (primarily short-term value) with establishment of community infrastructure such as blog and documentation, which is primarily long term value.
    'scope': 0.8,   # The number of participants is fairly large and there are clearly defined deliverables and KPIs. The KPIs look as though they would be difficult to fail by anyone doing realistic effort, but the deliverables seem fairly reasonable relative to the amount of declared work. The price is 1.85mn PKT per declared person-month which is quite competitive.
    'risk': 0.6,    # The contact person for the project delivered pkt.cash, demonstrating his capability for delivering a media project. We must acknowledge the risk that the short term aspects of the project are successful but the longer term community infrastructure building, less so. By the stated deliverables, the project seems like something that can reasonably be achieved by a dedicated team.
    'hazard': 0.3,  # These is a conflict with two of the NS evaluators, myself included. Also because of the basic nature of media deliverables, it will be difficult for us to reject anything showing even the slightest amount of effort and dedication.. Also because this is a project which will create communication materials, there is an inherent risk that these materials take on a "get rich quick" theme which is incongruent with the project vision - but the project proposal seems sensitive to the project vision and in fact contains a declaration of the intention *not* to "pump" the coin, also the pkt.cash website by the same applicant, I find to be tasteful and representative of the true project vision.
  },

  'gridfinity': {
    # This is a re-visit of the tech support project of 2020-07-24, but with 3 significant changes: 1. The term is shortened from 24 months to 3, 2. There are clearly defined success criteria, 3. There has been pre-project work in the form of successfully landed pull requests.
    'short': 0.6,   # The pktd software is easy to forget about because as long as "it works" it's not the highest priority to improve, but it is the base upon which all other things are built and there are changes to the Bitcoin core which need to be ported for the project strategy. In addition, to the extent that this maintenance effort extends also to the wallet software, this can have a very significant impact on every user of the PKT chain.
    'long': 0.6,    # For me this has a very high long term value because the ritual of maintaining the commons upon which PKT is built is necessary to building a robust community around the project.
    'scope': 0.7,   # The KPI of 60 accepted pull requests will be easily surpassed with a continuation of the current effort load, and we must acknowledge that "no KPI is perfect" and the applicant made an effort to indicate what it was that they're trying to aim for. The applicant also provided an estimate of the hours per week spent on these topics which can be used to estimate the effort resulting. Because of the limited term of the project, there is not a huge amount of risk if the cost/benefit turns out to be less than expected. As a final note, the pre-project work gives a very good idea of what the applicant intends to do, which is impressive.
    'risk': 0.8,    # The nature of this project is not highly ambitious (it does not contain fundamental research), secondly the KPIs are easy to achieve (this is not a good thing, but it makes the project less risky), and finally the applicant has already demonstrated the ability to provide value to the pktd project through existing pull requests which were accepted and landed - so the risk involved in this application is very low.
    'hazard': 0.6,  # All of the projects in this round have declared conflicts, this project does not have any NS participants directly involved in the execution of the project itself, nor does it have any of the hazards associated with a project which produces communication materials
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
