# Routing Quality Indicators

This is a One Person Software Project. I plan make improvements to the
[cjdns-route-server](https://github.com/cjdelisle/cjdns-route-server) project.
The improvements are new tools for analysis of routing quality.

* Project Name: Routing Quality Indicators
* Contact Email: kat@fastmail.nl
* Requested rate: 50 EUR / hour
* Total requested contribution: 5250 EUR
* Maximum requested PKT contribution: 300000 PKT
* PKT address to pay to: pkt1qkucldklk8pxn25mvvnphgu2aamft4q7pzjsc22
* Repository with software which will be improved:
  I will create bespoke clients to https://github.com/cjdelisle/cjdns-route-server
  but will not edit the cjdns-route-server repository itself.

## About me

I am:

* [ ] The lead maintainer of the software
* [ ] A regular contributor to the software
* [ ] An occasional contributor to the software
* [*] Not a contributor yet

My previous Open Source work is related to MH-style user agents, particularly
the mail user agent nmh. Here are three of my previous code contributions
(patches), or otherwise previous Open Source work:

* [ejmejl](https://krabben.twilightparadox.com/fossil/ejmejl/dir?ci=tip):
  Conveniently check email on paper, for people who prefer paper over computers
  or who are coping with unreliable infrastructure
* [ch](https://krabben.twilightparadox.com/fossil/ch/dir?ci=tip):
  Manage contacts with nmh.
* [Various utilities to support nmh](https://lists.nongnu.org/archive/html/nmh-workers/2020-08/msg00000.html)
  * [mhrecoll](https://krabben.twilightparadox.com/fossil/mhrecoll):
    Search a [recoll](https://www.lesbonscomptes.com/recoll) database, and presents
    the results as an nmh folder.
  * [mhq](https://krabben.twilightparadox.com/fossil/mhq):
    Enqueue emails in the drafts folder and, later, send them all at once.
  * [nmh-contrib](https://krabben.twilightparadox.com/fossil/nmh-contrib) (assorted utilities):
    Deduplicate emails, unsubscribe from mailing lists, compose mail based
    on a mailto link, and more.
  * [fzprompter](https://krabben.twilightparadox.com/fossil/fzprompter):
    Compose templated emails.

Beyond these open source projects, I have worked substantially in data
collection and analysis. The above projects differ in topic from my data
analysis work, but they use some of the same skills.

## Goals
As the network grows it will be important that we understand routing performance
and develop a good algorithm for route selection. Unfortunately, little research
has been conducted in this area of great importance.

A good path selection algorithm will gradually converge on a good path.
This can be accomplished by the following high-level procedure.

1. When nodes are newly added to the network, choose paths path from, to,
   and through the node based on heuristics that do not depend on substantial
   data about the node.
2. After a node has been part of the network for some time (perhaps minutes
   or months), we will have collected data about its connectivity in terms
   of uptime, patterns of inter-node connections, and performance
   (e.g., bandwidth, latency) of the connections between this node and others.
3. Based on these data, we continue trying to deduce better routes. When we
   are confident that an alternative paths will be better than those presently
   selected, we test those paths gradually (e.g., by sending a portion of
   traffic through alternative paths).
4. If ever a new path appears to be worse than the existing path, revert
   to the old path.

To arrive at the details of the aforementioned algorithm, we need to quantify
route performance and determine key performance indicators of route performance,
and that is the focus of this project.

## Project deliverable
The present project selects a simple, high-impact analysis in the area
of routing performance. I propose only one deliverable:
**Log and analyze existing node-level data**

* Without modifying the route server, create a custom logger client that
  queries the /ni endpoint for data about individual nodes (not connections,
  paths, &c.).
* Log the result regularly, then deliver the logs.
* Analyze the logs to ascertain node-level patterns and indicators
  relative to the project goal, and deliver a report.

The analysis component may involve experimental, pseudo-experimental, or
observational analyses.

* Experimental analyses are those where I deliberately interfere with network performance
  in order to see how route selection and route performance respond. I may accomplish this
  turning devices off and on, limiting bandwidth, randomly dropping backets
  in a firewall, altering underlying routes, &c. These are the most time-consuming analyses,
  but, aside from that, these are the best.
* Pseudo-experimental analyses are studies of nodes whose connectivity is well understood
  at a lower level than CJDNS, e.g., through physical access to the node, but that I do not
  interfere with for the specific purpose of route analysis. For example, I may compare
  a mobile phone I carry with me to a co-located server that I always leave on.
  It is theoretically harder to justify causality (for example, whether a particular
  indicator of performance truly measures what we want it to) with
  pseudo-experimental analyses, but it practice I believe they will suffice for
  typical connection patterns. I foresee them being inadequete for study of
  connection patterns that presently are uncommon but may become common in the future.
* Observational analyses are those where I don't interfere with the network and don't
  have independent knowledge about connectivity patterns; in other words, observational
  analyses are everything other than experimental and pseudo-experimental analyses.
  It is difficult to infer causality in such studies, but their benefit is that they
  can be applied to a much larger quantity of nodes.

Intended billable time is 105 hours. In case PKT price decreases substantially,
complexity of the data collection and analysis can be reduced to a minimum
of 35 billable hours.

## Schedule
I plan on taking one or two holidays from my main work to work on this project.
I will conduct the majority of the project during the first holiday, including
development of analysis scripts. If I determine that I need to collect more
data, I will let the logger continue running for some time and then take a
second holiday to run the analysis scripts and further analyze the data.

I have not yet scheduled the holidays, and I won't schedule it until after
the project has been accepted. Assuming the project requires two holidays,
I expect to complete the project within eight months of project acceptance.

### Milestones and payment

I understand there will be no up-front payment. I will provide milestone submissions when it is convenient for me to do so. If these milestones are accepted, I request that the NS transfer the amount of PKT necessary to cover the cost of the submitted deliverables **at the current market rate of PKT**, which I will declare in each milestone update. In any case, I accept that the total grants of this project cannot be any more than the "Maximum requested PKT contribution" specified above.

The deliverable will be presented in this repository.

> https://krabben.twilightparadox.com/ns-routing-quality

Collected data, custom code, &c. will be linked from the above repository.

* Conflicts
  * [ ] An organization is receiving the funds
    * [ ] Organization has financial relationships with one or more reviewers: *specify whom*.
    * [ ] Organization has no financial relationships with any reviewers
  * [*] An individual is receiving the funds
    * [ ] Individual works for same organization as one or more reviewers: *specify whom*
    * [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    * [*] Individual does not work for the same organization as any reviewer
* No Pumping
  1. [*] The applicant declares that they understand the community's
  [Ethical Communication Guidelines](https://docs.pkt.cash/en/latest/communication/)
  and will strive to follow these guidelines and represent the PKT community in the best way possible.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

* Proposed
