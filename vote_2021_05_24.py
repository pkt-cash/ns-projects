#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 40.0  # million
costs = {
  'lobbying': 3.5,
  'wallet': 21.0,
  'UOI': 40.0,
  #'UOI_1': 10.0,
  #'UOI_2': 10.0,
  #'UOI_3': 10.0,
  #'UOI_4': 10.0,
}
votes = []

# Ben
votes.append({
  'lobbying': {
    # I will begin by acknowledging that this proposal is in an area I have little personal
    # experience, therefore it is difficult for me to evaluate risk and benefit for such an
    # initiative. I would have preferred if Milestone 1 itself is an entire proposal, as the
    # output will help those involved in PKT learn more about the ecosystem, along with a
    # execution plan. If this proposal is not funded, I encourage a follow-up proposal of such
    # narrower scope and lower budget be submitted. In its current form, I am still generally
    # supportive of the proposal, as it allows us to gather knowledge in this domain.
    # Regardless of whether the campaign is successful, I would prioritize documentation of
    # our learnings.
    #
    # One area I believe the NS cannot commit to is taking on exchange risk with fiat. This
    # unfortunately has to be built in to the budget, since the process of the NS does not
    # have a way to handle that. I also think scoping down the proposal will help to manage
    # that risk. For this reason I have to reject the proposal as is.
    #
    # I also highly recommend the formatting of the document be better structured and in .md.
    # This is incredibly hard to read.
    'short': 0.7,
    'long': 0.5,
    'scope': 0.35,
    'risk': 0.0,
    'hazard': 0.4
  },

  'wallet': {
    # I appreciate the intention to make onboarding general audience easier, but don't
    # think that browser-based mining is the best solution. Short-term we may see more
    # people try it out, but I cannot imagine anyone long-term mining from a browser
    # tab, even though it is wasm. Then we have to deal with the non-custodial management
    # of the private key, which if someone knows how to do that, they can manage a native
    # miner. I am also cautious of the NS funding yet another wallet project at this time,
    # at this stage of the project it may create more confusion than benefit. I also think
    # this is both risky and expensive for the potential impact.
    'short': 0.4,
    'long': 0.1,
    'scope': 0.3,
    'risk': 0.5,
    'hazard': 0.7
  },

  'UOI': {
    # I like this proposal and think it is timely, as the NS receives more broadly scoped
    # proposals that often extend beyond the domain expertise of the NS team. An arrangement
    # with an experienced and reputatable institution not only takes some load off the NS,
    # but also adds legitimacy to our ecosystem. I expect a lot of learning to come out of
    # this engagement.
    # 
    # I recognize the conflict position of groups having financial relationships with Caleb,
    # who is part of the NS, but understand that clear boundaries and processes are in place
    # with respect to use of funds. Secondly, this is a big amount to allocate to one project,
    # but because of the nature of it, we do need a bigger commitment to see results.
    #
    # Some things I would recommend is, if things don't go well we have an understanding that
    # the NS can decline to fund the next milestone. By the end of the grant, if the process
    # goes well, we can revisit the allocation of PKT for administrative vs. grant. Both these
    # are addressed / possible in the current proposal as written.
    'short': 0.75,
    'long': 0.85,
    'scope': 0.7,
    'risk': 0.65,
    'hazard': 0.65
  }
})

