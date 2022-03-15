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

# benhylau
votes.append({
    'pktdesk_blog': {
        'short': 0.9,
        'long': 0.3,
        'scope': 0.8,
        'risk': 0.8,
        'hazard': 0.7,
    },

    'wrkforce': {
        'short': 0.6,
        'long': 0.7,
        'scope': 0.3,
        'risk': 0.3,
        'hazard': 0.7,
    },

    'pktpay': {
        'short': 0.6,
        'long': 0.7,
        'scope': 0.9,
        'risk': 0.7,
        'hazard': 0.8,
    },

    'pktchat_upgrade': {
        'short': 0.8,
        'long': 0.6,
        'scope': 0.8,
        'risk': 0.8,
        'hazard': 0.9,
    },

    'fastercrypt': {
        'short': 0.6,
        'long': 0.8,
        'scope': 0.4,
        'risk': 0.6,
        'hazard': 0.7,
    },

    'pktchat_app': {
        'short': 0.7,
        'long': 0.3,
        'scope': 0.5,
        'risk': 0.8,
        'hazard': 0.4,
    },

    'route_server': {
        'short': 0.9,
        'long': 0.75,
        'scope': 0.65,
        'risk': 0.7,
        'hazard': 0.8,
    },

    'docs': {
        'short': 0.7,
        'long': 0.3,
        'scope': 0.4,
        'risk': 0.7,
        'hazard': 0.5,
    },

    'punks_match': {
        'short': 0.7,
        'long': 0.6,
        'scope': 0.4,
        'risk': 0.2,
        'hazard': 0.4,
    },

    'punks_atomic1': {
        'short': 0.7,
        'long': 0.5,
        'scope': 0.3,
        'risk': 0.1,
        'hazard': 0.2,
    },

    'punks_atomic2': {
        'short': 0.7,
        'long': 0.5,
        'scope': 0.3,
        'risk': 0.1,
        'hazard': 0.2,
    },

    'punks_atomic3': {
        'short': 0.7,
        'long': 0.5,
        'scope': 0.3,
        'risk': 0.1,
        'hazard': 0.2,
    },

    'mining_output': {
        'short': 0.7,
        'long': 0.5,
        'scope': 0.55,
        'risk': 0.6,
        'hazard': 0.8,
    },
})

