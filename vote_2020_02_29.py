#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 90.0
costs = {
  'repo': 4.0,
  'price_display': 8.0,
  'faucet': 16.0,
  'cloud': 30.0,
  'vpn': 30.0,
  'route_server': 30.0,
  'cjdns_wifi': 36.0,
  'cjdns_wireguard': 24.0
}
votes = []

# Arceliar
votes.append({
  # Commenting in everything in detail since this is the first vote.
  # My hope is that this will be useful for future project proposals, which may
  #   want to see what the thought process is like for at least one voter.
  # A couple general notes:
  #   1. For scope, as a starting point, I've normalized things against the project
  #     with the lowest cost per work-month. This has then been adjusted on a project
  #     by project basis I don't know that I'll keep this normalization rule the
  #     same moving forward (too easy to exploit, just work slower), I'm just using
  #     it as a starting point for lack of better ideas. In particular, normalizing
  #     this way only makes sense if all work-months are equal, which is unlikely
  #     to be true, but I don't have a better idea right now.
  #   2. Projects need to disclose conflicts of interest in the application, and
  #     failing to do so is disqualifying as far as I'm concerned. Most of the
  #     applications are submitted on behalf of teams where I know one or more
  #     members are known by the NS in some capacity, and make no mention of this
  #     fact. This is unacceptable. There are a couple projets where I'm not aware
  #     if or to what extent the applicants are associated with other NS members,
  #     so I can't fairly rate anyone if I take conflicts of interest into account
  #     the way that I should. As such, since this is the first application period,
  #     and I genuinely believe that the applicants just didn't know any better,
  #     I won't hold the lack of disclosures against them. Since this is the first
  #     round of our formalized approval process, I'm just going to assume that anyone
  #     who knew enough to submit an application is probably associated with the NS
  #     in some capacity and rate them as if they had disclosed this information.
  #     In the future, if I'm aware that there's an undisclosed conflict of interest,
  #     I'm just going to give the project an automatic zero in the hazard category.
  #     If the NS habitually approves such projects anyway, then I can't continue to
  #     participate. I would strongly recommend all proposals include a short
  #     section on conflicts of interest, whether or not they have anything to disclose,
  #     and just make a statement that there's no conflict if there isn't any.

  'repo': {
    # Generally a very reasonable low-risk proposal with obvious direct and immediate benefits
    'short': 0.8,   # it's hard to overstate how important easy installation/setup is
    'long': 0.2,    # realistically, someone would set up a repo eventually even if we don't fund it
    'scope': 0.125, # 0.5 M/wm baseline divided by 4 M/wm for this project
    'risk': 0.95,   # realistically very little chance of failure, if anything the risk would be failing to have things completed by the target deadline (particularly if other projects are awarded to the same recipient)
    'hazard': 0.5   # Applicant is known by NS members. Failing to disclose this will be disqualifying in the future, but I'm letting it slide this once for the sake of approving anything.
  },

  'price_display': {
    'short': 0.5,     # this would be 1.0 if the prices were accurate and realtime. Since seigniorage is an estimation (and not one I'm confident adjusts quickly enough to be useful in a realtime ticker -- difficulty doesn't retarget that fast), I'm penalizing this by half. I'm not sure if that's too much or too little, it's mostly to indicate that it leaves a lot to be desired.
    'long': 0.1,      # the estimation becomes much less useful the moment anyone opens an exchange and starts providing those prices in real(er) time. Unless you're actually mining in the environment the seigniorage estimation is based on, in which case it's difficult to understate how useful that information is, but I feel like the miners will figure that out on their own without NS funding.
    'scope': 0.09375, # 0.5 M/wm baseline divided by 8/1.5 M/wm for this project
    'risk': 0.0,      # I posted a long comment about this in the cryptpad. Long story short: by my understanding, the estimation would require a lot of assumptions which weren't stated in the proposal. It's not obvious to me that the approximation would be broadly applicable enough to be useful after those assumptions are taken into account.
    'hazard': 0.0     # Relating to the above, if there's a NS-funded ticker that's giving inaccurate price information, then that could lead to a lot of problems (ranging from discouraging adoption if we under-value the currency, to accidentally starting a panzi scheme if we over-value it)
  },

  'faucet': {
    'short': 0.75,  # This is a nice project from a short-term perspective. It gives people a way to get a few pkt without mining, knowing someone they can buy/trade/be-gifted pkt from, or waiting for an exchange to open. Since cryptocurrency isn't a new concept anymore, I don't think it would be as useful as it was with e.g. bitcoin, but generally speaking for now I'd strongly prefer having a faucet over not.
    'long': 0.0,    # Assuming we don't fund it forever, this eventually becomes completely useless, +- whatever long-term benefit comes from redistributing the code (which could be useful to other projects, but probably not to pkt)
    'scope': 0.05,  # 0.5 M/wm baseline, divided by 16/12 M/wm, gives 0.375. However, only 2.4 / (16+2.4) ~= 13% of the budget is actually going to be distributed by the faucet, and the rest goes to developing the faucet. That seems like an insane overhead. I'm not sure how to really account for that, since I don't really know what an appropriate overhead would be. My best approximation is to just multiply by the 2.4/18.4 ~= 0.13 factor to account for the fact that we'd be paying so much to distribute so little, which seems like a very inefficient use of funds (ignoring the optics of the situation, for the moment, that goes under hazard).
    'risk': 0.95,   # If funded, I wouldn't expect this project to have much risk of failure... it's been done before, so it's not exactly breaking new ground.
    'hazard': 0.0   # Tied to the scope, I consider it unacceptable to pay anyone so much to distribute so little, it just looks really irresponsible at best. It looks transparently fraudulent when we consider that the applicant and team members are known by some NS members.
  },

  'cloud': {
    'short': 1.0,   # If executed successfully, this proposal gives people an incentive to use pkt, something to spend pkt on, and the kinds of things the users will do with it are likely to contribute to further growth. Parts of the code (related to payment processing etc) are potentially of value to other projects as well, if only as working examples.
    'long': 1.0,    # This is in keeping with the general theme of separating service providers from infrastructure itself, and distributing ownership and operation of the infrastructure across the community at large.
    'scope': 1.0,   # By the cost per work-month metric that I'm using now, for lack of better ideas, this is the most cost effective proposal. So it's the standard by which I'm judging the other projects for the time being.
    'risk': 0.05,    # Unless the applicants have cracked the secret to high-speed fully holomorphic encryption, and found a way to transparently run existing code in such an environment (in which case, money is probably the least of their worries and we shouldn't be wasting funds on them), then I don't see this being up to par (never mind better) from a safety perspective. I'm going to go out on a limb here and guess that most users (businesses) will have at least some private information or proprietary business logic that they need to run on their servers. If they run their code on one of the major existing cloud computing platforms, then they can be reasonably sure that the provider won't steal their secrets -- since, if they did, it would be easy to bring a lawsuit against them. It's much harder to sue someone when they're just some random node in a distributed network and payed by a cryptocurrency, and that lack of obvious legal recourse means it could be a very hard sell for anyone with anything secret involved in their workflow -- I don't doubt that somebody can find a use case for this, but currently I have no reason to believe that such a use case would be of any particular benefit with regard to the goals of the pkt project and the NS.
  'hazard': 0.0     # To be blunt, approving a project this large and risky, which was submitted by a team known to associate with NS members, would look far more nepotistic than what I can tolerate. There are definitely elements of this proposal that I like, so I would encourage the project team to consider reapplying with a smaller and safer subset of the project, convince us that they have a plan to ensure that compute nodes won't be able to steal their user's private data and/or code without being held accountable, or show us something to indicate that the demand for potentially-nefarious computing power is still high enough that the lack of accountability is unlikely to be an issue.
  },

  'vpn': {
    'short': 0.75,  # Good for largely the same reasons as the above proposal. Being android-only and a vpn, it's a little less broadly applicable
    'long': 0.25,   # *this* proposal is limited to cjdns over android. That's nice, but I don't think by itself it's enough to have an especially large long-term benefit. I also don't foresee as much potential for additional projects to be built on top of it (at least, not to the extent that the cloud service proposal has
    'scope': 0.27,  # 0.5 M/wm divided by 30/16 M/wm, though I have concerns about the accuracy of this one (see hazard, below)
    'risk': 0.75,   # I expect the project will be successful in the sense that it will provide functioning vpn software. I have serious doubts that it will be able to meet its performance goals (finding the "fastest VPN, thereby providing the best possible network speed to the user") -- I'm not confident cjdns and the route server will be up to the challenge before the project period ends.
    'hazard': 0.25  # Applicant is part of the NS, and other project participants are known by the NS. Failing to disclose this will be disqualifying in the future, but I'm letting it slide this once for the sake of approving anything. Additionally, while in principle I appreciate effort that went into breaking down and justifying the estimated cost of each component, the end result is a suspiciously round number. It's pretty clear that the budget started from the end result and worked backwards, and the math doesn't even work out -- the total project's final estimated pkt cost is off by 1 with respect to the components. There's no way the applicant knows an estimated cost with a real precision out to 6 digits in USD, or out to 8 digits in pkt, or the number of hours that will be needed out to 4 digits. That comes across as deceptive, and I'd consider it harmful to the NS to approve projects that do this without taking it into account somehow, so that basically cuts this score in half in my book.
  },

  'route_server': {
    'short': 0.8,   # If the route server can't keep up with demand, then that's a blocker for other projects
    'long': 0.2,    # The long-term problems with the route server have little to do with the implementation. Dijkstra isn't going to scale, that's kind of why the internet ended up with assigned address and CIDR in the first place (which *also* doesn't scale, but at least that's for interesting reasons, c.f. arxiv:0708.2309)
    'scope': 0.17,  # 0.5 M/wm divided by 30/10 M/wm
    'risk': .75,    # I'm pretty confident that a rust implementation of the existing route server will result from this project. I'm less confident that the implementation will be a meaningful improvement upon the nodejs implementation, unless the node implementation is particularly poorly written and unoptimized, in which case I'm not confident that rewriting it in rust is worth the manpower compared to optimizing the node code. I wold expect the last milestone in particular to be the sort of thing that, if it works at all, would be easier to prototype in the node code. So I worry that there's a chance this could result in a lot of work just to reach feature parity and be marginally better by a constant factor. But if it fails, then at least this should (hopefully) be instructive, so I don't want to take too much off for this.
    'hazard': 0.5   # I have no idea if the applicant has any associations with the NS or other relevant conflicts of interest. For lack of better ideas, to not bias things in favor of a project due to my own ignorance about the applicants, I'm starting with the same baseline (relatively poor) hazard rating as the above projects. My apologies to the applicants if this is not the case -- obviously I may vote differently in the next approval cycle if you don't get accepted in this cycle and reapply next time.
  },
  'cjdns_wifi': {
    'short': 0.75,   # This would be useful in a common use case near the edge of the network, especially on devices that don't support ibss/adhoc or meshpoint modes ...
    'long': 0.1,    # ... but my understanding is that being a wifi client really does mean you're a *client*, you don't get to directly interact with other nodes without going through the AP, and most (all?) hardware+driver combinations do not support associating with multiple APs at once (or being an AP and a client at the same time). It's still useful for clients that are too low powered to route traffic or meaningfully participate in the network without offloading the crypto. Since this is only really applicable to leaf nodes at the edge of the network, and wirelessly connected leaf nodes are probably end-user devices. In the long run, I think any end user device that's fast enough for a comfortable user experience is probably going to be fast enough to handle the cryptography without needing to offload it to the wireless hardware, which seems to be the main advantage to using AP/client modes this way.
    'scope': 0.17,  # 0.5 M/wm divided by 36/12 M/wm
    'risk': 0.9,    # This is kind of uncharted territory as far as I know, so while it's not obvious that this will definitely succeed, I would be fairly surprised if it doesn't work out.
    'hazard': 0.5   # As in the above project, I don't know if there are conflicts of interest associated with any of the team, and there's nothing in the application to indicate one way or the other. So I'm starting with the same baseline score as in the projects with known conflicts.
  },
  'cjdns_wireguard': {
    'short': 0.2,   # The switch to wireguard itself doesn't seem game-changing in the short term, but getting cjdns to integrate with rust code opens up a lot of possibilities.
    'long': 0.8,    # I trust wireguard and cloudflare's boringtun to be vetted and properly maintained far more than cjdns's cryptoauth, no offense intended. Less than a 1 only because I'm basing this score off of their current implementation, and the fact that cjdns keys are tied to IP, so it would be disruptive to migrate to new keys if it becomes necessary to switch to something quantum resistant.
    'scope': 0.17,  # 0.5 M/wm divided by 24/8 M/wm
    'risk': 0.95,   # It seems like there isn't much risk of failure, and even partial success (milestone 1) would be beneficial, so this seems relatively low risk.
    'hazard': 0.5   # As in the above couple of projects, I don't know if there are conflicts of interest associated with any of the team, and there's nothing in the application to indicate one way or the other. So I'm starting with the same baseline score as in the projects with known conflicts.
  },
})

