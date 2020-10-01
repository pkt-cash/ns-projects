# TokenStrike
* Project Name: tokenstrike
* Contact Email: cjd@cjdns.fr
* Project participants:
  * Caleb James DeLisle will work 20% of fulltime
  * Ben Le will work 20% of fulltime
  * Miracle Attainment Employee will work 90% of fulltime (likely Mitchell Clark)
* Projected duration: 6 months
* Projected effort: 7.2 person-months
* Pre-project effort: 0.2 person-month
* Requested PKT contribution: 40mn
* PKT address to pay to: pkt1qju5ru8em5jz34r4g6htfvdp4cqjt4ey7ktmvv5

## Project summary

The objective of this project is to establish a protocol for the issuance and exchange of tokens. Tokens must be able to be issued and exchanged with minimal effort (gas fees needed for exhange of Ethereum tokens are unacceptable). A holder of tokens should be able to exchange them in a fully untrusted Lightning Network HTLC transaction. We relax the requirement that holders of tokens must be secure from attacks by the token issuer, and in it's place we add the requirement that any attack by the issuer of a token should be able to be proven to have taken place, such that an issuer who breaks protocol will be *discredited* and nodes will cease to interact with them until they are manually reset.

A system for nearly-free token issuance is required in order to pursue the objective of a Decentralized Bandwith Market.