# Adonis
votes.append({
  # I LOVE this idea. I want to see this proposal again
  # However there are some major issues that must be corrected first.
  # For these reasons I think the proposal must be disqualified on principle:
  #
  # 1) The proposal doesn't explain how it will acheive any of it's goals.
  #    Even though I personally know Alex has done lobbying work in the past
  #    and is at least in part responsible for the government (and therefore
  #    global) adoption of IPv6, the proposal sounds like bullshit because
  #    it doesn't detail well any of the work required to acheive the
  #    milestones.
  # 2) The project doesn't mention Alex's work with Anode (CJ and Adonis)
  #    Which in vote_2020_02_29 is mentioned as an immediate disqualifier
  #    at at the very least is bad form. Alex's relationship with Anode is
  #    contractual and Anode builds technology based on PKT so I believe
  #    there isn't much potential for conflict of interest, but still I believe
  #    the relationship must be indicated publicly in the proposal
  # 3) The propossal doesn't follow the template format.
  #    Alex has submitted proposals before, I know he already knows the format.
  #    There is no excuse for this sloppiness and I believe this alone
  #    is grounds for disqualification.
  #    The format is not difficult and maintaining as standard makes it easier
  #    for the NS to get a sense of what's happening quickly and compare it to
  #    other projects. It makes it easier for future authors to understand what
  #    the submission process is and how to create a good project proposal.
  #    It trains repeat submitters (of who Alex is an example)
  #    to follow a stadard way of doing things.
  # 4) The proposal asks for more PKT if the price drops. I'm very conflicted
  #    about this. I sympathize that crypto fluxuates in value and that bills
  #    must be paid but also this: are you kidding me? If PKT goes up, the
  #    proposal don't ask for less of it. The people working on this project
  #    are supposed to be incentivized by the increased value of PKT that they
  #    hope will be the result of the increased value they've created for it
  #    or by the goodwill they earn from contributing to an Internet technology
  #    for the greater good of humanity. The NS is itself funded by PKT, not
  #    a fiat, so when PKT goes down, we can't fund as many projects. Everyone
  #    suffers. We shouldn't be taking additional resources away from potential
  #    projects because one projects demands more in bad times than it got in
  #    good. While practical, I think it's skeezy and I think it would set a
  #    terrible precident to approve a proposal that had this condition.
  #
  # If it weren't for these four things, I would probably grade this proposal
  # very highly. I love the idea and I believe Alex is the person to do it.
  # I think it falls within the scope of the NS and generally I think it's
  # proposed at a reasonable price.
  'lobbying': {
    # The proposal claims that there will be podcasts, larger followings,
    # politicans, influencers, and more talking about the project
    # Those are great things, but I don't think the immediate tangible benefits
    # are many in this case. I think those are the seeds that lead to a more
    # fruitful future.
    # I do believe that the talking points, assets, and presentation materials
    # will be useful in explaining the PKT projet to newcomers.
    #
    # 'short': 0.2,  # this is my actual vote
    'short': 0.0,    # This is my 'disqualifier' vote

    # PKT currently has a problem. People don't know how to talk about it.
    # One solution to this problem is to create talking points, presentation
    # materials, and assets that can be used to share the word.
    # On top of that, aligning influencers in the political spectrum that can
    # champion PKT as a tool rather than a weapon is important.
    # I'm aware that Alex has been able to gavlanize governments around the use
    # of IPv6, making it the dominant IP protocol to succeed IPv4.
    # If he can do the same for PKT, that would be fantastic.
    # Especially as crypto and other decentralized technologies are facing
    # scrutiny, regulation, and bad press. I worry that there is a such a
    # deep-seated fear of individuals saying or doing bad things that
    # governments (and corporations) will be willing to slowly reduce individual
    # rights and liberties around communication, finance, payments, and other
    # things that employ encryption technologies and are being decentralized.
    # PKT has tremendous potential for the creation of independently
    # owned businesses that benefit from fast micropayments and encrypted
    # communication.
    # If we don't advocate for that, who will?
    #
    # 'long': 0.8,  # this is my actual vote
    'long': 0.0,    # This is my 'disqualifier' vote

    # If I were to read "scope" here as "is this within the scope of the NS?"
    # Then I'd say "yes": 0.8.
    # Although I don't think of the Network Steward as a political organization
    # I believe this is a case where it must speak up and act. It's existence
    # is conditional governmental acceptance of crypto and encrypted data
    # transmission, both of which are sadly under fire.
    # In the same way that the Egg Farmers of America must lobby to advocate
    # for their rights, I believe so to must PKT.
    #
    # 'scope': .8,  # this is my actual vote
    'scope': .0,    # This is my 'disqualifier' vote

    # I see two potential issues here
    #
    # The first is that wealthy politicians don't like PKT and that somehow they
    # are galvanized into negative action by the idea that private Internet
    # owned by peolpe other than ATT and Comcast. That would be terrible, but
    # would probably be inevitable with or without lobbying. In that
    # case it's better to lobby anyway because then at least we control the
    # narrative
    #
    # The other is that this projects ends up turning into a marketing campaign
    # of youtube videos and podcasts hyping up PKT cash, which I think would
    # be terrible.
    #
    # Since I've seen some of Lightman's work, I believe it won't be a series
    # of marketing videos, but since the proposal doesn't outline how things
    # will be done, how people will be qualified, or any examples of how
    # things will look or sound, I'm not inclined to trust it.
    #
    # Other than that, I think the proposed timeline and budget is within reason
    # (except for the additional PKT hedge).
    #
    # i would love to fund this alongside the User Operated Internet Fund
    #  proposal. I think they complement each other well.
    #
    # 'risk': 0.2,  # this is my actual vote
    'risk': .0,     # This is my 'disqualifier' vote

    # Cj and I do work with Alex Lightman through a company we have together.
    # so it could be percieved as a conflict of interest to favor this proposal
    # However, I believe the other criteria outweigh this possible bias.
    # I don't see that relationship stated in the proposal anywhere.
    # It's important to disclose possible conflicts of interest are
    # are referenced in vote_2020-02_29 as justification for disqualification.
    #
    # 'hazard': 0.1,  # this is my actual vote
    'hazard': .0      # This is my 'disqualifier' vote
  },
  # This is a really interesting idea, but frought with risks.
  'wallet': {
    # I think this project is super interesting. I think one of the issues
    # with PKT today is that mining is challenging. It requires a Linux computer
    # a lot of bandwidth, and knowledge of the command line.
    #
    # I personally have never seen a browser-based miner that works well.
    # PKT uses a *lot* of CPU and can basically grind a computer to a halt.
    # Sure, using it in the browser would make it easier to use, but only
    # for people who are basically willing to give up use of their desktop
    # or laptop anyway, so in that case why not have a dedicated computer?
    'short': 0.3,

    # One potential I see for this project is that, since mining is effectively
    # routing, any home user could became a PKT router, sharing their spare
    # bandwidth while they are surfing. With that, it may be possible to
    # encourage normal people to become micro-ISPs for their friends and
    # neighbors.
    #
    # I also see potential here for increasing the number of people aware
    # of PKT tremendously, as deep technical expertise will no longer be
    # required to interact with PKT. It will be like Bitcoin in 2011-2013,
    # where people still must be comfortable with keys to send money, but
    # honestly there are better PKT wallets that people can keep on their
    # desktop that don't require keeping track of private keys.
    #
    # But that's all conditional on this being promoted the right way
    # agree with Arc about the risks of this being percieved as a negative.
    # This also has the potential to radically polarize people against
    # PKT as a the symbol for malicious browser-based crypto mining.
    'long': 0.1,

    # In reading "scope" as "can this project be done?":
    # I'm not sure why this needs to have a private-key payment system
    # there are plenty of PKT wallets. I know of 3 already and two more in
    # development. The miner is interesting and it can send to one of
    # these wallets.
    #
    # The other thing is that no wallet tech is listed, so how is the wallet
    # built? It's difficult to know if this project is even achievable
    # within scope without knowing if the wallet will be built from scratch
    # or use an existing tech.
    #
    # scope; 0
    #
    # in reading "scope" as "should the NS fund this project?":
    # I see wallets and miners as generally in scope of the NS, but we already
    # have so many wallets. Unless one is mind-blowing (and please, show me
    # wireframes or mock-ups and workflows at this point to prove it), I don't
    # see the need for yet another wallet.
    #
    # As a miner I think it's an interesting project, but it carries a lot of
    # risk. Should the NS fund a miner that could be used maliciously before
    # PKT is even widely known or used? The potential bad will could outweigh
    # the good, setting back not only PKT but crypto for decades.
    #
    # scope: 0
    'scope': 0.0,

    # If the goal is to build a miner on the browser with the given funds,
    # probably that's doable. If the wallet is built from scratch, I don't
    # know how achievable that is. If the wallet is modified from another
    # project, probably it's doable. It's hard to rate without knowing
    # what the sallet technology is.
    'risk': 0.0,

    # I see several potential issues with this proposal
    # 1) although three participants are described, only one
    #    has a GitHub or website link, despite the team claiming to be composed
    #    'software developers and blockchain and webdevelopment experts'
    # 2) No organization is formed, so the payout could to an individual, but
    #    it's unclear who. This is not a disqualifier per se, but it's unusual
    # 3) a browser-based miner could be used maliciously, so I don't think
    #    the NS should fund a project like this at this point. Perhaps in the
    #    future when the public is more aware of these things or there are
    #    mechanisms to prevent malicious use of this type of technology or
    #    or browsers implement detections to detect malicious blockchain
    'hazard': 0.0
  },
  'UOI': {
    # I don't believe there will be any short term impact.
    # I percieve this change is being similar to the splitting of Xorg from
    # the X11 foundation. In name and principle only and totally without
    # consequence the time it took for the Xorg foundation to release a new
    # project.
    #
    # There's a possibility it will have some impact in that people will
    # percieve the PKT community as being in support of standards,
    # best practices and good governance.
    'short': 0.1,

    # I think this will have tremendous far-reaching consequences for PKT
    # I believe this will alter the course off what is possible with the
    # community and the technology, in the same way that the IETF has made
    # it possible to produce and canonize SPF, SASL, Oauth and more.
    #
    # Since the payout of this project's fund is denominated in EUR,
    # I also think that a project like this will reduce the temptation for
    # clauses such as the one in the lobbying proposal to take a variable
    # amount of funding depending on the price of the crypto
    'long': 0.9,

    # This is one of the few projects I can think of that both requires
    # relatively little upfront work and yet has a lot of long-term impact.
    # In that way it reminds me of the Network Steward. It took almost
    # no effort to set up ompared with building a product and yet produces
    # value to the people who contribute to the PKT ecosystem.
    #
    # This is something I know personally that CJ has has been talking
    # about since the start of the Network Steward, so I believe
    # he will carry it through.
    #
    # The financing and milestone struture is strange for this projet
    # It attempts to seek a flexible budget (apparently considering that other
    # projects deserve funding and so it must be flexible in that funding), and
    # to consider each payout as a separate project to acheive that, given
    # the mechanics of funding by the NS.
    #
    # It's an interesting way to approach flexible funding. I assume the extra
    # PKT will go to provide more support for projects submitted to it.
    # However since it lists several support activities it will provide such as
    # security auditing, and because it can receive donations at any time,
    # I don't see why it wouldn't seek to create the organization and a smaller
    # set of services in the beginnig and then ask for more once it's achieved
    # a smaller goal.
    'scope': 0.5,

    # One thing I like about this project is that it could bring PKT from
    # an association of like-minds to a formally recognized body such as the
    # IETF, complete with oversight that would build public trust.
    #
    # I would love to fund this alongside Lightman's proposal. I think they
    # complement each other well.
    #
    #
    # One thing I saw recently that bothers me is that Signal took a donation
    # which would have paid for its operation for years, but then got flooded
    # with new users when Elon Musk tweeted "use signal," which probably reduced
    # Signal's runway from that donation by eating up infrastructure costs
    # It happens that Signal was releasing a crypto currency around that time,
    # which went up 10x in value over the course of a couple weeks, fell 30%
    # in a day, and then fell back down to its original price over the next few
    # weeks. It is possible, or it would be at least tempting for them to have
    # pumped up their own crypto and sold at peak to pay for years of
    # infrastructure costs.
    #
    # The NS does not do marketing, so I hope it would be difficult for the NS
    # to perform a trick like this, but I can envision that the temptation
    # would be there since not only are some or all of the NS members PKT cash
    # holders and/or have companies that employ PKT technology and the NS
    # funds projects in PKT so the budget for funding increases when the price
    # increases. Having an NGO that can accept donations in any crypto and is
    # governed by strict government oversight in a country such as the
    # Netherlands where there is both a favorable tax regime and socially
    # responsible laws regulating NGOs further reduces this risk.
    #
    # A potential down-side is that the regulation will make the proposals
    # and funding process more challenging and time-consuming. In working
    # with the IETF in the past, I found their feedback process slow and their
    # submission process technically challenging and antiquated. It may deter
    # casual / crazy submissions but it also deters great ideas that don't want
    # to jump through 10 mile hoops.
    'risk': 0.5,

    # I work with CJ in both Anode and PktPal, so there may be a conflict
    # of interest on this. Also CJ is part of the NS, so funding his project
    # may come off as favoritism.
    #
    # I personally believe that the vision of this projet is much bigger than
    # me or CJ, and that CJ has proven his ability to operate this type of
    # organization through the genesis of the Network Steward.
    'hazard': 0.5
  }
})

