# New Network Steward Vote

* Project Name: New Network Steward Vote
* Contact Email: cjd@cjdns.fr
* Project participants:
  * Caleb James DeLisle
  * Whoever wins the vote
* Projected duration: 10 weeks
* Projected effort: I don't expect payment for this
* Pre-project effort: About 2 person/months, but I don't expect payment for this
* Requested PKT contribution: 16 million PKT
* PKT address to pay to: pkt1qkx7feflncphh4hqchueqln3k8vts60g3lwtz9j

The object of this proposal is to establish the new Network Steward voting system prior to
implementing a soft fork in the chain.

I have already developed:
1. A vote counting system: https://github.com/cjdelisle/Electorium / https://github.com/cjdelisle/Electorium_go
2. Ability to cast a vote with PKT-Lightning-Wallet: https://github.com/cjdelisle/PKT-Lightning-Wallet/blob/master/proto/rpc_pb/rpc.proto#L4140
3. Ability to cast a vote with (old) pktwallet: https://github.com/pkt-cash/pktd/blob/dfc2b99e9226b70ec108738962138a7179744690/CHANGELOG.md?plain=1#L6
4. Vote computation system in pktd based on Electorium_go https://github.com/pkt-cash/PKT-FullNode/pull/3/files

As of now, it is possible to cast votes, and to count them. There are currently 4 voting
addresses, 2 of them are mine and 2 are from other community members.

Currently the Network Steward address is yielding 1.596 million PKT per week. If the new
system were in place now, this is how much would go to the winner of the election each week.

What I would like to do is take custody of 19.2 million PKT up-front and then begin paying it
out in batches of 1.6 million each week from the start of the project.

The project will begin when I have received the coins and when there are over 100 million PKT
currently being used for voting. This sets a simple target threshold which is easily
achievable if there is any amount of community engagement.

My long term plan is that we use this project, and consider extending it over time, in order
to manage the Network Steward on a go-forward basis. When we have reached a high level of
confidence in the correct operation of the new voting system, we will pursue a *soft fork*
which imposes an additional rule, namely, that the *old system* Network Steward, i.e.
pkt1q6hqsqhqdgqfd8t3xwgceulu7k9d9w5t2amath0qxyfjlvl3s3u4sjza2g2, is forbidden from making
payments to anyone except the *new system* Network Steward, i.e. the winner of the vote.

After the soft fork, the *old* Network Steward will not be capable of awarding funds to
anyone except for the winner of the vote in the new system - but will still be capable of
halting the funding in case of a major incident such as a security exploit.

Then at some point in time after we have become adaquately comfortable that the soft fork
is stable and the chance of some incident is neglegable, I will envite my colleagues to
publish your private keys such that the old Network Steward address will become a simple
pass-through.

## Milestones

### 1. Funding event
When the coins have been received and are in my custody, milestone 2 cannot take place
until this milestone has completed.

### 2. Election concludes with over 100 million votes
This event will take place when there has been an election with 100 million coins counted
as votes. Elections in the new system take place at a period (once per week), if there
are 100 million coins in votes before the election but then some of those coins are spent
or the votes withdrawn, it will not count. Furthermore, if there are 100 million coins in
votes but then after the election, they are spent of withdrawn, the project will not halt.

### 3. Funds exhausted
Each week after the election takes place and has been counted, I will transfer 1.6mn PKT
to the winner.

## Project Halt Conditions
It is my greatest intention to ensure that this project follows, as closely as possible,
how the new Network Steward will behave in real life. To that end, I do not intend to
make any value judgements on how the coins are being used. If one believes in democracy
then one must believe in democracy even when they disagree with the outcome.

There are, however, two possible conditions over which I will halt the project:

1. If I believe that the transfer of coins to the winner would constitute a crime: For
example if the winner is an OFAC designated terrorist organization.
2. If I believe that the vote counting code has malfunctioned and is either not able to
produce a result at all, or produces a result that does not match the result that should
be expected from manually computing the delegated voting process over the duely cast
votes.

In case of a project halt, I will re-start the project once I believe the condition has
been remediated, or I will refund the coins to the original Network Steward address if
I do not foresee remediation within what I consider a reasonable timeframe.


## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I
intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
  1. [ ] An organization is receiving the funds
    1. [ ] Organization has financial relationships with one or more reviewers: *specify whom*
    2. [ ] Organization has no financial relationships with any reviewers
  2. [x] An individual is receiving the funds
    1. [x] Individual works for same organization as one or more reviewers: Myself, I will not review my own propsal.
    2. [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [x] Project results will present information which might lead to PKT price speculation
    * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially misleading the public.
  2. [ ] Project results will not present information which might lead to PKT price speculation

## No Pumping
100% of the funds allocated in this project will be forwarded to the winner of the vote to
do what they see fit with them, so the indirect communications are beyond my control. There have
been and will be direct communications in order to encourage PKT holders to understand the system
and to vote, but they do not encourage or discourage the purchase or sale of any asset.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

Proposed...