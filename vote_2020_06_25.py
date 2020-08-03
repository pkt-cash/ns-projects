#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 80.0  # million
costs = {
  'runewallet': 80.0,
  'techsupport': 48.0,
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

## Benedict Lau
votes.append({
  'runewallet':  { 'short': 0.7, 'long': 0.7, 'scope': 0.5, 'risk': 0.8, 'hazard': 0.9 },
  'techsupport': { 'short': 0.8, 'long': 0.5, 'scope': 0.7, 'risk': 0.9, 'hazard': 0.7 },
  'tokenstrike': { 'short': 0.6, 'long': 0.7, 'scope': 0.8, 'risk': 0.9, 'hazard': 0.7 },
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

# Caleb
votes.append({
  'runewallet': {
    'short': 0.8, # This is a very impressive set of features to be developed, while it will not distinguish PKT from other blockchains, this will provide a very solid path forward for the project.
    'long': 0.3, # The Open Transactions system can potentially be a good answer to the need for micropayments for a bandwidth market and tokens for representing bandwidth resources, however these solutions are also being developed by Lightning Network developers and many Ethereum-like smart contracting platforms and this proposal does not seek to address any of the more niche requirements of the PKT project.
    'scope': 0.6, # There are two ways that this proposal's success criteria can be read. If we ignore the line "Perform all the already implemented OT transactions that are available on a Notary on PKT, BCH and BTC." then what we have is a wallet with off-chain transacting capability and colored coins which supports iOS, Android, Mac and PC. If we consider that the above line means support for the above-documented "Transfers", "Cash", "Cheque", "Voucher", "Invoice", "Market Offer", "Recurring Payments", and "Smart Contract", then we have additional features, including an important feature which is built-in decentralized exchange functionality. Unfortunately we cannot afford a charitable reading of a proposal when later on we must decide whether the delivered work warrants payment. However, a wallet supporting the major operating systems with colored coin and off-chain transaction support is still a significant amount of work. It is hard to quantify exactly how much work is needed to produce these results, clearly a basic wallet can be achieved for cheaper, for example by a simple Electrum fork. However, it is clear that the Open Transactions team has historically taken the high road and invested significant effort into building their technology and there is no reason in my mind to think that the person-month figure is a scam. The person-month cost is 1.78mn PKT per person-month, making this the cheapest project per declared person-month. However we must also consider the value to the PKT project. As I had said before, a good set of the real needs of the PKT project can be more cheaply achieved with different technologies, so while the work-effort is an incredible bargain, the results are competitive but not outstanding.
    'risk': 0.6, # The success criteria for this project are very well specified, payment is evenly spaced between the milestones and even if milestone 1 is the only milestone successfully delivered, it contains a nice set of success criteria which constitutes delivery of a working desktop wallet app. These risk controls are of very high quality though it must be recognized that the budget and projected effort of this project is larger than any project which has come before it and therefore the inherent risk of the project is particularly high. The up-front payment is 5mn PKT which is not insignificant but is small in comparison to the scope of the project as a whole.
    'hazard': 0.8, # As far as I am aware, there are no conflicts of interest with the NS team. I also see no obvious sign that the project benefits one party over any other. There is a 5mn PKT up-front payment which means the applicant would benefit from running with the loot, but this applicant carries with them a fairly reasonable reputation which would be lost if they were to do so - put differently, they would have to believe that PKT has no future in order for that move to be advantageous. The timeframe given is "3+ months" which is unclear about exactly how much time the applicant plans to spend before submitting milestones, one form of arbitrage which the NS is attentive to is using a project as an "option" to do the work and acquire the PKT later on - pending a rise in the price, but to abandon the project otherwise. It does not seem that this is the case here. Another form of arbitrage which must be considered is whether the amount of work required is in fact 43 person-months, this is a more complex question because it is difficult to ascertain how much work must be done to achieve the stated milestones. Because, as stated in section 3 "Use of Resources", there are likely faster ways to achieve similar objective but there is no evidence of over-charging, I find that a perfect score cannot be awarded but I do not wish to deduct too many points for what is simply a complex topic - opaque to evaluation but by no fault of the applicant.
  },
  'techsupport': {
    'short': 0.8, # The idea of having someone spend time patching and updating pktd definitely has short term benefit to the project
    'long': 0.6, # My feeling is that longer term, as more pools and miners establish themselves, this will become less and less of a necessity
    'scope': 0.3, # Under a normal cost analysis right now, the project is reasonably priced, but because it is stretched over such a long period, 2 years, there is a distinct possibility for the applicant to end up getting paid an exorbitant amount for their work. Not that any other applicant is getting less, but other applicants are expending labor *now*, at a time when the price of PKT is very low. If the timeframe is in the 3-6 month range then I would give this an 8.
    'risk': 0.9, # There is little risk of the project not succeeding because the project lacks solid metrics to define success
    'hazard': 0, # I'm going to fail this project on the hazard scale because of the combination of the long timespan and lack of success criteria. While I don't believe it is the intent of the applicant, I find the success criteria to be lax enough that the project could be successful without any work done other than the day-to-day operation of a for-profit mining pool. This hazard is exasperated by the timespan of the proposal. In one year's time, the now reasonably payment could become so exorbitant as to bring scandal to the institution of the NS, and without clearly defined written success criteria, we would be unable to prove to the incredulous examiner that this was anything more than a handout to friends of the NS. If the timespan were 3 months and there were clearly defined success criteria then I would have nothing to say against this project but as it is I cannot accept it.
  },
  'tokenstrike': {
    'short': 0.8, # mechanically set to the average of the other two projects because I have a confilct of interest
    'long': 0.45, # mechanically set to the average of the other two projects because I have a confilct of interest
    'scope': 0.45, # mechanically set to the average of the other two projects because I have a confilct of interest
    'risk': 0.75, # mechanically set to the average of the other two projects because I have a confilct of interest
    'hazard': 0.4, # mechanically set to the average of the other two projects because I have a confilct of interest
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