# Caleb
# There seems to be three "applicant groups" who have proposed projects.
# Awarding all projects to a single group may be risky, especially as the project is too young
# for any applicant to have a proven track record. The group which applied for the Cloud Computing
# project and the PKT Faucet project has proposed projects with both the highest, and the lowest price
# per person-month which creates questions about how they have planned their projects.
votes.append({
  # A repository to allow people to easily install cjdns, Yggdrasil, pktd and pktwallet would help adoption,
  # however the key focus will probably be on commercial apps which build on the technology, repositories
  # really only support open source adoption. In the long term, this repo will probably not be very
  # significant as there will be many places to get this software from. 1 PM for a debian repo is somewhat
  # expensive, it's unclear what the website offers, 4mn PKT per PM is somewhat on the high side.
  # Success criteria "when the software repository is live" and "At least one major software program
  # successfully packaged, with at least one independent user of that package", are fairly weak, giving the NS
  # little leverage to fail milestones of the project for not complying with the success criteria.
  'repo':            { 'short': 0.7, 'long': 0.5, 'scope': 0.2, 'risk': 0.2, 'hazard': 0.6 },

  # A price calculator might be a neat bonus item but it is not critical to the development of a bandwidth
  # market and in the long term, this role will be filled by exchanges. The time effort of 1.5 PM for a price
  # ticker is high, but not ridiculously high, however 5.3mn PKT per PM is the highest price charged by any
  # application. There are not a lot of success criteria placed on the milestones, so the NS does not have very
  # much leverage to reject milestone reports as not meeting the success criteria. The proposal contains the text
  # "may include banners linking to other resources related to the PKT network, such as Gridfinity or a wallet
  # service" which appears as though it might benefit certain parties more than others.
  'price_display':   { 'short': 0.3, 'long': 0.3, 'scope': 0.1, 'risk': 0.3, 'hazard': 0.5 },

  # A way for people to acquire a small amount of PKT is indeed an interesting idea, however PacketCrypt was
  # designed in such a way as to allow casual mining of small amounts of PKT using announcement mining so this
  # should not be necessary. There is also evidence that crypto faucets can be run as successful businesses so
  # this project does not bypass a tragedy-of-the-commons problem which blocks the natural emergence of a piece
  # of key infrastructure. Development of an app of this complexity should take 1 to 3 weeks of developer time.
  # The 12 person-months quoted is unacceptable for reason of "significant damage to the perceived legitimacy of
  # the Network Steward" because accepting this project will appear as a handout to the applicant.
  'faucet':          { 'short': 0.2, 'long': 0.2, 'scope': 0.0, 'risk': 0.5, 'hazard': 0.0 },

  # Though it is not in the immediate plan for the PKT ecosystem, this project may be considered useful to the
  # ecosystem because it creates another use case for PKT. It does not, however, directly align with the long
  # term goal of creating infrastructure necessary for the emergence of a bandwidth market.
  # There is an interesting research problem around automatic splitting of computation between multiple computers,
  # homogenous and heterogeneous. However this field remains in its infancy and is likely not worth the limited
  # resources of the Network Steward. The applicant has not expressed their intention to publish any papers and
  # the application does not alude to the development of any breakthrough technology, so it is likely that the
  # applicant intends to use off-the-shelf software such as Kubernetes, Docker and Tahoe-LAFS. Whatever the case
  # may be, since the applicant has made a commitment to performing fundamental research, the Network Steward must
  # assume that they intend to use existing technology. The development of an application with the features
  # described in the proposal should not be expected to require more than 4-6 person-months. With 60-120
  # person-months of effort and the declared scope, this project is unacceptable for the reason that it would
  # appear as a handout to the applicant. If the applicant wishes to re-apply, the Network Steward encourages them
  # to create a prototype, or apply for a project to create a prototype, such that they may have a working
  # demonstration to better clarify the project scope. It should be noted that the line "The software will be
  # available under applicable open source licenses when possible" creates uncertainty. Results of Network Steward
  # funded projects must be available to everyone in the ecosystem equally without unfairly benefitting any one
  # participant over any other. In cases when it is impossible to make certain components of a project open
  # source, applicants should be clear about exactly which components, why, and why the project is not unfairly
  # benefitting any one participant, i.e. the owner of the intellectual property.
  'cloud':           { 'short': 0.4, 'long': 0.4, 'scope': 0.0, 'risk': 0.4, 'hazard': 0.0 },

  # The VPN app proposal is an important first step in developing a bandwidth market according to the overall plan
  # of the PKT ecosystem. The apparent separation of VPN operators from the website/server could also be argued to
  # advance the separation of "network administrator" from "infrastructure operator" roles.
  # The project describes a client app (Android), a VPN docker container, and webapps for the client and VPN operator
  # to interface with their assets. The success criteria for each milestone are reasonably well defined and the time
  # estimate of 16 person-months seems within the expected range for a project of the defined scope. The costing
  # exercise is particularly complete, and though it is not something the Network Steward is willing to take on
  # faith, it shows significant commitment and planning from the applicant. The applicant is One Of Our Own so we
  # must consider the hazard risk of this as a real or perceived conflicts of interest with the NS team. However,
  # the project seems to be not only the greatest short term impact, but also the best overall value at 1.875 mn PKT
  # per person-month with no obvious inflation of the person-month count.
  'vpn':             { 'short': 0.9, 'long': 0.7, 'scope': 0.9, 'risk': 0.9, 'hazard': 0.5 },

  # A high performance route server can be used in the short term to provide link quality information for the VPN app
  # project. The measurement of link quality and computation of paths through the network seems to align with the PKT
  # bandwidth market strategy. It is foreseen that the route server will become a significant piece of infrastructure
  # to the emergence of a bandwidth market and in order to maintain fairness, it is important to have a compelling
  # implementation which is equally available to all participants such that the ecosystem remains open to new entrants.
  # The time effort of 10 person-months seems within the realm of reason for the scope of the project.
  # This project does not demonstrate significant planning as does the VPN app project and it does not have a defined
  # maintainer, but the success criteria are very clearly defined, perhaps the most clearly defined because it must be
  # a drop-in replacement to existing software.
  'route_server':    { 'short': 0.8, 'long': 0.9, 'scope': 0.8, 'risk': 0.8, 'hazard': 0.9 },

  # Automatically connecting to encrypted wireless access points is a significant step in the process of rolling out
  # an internet sharing device and then later local mesh networks which will provide last mile connections to the
  # bandwidth market. In the immediate term, the focus is on VPN technology so this is not immediately necessary, but
  # it will become necessary soon as the next step in the plan is to move into internet sharing. The time effort of
  # 12 person-months seems within the realm of reason for the scope of the project. The project is inherently somewhat
  # risky because it contains research (finding a secure protocol which works on iPhone and Android), however the
  # success criteria are well defined and the first milestone proves the feasibility of the project so the Network
  # Steward probably won't lose more than the up-front contribution of 1/4 if the research proves fruitless.
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.6, 'scope': 0.6, 'risk': 0.6, 'hazard': 0.8 },

  # In order to build out a serious VPN network, we will need a high speed software VPN implementation such as
  # Wireguard. In the longer term, this high performance software implementation will be necessary in order to
  # prototype what will eventually be made into official RFCs and then hardware devices. The time effort of 8
  # person-months seems within the realm of reason for the scope of the project. The success criteria are clear,
  # but the 1/3 up-front payment makes the project less competitive than the cjdns wifi project or the Route Server
  # project, which are otherwise very similar.
  'cjdns_wireguard': { 'short': 0.6, 'long': 0.8, 'scope': 0.7, 'risk': 0.7, 'hazard': 0.7 },
})

