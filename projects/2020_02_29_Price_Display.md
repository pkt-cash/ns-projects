# PKT Price-Display Project
* Project Name: PKT Price-Display
* Contact Email: jeff@gridfinity.com
* Project participants:
  * Jeff Johnson - Project Owner (jeff@gridfinity.com)
  * Vishnu Seesahai - Assistant Project Owner (vishnu@gridfinity.com)
  * Armand Gilbert
  * *Other participants will be added as needed*
* Projected duration: 1 month
* Projected effort: 1.5 person-months
* Requested PKT contribution: 8 million PKT
* Project status: **PROPOSED**

## Project summary
We propose to create a website that displays the price of PKT in US Dollars in quasi-real time by using the seigniorage method.

[TOC]

## 1. Project Relevance to the PKT Network

PKT is a [crypto-incentivized mesh network](https://www.gridfinity.com/how-to-build-a-decentralized-web/), and the incentive of the cryptocurrency relies on its ability to be used as a [Medium of Exchange](https://www.investopedia.com/terms/m/mediumofexchange.asp), and represent a standard of value. For this reason, calculating the value of PKT is relevant to validate its use as a Medium of Exchange, supporting PKT network to grow as a crypto-incentivized network. 

For this project, we will calculate a standard of value of PKT cash in US Dollars. The price of a cryptocurrency in US Dollars can be determined in two ways:

* **[Market Supply and demand](https://www.investopedia.com/tech/what-determines-value-1-bitcoin/)** to exchange the cryptocurrency for US Dollars.
* **[Seigniorage](https://www.investopedia.com/terms/s/seigniorage.asp)**.

As of today, there is no publicly available record of the use of PKT in exchange for US Dollars, and there is no PKT crypto exchange; therefore, the only way to determine the price of PKT is by the seigniorage estimation, but this project will eventually expand in scope to record P2P sales.

We propose to create a website that displays the price of PKT in US Dollars in quasi-real time by using the seigniorage method.

> "The reward for creating a block that adheres to the rules is a [payout](http://pkt.cash/), or cryptocurrency" (...) "Early adopters of a crypto-incentivized mesh network, stand to gain the greatest returns from the ensuing bandwidth gold rush." <br> — [Vishnu J. Seesahai](https://www.gridfinity.com/how-to-build-a-decentralized-web/)

## 2. Project Deliverables
The key deliverable will create new software for the front-end and back-end for a PKT Price Display website.

### 2.1 Seigniorage Method

This calculation is a seigniorage price for PKT Cash using a known Gridfinity miner as a reference hardware device. This calculation is not the average seigniorage pricing across the network. The distinction here is that the hashrates per watt of other types of hardware mining devices were not weight averaged against known Gridfinity mining prices. 

#### Example:

Price / Coin **=** Hashes / Block **x**  Block / Coins **x** KW / Hash **x** Price / KW

**hr** = hash rate<br>
**s** = seconds<br>
**D** = difficulty<br>
**C** = coins per block = (roughly 3300 at current time)<br>
**dt** = change in time, or time elapsed

* **Hashes / Block = 4096:**<br>
D = hr X dt or  hr = D / dt =>hr = D / 60s<br>
(hr) X s / C = (D / 60s) X 60s / C =  (D / 60s) X 60 / 3300

* **Use RPCs to get D and C:**<br>
D = result of getDifficulty RPC<br>
C = result of getCoinbase RPC, (roughly 3300 at current time)

* **Therefore:**<br> 
Block / Coins = 1 / 3300 <br>
KW / Hash = **.00001 KW/Hash** <br>
**Note:** This depends on the hardware efficiency. We can assume that the majority of nodes are gridnodes and know how much energy is spent on a hash. Currently: 90Hashes / Watt (on gridnodes) or **.01 Watts/Hash = .00001 KW/Hash**

* Price / KW =**.12 / KW** <br>
**Note:** This will depend on local energy prices, we can use a mean (average) to estimate this. Average price per KW in USA is **.12 / KW**, for example.


**Full Calculation Example:<br>
.00001 X .12 X 4096 / 3300 =<br>
.0000012 or 1/ten thousandth of a penny = <br>
.00012 / penny**

### 2.2 Wireframe

The following image is a wireframe of the website for illustration purposes. The design and location of the features may differ in the final version.

<div style="max-width:500px" align="middle"> <div style="max-width:80%"> <img src="https://tfeed.gridfinity.com/PKT_Price_Display.png" width=80%> </div> </div> <br>

### 2.3 Milestones
The following are milestones for the progress of the project by which the network steward can evaluate the success of the project.

* [ ] **M0 - Kickoff**
<br> At the kickoff of the project, the network steward will grant 2 million PKT to the applicants, and the project will begin.

* [ ] **M1 - Complete version**
<br> Milestone 2 will be achieved when the algorithm to calculate the price is developed and can be used used to display the price in quasi-real time on a website domain. Upon completion of Milestone 2, a report will be written, and the applicant will seek approval from the network steward. Upon approval, payment of 6 million PKT will be issued. At this point, the development stage of the project will conclude.


### 2.4 Development overview

* The deliverables are a new website. The website domain will be defined during the development stage.
* The software will be available under the [ISC](https://opensource.org/licenses/ISC) license.
* All artistic non-software assets will be available under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
* The maintainer of this software will be: Jeff Johnson
* The website may include banners linking to other resources related to the PKT network, such as [Gridfinity](https://www.gridfinity.com/) or a wallet service.
* We will define the programming language during the development stage. We estimate that, most likely, the majority of the development will be PHP and HTML.
* The software will be hosted on https://github.com/pkt-cash, if the network steward wishes it so.


### 2.5 Team qualifications
* **Jeff Johnson** is a UNIX system admin. He's built cjdns-based urban distributed mesh networks used in production in South Florida.

* **Vishnu Seesahai** is a mathematician and researcher specializing in engineering innovation across global markets, with a focus on stochastic processes, computing, and blockchains. He is also the founder of Healthmatica, a public benefit health tech. He is a graduate of Cornell with a BS in Computer Science and MS in Applied Mathematics from the Theory Center for Advanced Computing. He formerly served as SSWE at Ovid, the first health-tech company to offer full-text search of medical databases, and later CTO of Pixelpark AG, a subdivision of Bertelsmann. He is also the co-creator of the first DVAV (Digital Video Audio Village), purchased by Lionsgate Entertainment, which is currently in use on film/tv productions within their ecosystem.

## 3. Success Criteria
* At least one successful independent installation of the PKT Price Display.
* At least 90% achievement of the described features.

## 4. Payments
Each payments shall be distributed to the following address: `pkt1qwqhe6zw7ylfdcw2genxptw70duk7u8d52q9jwy`

## 5. Legal
The applicant understands that the network steward is not a legal entity, and no part of this project constitutes any form of legal agreement. The applicant accepts that the network steward exists thanks to the effort of volunteers, and the applicant has no reasonable expectation of any action, payment, or communication from the network steward at any time. For their part, the applicant has no binding commitment or obligation at any time as a result of their participation in this project.

All products and services to be provided by Jeff Johnson and Vishnu Seesahai (collectively referred to as "Team") are provided “as is” without any warranty whatsoever. Team expressly disclaims all other warranties, terms or conditions, whether express, implied, or statutory, regarding their products and services, including any, warranties of merchantability, title, fitness for a particular purpose and infringement. No representation or other affirmation of fact, regarding the products and services Team provide, shall be deemed a warranty for any purpose or give rise to any liability of Team whatsoever.

In no event shall Team be liable for any incidental, indirect, exemplary, special, punitive or consequential damages, under any circumstances, including, but not limited to: lost profits, revenue or savings, or the loss, theft, transmission or use of any data, even if the PKT Network Steward or Team have been advised of, knew, or should have known, of the possibility thereof, and even if the event is caused or alleged to have been caused by Team, or by the performance or nonperformance of any products or services Team provides.
