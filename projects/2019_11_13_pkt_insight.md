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
* **F_EARNING** Amount of PKT which the address earned in the past day
* **F_EARNING_CHART** Chart of income per day
* **F_MINING_TAB** Tab for mining income transactions and other tab for all other transactions

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