For both Miracle Attainment and Anode, we will require the function of secure KYC check and interoperability, preferably tied to traditional and innovative financial payment rails, where financial assets which are native to public blockchain can interact with established payment networks such as SWIFT and other international payment standards. One good potential partner on this KYC payment solution, we reccommend planning ahead for our Proposal to be integrated with [Proton Open SDKs](https://blog.metalpay.com/announcing-early-beta-releases-of-proton-open-sdk/?fbclid=IwAR15_qq5FsrvbxlEbEyGGf837YVkdnwtJOk5n51QzWuPpZiC_WIjrmEOiLE).

## Team and Past Work
The technical lead will be Caleb, the bulk of software development will be carried out by Miracle Attainment's employee (likely Mitchell Clark) with Ben Le and Miracle Attainment Corp and Caleb and Anode LLC acting as use case providers.

Miracle Attainment Corp is an Exempt Telecommunications Company and FCC-Certified Open Video System and Online Video Distribution Network servicing all USA households as well as Indigenous Tribes and focusing on free or nearly-free services including Ads-Supported Video On Demand.

MIRACLE ATTAINMENT's Company Mission is to provide 24/7-backed up Crisis Communications Services assisting the 1st Responders in Disaster Recovery. According to the Deregulation of Telecommunications Act of 1996, Miracle Attainment has attained FCC Certification to become an Open Video System, which is 50% a Telecommunications Company, and 50% Cable Media Company, deploying to IP HDTV/Ultra HDTV / 4K / 8K signals via the ATSC 3.0 Standards, mobile phones, PC and laptop devices and social media networks. 
https://docs.fcc.gov/public/attachments/DA-20-728A1.pdf

## Project deliverables

* [x] New open source software
    * Which license(s) which you will use:
      * [ ] [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
      * [x] [MIT](https://spdx.org/licenses/MIT.html)
      * [ ] [GPL-2.0-only](https://spdx.org/licenses/GPL-2.0-only.html)
      * If your license(s) is/are not shown, please add them using the [SPDX license list](https://spdx.org/licenses/)
    * The maintainer of this software will be: Caleb
    * The software will be hosted in: *unknown, github.com/pkt-cash if desired*
* [ ] Contributions to existing software
  * List software projects
    * [ ] [cjdns](https://github.com/cjdelisle/cjdns)
    * [ ] [yggdrasil-go](https://github.com/yggdrasil-network/yggdrasil-go)
    * [ ] [PacketCrypt](https://github.com/cjdelisle/PacketCrypt)
    * [ ] [pktd](https://github.com/pkt-cash/pktd)
    * If the project is not shown, please add it with a link to its code repository
* [ ] Other deliverables (please describe)

### D1 Issuance server
When creating a token, the issuance server will create a "sig chain" (a chain of updates to a token database state, otherwise known as a "permissioned blockchain").

Details of the protocol can be found in the [protocol spec](https://cryptpad.fr/code/#/2/code/view/mrFy3iNr7CvaffxBkdcA4Qc9GYllfznA7JEmHRtaUNQ/present/).

### D2 Replication server
The replication server will keep track of the histories of one or more tokens and will watch for signs of an issuer breaking the protocol.

### D3 Token wallet
The wallet will be capable of creating keys for receiving and sending of tokens, as well as trading tokens for a secret value (HTLC Lightning Network atomic swap). No wallet GUI is explicitly required by the project.

## Success criteria

* Capability of people to send tokens to one another using wallet
* At least one public operating replication server
* Multiple issued tokens in existance

## Milestones

### Milestone 0 (Kickoff)
The TokenStrike protocol was roughly specified so that the complexity and security properties of the project could be understood. See: [protocol spec](https://cryptpad.fr/code/#/2/code/view/mrFy3iNr7CvaffxBkdcA4Qc9GYllfznA7JEmHRtaUNQ/present/). Also discussions were had in order to identify the best team for the project.

Because we are still finalizing the team who will perform the work, we ask that the Network Steward approves this project with **no initial payment** and we will solidify the execution team as soon as possible. Payment will commence on successful delivery of Milestone 1.

### Milestone 1
#### Success criteria
* Use case reports from Miracle Attainment and Anode LLC
* API specification for v1 wallet and issuance server, with calls listed below: 
  * Anyone -> Anyone
    * `discredit(issuer_key, reason_data)`
  * Wallet -> Issuer: `lock_tokens_for_transfer(tokens_id, transfer_to_key, hash_of_secret) -> LockId|FAIL`
  * Wallet -> Issuer: `transfer_tokens(lock_id, secret_preimage) -> OK|FAIL`
  * Issuer -> Anybody: `update_state(change_num, change_id, patch, justifications)`
  * Replicator -> Anybody: `gossip_update_state(issuer_key, update_state_message)`
  * Wallet -> PKT Mining Pool: `Announce(I_am_locking_these_coins)`
  * Wallet -> PKT Mining Pool: `Announce(I_am_transferring_these_coins)`
  * PKT Mining Pool -> Anybody: `Announcements`
  * PKT Mining Pool -> Anybody: `Announcement with time proof merkle`
  * Replicator -> Anybody: `discredit(issuer_key, reason_data)`
  * Wallet -> Replicator: `Announce(I_am_locking_these_coins)`
  * Wallet -> Replicator: `Announce(I_am_transferring_these_coins)`
  * Wallet -> Replicator/Issuer: `get_headers(last_valid_block)`
* Issuance server which is capable of locking tokens and affecting transfers as well as unlocking them in case of a failed transfer based on time (proven by blocks in the PKT chain).
* Wallet which is able to send and receive a transfer of tokens. The sender of tokens will do both `lock_tokens_for_transfer()` and `transfer_tokens()` calls, we are not doing atomic swaps yet.
* Updates to PacketCrypt in order to allow listening to pool servers for particular types of Announcements.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.

### Milestone 2
#### Success criteria
* Replication server is able to track updates from multiple tokens on multiple issuers.
* Library for verification of updates from issuers to verify their validity and create succinct accusations if they are not valid.
  * Did the issuer create two blocks of the same height?
  * Did the issuer lock token without a signature from the key owning those token?
  * Did the issuer transfer token without the proper secret preimage or to the wrong recipient?
  * Did the issuer fail a transfer (unlock) a token for which the secret preimage was in fact broadcast?
  * Did the issuer refuse to lock token when a wallet requested?
* Update to PacketCrypt block miner to allow miner to submit the merkle branches of announcements upon finding a block, additionally update of block handler to provide them to interested parties.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.

### Milestone 3
#### Success criteria
* Finalized API specifications for wallet, issuance server and replication server.
* Demo of an atomic swap of tokens for coins in a lightning network transaction.
* Wallet able to broadcast PacketCrypt Announcements in order to prove that the transaction went through.
* Temporary gossip protocol developed for exchanging accusations and trade proposals, for use cases where protocol is not embedded in another application.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.

### Milestone 4
* Development of a test suite which implements a matrix of different scenarios including: issuer goes offline during trade, purchaser goes offline during trade, seller goes offline during trade and fork of PKT blockchain during any of these events.
* Documentation for operators of issuer server, replication server and wallet.
* Establishment of a public replication server which is able to validate any issuer.
* Establishment of the first stable public demo token.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.


## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I intend to make effort, influence the Network Steward to accept this or any other project I have submitted.

*Please check one or more:*

1. Conflicts
  1. [ ] An organization is receiving the funds
    1. [ ] Organization has financial relationships with one or more reviewers: *specify whom*
    2. [ ] Organization has no financial relationships with any reviewers
  2. [x] An individual is receiving the funds
    1. [ ] Individual works for same organization as one or more reviewers: *specify whom*
    2. [x] Individual has other financial relationships with one or more reviewers: I am one of the reviewers.
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [ ] Project results will present information which might lead to PKT price speculation
    * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially misleading the public.
  2. [x] Project results will not present information which might lead to PKT price speculation

### Conflict statement
I am one of the reviewers but I am also dedicated to PKT and did a good project making the block explorer. Like with the block explorer, if this project is won I intend to make every effort to ensure that the project completes successfully. I will also recuse myself from judging my own proposal and milestone report submissions. In case a grade is required from me as part of the process, I will grade this project as the average of all other projects which I have graded.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

* Submitted, awaiting review