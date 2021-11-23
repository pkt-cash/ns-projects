## double_wallet project

* Project Name: double_wallet
* Contact Email: jesse@anode.co
* Project participants:
  * Jesse Berger - coordinator - 10% fulltime
  * Anode LLC & Gridfinity LLC - project coordination
  * Caleb James DeLisle - (@cjd on pkt.chat) - contracted developer - 30% fulltime
  * Michael “Mehow” Pospieszalski (mehowfnm@me.com) - 10% fulltime
  * Justus Ranvier (Justus@opentransactions.org) - 30% fulltime
  * Lin Fisher (linfisher@mac.com) - 3% fulltime
* Projected duration: 3 months
* Projected effort: 8 person/months
* Pre-project effort: 2 person/months
* Requested PKT contribution: 40mn PKT
* PKT address to pay to: pkt1q2mk0pmhmnte00n8ylp7h2pejmde07pswv7ywg3

## Project summary

To create two new fully functioning desktop wallets, one being Electrum based and the other based on Open Transactions (Rune wallet). Both wallets will be capable validating PacketCrypt proofs and making basic payment operations on the PKT chain. Electrum wallet will be capable of off-chain transactions using Lightning Network while Rune wallet will be capable of off-chain transactions using Open Transactions system.

The point of developing **two** wallets with two different off-chain transaction mechanisms is to maximize the likelihood of a successful outcome for the PKT chain.

## Team and Past Work

Michal Pospieszalski - former profesional government and private enterprise hacker and CTO that has developed and supervised the delivery of millions of lines of code to various private and public entities since he graduated from the University of Virigina.  Formerly certified by Microsoft, Novell, Cisco, Sun and Oracle with over 70+ IT certifications.  Fluent in Java, JavaScript, Swift, C++, SQL.  In the last year delivered two IOS apps to customers.  Has been working as Presdient at Rune Wallet since January 2018.  Michal shall be the manager of this project.  Linked in: https://www.linkedin.com/in/michal-mehow-pospieszalski-1b3b4443/

Justus Ranvier - Chief architect, currently maintaing Open Transactions at https://github.com/FellowTraveler/opentxs.  Justus is an expereinced protocol design and C++ architect/developer, withe expertise in crypto and blockhain.  Justus is the inventor of BIP-47 and has been working with the OT libarary in Lead Architrect roles at Monetas, Stash Crypto, and Rune Wallet since 2015.  Prior to attending the Univesrity of Texas, Justus was a Nuclear Reactor Operator in the US Navy for 8 years.

Justus and Mehow and friends will be supervising a team of 13 additional staff.

