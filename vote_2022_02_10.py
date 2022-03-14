#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 20.0  # million
costs = {
  'pktdesk_blog':    0.350000,
  'wrkforce':       12.250000,
  'pktpay':          0.085000,
  'pktchat_upgrade': 0.275000,
  'fastercrypt':     8.500000, # total cost not clearly stated
  'pktchat_app':     0.600000, # total cost not clearly stated
  'route_server':    0.300000,
  'docs':            0.400000,
  'punks_match':     1.260000, # total cost not clearly stated
  'punks_atomic1':   0.504000, # total cost not clearly stated
  'punks_atomic2':   1.008000, # total cost not clearly stated
  'punks_atomic3':   2.016000, # total cost not clearly stated
  'mining_output':   0.591000,
}
votes = []

# Caleb
votes.append({
    'pktdesk_blog': {
        # I really want to like this project, it is honest work at a reasonable rate by a person who clearly believes in PKT and has been working for a long time already. This is the kind of person who *should* be funded.
        # However, there is a huge amount of risk associated with any kind of communication and even with the applicant's assurance that articles will strictly follow the community guidelines for ethical communication, communication related projects still carry a significant risk to the reputation of the project and to the public.
        # Also the effort is not specified in a stable currency so there is risk and hazard associated with PKT price changes.
        # Also the project is slightly vague about the deliverables and success criteria, making it hard to validate and increasing the risk and hazard somewhat.
        # I really would like to see this applicant get funded, but perhaps with a project structured more like the pkt_technical_documentation proposal.
        'short': 0.6,
        'long': 0.3,
        'scope': 0.6,
        'risk': 0.1,
        'hazard': 0.4,
    },

    'wrkforce': {
        # * The objective of this project is of critical short term value and it is of high long term value.
        # * 30k has been spent on preparing the application, and this seems excessive to me, but if the project is able to deliver value then I can see this price being reasonable amortized in.
        # * The main problem with this project is that it will take 3 months and 140k USD before we know if the platform works or not. This is an incredibly large risk for the NS to take. I would not be against funding all of these activities, but I want to have results quickly and then be able to expand funding with results in my hand.
        # * The applicant argues that it is not feasible to do the project in an agile way because there must be attention to compliance, legality, and data protection. But features such as user workflows, figma designs, public API, and notifications, to name a few, are clearly not necessary to achieve compliance, legality, and data protection, so I reject this argument.
        # * I'm giving this project a 0 on risk because I think it doesn't produce results soon enough to provide safety. I urge the applicant to come back with a bite-sized project which can start off this initiative.
        'short': 0.9,
        'long': 0.6,
        'scope': 0.3,
        'risk': 0.0,
        'hazard': 0.4,
    },

    'pktpay': {
        # * This project is quite useful for the short-term value of PKT, in the long term it is less important.
        # * The cost is fairly reasonable.
        # * This project has some code already existing. The risk would be better if the first payment were smaller.
        # * Hazard is relatively low.
        'short': 0.6,
        'long': 0.3,
        'scope': 0.6,
        'risk': 0.6,
        'hazard': 0.8,
    },

    'pktchat_upgrade': {
        # * Short term value of this project is very high, pkt.chat is used daily.
        # * Long term value is significant but not as high as short term, Matterfoss is a public good.
        # * Risk is quite low, the applicant has worked on this exact code before.
        # * Hazard is moderately high because of the past connection between the applicant and myself.
        # * I want to make an additional note that the applicant was highly accepting of guidance and promptly made the requisite changes to the proposal.
        'short': 0.9,
        'long': 0.5,
        'scope': 0.6,
        'risk': 0.7,
        'hazard': 0.4,
    },

    'fastercrypt': {
        # * The short term value of this is very high, long term value is low but not zero because these are valuable algorithms to make faster.
        # * The plan of giving teams access to the server for a "specified time" seems likely to become a problem
        # * This seems to be more complicated than it needs to be, surely this can be done but in the first round simply running `packetcrypt bench blk` ought to provide adaquate data, assuming the measurement code is verified not to have been tampered with.
        # * Risk is reduced because there is only payment after M1.
        'short': 0.9,
        'long': 0.2,
        'scope': 0.6,
        'risk': 0.5,
        'hazard': 0.6,
    },

    'pktchat_app': {
        # * This is very necessary because we're missing push notifications right now.
        # * Long term it is not very high value.
        # * The application is not entirely complete, the total amount is unclear, seems to be about 600k
        # * Updated after the deadline, added some specificity.
        # * Because it has involvement of one of the NS team and the specification of the project is not great, I think we need to regard it as quite hazardous because of the vagueness of the proposal and the closeness to the NS - it can look like we gave our own guy a "wishy washy handout" project. However, I think this should be promptly corrected and re-applied in the next round.
        # * Would prefer to see dollar denomination, ideally using the One-Person-Software-Project template.
        'short': 0.9,
        'long': 0.3,
        'scope': 0.7,
        'risk': 0.5,
        'hazard': 0.0,
    },

    'route_server': {
        # * Visualization of route server data is quite significant in the short and long term.
        # * The success criteria on the (one) deliverable are could be subject to interpretation which could mean we are in for a surprise with regard to use of resources.
        # * Existance of previous OSS work reduces risk.
        'short': 0.7,
        'long': 0.7,
        'scope': 0.5,
        'risk': 0.7,
        'hazard': 0.5,
    },

    'docs': {
        # * This project is simple and straight forward, and documentation is needed.
        # * It could be considered a little bit expensive for documentation, and given Jeremy's closeness to the project, this creates some perceptual hazard. But I believe if we received a similar straight forward documentation propoasl we would redily accept it.
        'short': 0.9,
        'long': 0.3,
        'scope': 0.4,
        'risk': 0.7,
        'hazard': 0.4,
    },

    'punks_match': {
        # * The general idea of matching sellers and buyers together in a decentralized way is quite useful in the short term. Long term it is reasonably useful.
        # * I appreciate the attention to detail, pricing in stable currency makes the application much stronger.
        # * I'm concerned about the way some of the deliverables are specified. "Encrypted Chat" and "Multisig wallet escrow" are both highly complex technologies, not to be taken lightly.
        # * I'm surprised not to have seen any mention of other DEX efforts, including OpenDEX, which aimed at using atomic swaps.
        # * The "dispute resolution board", "Governance", and "Regulatory Risk Management Fund" indicates that the objective of this project is to bootstrap a legal entity. In the event that the dispute resolution board resolves a dispute in a way that is not to the liking of one of the parties, that party may reasonable initiate legal action against the entity for what they claim is fraud/theft. Furthermore, this entity is likely to be perceived by governments as an unregulated exchange which will lead to further legal trouble. Finally, it strikes me that participants in this entity (executor, dispute resolution board, etc) would be highly likely to benefit from this project more than the average member of the community, meaning it should fail the "no unfair benefit" clause of the Hazard definiton.
        # * It is reasonable to imagine that a project like this could help improve security of certain activites which take place within the PKT ecosystem, but it comes at the expense of creating an entity which has a lot of relationships, and which makes the overall ecosystem more fragile than it is already.
        # * I would very much like to see a developer write software for HTLC making simple atomic swaps with conditional transactions in PKT, but this is *software*, developed and published open source, for any person to use as they want. Furthermore I would like to see the project begin small (less than 10k EUR) in order to build confidence that the developer is capable of delivering and continue with follow-on projects.
        # * I'm afraid that this project has an unacceptable level of risk because it is about creating an entity which will be a defacto unregulated cryptocurrency exchange.
        # * Furthermore, I see it as impossible to verify that the benefit to the named participants in the entity won't be unfairly benefitting from this project more than the public, and since one of the named individuals is also one of the Network Steward team, a fact which is mentioned in the text but not in the conflict disclosure, I have to also fail this project on hazard.
        'short': 0.7,
        'long': 0.4,
        'scope': 0.5,
        'risk': 0.0,
        'hazard': 0.0,
    },

    'punks_atomic1': {
        # * Short term value of executing an atomic swap is pretty big, lots of possibilities within the community open up when we have the capability to do effective atomic swaps.
        # * Long term value is relatively significant as well, but not as big as short term.
        # * The scope is not too bad, the success criterium is laid out reasonably well. Use of resources is not very good because it could potentially be met with "demo code" hack. A stronger proposal would be to build tech which anyone can reliably make an atomic swap using the wallets and a simple block explorer style webapp.
        # * Risk looks pretty low because the team seems to be qualified and the success criterium is not particularly difficult to achieve. Risk would be lower if the project did not constrain itself to technical decisions such as using Rust programming language in the application.
        # * Hazard is likewise fairly low, as this is simple delivery of open source code in exchange for payment.
        # * As a side note, the duplicated text between project is annoying because I can't be sure what I can skip reading.
        'short': 0.7,
        'long': 0.4,
        'scope': 0.3,
        'risk': 0.8,
        'hazard': 0.8,
    },

    'punks_atomic2': {
        # * It looks like the objective of this project is to integrate atomic swapping into the default PKT electrum wallet. This might be high value if phase 1 proves to be working.
        # * Scope is likewise not that good, as with phase 1.
        # * Risk is high because it is dependent on phase 1 succeeding so risk is additive. I'm going to put risk to zero because I want to see phase 1 successful before we try to begin another phase.
        # * Hazard does not seem particularly high for the same reason as with the other tech projects proposed.
        'short': 0.7,
        'long': 0.4,
        'scope': 0.3,
        'risk': 0.0,
        'hazard': 0.8,
    },

    'punks_atomic3': {
        # * Short term value is pretty high, in the long term I think this should be supplanted by some client side software, but it is an important step in the process of getting atomic swaps stabilized.
        # * The scope is well enough defined, but the use of resources is not very good, I would like to see more than an adaptation of boltz.exchange for 40k.
        # * Risk is probably managable but because it is additive with other phases, I want to give this project a zero on risk until we know more from the applicant.
        # * Hazard does not seem particularly high for the same reason as with the other tech projects proposed.
        'short': 0.7,
        'long': 0.4,
        'scope': 0.1,
        'risk': 0.0,
        'hazard': 0.8,
    },

    'mining_output': {
        # * The short term value of nicer mining app console logs is undeniably high and I would give this a 7, long term is practically 0 since this mining software will probably be replaced as time goes by.
        # * Scope is clearly defined, this project has specific success criteria which are what I really like to see. Use of resources is good at the declared PKT price, but because this project is technically requesting payment in fixed amounts of PKT, this could become a majorly expensive project if PKT were to encounter a significant price run. I'm going to give this a 2 on scope.
        # * Risk is fairly low in general but if this applicant team is working on another project at the same time, I would prefer to see them make a first delivery on the other one before we accept a second one. So I will give this a tenative zero on risk.
        # * I would like to see this project proposed again in a following round, with the pricing explicitly established in stable currency, and after the group who is applying has had a chance to demonstrate their skills with another project.
        # * I don't have much to say about hazard, the project seems clean.
        'short': 0.8,
        'long': 0.0,
        'scope': 0.1,
        'risk': 0.0,
        'hazard': 0.8,
    },
})

# Template
votes.append({
    'pktdesk_blog': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'wrkforce': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'pktpay': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'pktchat_upgrade': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'fastercrypt': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'pktchat_app': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'route_server': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'docs': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'punks_match': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'punks_atomic1': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'punks_atomic2': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'punks_atomic3': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
    },
    'mining_output': {
        'short': 0.5,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.5,
        'hazard': 0.5,
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
