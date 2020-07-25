PKT Rune/Open Transactions Wallet

* Project Name: PKT_OTRUNE_WALLET
* Contact Email: mehowfnm@me.com
* Project participants:
Michael “Mehow” Pospieszalski (mehowfnm@me.com) 
Justus Ranvier (Justus@opentransactions.org)
Lin Fisher (linfisher@mac.com) 
* Projected duration: 3+ months, 2 architects, 2 front end developers, 11 coders
* Projected effort: 45 person months
* Pre-project effort: 0
* Requested PKT contribution: 80 million PKT
* PKT address to pay to: contact Mehow for address when approved.

## Project summary

Create a fully functioning PKT wallet desktop, IOS, and Android app with support for the PKT,Bitcoin and BCH chains and BIP 47 universal payment addresses, SLP Colored Coins and Open Transactions notaries.  The wallet will also offer secure messaging vis BIP-47.  Pls refer to our white paper here:  https://drive.google.com/file/d/18pZ44d8N1rgTtoP09_4k7hCFSpju3F14/view?usp=sharing

## Team and Past Work

Michal Pospieszalski - former profesional government and private enterprise hacker and CTO that has developed and supervised the delivery of millions of lines of code to various private and public entities since he graduated from the University of Virigina.  Formerly certified by Microsoft, Novell, Cisco, Sun and Oracle with over 70+ IT certifications.  Fluent in Java, JavaScript, Swift, C++, SQL.  In the last year delivered two IOS apps to customers.  Has been working as Presdient at Rune Wallet since January 2018.  Michal shall be the manager of this project.  Linked in: https://www.linkedin.com/in/michal-mehow-pospieszalski-1b3b4443/

Justus Ranvier - Chief architect, currently maintaing Open Transactions at https://github.com/FellowTraveler/opentxs.  Justus is an expereinced protocol design and C++ architect/developer, withe expertise in crypto and blockhain.  Justus is the inventor of BIP-47 and has been working with the OT libarary in Lead Architrect roles at Monetas, Stash Crypto, and Rune Wallet since 2015.  Prior to attending the Univesrity of Texas, Justus was a Nuclear Reactor Operator in the US Navy for 8 years.

Justus and Mehow and friends will be supervising a team of 13 additional staff.

## Project deliverables

* [ X] New open source software
    * Which license(s) which you will use:
      * [X ] MPL-2
    * The maintainer of this software will be: Justus Ranvier and Michal Pospieszalski
    * The software will be hosted in: https://github.com/FellowTraveler/opentxs.

For clarity we are elucidating how each feature will merge in with our existing crypto wallet. Existing wallet code is available for inspection at https://github.com/FellowTraveler/opentxs.

The following are bullets directly from the NS project list
•	Checking the authenticity of the blockchain by verifying the PacketCrypt proofs on a configurable number of the most recent blocks and verifying only the connectedness of all earlier headers
•	       We already have begun coding our own BitCoin wallet that doesn’t require a dedicated node to function. As such, all the blockchain verification checks are performed on the client device. Therefore, the above requirement would be met by adding additional methods to the existing client-side verification scheme.
•	Ability to issue, transfer and validate colored coins
•	       We are coding SLP support presently.
•	Ability to validate a message as signed by the current holder of a given colored coin
•	       This is already done in our messaging system.
•	Ability to offer a colored coin for sale in a swap and ability to take such a swap transaction and accept it
•	       Swaps are currently supported natively in Open Transactions.
•	Future interoperability with Lightning Network
•	        We’re supporting BTC and BCH in its entirety.
•	Compatibility with Android, iOS, Linux, OSX, Windows
•	        Rune/OT Wallet currently compiles on all those platforms.
•	Graphical, command line and library modes
•	        Native to existing wallet.
•	Low resource footprint
•	        We’re using on-client filters that don’t require a node for blockchain queries. We believe this is as lightweight as possible without offloading work to external machines which will compromise privacy.
•	Additionally – the wallet already supports BIP47 identity and traditional legacy receiving addresses. BIP47 allows for KYC/AML and send/receive of funds w/o having to generate receiving addresses:
          “The BIP-47 Payment Code is a way to format blockchain addresses so that each user can have a single, re-usable address across all blockchains, without the address itself appearing in any on-blockchain transactions, and thus cannot be observed publicly on-blockchain by any third parties, unless they have the party’s private key. Instead, the receiving addresses are calculated deterministically via “spooky action at a distance” using a Diffie-Hellman shared secret. This is a process whereby each party, using his/her own private key and the other party’s public key, is able to calculate a shared secret key, which no one else can calculate without one of the private keys. The parties also increment an index after each transfer, so there is a new blockchain receiving address calculated for each transaction between them.”
          Furthermore, the wallet already supports Open Transactions such that the wallet can store funds on an off-chain Notary and perform instantaneous transactions on Notaries of the user’s choosing.
         “The Open-Transactions (OT) project is a collaborative effort to develop a robust, commercial grade, fully-featured, free- software toolkit that implements off-blockchain transactions purely as cryptographic proofs.”
          We define an off-blockchain transaction as a group of operations on contracts capable of objectively proving balances (and changes of balance) between adversarial parties. All transactions use the same basic structure: the parties involved sign agreements which, are then countersigned by an independent notary server. Transactions are irreversible since the receipts are always formed and signed on the client side first, before being notarized by any server.