# Adonis
votes.append({
  'repo':            { 'short': 0.2, 'long': 0.0, 'scope': 0.5, 'risk': 0.8, 'hazard': 1.0 },
  'price_display':   { 'short': 0.8, 'long': 0.1, 'scope': 0.2, 'risk': 0.8, 'hazard': 1.0 },
  'faucet':          { 'short': 0.8, 'long': 0.1, 'scope': 0.2, 'risk': 0.8, 'hazard': 1.0 },
  'cloud':           { 'short': 0.2, 'long': 0.4, 'scope': 0.4, 'risk': 0.3, 'hazard': 0.1 },
  'vpn':             { 'short': 0.2, 'long': 0.8, 'scope': 0.8, 'risk': 0.8, 'hazard': 0.8 },
  'route_server':    { 'short': 0.5, 'long': 0.8, 'scope': 0.8, 'risk': 0.8, 'hazard': 1.0 },
  'cjdns_wifi':      { 'short': 0.0, 'long': 0.3, 'scope': 0.8, 'risk': 0.8, 'hazard': 0.8 },
  'cjdns_wireguard': { 'short': 0.0, 'long': 0.3, 'scope': 0.8, 'risk': 0.7, 'hazard': 0.8 },
})

# Neil Alexander
votes.append({
  'repo':            { 'short': 0.8, 'long': 0.8, 'scope': 0.6, 'risk': 0.9, 'hazard': 0.9 },
  'price_display':   { 'short': 0.6, 'long': 0.6, 'scope': 0.5, 'risk': 0.2, 'hazard': 0.4 },
  'faucet':          { 'short': 0.7, 'long': 0.1, 'scope': 0.3, 'risk': 0.1, 'hazard': 0.0 },
  'cloud':           { 'short': 0.4, 'long': 0.8, 'scope': 0.5, 'risk': 0.6, 'hazard': 0.6 },
  'vpn':             { 'short': 0.8, 'long': 0.6, 'scope': 0.8, 'risk': 0.7, 'hazard': 0.8 },
  'route_server':    { 'short': 0.8, 'long': 0.9, 'scope': 0.8, 'risk': 0.9, 'hazard': 0.6 },
  'cjdns_wifi':      { 'short': 0.3, 'long': 0.5, 'scope': 0.3, 'risk': 0.2, 'hazard': 0.7 },
  'cjdns_wireguard': { 'short': 0.7, 'long': 0.7, 'scope': 0.8, 'risk': 0.8, 'hazard': 0.9 },
})