## Project deliverables
* PacketCrypt proof checking library
  * New open source software
    * [LGPL-2.0-only](https://spdx.org/licenses/LGPL-2.0-only.html) OR [LGPL-3.0-only](https://spdx.org/licenses/LGPL-3.0-only.html)
    * The maintainer of this software will be: Caleb James DeLisle
    * The software will be hosted in: https://github.com/cjdelisle/packetcrypt_rs/tree/master/packetcrypt-dll
* PKT Electrum
  * New open source software
    * [MIT](https://spdx.org/licenses/MIT.html)
    * The maintainer of this software will be: Caleb James DeLisle
    * The software will be hosted in: github/pkt-cash/pkt-electrum
* Rune Wallet
  * Contributions to existing open source software: https://github.com/FellowTraveler/opentxs


## Success criteria

* S_ELECT_1: Person able to receive and spend PKT with Electrum wallet
* S_ELECT_2: Electrum wallet verifies PacketCrypt Proofs to ensure the chain is valid
* S_ELECT_3: Person of technical ability able to operate an ElectrumX server for PKT chain
* S_ELECT_4: Person able transact PKT off-chain using Electrum wallet with Lightning Network payment channels
* S_ELECT_5: Windows and OSX binaries of PKT Electrum wallet
* S_RUNE_1: Person able to send and receive PKT using Rune wallet
* S_RUNE_2: Rune wallet verifies PacketCrypt Proofs to ensure the chain is valid
* S_RUNE_3: Person able to transact PKT off-chain using Open Transactions notary servers
* S_RUNE_4: Windows and OSX binaries of Rune wallet

## Milestones

### Milestone -1 (pre-project effort)
Before the beginning of the project, ther has already been work done on:
* https://github.com/cjdelisle/packetcrypt_rs/tree/master/packetcrypt-dll
* https://github.com/cjdelisle/electrumx/tree/pkt
* https://github.com/cjdelisle/pkt-docker-electrumx

In addition, initial work on PKT Electrum has been completed, the intellectual property is owned by Gridfinity LLC who has made binaries available for review and evaluation but with NO WARRANTY https://drive.google.com/drive/u/1/folders/1s4uX7D29bSEq8qUhAznY0sbkBv0L-a2A

### Milestone 0 (Kickoff)

After the project is accepted, the Network Steward will pay **10mn** PKT

### Milestone 1

#### Success criteria
Electrum release with S_ELECT_1,S_ELECT_2,S_ELECT_3,S_ELECT_5 (all feature except Lightning Network support). Windows/OSX and Linux binaries and source code made available.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.

### Milestone 2
Rune wallet release with S_RUNE_1,S_RUNE_2,S_RUNE_4 (all features except off-chain transacting with Open Transaction notaries). Windows/OSX binaries and source code made available.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.

### Milestone 3
Releases of Electrum and Rune wallet with off-chain support (S_ELECT_4,S_RUNE_3)

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send **10mn** PKT.


## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I
intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
  1. [x] An organization is receiving the funds
    1. [x] Organization has financial relationships with one or more reviewers: *Caleb James DeLisle* and *Adonis Gaitatzis*
    2. [ ] Organization has no financial relationships with any reviewers
  2. [ ] An individual is receiving the funds
    1. [ ] Individual works for same organization as one or more reviewers: *specify whom*
    2. [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [ ] Project results will present information which might lead to PKT price speculation
    * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially misleading the public.
  2. [x] Project results will not present information which might lead to PKT price speculation

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

### November 26, 2020
Project accepted and initial payout of 10mn PKT made in transactions:

[1](https://explorer.pkt.cash/tx/9438073c35eb5ac9b2479c8e0845bfc3cdd4005522a57fab2c3aeba28ff25326)
[2](https://explorer.pkt.cash/tx/420496df5bd611300ad2319653e4421c3630dd9854ccce097f0c115edab085e1)
[3](https://explorer.pkt.cash/tx/c1214b65bb83547d70c19b73a5ea859341eccd5827064bdfd2d2ffbba715d738)
[4](https://explorer.pkt.cash/tx/73a365fd70f5651172d9b405396ff65d3cf5d1b478dbc9eeca88eb816f6516f1)
[5](https://explorer.pkt.cash/tx/b1ea5377e3c4f3d9805161eca4b112a120f30adcd26e6c516101250ce476caf5)
[6](https://explorer.pkt.cash/tx/7d01eab27acbc943fd930fb5a0979588a14802a07395ae59b98f0ef3d64ee1fe)
[7](https://explorer.pkt.cash/tx/e4a5639dd6e9e67f1b5d6e9bed14ba7048a94dc11066c43e94665447f8d14607)
[8](https://explorer.pkt.cash/tx/fa492dd992835c9c9efe237974acef03ec38aa67371579c337988ed4a04bf9d0)
[9](https://explorer.pkt.cash/tx/9e3d3428ac503182a55b73951273f1fb34e4b84d8017d95a2c85e11bc16c61eb)
[10](https://explorer.pkt.cash/tx/b339f7a15a73b4ca069cdd8995d957d9c7f79cb31cc67c7d3d01949782329c04)
[11](https://explorer.pkt.cash/tx/7e051041b7b10c3cf44824c53de24ce776bab4bb77d0cd169bfbc8a5184f048b)
[12](https://explorer.pkt.cash/tx/62689cddb46503934fcb62b810f0f42053ff636f7644144689b803ef46b5508a)
[13](https://explorer.pkt.cash/tx/51e3ff3845ebbb76abc5d8a41d98da1d142c1a41f41ab14961be81c7ccdea397)
[14](https://explorer.pkt.cash/tx/551028b5cd5d09dac4e5301e378c54f1653efc087fbc35456a981251eaa3a257)
[15](https://explorer.pkt.cash/tx/2a4635c796fd7d3f29dd6661db901e2ebaa1646a197597c775fbc3c8a9e33048)
[16](https://explorer.pkt.cash/tx/c55d91965ec282fd1c5022b44dbcd2b54830bbcca16e5474a116deb6cc925233)
[17](https://explorer.pkt.cash/tx/9f8a4afab395ca2c57f513d97cd7f2ba53c55e3d8ed42a74ae9d221b04c795dd)
[18](https://explorer.pkt.cash/tx/db81838eaf9e56a8af2c411ee435bdaf182b1c5442344a3fb912e7f53b8d9f8d)
[19](https://explorer.pkt.cash/tx/c5a7667d2f1a9e839b8b3267a00fcaef55fcf38b614968403a6890fb575c0f45)
[20](https://explorer.pkt.cash/tx/a3868414c44f870aad5f2de1636023a4e23fe604399aff6acb3128541d0da741)
[21](https://explorer.pkt.cash/tx/daa67fcf1858995f215d95a1b76ff45058353f371eb0fd6a81c9b46b137ef246)
[22](https://explorer.pkt.cash/tx/6666315965bbc80371901b62de70df360ec1029b7ac941e8042b6f91848102d5)
[23](https://explorer.pkt.cash/tx/fa0ae4cbbad61578f6f7fa730d6d5520951b47dfb94dca7d330734c078869b7b)
[24](https://explorer.pkt.cash/tx/393b9c7e98754a9d0ab31e59659dcb2ca062d768556a283d9259a7f773b671de)
[25](https://explorer.pkt.cash/tx/909e6fc4bb8b15ceddd5d4bef0bbc5c51b6203bf49b50ae7b481a1ba5600e91b)
[26](https://explorer.pkt.cash/tx/8761bcb60c42d4a4ce6fbda01144eaf504ebf243ddf0193d38e04d242e384a7f)
[27](https://explorer.pkt.cash/tx/b931a3e15dfc09280a982b7b0e0f214a5c4ff84530fbfe2ee10656a2ef4ce3af)
[28](https://explorer.pkt.cash/tx/afeed450a40c6ce25b486efe093cacad375b5e81599fd53d2203eea1f6f69580)
[29](https://explorer.pkt.cash/tx/256c76b3fe5352559f69fe24559f1c977359b07986c4b0a7985f525fbef6453c)
[30](https://explorer.pkt.cash/tx/ec635d2beed904dc6df0f794b2275b3956760fedde461553c2394e1f0255c29e)
[31](https://explorer.pkt.cash/tx/b8fe1c34593969cd9c6806a09f349f70e1dc641d4a6a7ecf675944b14b00ca29)
[32](https://explorer.pkt.cash/tx/dd3e4a6e61526ac511d928f06ede703e3d70662660fb50d99d1cad88d33d740c)
[33](https://explorer.pkt.cash/tx/f1196bbe5502bf09d1b04406da53751a930d8f865d8fa0add07059d87440f8da)
[34](https://explorer.pkt.cash/tx/ae57482857853498b48157b6f63555c6f57741607299276796712ad966ac4836)
[35](https://explorer.pkt.cash/tx/b8eb5875a35617b49bca1beac86c318e77d3d2d5815bebec6c12aeb048fdc518)
[36](https://explorer.pkt.cash/tx/3625fc8eff7e54333ba4f98abe3e533c89a1a761487fd0c635544be0ce53d0bf)
[37](https://explorer.pkt.cash/tx/c2fa401988215790498502e79641c3130dc046e28e55d32fa9a9383bbffad6ab)

### Milestone 1 - Nov 23 2021

> Electrum release with S_ELECT_1,S_ELECT_2,S_ELECT_3,S_ELECT_5 (all feature except Lightning Network support). Windows/OSX and Linux binaries and source code made available.

* S_ELECT_1: Person able to receive and spend PKT with Electrum wallet
  * See instructions https://docs.pkt.cash/en/latest/electrum/
* S_ELECT_2: Electrum wallet verifies PacketCrypt Proofs to ensure the chain is valid
  * Logic for doing this is here: https://github.com/cjdelisle/electrum/blob/pkt-4.1.x/electrum/packetcrypt.py
* S_ELECT_3: Person of technical ability able to operate an ElectrumX server for PKT chain
  * Packaged in easy to deploy docker container: https://github.com/cjdelisle/pkt-docker-electrumx
  * One indepenedent community electrumx server is currently running: `electrumx.randgen.xyz:64767`
* S_ELECT_5: Windows and OSX binaries of PKT Electrum wallet
  * Windows, Mac and Linux versions linked from here: https://docs.pkt.cash/en/latest/electrum/