This prevents the notary from falsifying receipts since it can’t forge the client’s signature. This basic structure can be built uponto create many types of financial instruments. Those supported by Open-Transactions include:
         Transfers. An atomic movement of funds from one account to a different account, similar to a bank account-to-account transfer.
         Cash. Untraceable cryptographic tokens which can be securely redeemed by the recipient without revealing the sender
         Cheque. A payment that is not deducted from the sender’s account until the recipient claims it.
         Voucher. A payment that is deducted from the sender’s account at the time of creation.
         Invoice. A payment request which the recipient can opt to pay from any of his accounts.
         Market Offer. An open agreement to exchange a given quantity of one unit type for a given quantity of another unit type.
         Recurring Payments. An agreement between two parties that includes an optional initial payment, followed by a set number of additional payments over a specified period of time.
         Smart Contract. A customizable agreement between multiple parties, containing user defined scripted clauses, hooks, and variables.”
         
Please see attached white-paper https://drive.google.com/file/d/18pZ44d8N1rgTtoP09_4k7hCFSpju3F14/view?usp=sharing on the BIP47/OT ecosystem which explains Notaries in depth. Presently all functionality is available except for the Voting Pool.


## Success criteria

The Network Steward should evaluate the success or failure of the Rune project by
•	Users will be able to access balances and transfer PKT,BTC,BCH on chain to other users and transfer it to OT (Open Transaction) notaries using standard receive addresses and BIP-47 via command line and UI.  Users will be able to securley message each other.
•	All functional requirements will operate as proposed and within required parameters - see above list for planned features.

# Milestones

The following are milestones for the progress of the project by which the network steward can evaluate the success of the project. The goal of these milestones is to work towards building features that unlock future work throughout the project.

# Milestone 0 - Kickoff

Instructions: We begin development of a test app with a completed wallet UI supporting BIP-47, OT Notaries (for off-chain transactions) and PKT, BCH, BTC for on chain transactions. In addition, we will simultaneously work on adding PKT support into the OT wallet.
The coin cost for this milestone will require 5M PKT

# Milestone 1 - 1 Month
At this point, a user will be able to … Navigate the basic desktop Wallet UI including:
-	Initialize / seed their wallet or restore from previous secret words.
-	See their on-chain PKT balance.
-	See their off-chain PKT balance on a OT Notary.
-	Create a on-chain PKT transaction by inputting another user’s receive address.
-	Create a off-chain instant PKT transaction (“swap”) with another BIP-47 user via OT Notary.
-	Securely chat with other BIP-47 PKT users.
-	Perform above transactions on BCH and BTC.
-	Perform all the already implemented OT transactions that are available on a Notary on PKT, BCH and BTC.
The coin cost for this milestone will require 25M PKT

# Milestone 2 - 1 Month
Working command line wallet and progress on IOS, Android, Mac, PC GUI Wallets.
At this point a user will be able too:
-	Perform the above functionality from command line (except for the BIP-47 chat)
The coin cost for this milestone will require 25M PKT

# Milestone 3 - 1 Month
Working GUI wallets. At this point a user will be able too:
-	Perform the above functionality with the GUI on IOS, Android, PC and Mac.
-	Additionally perform SLP token (“colored coin”) transactions via both command line and GUI.
The coin cost for this milestone will require 25M PKT

## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I
intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
  1. [ X] An organization is receiving the funds (RUNE Wallet - a Texas Public Benefit Corporation)
    1. [ ] Organization has financial relationships with one or more reviewers: 
    2. [X]  Organization has no financial relationships with any reviewers: 
  2. [ ] An individual is receiving the funds
    1. [ ] Individual works for same organization as one or more reviewers: *specify whom*
    2. [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [ x] Project results will present information which might lead to PKT price speculation
    * Rune Wallet will not keep the development of the "fancy PKT" wallet a secret.  The development will be available for inspection on GitHUB.
  2. [ ] Project results will not present information which might lead to PKT price speculation

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

Pardon any typos - Mehow
