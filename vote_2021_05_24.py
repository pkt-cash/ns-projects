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

# Caleb
votes.append({
  'lobbying': {
    # This proposal is about building a non-partison lobbying campaign for Internet freedom, decentralization and
    # privacy. It has been said that if you don't tell your story then someone else will, and we have already begun
    # to see blockchain, crypto mining, privacy, and end-to-end encryption being cast in negative light. The US and EU
    # governments have been mulling bans on end-to-end encryption or mandatory backdoors, and cryptocurrencies are
    # increasingly are coming under regulatory scruteny with some discussion of outright bans on privacy coins such as
    # Monero. There is also an apparent PR war against crypto mining, with its supposed environmental impact getting
    # more media attention than that of even oil and coal exploration.
    #
    # The communities around these technologies have clearly been bad at explaining their importance to society, and I
    # think there is very real possibility that governments around the world will begin to turn their backs on freedom
    # of communication, which would have very real short term impact on the ability of PKT to fulfill the vision.
    'short': 3/5.0,

    # It has been said that the price of liberty is eternal vigilance, and to this day we see autocracy,
    # totalitarianism, and oppression being proposed as "for the greater good", despite their historically poor
    # longevity and association to some of the most horrible atrocities in history.

    # Blockchains enable individuals to leverage simple freedom of communication and organize themselves in ways
    # that were previously not possible without dependence on government, existing businesses, and the banking
    # system. This puts blockchain at the forefront of the struggle for individual liberty, but blockchain
    # communities currently do not make significant concerted efforts to promote the freedoms upon which they
    # depend. So I think there is a long term necessity to continue to communicate about the importance of end-to-end
    # encryption, open source software, freedom of communication, privacy, and decentralization.
    'long': 4/5.0,

    # The project proposal does not follow the standard template which makes it difficult to understand, but it does
    # seem to have strong success criteria for the amount of declared work. The declared work seems to be 320+80+160+160
    # hours (or roughly 4.8 person-months) and the cost seems to be 3.5 million PKT. As the current price in the informal
    # trading chat seems to be roughly 5 cents, this makes the average hourly cost about 243 dollars per hour which is
    # a bit high. Furthermore there is a disclamer where it is mentioned that the milestones require 75k, 50k, and 50k
    # USD respectively which comes to the same numbers. Unfortunately the project is proposed in such a way that in case
    # of a rise in PKT price, the applicant wishes still to receive the entire payment but in case of a drop in PKT price,
    # they wish the payment to be more. I'm not ready to fail the project on this point but I think it has serious flaws.
    'scope': 1/5.0,
    
    # It is difficult to understand what is being requested, but the project proposal seems not to ask for any payment
    # until after the first deliverables are provided. The payment seems to be well spaced across the milestones, but
    # there seem to be many "extra options" and it is unclear if the applicant expects the Network Steward to vote on
    # each one of these as though it were a separate project, or which of these may or may not be included in the
    # declared time effort. My feeling is that if the proposal were re-phrased to be clear, then it would have fairly
    # good risk control, but as of now, the biggest risk is that the Network Steward might mis-interpret the proposal
    # and disagree with the applicant as to which milestones were delivered and what should be paid out, or how much
    # PKT should be paid, as the applicant is unsure if 3.5mn PKT is enough. I think I have to fail this project for
    # being under-specified, it is a good overall idea but the application is not developed enough to be handled
    # directly by the Network Steward.
    'risk': 0/5.0,

    # As far as conflicts, the template was not used and the declaration is missing. There is a "minor" relationship
    # between Anode LLC (myself / Adonis) and one of the project participants (Alex Lightman), as he is also in a
    # software development contract with Anode. I don't think the applicant was intentionally hiding this fact, nor
    # that this constitutes a conflict for which we should step out from evaluation.
    # As far as "unfairly benefitting any one participant over any other", the hourly costs in the project are high
    # and it is unclear whether the declared hours are for the plain project or the project with "add-ons" included.
    # Most problematically, the costs are expressed in a "rachet" form where the applicant expects costs covered in
    # case of a decrease in PKT price but wants to keep the difference in case the price should go the other way.
    'hazard': 2/5.0
  },

  'wallet': {
    # Despite significant Network Steward support in the past, the wallet story is clearly not the strongest aspect of the PKT project.
    # There are currently 3 different wallets, a command line wallet which is robust but not user friendly, an electrum based
    # wallet which is user friendly but not robust enough to support thousands of payments which occur when mining, and Zulu
    # which is a GUI frontend for the command line wallet, but which only works on Apple computers.
    # There is an entirely separate wallet in development by the team who produces OpenTransactions, but this has not yet been released.

    # My observation is that there is an abundance of wallet "technology" but a lack of "product", so for example technical
    # support ends up falling on the open source community which means it inevitably has a "helping eachother" aesthetic
    # rather than one of a smooth experience with a complete product.

    # It is my opinion that the PKT community needs a business to step up and build a wallet product which has a financial model
    # that puts the customer in charge. The development of additional open source wallet technologies by the Network Steward is
    # certainly not worthless, but in my evaluation it does not meet the current pressing need.
    'short': 3/5.0,

    # This project is not described in terms of long term impact to decentralizing internet infrastructure. One might argue that
    # short term impact drives long term impact, but short term impact has it's own category in this evaluation.
    'long': 0/5.0,

    # Any endevor to build a crypto wallet must necessarily be based on either existing wallet technology such as PKTWallet
    # or ElectrumX, or on an entirely new wallet technology. Ideally a proposal such as this would specify whether it is to be
    # based on new or existing technology, and in the case of new tech to explain why it is important to have this new technology
    # and how it would work, and in the case of existing technology, to give a brief rundown of the tech stack so that
    # feasibility, cost, and risk can be evaluated. Since this proposal did not provide any of these details, we need to make a
    # guess as to intent, with an eye to the minimum deliverable that would satisfy the success criteria.
    # Since the proposal says "everybody should be able to send and recieve PKT" it seems that the focus is more about bringing
    # technology to the consumer rather than creating new technology, so I think it is fair to assume that the intent is to
    # leverage existing technology, which is also the cheaper option.
    # Building a new wallet based on existing technology should probably take somewhere around 1 person-month of effort to specify
    # and design, 3 PMs to develop and test and 1 PM to manage, which comes out to 5 PMs total. So the proposal's estimate of 10 PMs
    # is perhaps high, but not ridiculous.
    # On cost, the current price of PKT in informal trading seems to be roughly 5 cents, this places the total project cost at
    # 1,050,000 and thus the person-month cost at 105,000.
    # Assuming every month to be 4 40 hour weeks of fulltime work, the cost would be around 650$/hr which is very high.
    # I'm not going to outright fail the project on this point but I would only be inclined to accept a project of this cost if
    # there was nothing better.
    'scope': 1/5.0,

    # There are 5 milestones and payouts are reasonably spaced. Without knowing what existing wallet technology this project would
    # be based on, or if new, how the new wallet technology would work, I can't reasonably give this better than 2 of 5.
    'risk': 2/5.0,

    # On the question of hazard, the checkboxes for declaration of conflicts were not filled, but I don't know the applicant
    # and don't know of any conflicts myself. However the applicant is asking for what is, if we consider the informal trading
    # chat quote of 5 cents, over a million dollar grant. I see no mention of any business entity which would be in charge of the
    # project so it appears as though an individual would be receiving the funds. It is very irregular for an individual to receive 
    # a grant of over 1 million dollars in value rather than an entity with a public accountant. Also if the price of PKT were to
    # rise in the next couple of months, there is no provision in this project for the applicant to receive partial payout for
    # subsequent milestones which means this project could conceivably become worth tens of millions of dollars and have an
    # effective person-month rate of tens of thousands of dollars per hour so in my opinion this project fails the test of
    # "without unfairly benefitting any one participant over any other" and I am going to fail it on hazard control.
    'hazard': 0/5.0,
  },

  # Because there is a conflict, I have mechanically set the UOI rating to the average of the others, however
  # I have set hazard to zero instead of one because I have failed both of the other projects so is it best
  # in keeping with the intent of non-intervension for reason of conflict that I also fail the UOI project.
  'UOI_1': {
      'short': 3/5.0,
      'long': 2/5.0,
      'scope': 1/5.0,
      'risk': 1/5.0,
      'hazard': 0/5.0,
  },
  'UOI_2': {
      'short': 3/5.0,
      'long': 2/5.0,
      'scope': 1/5.0,
      'risk': 1/5.0,
      'hazard': 0/5.0,
  },
  'UOI_3': {
      'short': 3/5.0,
      'long': 2/5.0,
      'scope': 1/5.0,
      'risk': 1/5.0,
      'hazard': 0/5.0,
  },
  'UOI_4': {
      'short': 3/5.0,
      'long': 2/5.0,
      'scope': 1/5.0,
      'risk': 1/5.0,
      'hazard': 0/5.0,
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
