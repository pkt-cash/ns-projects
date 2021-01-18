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

Submitted
