# PKT Block Explorer Project

* Project Name: pkt_insight
* Contact Email: cjd@cjdns.fr
* Project participants:
  * Caleb James DeLisle
  * *Other participants will be added as needed*
* Projected duration: 2 month
* Projected effort: 4 person-months
* Requested PKT contribution: 25 million PKT
* Project status: **APPROVED**

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
* **F_BLK_BANDWIDTH** Estimated total bandwidth (MB)

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
* **F_BLK_BANDWIDTH**

Furthermore, Milestone 1 must be validated by a continuous integration build using a publicly
accessible continuous integration service such as travis-ci (**S_CI**).

Upon the completion of Milestone 1, a report will be written and the applicant will seek
approval from the network steward. The network steward will pay 5mn PKT for the completion of
this milestone.

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
approval from the network steward. Upon approval, payment of 10mn PKT will be issued.

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

## Kickoff

First payment of 10mn completed to address
[p7Gdf7YhaxSkWm6u6yU452S6C9mJpuTfwu](https://pkt-insight.cjdns.fr/#/PKT/pkt/address/p7Gdf7YhaxSkWm6u6yU452S6C9mJpuTfwu)
with transactions:
[1](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/c66ba644a7fd637a100a4285a59ab1cae5358247a70ff40dfe5a86e4747a278c)
[2](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8cfdf56eb33ebaa44c93067b684a9d2aa565153063ce328d380cfe465ee09773)
[3](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f87c5f625f2c13660fc8e35b5d657c483ebe2202efb69f7488f573e3f5823423)
[4](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f55b9dbeefc8d38507ed0bb98c82ce2711b04d3c46b793447e58c4821a654403)
[5](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d9d848914a33794a4b0f0b69ecd469259d4b0c26f31a5e722789f3c66cb817cf)
[6](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/17c13eee951ae103add8e04d560c767e265c3947dc30727b5249f014b0fb096e)
[7](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/276aa02f6e8e7bed6f42d460ce6c04234e134f91c8526e0b13aa2c74e937044c)
[8](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/92cdfe570344c1208e45ec075a958654ca023e155d9059109724aca3e298d704)
[9](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/ca40f94fe98e97164a71f1b476e9d5c01b9760af04545ce85988d4baa738dff1)
[10](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/1146ae6cc8d8af5b93114d85d643343e23cf8d8126405c5ecb663ed9c4c1bb4f)
[11](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/79d32535b50fd0a7d0bf1ff5f98fce94999e4aa539b301155bb82aacc13549dc)
[12](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/70841535a2c4c3bc1d58d297333dffef7959b11b00635d9bcb376eb18e421b6f)
[13](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/064e4d4c01145ffc3bb444f96facfeadb3c76cf4fcd274e95595233154aeeb8b)
[14](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/1f7a216394c278cb2433e51683bf7771e8e1814ed9609401fa6015bb1d747034)
[15](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8136e214d03f5f4b2042a5144bf02e11f9f000ceec3babe694e48a784409000c)
[16](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/c2311b165f72abe75e7bc95944170c97501a41bd2b1591fb13e0420e1a9485d0)
[17](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3a89b5c0d32d934732b9f8dcdc3d22dfc69dd0ac7d668ee4deed4c63fb104895)
[18](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/360b4c9408b872e9e9c1fe5432b86f121eab427030937c3b7a5891d709cb21bc)
[19](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3ad1d7b74270cfcc4dd22d3d74de2e0cb72d87407e6137777ba71bb035e7ef38)
[20](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/b8679a0c7843887513e30dc6d1dd8d275abc7087af6c0dcd03484a766e2181e0)
[21](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d3bb52780ae890bac41484e0b548afee9cb6f94f4959716e9ec59157f3efec6c)
[22](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/64e236436b4d51c4651d29e60791f99cea35b570c41d96be7efb10dc67779d4a)
[23](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f2012915498362c8a61d1517ab558f2aa105e4b9abdd23b02db92e9d2f1286c5)
[24](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/a184204ddee752fef41525a1b262bfca5205b2ba9c4a055d88c06e08fc84d7a9)
[25](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/b0d5040b708e9d5c9367f89d217902c5cf8a0843cb3ea4ed8d979481e882176b)
[26](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/c29cf9489ef79cc460d4134cba591fa3933d58ab8b58fda2a6e5f2d33907703e)
[27](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/a77106785bed7cd24e0b6f4e6ffaa762f112db3101d201060850e50670ded445)
[28](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/bf81890b5feb9f067a3fc65979eed7ff018169af57dade85ce6868d8cad87971)
[29](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/129779dce8fc45e9e53e9a0b84de8b33ccc31758c4ea7f01e43bd0e8c2f54a21)
[30](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d8943bb0822354aa38aab13ad8bf64a85186e5eca939be51a52defcdaa21cbe7)
[31](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/b59806a6e28bd607798334516137b89bf9fdadcb4f6f003e19b3f32bc259d881)
[32](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d11900f7dc64669568d3c4ea07f93ec958cfbd5fab53f6c5eec31704ae77a6f4)
[33](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/4042ab4ac2744a371e72e29de940f639142bb768bd9a1a9953bc67b1da3525f8)
[34](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/5880f14a6805f1fca71904e0650afc5e2a5778dda874b827acab17b68208caea)
[35](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f1812191cb922008efcd0129315ef2499f4eed792ffa9a4cfe86c40adf57cf6a)
[36](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/712474852e69c05174ced55531671f9517aea4ab0df15e6330d12f8d7db2590f)
[37](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/a70005b7529849a62ff752090f83b97666efa1e09288fcbe23309dfb5595a734)
[38](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/e0490d40988bd938758716028c62227c656e1d1cd0863bdc4fe22047b11738b5)
[39](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/672848bf7f3f7c2be29e5d2c70be4bad4a4bfed5ad1811db5a28d395073bf5a2)
[40](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d68dea39976054255e294f6d7375243f5d907e5b3f1050887984ce04ee018d65)
[41](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/a4b926f8ee39b20e89ea7794b82ede490e17e7c2b2d89234ab9ebcbc5b7b2770)
[42](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/e79f8f7fdda3a2ff6f8ee521c72f0fcb822006187b268b771717ddb590f9deb8)
[43](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f3f53fea11244941958071297a5c9b87bcfe4afa25de7ac4c2ed8e064bda15ad)
[44](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/2e9b0e2ad0863120650fb3e172581af7e30afffef86e171c43881b3291cd3fcb)
[45](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/674ef53629ab0e7ada47dbb2608c3bf701f14505407a93f26bc8fce30a69abb9)
[46](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/cd1c21f2e8ea9250557ca20308e2d3912f63fb5ea34f04a5b96bfc7153eb8d06)
[47](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/0243688f3cfb4c8ad057d9be3b02ffdd4e720d49871d0a0375fa273433f547ba)
[48](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/ddc3e25f29dd6108f01ac2fe5ae36a71ff4e8453a85e938f1ab3b36c47fd82c9)
[49](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/93cfd3b3617169b0091a60943b30bd91d724f27eb1649ef8255a6f90f227ea79)
[50](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d489652bbfa6e9e42886a5b645f647d68494df5b57a51683f2bd5a904e5f64c2)
[51](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/efefa38b723277ae1e3a45a51ea00601ee210688a2be55b58ae55c387f832b52)
[52](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/60fa1e3667ace9159b4e1030bef5e6640c6ee0c770a431326c40eb5a6a2da070)
[53](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/ec1fa4b6f652fc60879ed52d8bdd71f87021386269013ac4b809f919f8495562)
[54](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/83778e6ec23c758207acd347b4b98718d68d41d608874b412241c3f4dee6803f)
[55](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/966537d6de18a272da17c31fc4cb699023304d9a5e6351d7e1c00cc4546851f9)
[56](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/6d97031ac8b08bcf68eaf1255b623bad6679db3f0876e437e5f307ed9b500ea4)
[57](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/5b2afea996a275d599a3be0b7ca6f3eedc9bfe00f1dba79a93c34033ce76a828)
[58](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/13df4ef649e72f7413b93dcb82cb1eced1552be4033eb67dc2b0acb151b887dd)
[59](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/c967ea2780e1e361094c84cb559810329cecf6563b55e413af3c4da5b3e22c37)
[60](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/467066401953794f302690f43a41ed91ac5481d4aef3670af041cefb39472cc9)
[61](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/71a813495380f7704f573a5b993de932e74dad40a9880f329eb138626a89bf4d)
[62](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d76fe817f6f0b7d75e1a858da5f6c5e76fee3002eb28c235fe28816f0f754e5d)
[63](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/cf44c747acda919ce62c1e6a05ebfd0790db2fc9c17ec8179e32a0132c8b1685)
[64](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d647e4c6ad65ca595eb1caf92e87b8709f4070b8b50cb09d0498768239a1db48)
[65](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/35dc00daa2f7394ffa2a2c1b5e2d1e60f1be05f26588e10ad392802d9d85f5d5)
[66](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/82c597350860b553870627f3a77ed2b741d97143701e14ab7c85819f95f29edf)
[67](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/9d149b7286e33d5929712f3fd1e65b4de119765e2aadce5ad03088038af32b4e)
[68](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3356c4309dec5b032f3a47c883967d2605e4ec88e19911d0fcd8684794cd2e21)
[69](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/65c90fae30eae7b2f1f5ac9e88d2fb5bc6db95afd4916d1b0f5d60ceab0c39e6)
[70](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/2269ddc10f29768e2597792e344069eadf2fbd8fe80d95fcff194d7aca9cb946)
[71](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/589e9bb51f519001a413cc7addc2e1d6a15bfe184307cdc387d948439cddb457)
[72](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/4ed7ff5e591acb60a0aa3611f55efd632add1a5c0285527a0691d1bd13fc5117)
[73](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/dc7b68fd4ea2792736622074bdf088d1d326b43f6ce881ecb5adbd63480e0b77)
[74](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/578ae00c7fbaff96bbf8c869cc22d8a7e045d7b36cca9362049bfc039297063c)
[75](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/2412177ca6bf26eb7794214f0a90ac32fb72a8f0f0884945b154a1e889f030a5)
[76](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8833c2bcde666d878b228d98207eb6351220ebbda9f97f46a2421210cf970d82)
[77](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/aad92b76947150197af8f9c94a1a4fe02a1bcb9982c84375b8dec1be77c8aa10)
[78](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/30f9ee3e2d82b35eeff74381215ca5b56a12d2bfde485b1db555bd65a8d30968)
[79](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/bb2109adf310bf1c189f12ebcf35b26a36d69b807f2410ce589cf0941a621f2d)
[80](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/eaedc00323ab8124b024b7505cb6522060130d6593b556d1188203b9ebb809ab)
[81](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/b82628400fa9ac79c41ec42a160ca86f3b8380b54e0b94a4de802032fff673e7)
[82](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/6077aa9740da299e9756009736a949e8648c11f08ef0f1295e868ce422adaf99)
[83](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/977f3395a2e2ba897f397527b89fab1712eecf73b3f74590d9463663ecac9d1b)
[84](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/18d2d5187219ff23d711b5fe2d17feb3ff1bea711e71b42c0f719db32f5307c8)
[85](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/e08891cf06b09a967d5323cc05d1e406ea992220e526c138f97741da8c3efe80)
[86](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/65693b32c6adf96736ab6711ca1e0115b43fdc489e438a29502fb94584efc19c)
[87](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/df34ba8c4d28983ab2ccae2c6f487318bead14213ffa56a6ae81108154d0c95d)
[88](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/2860c5971fec32064055195b7cb21dbf23b5fbeecc6473cceeba200e446555fa)
[89](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/ad3b280b7a606f8c8e08d15ef903e4709d6af9c026eef362397e701639c48366)
[90](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3eec1cf83e86077e41bf8aa54e1736cedf43afa551b8f535346413f0bf2b62b1)
[91](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/04d60a0be8485906f4dcd10eb9fcfb2b6c8e947c5261fff358062573897481fd)
[92](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/386258a23df5dd8ef5cf33b8aaece328ff0508744077940d34c36137ec89502b)
[93](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/52cb1cc1fb7499afda54d2e6e6430ebcf754885e4dea3cc070b1ade3b896f003)
[94](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/55c98034a394abc3c372423bceeaf2369f2ab3001b651024e6eafc7b7cbef3d7)
[95](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/85d5713de68398bb4dd47ee909756dbcedde1882d46fee219c8756df1be21b68)
[96](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/b389180672323f8fb8141943a09fb486a85cef5f37c75e678f90a57f95562829)
[97](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/682f5ce58d567db4a3eca338576f6d6728cf15b9aa1e6eea078ba7e58c0c1c85)
[98](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8510d650a5daf6071e3610553859a1bd077e1a79d56e0f06ac0b087268de562b)
[99](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/7de8bbd8f1b5395ccfd55d90ba924019ee4707e1a56147fb92a24c519f55a53f)
[100](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/6cc2f3148c906f329f1e0486d9e9c6936393209bf21df3531ca9b4fffcbf59cc)


## Milestone 1 report - 2020-03-19
The key objective of this project is to evolve the prototype that was delivered during the intial application. However, it was judged that the software on which the prototype was built was not suitable for a more featureful block explorer so a decision was made to re-write a block explorer from scratch to the same level of features, plus the deliverables for this project.

Therefore we are pleased to announce that we have an entirely new explorer backend server, plus two new frontends, one based on the prototype and a new one. Since the original prototype and the final result share no code in common, we intend to keep the original prototype online to serve as a "second opinion" of the state of the blockchain.

### Project results

1. [Bitcore backend](https://github.com/cjdelisle/pkt_insight_bitcore) (original prototype)
  * Hosted: https://pkt-insight.cjdns.fr/api/PKT/pkt/block?limit=1
2. [Bitcore Insight based frontend](https://github.com/cjdelisle/pkt_insight_bitcore/tree/pkt/packages/insight) (original prototype)
  * Hosted: https://pkt-insight.cjdns.fr/
3. [PKT Explorer Backend](https://github.com/cjdelisle/pkt-explorer-backend) (new)
  * Hosted: https://pkt.cash/api/v1/PKT/pkt/chain/down/1
4. [Insight frontend adapted to PKT Explorer Backend](https://github.com/cjdelisle/pkt-explorer-insightfe) (new)
  * Hosted: https://alpha-pkt-explorer.cjdns.fr
5. [PKT Explorer Frontend](https://github.com/gorhgorh/pkt-explorer) (new)
  * Hosted: https://newalpha-pkt-explorer.cjdns.fr

### Success criteria for Milestone 1
The objective of milestone 1 was to provide the original prototype plus the following additional features:

* [x] F_ADDR_EARNING - Address page, amount of PKT which the address earned in the past day
  * We exclude non-mining income from this chart to make it more relevant to the user.
  * [See address page](https://newalpha-pkt-explorer.cjdns.fr/address/pkt1q6hqsqhqdgqfd8t3xwgceulu7k9d9w5t2amath0qxyfjlvl3s3u4sjza2g2) "Mined last 24h"
* [x] F_ADDR_EARNING_CHART - Address page, chart of income per day
  * We exclude non-mining income from this chart to make it more relevant to the user.
  * [See address page](https://newalpha-pkt-explorer.cjdns.fr/address/pkt1q6hqsqhqdgqfd8t3xwgceulu7k9d9w5t2amath0qxyfjlvl3s3u4sjza2g2) chart in the upper right
* [x] F_ADDR_MINING_TAB - Tab for mining income transactions and other tab for all other
  * [See address page](https://newalpha-pkt-explorer.cjdns.fr/address/pkt1q6hqsqhqdgqfd8t3xwgceulu7k9d9w5t2amath0qxyfjlvl3s3u4sjza2g2) click "Mining income"
  * Note: Rather than showing each transaction, we only show income by day in order to be less confusing because there is one transaction per block.
* [x] F_FRNT_BW - Network Global Bandwidth
  * [See front page](https://newalpha-pkt-explorer.cjdns.fr/) "Network Bandwidth"
* [x] F_FRNT_CSS - Network CryptoCycles per second estimate
  * [See front page](https://newalpha-pkt-explorer.cjdns.fr/) "Encryptions Per Second"
* [x] F_FRNT_CHART - Bandwidth and encryptions per second chart
  * [See front page](https://newalpha-pkt-explorer.cjdns.fr/) front-and-center
* [ ] F_BLK_PCVER - (block page) - PacketCrypt version
  * This was not implemented because it is version 2 for all but the very early blocks and we decided that it was not actually relevant information. If the Network Steward wishes it, this can be trivially added but we believe that adding it would take away value.
* [x] F_BLK_CRYPTOCYCLES - (block page) - Estimated total encryptions
  * [See block page](https://newalpha-pkt-explorer.cjdns.fr/block/d16f6ad7e95fa315d31d020a82d7c4c09c0b0d68d2f95f2cbce45aa2945e5370) "Estimated Encryptions Per Second"
  * We chose to display an estimate of encryptions **per second** rather than the total number of encryptions which made the block, so that the information is similar to F_FRNT_CSS on the front page.
* [x] F_BLK_BANDWIDTH - (block page) - Estimated total bandwidth (MB)
  * [See block page](https://newalpha-pkt-explorer.cjdns.fr/block/d16f6ad7e95fa315d31d020a82d7c4c09c0b0d68d2f95f2cbce45aa2945e5370) "Estimated Bandwidth"
* [x] S_CI - Codebase passing automated continuous integration build
  * [PKT Explorer Backend CI](https://travis-ci.org/github/cjdelisle/pkt-explorer-backend)
  * [PKT Explorer Frontend CI](https://travis-ci.org/github/gorhgorh/pkt-explorer)

### Additional features not written in the proposal
This project took on the objective of creating a *great* block explorer, regardless of what the proposal dictated, so there were many features added which were not in the original proposal.

* Front page
  * Current difficulty
  * How many coins have been mined to-date
  * How many coins per block reward (currently)
  * How many coins remain to be mined
* Transaction page
  * Total fees which were collected from all transactions in the block
  * Block reward
  * Content of the coinbase
* Address page
  * Display transactions as "income" and "spending" with expandability to show the exact transaction
* Transaction rendering
  * For inputs, show the number of individual transactions which were aggregated for one address to fund the current transaction
  * For outputs, show whether the payment was spent by the recipient
* Tooltips everywhere to help people navigate

Second payment has been partially made in transactions:

[1](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/0fa922fdc76d6b9aae5e2512ebc97c49b7aeb41663a5b777f2a577cdd25a5e1e)
[2](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/e144a127075e0a9e32a0cd1d8b91d56d643cc99548b4433b2425584071a8434f)
[3](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/112cc4eee85092a6b16c9df41508c4cafd80892806aa50d22f3f1d1caa51e284)
[4](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/5b78d536f4ffc838ef2cae6cb55dc1ff9d8ff224c7542975a0009b709eca2b8c)
[5](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/134e14afe3dffeb499144b13005ea9c3456bcfeff3d3215304f75b713e6b4c76)
[6](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d7dd72b3607bdc247ba598af2019db6a53ca8c347e5a94ecddcd1b2632847fdf)
[7](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3f6eac52f326aab009568049c71dabeb87cf3f6ae559d91883521733a49d2973)
[8](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/0e8ba4f54d400b730bf10cee0150acde277049d70c50feef42c712ef2ff8aa80)
[9](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/1e9b93e54fa4eaf118571a60fc626394ea618015baa25af534cc488c9008001a)

Due to a technical difficulty, the NS was unable to pay the last 0.5mn PKT, the applicant has signaled that they are willing to accept payment later.
