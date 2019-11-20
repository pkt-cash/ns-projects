# PKT Block Explorer Project

* Project Name: pkt_insight
* Contact Email: cjd@cjdns.fr
* Project participants:
  * Caleb James DeLisle
  * *Other participants will be added as needed*
* Projected duration: 2 month
* Projected effort: 4 person-months
* Requested PKT contribution: 25 million PKT
* Project status: **PROPOSED**

## Project summary
The objective of pkt_insight is to develop software which will make it easier to collect and track data about the blockchain for debugging purposes and for checking the status of transactions and addresses.

## Project deliverables

The key deliverable will be a fork of [bitcore](https://github.com/bitpay/bitcore/) with a modified version of the Insight block explorer to work with PacketCrypt and the specific needs of the PKT project.

This deliverable is:
* New open source software
* Which will be available under the [MIT](https://spdx.org/licenses/MIT.html) license
* The maintainer of this software will be: **Caleb James DeLisle**
* https://github.com/cjdelisle OR https://github.com/pkt-cash if the network steward wishes it so

A proof-of-concept was developed and is available at https://pkt-insight.cjdns.fr/ which has the following changes from bitcore Insight:
* Modifications to work with PacketCrypt and PKT blockchain
* PacketCrypt section of block detail page
* Price page is removed because PKT is not actively traded
* Rich list page is added to display the richest addresses

### Evolution of the prototype

The pkt_insight project will add the following new features to the proof-of-concept prototype:

#### Front page:
Everything in the front page of the PoC, plus:
* **F_FRNT_BW** Network Global Bandwidth
* **F_FRNT_CSS** Network CryptoCycles per second estimate
* **F_FRNT_CHART** Bandwidth and encryptions per second chart

#### Blocks page:
In the front page and in the "blocks" page there should be a list of blocks, each block in the table should display everything in the prototype plus the following items:
* **F_BLKS_RELAGE** Age (which is a relative time mouse hover shows the timestamp)
* **F_BLKS_RETARGET** If the block is a difficulty retarget, the row should be colored
* **F_BLKS_NXT_RETARGET** Expected next difficulty retarget (+ or - percent)

#### Block detail page
Everthing in the PoC, plus:
* **F_BLK_PCVER** PacketCrypt version
* **F_BLK_CRYPTOCYCLES** Estimated total encryptions
* **F_BLK_BADWIDTH** Estimated total bandwidth (MB)

#### Address page
Everything in the PoC, plus:
* **F_ADDR_EARNING** Amount of PKT which the address earned in the past day
* **F_ADDR_EARNING_CHART** Chart of income per day
* **F_ADDR_MINING_TAB** Tab for mining income transactions and other tab for all other transactions

#### Network Steward page
* **F_NS_CURRENT** Current network steward address
* **F_NS_TALLY** Amount of PKT voting for a new network steward
* **F_NS_RUNNERSUP** Addresses who might become network steward
* **F_NS_BURNED** Amount of coins burned
* **F_NS_BALANCE** Network steward address balance
* **F_NS_TX** List of transactions by network steward address - with links to relevant project pages

#### Mobile support
* The explorer will provide *basic functionality* on an android mobile device browser including at least:
  * **F_M_BALANCE** Ability to check address balance
  * **F_M_EARNING** PKT earned in the past day
  * **F_M_LASTBLK** Ability to check when the last block was produced
* Best effort will be made to support other mobile devices to the same level

## Success criteria
* **S_CI** Codebase passing automated continuous integration build
* **S_INSTALL** At least one successful independent installation of the explorer
* **S_FEATURES** At least 90% of the described features achieved

## Payments
All payments shall be made to `p7Gdf7YhaxSkWm6u6yU452S6C9mJpuTfwu`

## Milestones
The following are milestones for the progress of the project by which the network steward
can evaluate the success of the project.

### M0 Kickoff
At the kickoff of the project, the network steward will grant 10mn PKT to the applicant and
the project will begin.

### M1
Milestone 1 will focus on improvements to the address page, front page and block detail page.
Features expected to be completed include:

* **F_ADDR_EARNING**
* **F_ADDR_EARNING_CHART**
* **F_ADDR_MINING_TAB**
* **F_FRNT_BW**
* **F_FRNT_CSS**
* **F_FRNT_CHART**
* **F_BLK_PCVER**
* **F_BLK_CRYPTOCYCLES**
* **F_BLK_BADWIDTH**

Furthermore, Milestone 1 must be validated by a continuous integration build using a publicly
accessible continuous integration service such as travis-ci (**S_CI**).

Upon the completion of Milestone 1, a report will be written and the applicant will seek
approval from the network steward. No payment will occur at this time but if Milestone 1 is
accepted but Milestone 2 does not complete successfully, the network steward will pay the
applicant 5mn PKT on top of the initial 10mn PKT and the steward will retain the final 10mn
PKT of the budget.

### M2
Milestone 2 will focus on improvements to the blocks page, the creation of the network steward
page, and improved mobile support. Specific features which will be used to validate Milestone 2
will include:

* **F_NS_CURRENT**
* **F_NS_TALLY**
* **F_NS_RUNNERSUP**
* **F_NS_BURNED**
* **F_NS_BALANCE**
* **F_NS_TX**
* **F_BLKS_RELAGE**
* **F_BLKS_RETARGET**
* **F_BLKS_NXT_RETARGET**
* **F_M_BALANCE**
* **F_M_EARNING**
* **F_M_LASTBLK**

Upon completion of Milestone 2, a report will be written and the applicant will seek
approval from the network steward. Upon approval, payment of 15mn PKT will be issued, covering
Milestone 1 and Milestone 2.

At this point the project will reach the end of it's explicit funding, however the applicant
commits to the long term maintanence of the PKT insight software and the network steward commits
to continuing interest in the evolution of the software.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.