# Arc
votes.append({
  'lobbying': {
    # I don't expect any tangible short-term benefit. It may help to raise
    # awareness among politicians and regulatory bodies that there are some
    # political and regulatory road blocks in the way of innovation, but I don't
    # expect it to affect anything short-term. Whatever materials are produced
    # by the effort would likely be at least somewhat specific to some target
    # jurisdiction(s) (e.g. the US).
    'short': .1,
    # Any long-term benefits would have limited jurisdiction, so this doesn't
    # really have the same scale as some of the more technically innovative
    # proposals we've seen. The calculus on this would shift along with the
    # political landscape and changing regulations, so this could change if
    # reviewed again at a later date or as part of a carefully targeted
    # proposal. Right now, I expect technical problems and solutions, not
    # political ones, to make or break things for the PKT community.
    'long': .1,
    # Honestly, I have no idea how to score this one on principle. On the one
    # hand, I tend to think that directly funding political activity should be
    # considered out-of-scope for the NS. On the other hand, in some
    # hypothetical scenario where PKT was effectively banned, then there would
    # be hard to justify funding anything except lobbying. In any case, for this
    # proposal in particular, I don't think the milestone objectives are
    # sufficiently well defined.
    'scope': 0.,
    # The proposal states that each milestone requires the requested PKT or
    # enough to meet some budget requirement in national currency (at whatever
    # the exchange rate is at the time). I don't think that's something the NS
    # can or should agree to. I have to assume that, if the exchange rate
    # dropped and those funds were not made available, then the project wouldn't
    # be completed. That seems like a pointless and unnecessary risk to take,
    # given the volatility of crypto in general right now.
    'risk': 0.,
    # There's some past association between applicants and NS members, which
    # would normally earn a penalty of some kind (perhaps 0.75 or so). However,
    # there's quite a few problems with the application itself, unrelated to the
    # risk and scope of the project:
    #   1. The application is plain text, rather than following the markdown
    #      template. This makes it more difficult to review (both by the NS and
    #      any stake holders who want to monitor what the NS is approving). It
    #      gives the impression of something that was thrown together at the
    #      last minute, in a rush to submit something before the deadline.
    #   2. The application lists a minimum budget in national currency, and
    #      requests that additional funding be made available if the exchange
    #      rate drops. As I noted in the risk criterion, that's not something I
    #      think the NS can or should agree to. If we approve the proposal in
    #      its current state, then it would imply that the NS agrees to make the
    #      additional funds available, even if the exchange rate does not drop.
    #      That would set a precedent that we accept applications with these
    #      kinds of conditions, which I think would go against the interest of
    #      the NS. Note that I think this would be disqualifying by itself, but
    #      if it was the only issue with an otherwise promising application,
    #      then I could possibly be convinced to allow that clause to be
    #      removed.
    #   3. I realize there was some followup on git after the submission window
    #      closed, but we need to judge applications based on their state at the
    #      close of submission, barring exceptional circumstances. Based on that
    #      information, if we convert the budget to an hourly rate, then the
    #      requested amount seems unreasonably high. This is extra problematic
    #      when the applicants include known associates of the NS. Given the
    #      minimum funding requirements (in national currency) mentioned before,
    #      there's some implication that somebody worked out the minimum budget
    #      needed for the proposal to succeed. I think some sort of breakdown of
    #      that information would need to be included in the application,
    #      otherwise we can't really justify the pay relative to hours worked.
    # Taken together, I don't think the NS should accept this application in its
    # current state, even if the project was otherwise in line with the
    # interests of the NS.
    'hazard': 0.,
  },

  'wallet': {
    # As far as I know, this would be the first web-based frontend to a PKT
    # wallet. That at least has some short-term novelty to it.
    'short': 0.5,
    # There amount of long-term utility is more than none, I guess, but I
    # definitely see this as having more short term benefit. Worst case
    # scenario, the code could either be used as a starting point for a new
    # implementation, or an example of what not to do (if it fails for
    # interesting reasons).
    'long': 0.1,
    # It's not clear to me if the intent was to write a new wallet, or use an
    # existing wallet (which?) on the backend. I'll assume the intent is to use
    # whatever the "best" existing wallet is, since this seems to be more about
    # the frontend. Either way, this is yet-another-wallet. I don't think it
    # makes much sense to keep funding wallet projects, since at some point
    # they'll just be fighting over the same body of users. This rating could
    # change if the proposal was resubmitted in the future, depending on how the
    # other wallet projects turn out.
    'scope': 0.,
    # Assuming this is just a front-end, I don't think this is particularly
    # risky as wallet-related projects go. If there weren't already other
    # wallets in the works, then a web-based frontend would probably be one of
    # the less risky projects to fund, in my opinion. That's not the world we
    # live in, so I'm not sure the web based wallet would really attract that
    # many new users (be that from other wallets to itself, or to the PKT
    # community as a whole). On the whole, I see this proposal as kind of risky,
    # since it partly works against the other wallet proposals, but not so bad
    # that it would be disqualifying on its own.
    'risk': 0.5,
    # I don't think the NS should fund a web-based miner. I've come across too
    # many instances of malicious mining code being injected into web pages. If
    # the NS funded development of a web-based miner, and then it found its way
    # into e.g. a malicious advertisement, the negative press from that could be
    # bad for PKT (or at the very least, reflect poorly on the NS). Without that
    # aspect, I think this would be fine from a hazard aspect (but not great
    # overall, due to the relative saturation of wallet projects).
    'hazard': 0.,
  },


  # Note that, upon further reflection, I don't think the NS can accept the
  # applicants' suggestion to split this proposal into 4x 10M proposals and rank
  # them. Or split them at all, for that matter. I don't see a way to split
  # proposals (or otherwise support a flexible budget) within the constrains of
  # the current voting system, and it would be inappropriate to change the
  # voting system after a request for proposals has been issued (not to mention
  # after the deadline passes). I recommend that the NS treats this as a single
  # proposal for the full 40M in the request, on the grounds that this seems to
  # be the least favorable for the applicant (it maximizes the chances that we
  # don't have room for the project in our budget). If the rest of the NS
  # disagrees with my assessment, and wants to keep the 4x 10M proposals, then
  # my vote for those proposals can be assumed to be 0 on the grounds that this
  # is hazardous to the NS.
  'UOI': {
      # It's honestly really hard to judge short short term impact, since the
      # task is inherently open-ended and depends on what projects the UOI
      # decides to fund. For lack of better ideas, I'm assuming the average
      # project the UOI funds would be an average project, so that kind of sets
      # a baseline of 0.5 to go off of for both of these. The UOI can
      # (hopefully) do a better job attracting proposals and vetting/reviewing
      # them, so that adds favorably to the project. At the same time, the
      # projects the UOI chooses to support may not align entirely with the
      # interests of PKT or the NS, so that takes something away. For lack of
      # better ideas, I'm just going to say those two effects probably cancel,
      # so over all I would expect the results of funding the UOI to be about
      # the same as funding an assortment of average projects.
      'short': .5,
      # See above, exact same argument but for long term.
      'long': .5,
      # Bylaw 6, the worst case scenario is that 2/3 of the budget finds its way
      # to projects. If we assume that this is what happens, that the remaining
      # 1/3 is entirely out-of-scope, and that all funded projects are in-scope,
      # then I guess 2/3 is the obvious thing to put here. In reality, I guess
      # the funds spent on something other than regular projects should be less
      # than 1/3, and some fraction of that would be on things that are at least
      # tangentially aiming in the right direction (e.g. support projects), so
      # hopefully I'm being unnecessarily harsh here.
      'scope': 2./3.,
      # The risk here comes from basically two parts.
      #   1: 0.8 based on the risk that the UOI fund does not spend the funds on
      #      appropriate projects. This could happen if there are no
      #      (reasonable) applications to the UOI fund, or if the fund chooses
      #      to accept projects that aren't well aligned with the scope / the
      #      interests of the NS.
      #   2: 0.8 based on the average risk of the individual projects accepted
      #      by the UOI fund. I haven't gone through the history to check, but I
      #      think this is probably better than the risk I would assign an
      #      "average" proposal to the NS. I'm operating under the assumption
      #      that the UOI fund would receive applications of a similar quality,
      #      but the fund has the resources available to better review and vet
      #      the proposals and their applicants, so they should tend to reject
      #      the bad ones. This (hopefully) biases the risk criterion towards
      #      better projects, and it's the main thing that (arguably) justifies
      #      the overhead accounted for in the scope criterion (other than being
      #      less work for the NS and more convenient for applicants who prefer
      #      to be funded in euros rather than PKT).
      # These numbers are admittedly a little arbitrary. Theoretically, I guess
      # I should look through past applications, figure out the distribution of
      # submitted to accepted applications, and the success ratio of accepted
      # ones, and use that to calibrate my projection of the average risk of
      # projects. I don't think our sample size is large enough to be
      # statistically significant, and the UOI fund may attract a more diverse
      # pool of applicants (I would hazard to guess that more people are
      # comfortable doing work payed in euros than in cyrptocurrency).
      'risk': 0.64,
      # CJD is involved, which could look like favoritism. For any meta-project
      # of this style to succeed, at least starting out, it's probably going to
      # need some amount of feedback from the NS. So I think it's good that CJD
      # is involved, but it still looks bad compared to a project with no
      # involvement by NS members (and no conflicts of interest or other hazards
      # to get in the way).
      'hazard': 0.5,
  }
})

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
  'UOI': {
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
