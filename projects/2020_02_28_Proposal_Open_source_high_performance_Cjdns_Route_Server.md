# Open source high performance cjdns Route Server # 
* Project Name: Open source high performance cjdns Route Serve
* Contact Email: alexlightman@me.com
* Project participants:
  * Alex Makeev 
  * Sergey Prilutskiy
  * Rust developer
* Projected duration: 5-7 months
* Projected effort: 10 person/months
* Requested PKT contribution: 30M PacketCrypt tokens (3M tokens per man month)
* PKT address: pKHsMf6Eg8YB2jTJUpdRbCj7RpvpMpYRkU
* Project status: ACCEPTED



## Project participants ##
 
### Alex Makeev ###
"Graduated from Bauman Moscow State Technical University. 
 
18 years of programming experience (Assembler, C / C
++, Java, PHP, Perl, Python, JS, Rust, Solidity). Experience in developing Big
Data solutions of an industrial-scale Hadoop cluster.  
Worked as a Development Team Lead of
Search @mail.ru  (Top Russian Internet Company, listed at LSE, Internet search engine project). Worked as a System Architect in 1C company (SAP competitor). 
 
Areas of expertise: blockchain, Big Data, distributed computing, information security. "
 
### Sergey Prilutskiy ###
"Graduated from National Research Nuclear University """"Moscow Engineering Physics Institute"""" (MEPhI). 
Was engaged in reverse engineering, software protection and antivirus work research. 23 years of programming experience
(Assembler, C / C++, Perl, Python, JS, Rust, Solidity). 
 
Worked at Mail.Ru Group as a Leading Developer of various projects, and as a member Antispam team. Dealt with various systems
(from small high-load microservices and sites to large clusters for distributed computing).
 
Lecturer and author of the InfoSec course for Technopark (Bauman MSTU), MEPhI and NES (New Economic School).
 

### Rust developer ###
Graduated from Bauman Moscow State Technical University.  
 
3 years of blockchain experience, 4 years of C++\Rust development in system programming. 
 
Previously was engaged into fintech and dynamic disassembling.
 
Areas of expertise: decentralised protocols\consensus development, DeFi, data oracles. 

## Project summary ##

Create open source high performance cjdns Route Server in the PKT network. PKT ecosystem includes a special broadcasting network and a protocol, that can be used for building decentralized VPN services and Web 3.0. PKT team is going to create a worldwide online community of PKT protocol adopters and unite all supporters of decentralized web. Also PKT is a bandwidth market based on cjdns protocol, which rewards its members for bandwidth delegation. 

## Project deliverables ##
This project will deliver new open source software which will:
* Be licensed GPL-3.0-or-later
* The maintainer of this software will be: ___
* The software will be hosted in: https://github.com/<where> or in https://github.com/pkt-cash/ if the Network Steward prefers.

Note on delivery: the team 
* would plan to set up the software development process in two week long spring
* would be ready to discuss the current spring results and plans for next sprint every two weeks with the Stewards and other stakeholders



## Success criteria ##

Verify that performance of cjdns Route Server has significantly increased.
 
## Milestones ##
Creation of open source cjdns Route Server with high performance. Here are milestones for the progress of the project by which the network steward can evaluate the success of the project.

### Milestone 0: Kickoff
At the beginning of the project, the Network Steward will pay out 6M of PKT to the applicant.

## Milestone 1: Development of Rust libraries ##
Features expected to be completed include rust versions of cjdnsadmin, cjdnsann, cjdnskeys, cjdnsniff, and cjdnsplice

Upon the completion of this milestone, a report will be made for the Network Steward and if the Network Steward accepts this report, 6M of PKT will be paid out.

## Milestone 2: Rust version of cjdns node ##
Rust version of cjdnsnode should have these features:
* able to pull from another node (implement peer.js)
* has an implementation of handleAnnounce that verifies the announcement and returns a correct stateHash
    * implements the `/dump` http endpoint from cjdnsnode
    * uses threads to the greatest extent practical, with consideration to the fact that it may be interconnected with many peers sending large amounts of data

Upon the completion of this milestone, a report will be made for the Network Steward and if the Network Steward accepts this report, 6M of PKT will be paid out.

## Milestone 3: Evolution of Rust version of cjdnsnode ## 
Complete evolution of Rust version of cjdnsnode including:
* onSubnodeMessage implementation supporting 'pn', 'gr' and 'ann' messages
* `/ni` and `/walk` http endpoints
* uses threads to ensure that:
  * multiple requests to 'gr' can be processed at the same time
  * multiple requests to 'ann' endpoint can be processed at the same time
  * requests to 'gr' can be processed in parallel with requests to 'ann'
  * re-builds of the dijkstra tree are performed in parallel and exchanged with the live tree in order that lookups are never blocked.

Upon the completion of this milestone, a report will be made for the Network Steward and if the Network Steward accepts this report, 6M of PKT will be paid out.

## Milestone 4: Iterative updates to dijkstra tree ##
Two trees are present, one of which is active and the other is being updated. Periodically, the two are switched and then the updates are re-played to the one which is now out of date.

This constitutes the end of the project, at the end of Milestone 4, a report will be made for the Network Steward and if the Network Steward accepts this report, 6M of PKT will be paid out.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Status
### March 13th 2020
First payment of 6mn PKT made in 12 transactions:
[1](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/9ee9614b37bf844f3680aff1332fa837c9d2c73dd0dcda986540966389f6a8a3)
[2](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/773ac37d5d824d502d8b84763ef2dafc9ac774c11994d76b17cd6b9ef4a340ea)
[3](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/d2205a4506a5a530d93c35c8eb9831a882637e3158631231304bd6b9562a7e9f)
[4](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/7b1d648ec6fb2148275a04e29c3c0ba1116d2aa18efc9ebae95805754b5d2bd6)
[5](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3189715a68d9e90718f9483a9baa978652a8219f4d04ace94033d2924e5dcd22)
[6](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/cd6dc53839b9a71267ee1ba78875cf4b565a770523a9d7747e67596e2ab62277)
[7](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/4aa07ffb51c408c5dae87d9d61e390eced5ebd45f5dc4f95657e265ea5659eae)
[8](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/754e2ee2dd59a1857b33bb3fd2d8221082d62f91e9701c0422f9df344f6ef0d2)
[9](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/9eca20dd8a391d0589be93449e5717571ea60cfa15762401fdd13faee6f1adad)
[10](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/3b904c3174875c7c28794fd82648d2be6b99627d7c6b904c6ece5e6d2a96640c)
[11](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/2e60f81ad7c989e2914088d74bc0be26908929f98e0783d62a70a698798c65d7)
[12](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/9ae795980be3f335100def907a45bf332a03a4d0814218007863ae82cf7d503b)