# Arceliar
votes.append({
    'pktdesk_blog': {
        'short': 0.8, # The articles do contain useful information, and they are less sensationalized than most of the other pkt-related blog posts I've seen. I have some concerns about the writing quality, but I've addressed that in the 'risk' section.
        'long': 0.1, # Based on past blog posts, I don't think these are likely to be helpful in the long term (much of the information seems like it will become outdated). The parts that are unlikely to become outdated (e.g. basic info about how pkt works) is either already present on the blog, or can be found elsewhere, so I would not expect much long-term benefit from funding this
        'scope': 0.5, # Average. Neither so good nor so bad as to draw attention to this aspect of the proposal. This could be improved if it was a little more clear on what content is expected to be in the articles (e.g. a list of likely topics).
        'risk': 0.5, # There is little risk that the blog would fail to produce new content, but based on the blog posts that are already available, I don't think the information is presented very effectively.
        'hazard': 0., # Based on our past experiences with communication-oriented projects, and the blog posts available so far, I am reluctant to fund more communication projects in general. More importantly, some of the material on the site actively encourages people to financially invest in pkt mining (most notably the advertisements, such as on the main blog page, which list expected pkt/hr). Funding blog posts on a site that's covered in "Order Now" buttons would come off as the NS trying to pump the currency, even if the blog posts themselves are innocuous (and some of them already toe the line a bit -- the article reviewing CPUs also quotes expected pkt/hr).
    },
    'wrkforce': {
        'short': 0.8, # It's no panacea, but this would go a long way towards funding smaller projects and democratizing the direction of pkt.
        'long': 0.5, # If this works, I imagine more projects of this type will be developed (with or without NS involvement), but I see this as always being at least of average benefit, from a long-term perspective.
        'scope': 0.5, # Reasonably well aligned with what the NS already does. Not perfect, since there's bound to be some votes for things that would be out-of-scope (or at least the potential for such things occurring). The milestone objectives wander off track from what is strictly necessary to accomplish the task.
        'risk': 0., # More or less in line with what cjd said, this seems unnecessarily front-loaded with features that aren't strictly required for the platform to work. It's just too big of an investment before we would see any funds distributed based on the user votes.
        'hazard': 0., # The development cost is almost 5x the amount of funds being distributed. I realize there's always going to be some up-front cost, but those kinds of margins are unacceptable.
    },
    'pktpay': {
        'short': 0.75, # This would be nice to have, if you don't want to rely on a 3rd part multi-coin processor and don't want to roll your own. I think pkt is still young enough that I wouldn't trust 3rd parties to keep supporting it, and using this seems preferable to trying to roll your own (if nothing else, it would help sort-of standardize things). I see this as nice to have, but not crucial in the short term.
        'long': 0.1, # In the long term, there's enough financial incentives involved that I think something like this would emerge on its own, without us needing to fund it, so I don't think there's very much long-term benefit from this.
        'scope': 0.5, # Average. I don't think the NS should be funding development of things that businesses already have an interest in doing, then we're just subsidizing. This is small and simple enough that I don't think it's unreasonable to fund, since it's specifically solving an issue that affects businesses that are otherwise too small to deal with it themselves (without depending on a 3rd party processor, which could hurt their margins / raise their prices, and generally not make it worth while to accept pkt in some scenarios).
        'risk': 0.8, # This seems relatively low risk, due largely to how narrow in scope this project is. Despite how small and focused it is, I can still see some portions which could fail without tanking the entire project, so that makes it even less risky.
        'hazard': 0.8, # There's very little that's inherently hazardous about this project, though it's possible the tutorial video could become problematic (it could drift from "how-to" into advertisement territory, but it's a small enough part of the project that I think that's an acceptable risk).
    },
    'pktchat_upgrade': {
        'short': 0.9, # Useful in the short term, at least until upstream mattermost developments move too far ahead again
        'long': 0.5, # In the very long term, this will probably be superseded by future developments, but I would expect those to build on top of this, so I'd say it's of average importance long term (assuming pkt.chat isn't replaced by another platform)
        'scope': 0.8, # This directly relates to important infrastructure for the pkt community.
        'risk': 0.8, # This seems low risk... not really anything more to say. The main risk would be if the time/effort needed was underestimated, but even in that case, I don't expect the project to fail.
        'hazard': 0.5, # A bit hazardous due to CJD's involvement as the host / association with the dev who would be working on this.
    },
    'fastercrypt': {
        'short': 0.8, # Getting a better open source miner out into the world would be good in the short term.
        'long': 0.1, # I think there are enough incentives to improve the crypto speed already, so in the long run it doesn't seem like this would matter much. Maybe moreso for packetcrypt_rs, since it doesn't have as many eyes on i as the sodium libraries.
        'scope': 0.5, # Average. It's definitely pkt related, but I'm not sure it's the sort of thing we should really be funding in the first place.
        'risk': 0.1, # It's an interesting idea, but I'm not particularly confident that this will lead to meaningful improvements in any of the packages that are allowed to be modified. The bounty is fairly high for what could potentially be a trivial few % improvement to packetcrypt_rs, and no improvement to the more widely used sodium packages. The payout is in pkt, so it's subject to price volatility, which could potentially make the reward too small or hilariously large relative to any actual improvements.
        'hazard': 0.5, # This doesn't seem inherently too hazardous, but without knowing who the judges are / how they're associated with the contestants / the community, it's hard to say anything for certain. There's a potential for corruption if they e.g. disqualify "poor quality" code so they can give the reward to someone who they know or who bribed the judges, just for example.
    },
    'pktchat_app': {
        'short': 0.8, # It seems like push notifications would be nice to have.
        'long': 0.2, # I don't expect this to become less useful long-term, but it seems like something that somebody would be likely to work on without NS funding, in the long run.
        'scope': 0.8, # Same reasoning as the pktchat_upgrade proposal.
        'risk': 0.9, # It seems like there's very little risk that this project would "fail", and no funds are requested for M0, so even volatility shouldn't be that much of an issue (relative to most of the other submissions).
        'hazard': 0.5, # There's some hazard from Adonis's NS membership, much like the various projects CJD has worked on.
    },
    'route_server': {
        'short': 0.8, # In the short term, the data collected as part of this project could be very interesting.
        'long': 0.4, # I suspect this is a little less useful than average, long term, since future changes to the routing server may mean the data collected in this project becomes obsolete.
        'scope': 0.5, # Average. Improvements to the route sever are in scope, but this sort of study doesn't seem so strongly aligned or so misaligned with the interests of pkt and the NS that it warrants either a higher or lower than average score. This could change if we learn of a specific performance problem with the route selection algorithm, or if/when the bandwidth marketplace becomes a more immediate focus.
        'risk': 0.8, # Since there's no up-front payment, there's very little risk of receiving nothing from this project. I think the data collected could be interesting, but I'm not especially optimistic about how useful it will be (e.g. the data is there, but we can't figure out how to use it to meaningfully improve route selection).
        'hazard': 0.8, # I'm not aware of any specific hazard, but as I'm also not familiar with the applicant, there's the usual small hazard from accepting a proposal from an unknown/unproven applicant.
    },
    'docs': {
        'short': 0.8, # Useful in the short term, since this documentation is pretty lacking right now.
        'long': 0.2, # Less useful in the long term, since (assuming there *is* a long term) somebody is bound to do this eventually, with or without NS involvement. That said, having more/better documentation sooner will probably mean better quality documentation long-term, so there's still some benefit from this.
        'scope': 0.8, # It's important documentation, I'm not sure what more there is to say.
        'risk': 0.8, # Relatively low risk. I think there's almost 0 chance that documentation would fail to materialize as a result of this project, but we're talking about technical documentation, so there's some risk that it could prove inadequate or fail to communicate the information effectively.
        'hazard': 0.4, # A little hazardous, since documentation can end up containing some amount of general communication. The cost per hour and number of hours are both potentially a bit high, depending on the length/quality of the documentation, and the applicant is a known associate of an NS member, so that adds a little to the hazard.
    },
    # A few general notes about the remaining project proposals.
    # I appreciate that each proposal is reasonably detailed, and the projects are each relatively small and focused.
    # Unfortunately, the value of many of these projects depends on whether or not the other projects are approved.
    # The voting system that the NS uses does not have the ability to make it so a proposal's score is contingent on whether or not other proposals have been accepted.
    # While we probably could find some way to implement that functionality, it would be inappropriate to modify the voting system after the call for proposals has been issued (nevermind after it closes).
    # As such, I'm reviewing each of these in isolation, and then selecting only the "best" in the case of the atomic swap proposals (since implementing any one of them decreases the value of the others, at least to the extent that having any one atomic swap implementation should be sufficient to start building infrastructure atop it).
    'punks_match': {
        'short': 0.8, # Being able to more easily exchange pkt for something else (especially via atomic swaps) would be very nice to have in the short term.
        'long': 0.2, # There's enough financial incentive that I think, in the long term, something along these lines is likely to emerge even without NS funding. There's some value to having multiple matchmaking options, so there is some long-term benefit from this, but it's not as significant as in the short term.
        'scope': 0., # This would be average, at least in theory, for some version built on atomic exchanges. As written, and assuming an escrow-based model, this would presumably be used to operate an escrow business. I don't believe the NS should be subsidizing that sort of development, even absent any hazard or risk, unless it's absolutely vital to do so for the good of the pkt community at large. I don't think the escrow-based matchmaking system would ever rise to that level.
        'risk': 0., # As-is, this would be built to use either escrow or atomic exchanges, depending on whether or not atomic exchanges are implemented. Without knowing which, it's hard to fairly judge this proposal. I tend to think the escrow-based approach is not interesting enough / potentially hazardous enough to disqualify, but impartial software built on top of atomic exchange protocols could be worth-while. Since we don't know which version we would see, I would prefer to rank this as 0 for now, and potentially revisit this if there's continued interest in a future round (if one of the atomic exchange protocols is implemented).
        'hazard': 0., # For largely the same reasons as CJD outlined, though I consider this more a "hazard" than a "risk", in the sense that it's less about whether or not the developer will be able to deliver the completed project, and more about the potential harm to the pkt ecosystem if this was recognized as an unregulated exchange etc.
    },
    'punks_atomic1': {
        'short': 0.9, # There's a lot of potential to develop new infrastructure on top of the atomic swap protocol. So not only is this directly beneficial, but it opens the door for more interesting development in the future.
        'long': 0.5, # Long term, it's very likely that atomic swaps would happen with or without this proposal. It's also fairly likely that the first implementation will become the defacto standard, so this is still significant in the long term, but not to quite the extent as the short term.
        'scope': 0.5, # In general, any implementation of atomic swaps is reasonably well aligned with the long term goals of pkt. Nothing about this proposal in particular would indicate that it is more aligned with those goals than the other proposals this period. This is subject to change if, in the future, atomic swaps become a higher (or lower) priority.
        'risk': 0.5, # It depends on events happening in the BTC blockchain, so depending on the relative ptk and BTC value and volatility, transaction fees may be prohibitively expensive at times. Basically, just because we have atomic swaps doesn't mean anyone can afford to use them (at least, not on a small enough scale for all potential infrastructure someone may want to build on top of the atomic swap machinery). Additionally, from my (admittedly limited) understanding of atomic swaps, this is not an entirely solved problem -- there are some implementation details (e.g. how the delay before possible cancellation is scheduled) which may need fine tuning.
        'hazard': 0.5, # This applicant hasn't worked on a project from the NS before, so there's the usual uncertainty about whether or not they can deliver.
    },
    # To my mind, this is equivalent to atomic1, except more expensive. If we fund anything, I would prefer to fund atomic1 first, and reconsider other atomic implementations / other wallets after the reference implementation is available.
    'punks_atomic2': {
        'short': 0.9,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.,
        'hazard': 0.5,
    },
    # Same rationale as atomic2
    'punks_atomic3': {
        'short': 0.9,
        'long': 0.5,
        'scope': 0.5,
        'risk': 0.,
        'hazard': 0.5,
    },
    'mining_output': {
        'short': 0.5, # I may be biased, but while I think there's a short-term value to improving the output, I don't think it's high enough to score above average.
        'long': 0., # Almost guaranteed to be replaced, in the long run.
        'scope': 0., # While there's clear success criteria, this seems like such a minor issue (no pun intended), with enough incentives already in place to improve the software, that I don't think this is a cost effective use of NS resources. It's open source software, so if someone has a problem with the miner logging output, they're free to submit a PR. I would think that the pool operators, or anyone who owns a significant number of pkt, already has ample incentive to do this, if they think it would bring in (or retain) more people and thereby increase the interest in the pkt project and the value of the pkt that they already hold. If other people think this is really an issue, then I could be persuaded otherwise, but as-is this seems like a problem nobody's solved because nobody's actually that bothered by it.
        'risk': 0.8, # It's just logging output, so I think there's very little chance that the project would fail to deliver. There's some risk that it will hide critical errors by default, or fail to hide minor errors, or fail to communicate what the issue is effectively.
        'hazard': 0.4, # The usual issues with an untested applicant submitting proposals. Perhaps slightly more significant in this case, since it involves modifying existing software, and we have little knowledge about how familiar the developer is with that software / the importance of the various error messages / etc.
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
        individual_votes = [str(v[p][q]) for v in votes]
        sum_info = "(" + " + ".join(individual_votes) + ")"
        print "  ", trans[q], projects[p][q], sum_info