## Benedict Lau
votes.append({
  'repo':            { 'short': 0.9, 'long': 0.7, 'scope': 0.7, 'risk': 0.9, 'hazard': 0.8 },
  'price_display':   { 'short': 0.4, 'long': 0.4, 'scope': 0.4, 'risk': 0.8, 'hazard': 0.6 },
  'faucet':          { 'short': 0.5, 'long': 0.3, 'scope': 0.6, 'risk': 0.6, 'hazard': 0.6 },
  'cloud':           { 'short': 0.2, 'long': 0.8, 'scope': 0.5, 'risk': 0.1, 'hazard': 0.6 },
  'vpn':             { 'short': 0.6, 'long': 0.7, 'scope': 0.7, 'risk': 0.7, 'hazard': 0.6 },
  'route_server':    { 'short': 0.7, 'long': 0.8, 'scope': 0.7, 'risk': 0.6, 'hazard': 0.7 },
  'cjdns_wifi':      { 'short': 0.7, 'long': 0.8, 'scope': 0.7, 'risk': 0.5, 'hazard': 0.8 },
  'cjdns_wireguard': { 'short': 0.8, 'long': 0.9, 'scope': 0.8, 'risk': 0.4, 'hazard': 0.8 },
})

print "RESULTS NOT YET FINAL - winners: %s" % getApprovedProjects(budget, costs, votes)
