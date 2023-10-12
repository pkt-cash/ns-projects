

# PKT Cash VPN Utility Project

*   Project Name: pkt_utility (Project)
*   Proposal by: Anode, LLC
*   Contact Email: [jesse@anode.co](mailto:jesse@anode.co) 
*   Project participants:
    *   Adonis Gaitatzis
    *   Jeff
    *   Josh Berger
    *   Jesse Berger
    *   Jon Owens
    *   _Other participants will be added as needed_
*   Projected duration: 12 months
*   Projected effort: 16 person-months
*   Requested PKT contribution: PKT 30,000,000
*   Project status: ACCEPTED

## Project summary

PKT is a novel blockchain with immense potential. Its incentivization for providing bandwidth to the network will help PKT Cash become a public commodity. But in order for this coin to not be another speculative coin it needs to have a utility. And not just any utility, but one that helps its mission be realized. 

The project I propose is to create the first VPN application that uses PKT Cash as its fuel. This VPN will allow users to get base-line VPN for free and only pay for speed using microtransactions with PKT Cash. 

This project will be iterative as we leverage open-source technology to create a dynamic application. This first proposal of this application will be to create the VPN functionality that leverages the cjdns exit nodes for VPN access points. We will develop this application for Android to start with the intent to expand to IOS and desktop in additional proposals to come. 

Additionally, a website will be created for this new VPN, aimed at both operators and consumers. The website will educate users about the utility and use cases of the VPN, encourage downloads, and provide machine-to-machine services for both the VPN server and the Android app.

Looking into the future, our goal will be to incorporate Gridfinity, OpenVPN, Yggdrasil, and others as exit nodes in this VPN application. But those will come in subsequent proposals. Also the pay-for-speed functionality will be developed in our next proposal to the Network Stewards.

## Who we are and why us?

Our team consists of VPN and security experts who specialize in network routing, VPN, core internet infrastructure, and open-source technology. Our team has vast experience with everything from cjdns to running TOR exit nodes. We understand the ecosystem and know how to bring the value needed to make it a success. 

## Release Schedule and Budget

The VPN project will be created and deployed in stages. Each stage will be implemented in an order that most benefits the creation of a loyal community of users whose needs mature alongside the release of new features.

The project will consist of a VPN server, a client Android app, and a website for both the server and client, each targeted at is users.

The VPN server and its website will be designed for VPN operators who want to create a VPN server that routes traffic on the cjdns network. The server will allow inbound connections, will give a virtual IP address, and route traffic. Its website will encourage downloads and adoption, and will provide documentation and education about the VPN and cjdns.

The client app and its website will be designed for VPN consumers who want to connect to VPNs from their phone. The app will list and suggest VPN servers that support cjdns and will allow users to select and connect to these VPN servers. Its website will encourage downloads and adoption, and will provide documentation and education about the app and cjdns.

### Server

The version 1 VPN server will be a Docker container that runs a cjdns-powered VPN server. This VPN server will be used to encrypt and route traffic for consumers of the VPN service. It will compete with existing VPN services, so as to create utility for PKT using an known business case with existing user demand. 

 

The VPN server app can be deployed on Linux, so it can provide service from home and office users in rural areas as from server farms near urban areas. For adoption, a client app and a back-end server are both required

The VPN will attempt to auto-configure for the fastest VPN, thereby providing the best possible network speed to the user. The user can configure their own network settings if they so desire. A social-invite tool will be integrated to allow users to share pre-configured client software with friends, family, colleagues, or clients.

The VPN software will be deployed alongside a back-end server and an informational website that educates operators about the utility and use cases, and encourages them to download and install the VPN.

The Back-End Server will need to host REST or graphql APIs for use with an Informational Website and client App, providing:


*   VPN and other server lists
*   Send notifications to users
*   Account management
*   Other features

A draft specification of the REST API can be found in [Appendix 1: API Proposal](https://docs.google.com/document/d/1-QEdFw-z0rwtemDsOhp0X_o_A3BIq_SM4bsqn5wa4yE/edit#heading=h.vein41r07pcn).

The time estimate for the Back-End server is as follows:


|Total|Est. Hours|Est. Cost|Est. PKT|
|--- |--- |--- |--- |
|Development Time|211|$25,320|843,990|



A full feature/cost breakdown is listed in [Table 1: Server Development Cost Estimate](#heading=h.d07x5bgfcgye).

The Informational Website will need to:



*   Educate consumers and encourage adoption
*   Describe the utility of the VPN App and link to a download location
*   Allow users to manage their account
*   List VPN servers including their bandwidth usage and cost
*   Send transactional emails to users

The time estimate for the Informational Website server is as follows:

|Total|Est. Hours|Est. Cost|Est. PKT|
|--- |--- |--- |--- |
|Development Time|1007|$120,844|4,028,133|


A full feature/cost breakdown is listed in [Table 2: Server Website Development Cost Estimate](#heading=h.1x40ff2reqqd).

Additionally, a project manager will be required to manage the development of these features. Assuming the Android, Website, and Server are developed concurrently at a rate of $120/hour, the project management estimates are as follows:

|Total|Est. Hours|Est. Cost|Est. PKT|
|--- |--- |--- |--- |
|Development Time|1007|$120,844|4,028,133|


### Client

The client app version 1 will be a user-friendly, auto-configuring VPN client uses cjdns protocol to route traffic and PKT to value bandwidth. It will compete with existing VPN clients, so as to create utility for PKT using an known business case with existing user demand.  

The VPN app will be deployed on Android. The React Native user interface framework will be used to create a single UI framework that allows for future scaling of the VPN client onto other platforms such as iOS. For adoption, a front-end UI and a back-end server (also proposed) are both required.

A social-invite tool will be integrated to allow users to share pre-configured client software with friends, family, colleagues, or clients.

A client-side Android app is a top priority because:

*   Apps have enhanced visibility and sharing via the on-platform app marketplace.
*   Android users tend to install more apps, especially free and experimental apps
*   Android users tend to be more technology-focused

The client Android App will need to to:


*   Send/Receive data to Server API
*   Receive alerts
*   Integrate cjdns, into Android network stack
*   Enable users to create and manage their accounts
*   Configure their VPN settings

Wireframe mock-ups for the Android App can be found in  [Figure 1: Client App Wireframes](#heading=h.dwmlo5m2luqq).

The time estimate for the client Android App is as follows:

|Total|Est. Hours|Est. Cost|Est. PKT|
|--- |--- |--- |--- |
|Development Time|1,793|$215,217|7,173,913|


A full feature/cost breakdown is listed in [Table 3: Android App Development Cost Estimate](#heading=h.s01qk5c2x8eh). 

The VPN software will be deployed alongside an informational website that educates potential users about the utility and use cases, and encourages them to download and install the App and manage their account.

The Informational Website will need to:

*   Educate users and encourage adoption
*   Describe the utility of the VPN App and link to a download location
*   Allow users to manage their account
*   List VPN servers including their bandwidth usage
*   Send transactional emails to users

The time estimate for the Informational Website server is as follows:

|Total|Est. Hours|Est. Cost|Est. PKT|
|--- |--- |--- |--- |
|Development Time|738|$88,619|2,953,964|

A full feature/cost breakdown is listed in [Table 4: Client Website Development Cost Estimate](#heading=h.iepkrs1guano).

Additionally, a project manager will be required to manage the development of these features. Assuming the Android, Website, and Server are developed concurrently at a rate of $120/hour, the project management estimates are as follows:

|Total|Est. Hours|Est. Cost|Est PKT|
|--- |--- |--- |--- |
|Website Development Time|738|$88,619|2,953,964|
|App Development Time|1,793|$215,217|7,173,913|
|Project Management Time|2,532|$303,836|10,127,877|
|Total|5,064|$607,673|20,255,754|

### Total Project

Altogether, These two projects come together to make a VPN ecosystem of independent VPN operators and a global community of VPN clients, all using the PKT network to secure and route their traffic. 

The creation of this ecosystem enables future development which can incentivize the use of PKT Cash to buy and sell bandwidth on that VPN network, thereby creating utility and value for PKT cash.

The total cost for this project is as follows:

|Total|Est. Hours|Est. Cost|Est PKT|
|--- |--- |--- |--- |
|Server Software and Website|2,436|$292,327|9,744,245|
|Android App and Website|5,064|$607,673|20,255,754|
|Total|7,500|900,000|30,000,000|

# Project Deliverables

The key deliverable will be a VPN server and Android client app, as well as a website for each.

These deliverables are:

*   New open source software
*   Which will be available under the [MIT](https://spdx.org/licenses/MIT.html) license
*   The maintainer of this software will be: Adonis Gaitatzis
*   The software will be hosted in [https://github.com/anode-co](https://github.com/anode-co)

# Payments

All payments shall be made to `pkt1q9w78py6w9dprzajquw3ngenr826gsveu4c5x50`

# Milestones

The following are milestones for the progress of the project by which the network steward can evaluate the success of the project.

The goal of these milestones is to work towards building features that unlock future work throughout the project. Features such as database management and the network connectivity enable the next features such as the ability to create and manage user accounts from a central server, which in turn enable login-based features such as per-user bandwidth tracking.

As the VPN server and Android app work together, developing and testing features side-by-side is critical for developing a successful product.

## M0: Kickoff

At the kickoff of the project, the network steward will grant PKT 10,000,000 (1/3 of the project budget) to the applicant and the project will begin.

*   Hiring and Project Planning


## M1: Specifications

Milestone 1 will focus on sketching out how the various parts will look and function together. This will include wireframes, initial designs and mock-ups, and an initial API specifications and documentation.

Upon the completion of Milestone 1, a report will be written and the applicant will seek approval from the network steward. The network steward will pay PKT 5,000,000 (⅙ of the project budget) for the completion of this milestone.

**Progress:**

At this stage there will be:

*   Design specifications, clickable mock-ups, and preliminary documentation but no functioning code.


### Server/API

API Spec


### Server Website

Design


### Client App

Wireframes


### Client Website

Design


### M2: I/O, Transactions, and Account Management

Milestone 2 will focus on the development of the core features that enable the systems to talk to one another, as well as enable users to create and manage their account and receive notifications about changes to the status of their account. This will include reading from the Android system such as network connectivity, as well as being able to send and receive Resources via a REST or graphql API.

Upon completion of Milestone 2, a report will be written and the applicant will seek approval from the network steward. Upon approval, payment of PKT 5,000,000 (⅙ of the project budget) will be issued.

**Progress:**

At this stage there will be:

*   An app and VPN server that each allow users to register and perform account management features such as changing and resetting password. 
*   However the app will not yet route traffic or enable users to connect to a VPN.


### Server/API

The server will be able to send transactional emails

A VPN operator will be able to configure their VPN server settings


### Server Website

A user will be able to log into their account

The server will be able to send transactional emails

The server will be able to read and write to an Internet Database 


### Client App

The app will be able to send and receive data via a REST API

The app will be able to store data locally in an in-device database

The app will be able to receive push alerts

The user will be able to log in via a PIN


### Client Website

The user will be able to log in to their account

The website will be able to send transactional emails


### M3: Network Integrations

Milestone 3 will focus on getting the VPN to do it’s core job of receiving connections and acting as a bridge between the traditional Internet and the PKT network. These features will include bandwidth and load monitoring as well as registering with the VPN list so that users can discover and connect to VPNs through the app.

Upon completion of Milestone 3, a report will be written and the applicant will seek approval from the network steward. Upon approval, payment of PKT 5,000,000 (⅙ of the project budget) will be issued.

**Progress:**

At this stage:

*   The app will allow users to log in and manage their accounts, connect to a PKT VPN and route traffic through that VPN. 
*   App users will be able to browse a list of VPNs and see the bandwidth and load of each VPN. 
*   VPN server administrators will have a VPN server that accepts client connections and routes VPN traffic through the PKT network, register as a public PKT VPN, and perform account management functions.  
*   Android apps users will not yet be able to auto-configure their VPN.


### Server/API

The VPN will be able to connect to, send and receive traffic through the cjdns network.

The VPN operator will be able to register their VPN on the website

The VPN will report its usage statistics to the website

The VPN will report its version to the website


### Server Website

Users will be able to browse VPNs and their statistics via an API


### Client App

The user will be able to connect to a VPN and route traffic through the cjdns network

The user will able to input VPN configurations manually

The user will be able to view statistics about their VPN usage

The user will be able to browse VPNs from a list

The user will be able to select and connect to VPNs from the list


### M4: Polish and Debug

Milestone 4 will focus on turning features into a product. Existing features will undergo integration testing and usability testing and final features will be put into place that enable users to be welcomed into the app and have the hard decisions made for them when they so desire.

Upon completion of Milestone 4, a report will be written and the applicant will seek approval from the network steward. Upon approval, payment of PKT 5,000,000 (⅙ of the project budget) will be issued.

At this point the project will reach the end of it's explicit funding, however the applicant commits to the long term maintenance of the VPN software and the network steward commits to continuing interest in the evolution of the software.

**Progress:**

At this stage:

*   VPN operators will have a reliable VPN server that performs all the functions listed in the previous milestone. 
*   Android app users will also have a stable app with no major memory leaks that performs all the functions from the previous milestone, plus enables the user to auto-configure a VPN based on their location or other preferences.

In short, the server and app will be done.

### Server/API

The user will be able to install and configure a VPN following documentation


### Server Website

The user will be able to browse the site easily and find documentation and download links


### Client App

The user will be able to select the best VPN based on location, speed, or some other criteria

The user will be presented with a welcome screen upon first run

The user will be able to share the app with friends via a social sharing tool

The user will be able to find the app on the Android Play store or on the website

The user will be able to use the app without major memory leaks or common bugs

### Client Website

The user will be able to browse the site easily and find documentation and download links


## Legal

The applicant understands that the Network Steward is not a legal entity and no part of this project constitutes any form of legal agreement. The applicant accepts that the Network Steward exists thanks to the efforts of volunteers and the applicant has no reasonable expectation of any action, payment or communication from the Network Steward at any time. For their part, the applicant has no binding commitment or obligation at any time as a result of their participation in this project.


# Table 1: Server Development Cost Estimate

|Feature|Task|Est. hours|Est. cost|Est. PKT|
|--- |--- |--- |--- |--- |
|API|VPN server list|96|$11,509|383,632|
|API|VPN version info|58|$6,905|230,179|
|API|Email users|38|$4,604|153,453|
|API|Database functionality|19|$2,302|76,726|
|Total||211|$25,320|843,990|

Costs based on an estimated $120/hour engineering and designing cost and PKT = ⅓ US Penny.

# Table 2: Server Website Development Cost Estimate

|Feature|Task|Est. hours|Est. cost|Est. PKT|
|--- |--- |--- |--- |--- |
|Website|Design informational website (roughly 10 pages)|48|$5,754|191,816|
|Website|Informational home-page|192|$23,018|767,263|
|Website|VPN/cjdns information|96|$11,509|383,632|
|Website|VPN server information (countries, line quality, etc)|96|$11,509|383,632|
|Website|cjdns server information (line quality, etc)|96|$11,509|383,632|
|Website|account management|192|$23,018|767,263|
|Website|bandwidth usage and estimates|192|$23,018|767,263|
|Website|scheduled actions such as emails to users|96|$11,509|383,632|
|Total||1007|$120,844|4,028,133|

Costs based on an estimated $120/hour engineering and designing cost and PKT = ⅓ US Penny.

# Table 3: Android App Development Cost Estimate

|Feature|Task|Est. hours|Est. cost|Est. PKT|
|--- |--- |--- |--- |--- |
|Login workflow|Design Login/logout/forgot password workflow|38|$4,604|153,453|
|New account|Design account creation workflow|19|$2,302|76,726|
|Account management|Design account management workflow|19|$2,302|76,726|
|Connection types|Design connection types workflow|19|$2,302|76,726|
|Network Auto-configure workflows|Design auto-configure VPN workflows|96|$11,509|383,632|
|Network Select from list workflows|Design select from list VPN workflows|58|$6,905|230,179|
|Custom network workflows|Design custom VPN configuration workflows|38|$4,604|153,453|
|Welcome screens|Design Dashboard/welcome screens|96|$11,509|383,632|
|Core features|Send data to/from REST API|10|$1,151|38,363|
|Core features|Implement data models and conversion to serialized formats|19|$2,302|76,726|
|Core features|Email / Text information to user (Twilio integration)|38|$4,604|153,453|
|Core features|Location finding from IP|10|$1,151|38,363|
|Core features|Approximate distance to VPN from IP|10|$1,151|38,363|
|Core features|Read, write data to local database|19|$2,302|76,726|
|Core features|read notices from API|10|$1,151|38,363|
|Core features|check for software updates in API|10|$1,151|38,363|
|Core features|Push alerts|19|$2,302|76,726|
|Core features|banner notices|19|$2,302|76,726|
|Core features|background service or networking layer|96|$11,509|383,632|
|Core features|cjdns integration|480|$57,545|1,918,159|
|Login workflow|Authenticate with wallet|38|$4,604|153,453|
|Forgot password workflow|Backup wallet seed|19|$2,302|76,726|
|Forgot password workflow|Wallet password / PIN|19|$2,302|76,726|
|Forgot password workflow|Recover PIN from seed|19|$2,302|76,726|
|Create new account workflow|Create new account|38|$4,604|153,453|
|Create new account workflow|email activation code|19|$2,302|76,726|
|Create new account workflow|Activate account during account creation|19|$2,302|76,726|
|Account management|Change PIN|19|$2,302|76,726|
|Account management|Activate account from account manager|19|$2,302|76,726|
|Log out|Log out|19|$2,302|76,726|
|Usage|show bandwidth usage for period|96|$11,509|383,632|
|Choose connection method workflow|Choose connection method workflow|58|$6,905|230,179|
|cjdns workflow|Auto-configure|192|$23,018|767,263|
|cjdns workflow|Select from list (line quality, location)|96|$11,509|383,632|
|Total||1793|$215,217|7,173,913|

Costs based on an estimated $120/hour engineering and designing cost and PKT = ⅓ US Penny.

# Table 4: Client Website Development Cost Estimate

|Feature|Task|Est. hours|Est. cost|Est. PKT|
|--- |--- |--- |--- |--- |
|Website|Design informational website (roughly 10 pages)|48|$5,754.48|191,816|
|Website|Informational home-page|192|$23,017.90|767,263|
|Website|App information|19|$2,301.79|76,726|
|Website|account management|192|$23,017.90|767,263|
|Website|bandwidth usage and estimates|192|$23,017.90|767,263|
|Website|scheduled actions such as emails to users|96|$11,508.95|383,632|
|Total||738|$88,618.93|2,953,964|

Costs based on an estimated $120/hour engineering and designing cost and PKT = ⅓ US Penny.

# Appendix 1: API Proposal

These APIs can be implemented over or CoAP. CoAp is designed for low-bandwidth, machine-to-machine communication but is compatible with HTTP and supports Quality of Service (QoS) management.

## PKT VPN Server

Node/Network discovery and configuration

An API for computers to discover nearby servers and to register themselves on the network.

Registering with the server would let the server record it’s IP address

```
POST /servers/
```

**Body:**

```
{
	"publicKey": "<public key>",
	"ipPort": ["<ip:port>",...],
	"login": "<cjdns login>",
	"password": "<password>",
	"protocolVersion": "<version>"
}	
```

**201 Response:**

## Network Stats

```
GET /servers/<ip>
```

**Body:**

**200 Response:**

```
{
	"ipv6": "<ipv6>",
	"speed": "<byte/s>",
	"latency": "<latency>",
	"droppedPackets": "<avg dropped packets>",
	"load": "<estimated network load>",
	"location": "<city, country>"
}
```

## PKT VPN Control Panel

### VPN Configuration

The nearest VPN should be found by default. The API server should keep a list of VPNs and use the user’s IP or some other information to find the nearest or fastest VPN. Maybe the user can enter their preferred location for this purpose.

From here the node that is configured to use a compatible VPN should auto-configure for this VPN.

```
GET /network/vpns/nearby/
```

**Body:**


```
{
	"location": "<city, country>",
}	
```

**200 Response:**

```
{
	[
		{
            "url": "<url 1>",
            "droppedPackets": "<% dropped packets/s>",
            "ASNumber": "<AS Number>",
            "load": "<current load>"
        },{
            "url": "<url 1>",
            "droppedPackets": "<% dropped packets/s>",
            "ASNumber": "<AS Number>",
            "load": "<current load>"

        },{
            "url": "<url 1>",
            "droppedPackets": "<% dropped packets/s>",
            "ASNumber": "<AS Number>",
            "load": "<current load>"
    },

	]
}
```

## VPN Panel Configuration

### Login

OAuth and other login mechanisms violate REST as REST is stateless. Therefore we don’t want to use OAuth or some other login mechanism. However, we can test a user’s login before proceeding and use that to build a login wall.

Login

```
POST /account/
```

**Body:**

```
{
	"authCookie": "<authentication cookie based on wallet>"
}	
```

**200 OK Response :**

```
{
	"token": "<temporary authorization token>"
}
```

**400 Bad Request (invalid email address):**

### Account Management

Create a new account

```
PUT /account/
```

**Body:**

```
{
	"authCookie": "<authentication cookie based on wallet>"
}	
```

**200 OK Response :**

```
{
	"token": "<temporary authorization token>"
}
```

# Figure 1: Client App Wireframes

![drawing](2020_02_28_pkt-vpn-uitility-wireframes.png)


## Milestone 1 Report - 2020-05-21

### Overview

This document outlines the state of progress through the completion of the milestones outlined in the approved project proposal.

### Progress
Milestones 0 and 1 are complete and ahead of schedule. We have a development team, app wireframes, API specifications, and websites to host app binaries and APIs. 

In the process of completing Milestone 1 deliverables, we have also made progress on Milestone 2 and Milestone 3 deliverables.

**Most importantly, we have [released an Android APK](https://github.com/anode-co/AnodeVPN-android) that connects a user to a PKT VPN server and allows them to surf the internet from behind a PKT VPN exit node.**

#### Milestone 0: Kickoff
Status: Complete
Date Completed: 2020-05-04

##### Proposed Deliverables
At the kickoff of the project, the project will begin hiring and project planning

##### Accomplished Deliverables
As of May 4, 2020, a team has been assembled consisting of:
-   An Android developer
-   A technical project manager
-   A designer
-   A product manager
-   Other supporting staff

#### Milestone 1: Specifications

Status: Complete

Date Completed: 2020-05-20

##### Proposed Deliverables

We have accomplished our deliverables and begun implementing Milestone 2  and Milestone 3 objectives.

Milestone 1 focused on sketching out how the various parts will look and function together. These parts include wireframes, initial designs and mock-ups, and an initial API specifications and documentation. Completion of Milestone 1 results in the submission of this status report.

The parts of the project include:

###### Server / API
* API Specification (done)
###### Client App
* Initial  Design (started)
###### Client Website
* Wireframes (done)
###### Server Website
* Initial Design (started)

##### Accomplished Deliverables

In developing the App, we’ve reprioritized the milestone slightly. We focused on
1.  Ensuring that a VPN connection between the Android OS and a PKT VPN node is possible
2.  Ensuring that debug logging and software upgrades are possible so we can monitor and resolve problems with the app
3.  Ensuring the availability of information about PKT VPN nodes so that the App can create connections
4.  A phased UI design approach where we have placeholder screens for the developers to build towards as we simultaneously work with designers to create a beautiful, intentional and frictionless UI for the app

In doing so, we have accomplished the following:  

######  Server/API

**API Specification: Complete**
We have released an [OpenAPI 3.0 compatible PKT VPN API available on GitHub](https://github.com/anode-co/api-docs/blob/version-0.2/vpn-server.yaml).  
This API can be viewed in a human-friendly format using the [RestAway API Viewer](https://backupbrain.github.io/restaway/?q=https://github.com/anode-co/api-docs/blob/version-0.2/vpn-server.yaml), where endpoint descriptions, responses, and sample code can be seen.

**API Implementation: In-progress.**
Based on the API specification, we have begun implementing a working API on the server. This server allows the client to view the list of registered VPNs, request authorization to connect to the VPN, record debugging information, and check for software updates.


##### Server Website

**Initial Design: Started/Deferred**
Instead of designing the client-facing VPN Server website, which might attract VPN operators to the project before software is available, we’ve begun implementing the [App-facing API](https://vpn.anode.co/redoc/) described in the API docs above. This API server also implements [human friendly API documentation](https://vpn.anode.co/redoc/). A more feature-rich design will be made once we are prepared to create an informational resource for users who might download the VPN server software.


**From M2: The server will be able to read and write to an Internet Database (done)**
The server is has a working MySQL database and the ability to read and write data to it. Using a functioning API, the client is able to create, read, and delete data from this database remotely.


**From M3: The VPN will be able to connect to, send and receive traffic through the cjdns network. (done)**
The app can do exactly this. 


###### Client App

**Wireframes: Complete**
We have created a full, click-through suite of wireframes and [prototype mock-ups](https://anode.invisionapp.com/overview/Anode-VPN-App-ck9yato6x0bjt014s6j09h2on/screens?v=ARI695yFBSe73XQATpZEbw%3D%3D&linkshare=urlcopied) which the developer is using to implement a design while another designer is re-envisioning the app with an eye for the customer experience.

**App: In-progress**
We have created a prototype Android App that connects to a PKT-powered VPN, which is able to route traffic. The App is able to surf the Internet via the VPN connection. It also sends a debug log through the server API. **An Android apk binary has been created and is [available for download](https://github.com/anode-co/AnodeVPN-android).**


**From M2: The app will be able to send and receive data via a REST API (done)**
The Android app can send and receive data from the live REST server

**From M2: The app will be able to store data locally in an in-device database (done)**
The app uses an sqlite3 database to read and write data into permanent storage. This is how the app stores most data related to its configuration and use. Additionally, an encrypted storage space is used to permanently store keypairs related to the PKT wallet and to a public-facing cjdns public key.

**From M3: The user will be able to connect to a VPN and route traffic through the cjdns network (done)**
The App does exactly this. The App connects to a cjdns VPN exit point after its public key is approved (manually for now). Once connected, it can send and receive traffic from the public Internet via the routing of the VPN exit node.

###### Client Website

**Design: Started/Deferred**
A [landing rock for the Anode website](https://anode.co/) has been created, which houses the latest Android PKT VPN apk binary for download. Feature-rich designs will be made once we are prepared to create an informational resource for users who might download the app.


### Conclusion
The project is currently ahead of schedule in Milestone 1, having delivered more than specified in the proposal. We expect to proceed into Milestone 2 without any complications. The error-reporting is allowing the development team to more easily isolate and resolve potential problems with the app and its integrations.



## Milestone 2 Report - 2020-05-21

### Overview

This document outlines the state of progress through the completion of the milestones outlined in the approved project proposal.

### Progress
Milestones 2 is complete. We have a VPN app for Android where a user can:

* Create and remove accounts
* Login by email or username
* Change or reset their password
* Connect to and disconnect from a VPN
* Passively update the app when new versions are available

In the process of completing Milestone 2 deliverables, we have also made progress on Milestone 3 deliverables.

**Most importantly, we have [released a new Android APK](https://github.com/anode-co/AnodeVPN-android) that lets a user manage their account and connect to a PKT VPN server for secure surfing.**


#### Milestone 2: I/O, Transactions, and Account Management

Status: Complete

Date Completed: 2020-08-02

##### Proposed Deliverables

We have accomplished our deliverables and begun implementing  Milestone 3 objectives.

Milestone 2 focused on developing core features that enable the client and server softwares to communicate, as well as enabling users to create and manage their accounts. Completion of Milestone 2 results in the submission of this status report.

The parts of the project include:

###### App Usability
* User can register and perform account management such as resetting a password (done)
* App can not yet route traffic or enable users to connect to a vpn (Objective achieved - user can perform this task)


In our process of building Milestone 1 and 2 goals, we have deferred some features to later in the project, and removed others.

We chose to focus on connectivity first and then App implementation, which results in us having nearly completed the App and Server API without much on the "Server Website" side which will ultimately explain the project to customers and offer downloads. Instead, the binaries are hosted directly on Github and no customer-facing information is provided at this point.

Deferred features

* Server website design
* Client website design
* VPN configuration through API

We also implemented REST API and account authorization using the cjdns keys available on the App, which enabled us to provide VPN access to users who don't want to provide potentially sensitive information such as their name, email, or phone. This option, plus our focus on an App-first design removed the need or sometimes prevented the ability to provide certain services from the client website, including:

* Push alerts
* Account login on server website
* Account password management on server website

However, these changes also enabled us to move faster on certain goals from Milestone 3 and 4 related to App design and implementation.

##### Accomplished Deliverables

In developing the App, we’ve reprioritized the milestone slightly. We focused on
1.  Ensuring data sent between App and server is secure. We used the cjdns key of the App required to connect to the VPN to create a secure digest for sending REST API requests. This guarantees a message sent by a client is not modified or forged.
2.  Ensuring users can choose to remain private, by creating allowing account creation without an email address if desired by the user.
3.  Focusing on an App-first product so that all usable functionality is guaranteed to be in-App so users don't need to go to a website for any features

In doing so, we have accomplished the following:  


### Server/API

**The server will be able to send transactional emails: Complete** 
For features where it's required, a Coordinator API server can send emails to a user, for instance when the user registers a new email address or has forgotten their password.

**A VPN operator will be able to configure their VPN server settings: Done**
Although not all settings are yet accessible, VPN operators can register a new VPN on the network or take it down. They can upload their network configuration and other settings which are unique to their network

** From M3: The VPN operator will be able to register their VPN on the website (done)**
The VPN operator can register their VPN on the Coordinator API, which can then be read by the App.

**From M3: The VPN will be able to connect to, send and receive traffic through the cjdns network. (done)**
The app can do exactly this. 


### Server Website

**A user will be able to log into their account: Deferred**
VPN operators may later need to log into an account via a  website, but we have not determined how that will look yet.

**The server will be able to send transactional emails: Done**
This feature is related to similar functionality on the Server API.

**The server will be able to read and write to an Internet Database: Done**
This feature is related to similar functionality on the Server API.


### Client App

**The app will be able to send and receive data via a REST API: Done**
The client can perform all account management, VPN lookup, and VPN authorization via Rest API.


**The app will be able to store data locally in an in-device database: Done**
The app stores some information locally in a database, including the user's login session information

**The app will be able to receive push alerts: Deferred**
The choice to defer alerts is based on our decision to make a passive software update, where the need to deliver alerts to the user is not necessary at this time.

**The user will be able to log in via a PIN: Deferred**
We have deferred this feature until we have integrated a PKT wallet. Until that time time such security mechanisms are unnecessary.


**From M3: The user will be able to connect to a VPN and route traffic through the cjdns network (done)**
The App does exactly this. The App connects to a cjdns VPN exit point after its public key is approved (manually for now). Once connected, it can send and receive traffic from the public Internet via the routing of the VPN exit node.


### Client Website

**The user will be able to log in to their account: Deferred**
We are focusing on an app-first experience where a user will not need to log into their account through a website. 

**The website will be able to send transactional emails: Done**
This feature is related to similar functionality of the Client API


**From M2: The server will be able to read and write to an Internet Database (done)**
The server is has a working MySQL database and the ability to read and write data to it. Using a functioning API, the client is able to create, read, and delete data from this database remotely.


### Conclusion
The project is currently ahead of schedule in Milestone 2, having delivered more than specified in the proposal. We expect to proceed into Milestone 3 without any complications.



## Milestone 3 Report - 2022-09-01

### Overview

This document outlines the state of progress through the completion of the milestones outlined in the approved project proposal.

### Progress
Milestones 3 is complete. We have a VPN app for Android where a user can:

* Create, manage, and auntenticate their account
* Select a VPN frrm a list, connect to, and disconnect from it.
* Rate the VPN and see other people's ratings
* Passively update the App

Additionally, we have a VPN server which:
* Any user can download and set up.
* Can add to the VPN server list.


#### Milestone 3: Network Integrations

Status: Complete

Date Completed: 2022-09-01

##### Proposed Deliverables

We have accomplished our deliverables and begun implementing  Milestone 4 objectives.

Milestone 3 focused on developing features that enabled VPN connections and created a UI for users to interact with the VPN system, as well as a VPN server that could be run by administrators.

The parts of the project include:

###### App Usability
* User can select VPNs from a list and connect (done)
* VPN server software is freely available (done)

In this milestone, we focused on usability over features, expecting that a simple, yet reliable user interface will provide the user with the most utility.

##### Accomplished Deliverables


In working on milestone 3, we have accomplished the following:  

* An app that lets users select and connect to a VPN
* A VPN software that can be configured and installed


### Server/API

**The VPN will be able to connect to, send and receive traffic through the cjdns network.: Complete** 
VPN server works, source code hosted on [Github](https://github.com/anode-co/anodevpn-server)

**The VPN operator will be able to register their VPN on the website: Complete**
Completed in M2 - an API endpoint exists in the VPN coordinator API.

**The VPN will report its usage statistics to the website: Deferred**
Deferred to M4

**The VPN will report its version to the website: Complete**
All VPN servers are assumed to be version 1 until an upgrade exists.


### Server Website

**The user will be able to connect to a VPN and route traffic through the cjdns network: Complete**
The user can select any VPN from a list in their Android app, which can then make a VPN connection to that VPN endpoint using the cjdns protocol.


### Client App

**The app will be able to send and receive data via a REST API: Complete**
The client can perform all account management, VPN lookup, and VPN authorization via Rest API.


**The user will able to input VPN configurations manually: Complete**
Was implemented and then removed as it was considered a placeholder feature before the VPN list UI was built.

**The user will be able to view statistics about their VPN usage: Deprioritized**
This feature is built into the Android OS, so it has been de-prioritized

**The user will be able to browse VPNs from a list: Complete**
The user can browse through a VPN list.


**The user will be able to select and connect to VPNs from the list: Complete**
A user can select a VPN and connect to that VPN through the App UI.


### Server/API

**The user will be able to install and configure a VPN following documentation: Complete**
Documentation and software are provided for the VPN server on [GitHub](https://github.com/anode-co/anodevpn-server)


### Client Website

(no expected milestones)


#### Milestone 4: Polish and Debug

Status: Complete

Date Completed: 2022-09-01

##### Proposed Deliverables

We have accomplished our deliverables related to productizing an app. There is ongoing polish and UI enhancements, but at this stage we have a functioning, reliable app that can be dowloaded for free by users.

Milestone 4 focused on turning features into a product. Existing features and usability have been extensively tested and standard configurations have been implemented so that users don't have to make difficult decisions about VPN configurations.

The parts of the project include:

###### App Usability
* User can select VPNs from a list and connect (done)
* VPN server software is freely available (done)

In this milestone, we focused on usability over features, expecting that a simple, yet reliable user interface will provide the user with the most utility.

##### Accomplished Deliverables

In working on milestone 4, we have accomplished the following:  

* A working, reliable app that users can use to search, select and connect to a VPN
* Information to learn about and share the app with friends
* Information to learn about and set up a VPN

### Server/API

**The user will be able to install and configure a VPN following documentation: Complete** 
VPN server works, source code hosted on [Github](https://github.com/anode-co/anodevpn-server)


### Server Website

**The user will be able to browse the site easily and find documentation and download links: Complete**
Information about the servers are available on [anode.co](https://anode.co)


### Client App

**The user will be able to select the best VPN based on location, speed, or some other criteria: Complete**
Users can filter VPNs through a search tool


**The user will be presented with a welcome screen upon first run: Complete**
Anode app welcoms the user with a logo and a walkthrough of how to set up a PKT wallet.

**The user will be able to share the app with friends via a social sharing tool: Complete**
An "invite a friend" feature has been implemented on the [anode.co](https://anode.co) website.

**The user will be able to find the app on the Android Play store or on the website: Complete**
The app is available for installation directly from the [GitHub Project Releases Page](https://github.com/anode-co/AnodeVPN-android/releases)


**The user will be able to use the app without major memory leaks or common bugs: Complete**
The app has been extensively tested for memory leaks and we believe that the app is stable and reliable.


### Server/API

(no expected milestones)


### Client Website

**The user will be able to browse the site easily and find documentation and download links: Complete**
Information about the app is available on [anode.co](https://anode.co)


# Status
## March 13th 2020
First payment of 10mn PKT made in 19 transactions:
[1](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/a6b9f30968906d7ba4065004e6ff7724de29d2eae2128dc33dfcc26b46c0ed6e)
[2](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f1339ab70d89fe05826bf15b7eff08f9e8e79227012e252cdddf715f9d45bb3d)
[3](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8f118c7aa7a14033d938a9ebffbf4db6fefdd93b657e2f803db9159e43446633)
[4](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/707299030ebd2b28f1267bfdcdf230ab0ae03df30ae9ec82c56b38ea7e5f9bd7)
[5](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/5ce8df54387a11f404f1c7803d0fde79dd58b2b35c1ae20666fae465a994b391)
[6](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/7b210ecbf70b8b420f4179abcf3a90b88eb671ba5d7a43bda6d3deaba44d7237)
[7](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/0b2b7e45a4892da5e920233a51010e8e56e43063c6cba49f6c1cf6295ccaaf0e)
[8](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/f77a56d589b5a9dad3779bfe56b4f008b2d714b7ec100c60507940e0c6666137)
[9](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/da888829975273245b8f6f480868d462a6d4cc27940e5e61ba29672b32c2be24)
[10](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/e4960c9e3bbb3b9773058de0b6cf18483a40e9564758ef11fed9a2d9b4197a09)
[11](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/4179a0ada769da4917b16af0aae9964e5a1fa11a6ce9855b4b37ae163d840e72)
[12](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/541d98024d490652137d12d421939b033f0ea8f40f8013904f4a53658aded8c8)
[13](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/8b03151cc387a14e5f8b03ef82cfcc52cc53de6814973706ed8459cd846d168f)
[14](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/9c94faaafde5a5532ec28693b1f34409f4a098b1a6127cd09833c0d217619731)
[15](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/72a159bbfa2ce35727f0084b7b51f813590a557c2ed864328043324a53aaea9d)
[16](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/4cb4e79db6e3e444a86ec0be8c2999b84db9b657492b2c5096d0a94eeaebf616)
[17](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/5aa3a68365e50855c910741791e2dcb92490a3fca325a3d14808849c1d0bab74)
[18](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/79a5c1bd5a1d9aff2a125dd9633c953f524654aed209601c1a5c4572e1094fa7)
[19](https://pkt-insight.cjdns.fr/#/PKT/pkt/tx/0cc1bfda33f34cf084b27f55084eed05ce9e5b8a0121e9cda7893b987789415f)

## July 1st 2020
Milestone 1 was accepted and paid out 5mn PKT in transactions:
[1](https://explorer.pkt.cash/tx/103342795108477a68b4d8f945fcf042eb9ca7ce5fe182b07747fddf1d68375c)
[2](https://explorer.pkt.cash/tx/25df0f34dab93958b7ffff4628c7cb0908222827376cae85bfde687105666996)
[3](https://explorer.pkt.cash/tx/45cbdcff9980f981dbfbe21348014a6c018a34c2d7355459fcf2d9e9c2c45173)
[4](https://explorer.pkt.cash/tx/7b4d1eea9fc4225171484548e842bacb7c564d09c3cd910a56ce223e32c0e249)
[5](https://explorer.pkt.cash/tx/8932824dfedb0a7425b3019698d9cdc46792b630472a0613c698f425215cb0b8)
[6](https://explorer.pkt.cash/tx/8bc5ce5c66ab20d5fec4f45fde3eb529d76f5e25e1cdb68389ae1f1384504e3d)
[7](https://explorer.pkt.cash/tx/8be49e0b9c7a34e61b08accf62f80ba83acdbbaf3512146c1d908fcc58450697)
[8](https://explorer.pkt.cash/tx/91a7291cb10af0e02c0ac8506850aac02edac00fbfbf6086e6f2831e42d12187)
[9](https://explorer.pkt.cash/tx/a92a1385d135312bdb0ba15fa13c6623247b88b30768304c73a26d72f2c97860)
[10](https://explorer.pkt.cash/tx/b119b32c9068957b7c1beaeedfc1a137e04cd6ce20cac7d636d42ac0dadce95d)
[11](https://explorer.pkt.cash/tx/be0369f9f45a3f78bdaa1ee02a9bb94909d85a803c65d39e9f8c50b8b956fc86)
[12](https://explorer.pkt.cash/tx/d3381c55c19aa5f7990bdd946c8800c1ace317dbad680cbe4ed9eae32e2fa54c)
[13](https://explorer.pkt.cash/tx/e72eeb9467601bd3a7968b042c98cb476a66ad82c6c0e2961eb86dbfc447737e)
[14](https://explorer.pkt.cash/tx/fef842c0ee7ef22aaca8f0b68e886083704628160f525ac420741e1b64e0011d)
[15](https://explorer.pkt.cash/tx/19d4f1fae64f6d61e17c7605f78b2f39142ce0af747a2361260f49e655600ffb)
[16](https://explorer.pkt.cash/tx/3db1c3897bea04625c9cb025afe10813f85cc94a988455fbb029ade51094b6f1)
[17](https://explorer.pkt.cash/tx/4b959a8fdd1fcd1b15601198ff967d0bfa39818c7c21e819086d81ea716895a9)
[18](https://explorer.pkt.cash/tx/67e556febc1aec01c018ec86a271d3f56abee1ddc7ec7f5bba8e739750507ba7)
[19](https://explorer.pkt.cash/tx/dd9df2226d765c5233317fa41da952a4d37f3b527e3df5a97bca4377905eae3b)
[20](https://explorer.pkt.cash/tx/f481167527aebd610e7781d2118dee833084881df4c1a992e9044de69bfb4c55)

## November 26, 2020
Milestone 2 was accepted and paid out 5mn PKT in transactions:
[1](https://explorer.pkt.cash/tx/e21caec6995b9c896cfe92a1b74a8b976369f7b36c5cb034bd46270da37fbdfc)
[2](https://explorer.pkt.cash/tx/6a58a51afee4285c0cacea1fa1f9f9bb4d0baec8355dae939f6f531b485329e5)
[3](https://explorer.pkt.cash/tx/b8cee8161115ad2ba93c2666c70decaa099e9e8f5db24a719c3704bc3072ae10)
[4](https://explorer.pkt.cash/tx/2299971d66d1acb3ca1d660587db2f7e15a337c3fab9fd89f6f5257c4454e263)
[5](https://explorer.pkt.cash/tx/fad400152e6b79db29a276a9012744ecddda19cec09721f0e76daab55e617ed2)
[6](https://explorer.pkt.cash/tx/8c8647db0911ba0985cdc124d5abe5d993c05b22011918c80dbcfec1de2c8fcf)
[7](https://explorer.pkt.cash/tx/ea9569565b4af21624cd042afb780030c1ab9a25b6050d98cca6647cd0a5216a)
[8](https://explorer.pkt.cash/tx/de4ec5e71807d16682ce0c673144b055c2f078ae512703002008bcf149607702)
[9](https://explorer.pkt.cash/tx/733d2ff28d9023f896d450df74a722142dbf360fa99873c8daa65f64d8416a52)
[10](https://explorer.pkt.cash/tx/7981003513626e0b0b1137975d00794daea3949d78d577d852b4a13252e9b347)
[11](https://explorer.pkt.cash/tx/b77977c599c6bb62d53893a158ac7cd12c0a2652f1637644cbe62c7af4bdf438)
[12](https://explorer.pkt.cash/tx/b7d773e70043abe84bc10a550ec0c4fa63516e5e62472e2afcbb570e5ce42622)
[13](https://explorer.pkt.cash/tx/ae7829ca715585822d2721710937fe92a04d806cb5a660b73470a5d5c0a3ea51)
[14](https://explorer.pkt.cash/tx/9e171346deec3d2036d9a3197de2e563863de384daccf2d0d3618bec9392c62f)
[15](https://explorer.pkt.cash/tx/6c76db45f27520cde03848b16f644b44cd5d800678c08cfa3cca6b000fd7515c)
[16](https://explorer.pkt.cash/tx/8c2c47e4c85507bd29c8e52d7c53a5fe8e0e1ad3cd076ed782b8da47958bc665)
[17](https://explorer.pkt.cash/tx/8440cad78e12b33bf55085ec6a1833df96ed3c3c5ebcb2f5592d5391b906b425)
[18](https://explorer.pkt.cash/tx/58723d84cd3ada866ee93e11b1ba0a25b2cc8d8df92bd8c8e5aaf062dcddcabf)
[19](https://explorer.pkt.cash/tx/d1efd27c2108a00c52aa2d69418921c81304ab163f067476bfafeefc7f08d307)
[20](https://explorer.pkt.cash/tx/00b68e3fff05721a4e496b1fe4cf8b1a82f947a102a2272d1207d35a8d911650)
[21](https://explorer.pkt.cash/tx/269dffecec83adb7f227100dde99c5b0546a49cc2237691b6fd4d407a18ce72d)
[22](https://explorer.pkt.cash/tx/69f95fc265cbb404ae0643d6e2f8984b9617ffecddd312beb0feec7058de882b)
[23](https://explorer.pkt.cash/tx/25c7faa4a40b5f4ee06c33d5a8a5585f9c73bedc7a2481f5d9a33917dc36575f)

## OCT 12 2023
Milestones 1 and 3 have been accepted and paid out for a sum of 10mn PKT in transactions
[1](https://explorer.pkt.cash/tx/5e9fedd5b6f0272466b2bbed059a78fad9644c71f9b0f00bcbf10d60c1cde9c3)
[2](https://explorer.pkt.cash/tx/a8fb335effa6a49627c2cf4e57d893c81a30da4aa84e2e6aae06acdcf5531f7f)
[3](https://explorer.pkt.cash/tx/83b66b332b97213af0430e7530fab404eddbded690eac5dc38d310095282e28b)
[4](https://explorer.pkt.cash/tx/c9ff2e9c4cf391cd5bc11dd0949874673559d0daa06408cec1e11ae1aed2a921)
[5](https://explorer.pkt.cash/tx/6974db0f5a40538ec2f4748ce6013c0ecd6fabce59f58c18c0008a815cbdc1d5)
[6](https://explorer.pkt.cash/tx/c47fec5eccd19c9fdd5d2fd4574a09902ed51017b41ae3fea7af5cbbc8ffd6c4)
[7](https://explorer.pkt.cash/tx/1ebe71d25cde9dfd522f49da2e04945f965b9a26032d384e6921e9e7a276191c)
[8](https://explorer.pkt.cash/tx/87c79f2e5f817b340710849e996b8acf13f998db8b75cc5a49ffa8873e26e526)
[9](https://explorer.pkt.cash/tx/1f5e0437035409479bc1cbfc3d694c20831527ed0eb9de6d1877682f031a0e2e)
[10](https://explorer.pkt.cash/tx/53f1dfbf9b71e66fb81bac569d294348fe4b2920e71f5d2724b0b8dc51496e23)
[11](https://explorer.pkt.cash/tx/166946d0cb10ca511655c62612b651b980dea18bff822b43bf931ed1c419ffae)
[12](https://explorer.pkt.cash/tx/0d8f871de4db0e6b75b6a2da468a0dc5f2a16611af69fcca474ebecc25e3aa8a)
[13](https://explorer.pkt.cash/tx/f10f64cb3558e8b0bf0c5d5fd6adec3267460edd4bb606a437ce58418be81423)
[14](https://explorer.pkt.cash/tx/30599df383f5fc1498dd1acf344c3306afb11036c094c923059ff78b9b8247f3)
[15](https://explorer.pkt.cash/tx/3f8104ce886727963c747c711991f72cca8523c42579ff6af185f270ba3b7f85)
[16](https://explorer.pkt.cash/tx/20674edbbf29b3d4b2de624aab85f106e5b5234d339acf525f68655340828c68)
[17](https://explorer.pkt.cash/tx/e89ebf1f587f80d7a0fa7f3938d0b7bb9e761a39fec82fab182409364fe0f6c0)
[18](https://explorer.pkt.cash/tx/83d2c49200c855463ce0b5e3b6aae7014fab0a7b040989367d08ddd706df6478)
[19](https://explorer.pkt.cash/tx/43a78f815a9cc8bd34007db5720c5ac9d345a3db1bd08335f08a195ba6d2a01f)
[20](https://explorer.pkt.cash/tx/9333fd46b661511af7590b30eec5cf745ffb1b407cc2a6b5bd6f1e73f558d4c4)
[21](https://explorer.pkt.cash/tx/deecf4ef0133bdadc45f4aee727dadbf2b77995843a28c10e1c0f2096a132bf8)
[22](https://explorer.pkt.cash/tx/7907e09575a44150274c1fdcf09a254dfdabf7b7a30cd15fa203ca8a621b29e0)
[23](https://explorer.pkt.cash/tx/59babc8a989cf10d33c829bcb7d725ee6246eea6643139d1e87603297001ec95)
[24](https://explorer.pkt.cash/tx/4d0070fc84966949de743604f182ea4ad0b079c145089d846b31e3e30aa78dca)
[25](https://explorer.pkt.cash/tx/274e1f497a2fe0f9700027b0d5b7280e3411f1590b91f17665edd2c132f2c316)
[26](https://explorer.pkt.cash/tx/df8ee609ded68af1e359859b519c26a73c2809a11dd28ac49a47145ffb1294fc)
[27](https://explorer.pkt.cash/tx/c0a57d959a478f6eefc0c14c63de334d3e5544c43219696370147e3c823b8326)
[28](https://explorer.pkt.cash/tx/6382e8fdf0af61c3a3643f4a21867e4c1b06fcb4dd1817751158eb02fd16e11f)
[29](https://explorer.pkt.cash/tx/8a600009daf830fea6a0ea29710e9e30135faabb617cd56ec05038da5049041b)
[30](https://explorer.pkt.cash/tx/ed1bf012898b7a08e323e2555483b1b0e54ac46f33c981221ce2dde73214f8c0)
[31](https://explorer.pkt.cash/tx/20fc0224470a7d7f532086949e5684643b80a457ff9a90e4ee7f994580736908)
[32](https://explorer.pkt.cash/tx/291327ae401bff915682f237dc2f44597778b65a066df224b4ae39125b38b573)
[33](https://explorer.pkt.cash/tx/fce6f5a569e0056fe5cb7d9b6dfe8ac3299fecfb79d5e6462e163a5136381038)
[34](https://explorer.pkt.cash/tx/b404d720cac1aa34c2422889378651ad8a8eeb0fcce80bdafda5ea913fa66259)
[35](https://explorer.pkt.cash/tx/5e2689665e3326520247c7f562e9ca922f1c6c33d7378a833d384cd22d84434e)
[36](https://explorer.pkt.cash/tx/0f43cead55863b6945a18b2831aedc19b363e163549281ce2097151947522ecd)
[37](https://explorer.pkt.cash/tx/1e63e2bd47e1c29b24fcbee4fecf94cc7db44a341c3f4edd99d814961ef495ee)
[38](https://explorer.pkt.cash/tx/2dde7d4cde5e9f1cadf36124c189e8fad3ded62c2902ec8e09bf53ebd424228c)
[39](https://explorer.pkt.cash/tx/6744667b86472e06ad5003520181fabfeba4d37d1fcad6a21763c8d945f41760)
[40](https://explorer.pkt.cash/tx/637b8b74c3f0304ce8154317b0ec894485d2923e4d34afbe3e1c098bf7e2d04d)
[41](https://explorer.pkt.cash/tx/9953e441d0f1927e26a4dce91f8b888054ee01873869e45e1c64a624eca80620)
[42](https://explorer.pkt.cash/tx/4c991ee2eeb25d45ff7aea98ae72a476699a36d325554d1a3440707a745ce4e3)
[43](https://explorer.pkt.cash/tx/702088329c84caccfe157229dbaef18bc34268be0c42f828760f5b02850abeda)
[44](https://explorer.pkt.cash/tx/72ea885dfef3af5d5fb3341b97c3388ccf9587724a9f5dc15f427ffa3fec8e57)
[45](https://explorer.pkt.cash/tx/27a6926483240a60ba1fc77f17b316c353b63a35654e44df2b97f5114128db32)
[46](https://explorer.pkt.cash/tx/7d76d3fd413a8d3d99b8000e7bfc8e963371e3bfb2b89402ad04ff49c032344a)
[47](https://explorer.pkt.cash/tx/4c0ddb26f2f93b98d6d2a514d6b327040358ea5a4d3f73e5ec6d0eb7fd783aa2)
[48](https://explorer.pkt.cash/tx/1863a9a4fb258b8ad86e94775c8216da24b6be2fcc779d98bc1bd6a13e6b5f50)
[49](https://explorer.pkt.cash/tx/5dc355bc4a59e85a6613205825a35e248aa989ab65d12bba88375227e44b29a8)
[50](https://explorer.pkt.cash/tx/7eac3aa835f686e65bbe2d3a34f106436f4197fd49fe4b94fbba03701316c85c)
[51](https://explorer.pkt.cash/tx/7bdd77cc3b11366e1f372238ffaf69278ce94676ffda03a8be233d555b350e7b)
[52](https://explorer.pkt.cash/tx/312303361841dc02a4de4a97908bc798c12b330c59445644f9e3bfd163d01bc7)
[53](https://explorer.pkt.cash/tx/76755a90528899708993e22f83650f190f750fc168de77306134c762e638f369)
[54](https://explorer.pkt.cash/tx/813319da6759c425f19de623d5bf562878d4e3414f4c0765ff1dbdd08d52e705)
[55](https://explorer.pkt.cash/tx/b351be339cec30651fb6a7a500ff85ef6de9c5d2b0711502663b1ba80c85b79f)
[56](https://explorer.pkt.cash/tx/621f8a24cf66c558842823798014e397e877a1fa6584fe9568294a9f26da3460)
[57](https://explorer.pkt.cash/tx/76a3a7a8cf5b8ef9b0d232a3aacee4e6a65da09bc0e2d650a8763bb6f8bcd7ec)
[58](https://explorer.pkt.cash/tx/64ab1c153da053d632e9a3cbcfbcf69df9cc7af3581a98d3cacd98616c74dc91)
[59](https://explorer.pkt.cash/tx/e92380d1cbe25a3476720e2f79ed6bff28b0f61e216327eb22c0d009e3f3ce68)
[60](https://explorer.pkt.cash/tx/b013b2c79983a94779121e4d0abb26d32298c0d15107ac9fbf9acf7323583039)
[61](https://explorer.pkt.cash/tx/dd6ac9f8671ee83df6def7829c355a07f2494e8efa2000df74993ddedad01cf1)
[62](https://explorer.pkt.cash/tx/f805fda0682ad0eb72ca213b3353583283d500c969f84bdbfc5caaf4095cb2ae)
[63](https://explorer.pkt.cash/tx/df8b65847237d4fb2455bf5ba952bd24860fe34cc817b0256f4d21250e049aa8)
[64](https://explorer.pkt.cash/tx/9f3e06088d71a57b738b00bfafe961236138e226b9345da504b1fe049a50b84b)
[65](https://explorer.pkt.cash/tx/8078434a8629ee909aef60fd3a1b52fe89601e80c76da85ade368a25b7ec98b8)
[66](https://explorer.pkt.cash/tx/7f53452404caa4082c7068be40cd607a5576352608d6eab5de901b960f0ccbce)
[67](https://explorer.pkt.cash/tx/07e38db1b7379b4303d96195af0cdb328d40ea88f94b61dc35db7b60467dbfc0)
[68](https://explorer.pkt.cash/tx/bd1ddb22779a416d5c0ad9f83e27d8008f5948672c2a7f639875262757369681)
[69](https://explorer.pkt.cash/tx/7f3b15978483e67243eec35fde4356da8d17743d6a9c0644001ccde6560b70ef)
[70](https://explorer.pkt.cash/tx/570c31517849b0da5f308c4e696b363f4a92920149f4ccdb111133443d121172)
[71](https://explorer.pkt.cash/tx/61e9ea98a9b2ade106651d7d33bc328684982a1a0af42c666d7f6d0bce18b0e5)
[72](https://explorer.pkt.cash/tx/03679948fc4dc97348931c021e98f0fd7964355ed9ce676c660cb54ef9d27166)
[73](https://explorer.pkt.cash/tx/7c81de1483188ea831d0078c783b7ce5b22f030e23ebd6f018bf10e439a72beb)
[74](https://explorer.pkt.cash/tx/2c678fa7a5091833591c2663c393123d1b716b4b3667ffe6f404a3f4606180f5)
[75](https://explorer.pkt.cash/tx/cb4aea5f897904d9a957a98794c259ea222f7c47c17184de93051dfb12ff4b14)
[76](https://explorer.pkt.cash/tx/6b2f8d500d313dc33843e07b91220841cafb6f2444ca838145eddc7a18a0fc44)
[77](https://explorer.pkt.cash/tx/af0863f8efb236f065aa5fef9eb1fdb34aef9a50a3e7ad3b5691d4ef86f482d0)
[78](https://explorer.pkt.cash/tx/90fc722b439e437466675a8347099e52d9afe4ec337296431707ff91b8c0d22e)
[79](https://explorer.pkt.cash/tx/e18d7415c0303dda7b68eb96da592168ff4e27b054998cf2f8f4eb104304339b)
[80](https://explorer.pkt.cash/tx/91f3272492fe452db5f4f4e5fcba573c235db6454171232ac3d6d522ef946e66)
[81](https://explorer.pkt.cash/tx/47e60db5f7626e0625a28aef85c153cc1681c824e064ae186567e0961bb269b6)
[82](https://explorer.pkt.cash/tx/ad5428ef9a53c39b0a75a9fa7aa3d3fc79dcc133e4c41fe2f042dd1df91eec34)
[83](https://explorer.pkt.cash/tx/f19aabc07a0b274a7bf01c45ff9a7583f9abf1340145b7171c0953a9f21157c3)
[84](https://explorer.pkt.cash/tx/7383090b7133856411aa406b1efeb18c6571d2860288d994208d832591d58228)
[85](https://explorer.pkt.cash/tx/8565af96589c5c192b44360fc71e9c7fc478cc8be5ea0c704cbe13337e557ab4)
[86](https://explorer.pkt.cash/tx/eb40720c262193ad6bca980a626973ce695569105d21c234e1af6c73a0dcebe4)
[87](https://explorer.pkt.cash/tx/ecffffc766f6cc1d8b40e9e4b3aefdef431f37c7f68daa9636bacbe8fab7f58f)
[88](https://explorer.pkt.cash/tx/dca5230d9478c598c0be1befb2a5d3adc02fcad378219d1a85a239d7e2237885)
[89](https://explorer.pkt.cash/tx/008c5a5964fcda8814bdd16a89f118eb9e56a4da122de0a7b1a1f08dca52ff98)
[90](https://explorer.pkt.cash/tx/60a969283706a191490ff983539496825e5bd927b7a7f73cb2f46cccc1912509)
[91](https://explorer.pkt.cash/tx/33b0016d22195b96df610dacc0b6fae42817aa737d7541c10b1942a1376c7005)
[92](https://explorer.pkt.cash/tx/a50845aaafdda6751ffeed3dbaf99e7d3321aa733fadbf5f30cf2a1b0ad0022a)
[93](https://explorer.pkt.cash/tx/8c84d05a66def1ff135e67e62cbf9abc4cd7972b8bd04e66a85ecb145dc58d6d)
[94](https://explorer.pkt.cash/tx/2385829c6e787cc83b69ea84a7c5659c5b0fcb39dc3a344b8b2d3aa07289dd7c)
[95](https://explorer.pkt.cash/tx/d428a388305176c5582df9ba383fe51337b83c51f4ddb1c064474bd62cff5ba1)
[96](https://explorer.pkt.cash/tx/30f742b0d1a4b6b3894e3d0e53e5b9c563d0152abd707f3037eef4972f9a9020)
[97](https://explorer.pkt.cash/tx/50a175ff0721bc24638def84d407ef32a71e92c837f474390a6583c9b4b339ac)
[98](https://explorer.pkt.cash/tx/37b5cf78e475c24d31178bf3c9db7d3c27685b13faa30fd263087bd3fbfda444)
[99](https://explorer.pkt.cash/tx/571a662b19239a41fd3fc9430674340cdd674f0953fac3286023dd0800740358)
[100](https://explorer.pkt.cash/tx/23261dfe245ef2437d6bf89ac8a23f84e50a97b6a211e5e273a1bb6c6c291114)
[101](https://explorer.pkt.cash/tx/c0f6bbf5473a7c0a92b9e04ce69b9fcdc3873162f11235139d92011c04f7976c)
[102](https://explorer.pkt.cash/tx/d111e3a0d9457627d10c4e5489c4b1f07be6dde95f2cff2af98c3579aa83670c)
[103](https://explorer.pkt.cash/tx/f17cdc07a8913ba957492a79c9aea40a57035e34d2e560fa7dc0997e5e38d0f6)
[104](https://explorer.pkt.cash/tx/1acb580756e45acf7778a4ec50151918f589b9dd40b95ea4562fa58440eae524)
[105](https://explorer.pkt.cash/tx/d454e161dad7c11b2e182d7a8175077a60c3e7e0dbe9032b782e0f8813dd9186)
[106](https://explorer.pkt.cash/tx/b3c0750104936510ed22aa048be6aa880329c621bd4444fbd214c1ec6fe0cef5)
[107](https://explorer.pkt.cash/tx/41e3b9c24b6d7f0de52bfa428bb448040cfde23be3731d0eb587587696cf6118)
[108](https://explorer.pkt.cash/tx/9bbfa17437930d69e2e824fe486c9ee8b519ae2612ff363aed340d9295712e1e)
[109](https://explorer.pkt.cash/tx/dd61dbddb443a3a2ae7c21be1410784248d569033d827967a6df162370129de6)
[110](https://explorer.pkt.cash/tx/830837af71fa4d166f46d143e007a7afe767455868b8b54b0cd4d68fa2da6b66)
[111](https://explorer.pkt.cash/tx/ed6a570d7358659e9977881160887c7825cd93e36c33187199a864e07800a269)
[112](https://explorer.pkt.cash/tx/b2d97fd0ae39711ffbb571c2cd77224af95377f685b88ab23864e396187d6257)
[113](https://explorer.pkt.cash/tx/50142f5cb62141129debf53c02cec6c065f705ba102a24ebec150b4f90bb710e)
[114](https://explorer.pkt.cash/tx/c7433e60a78208cfd2471d287c0dbf8ea21088cfca27629f7515150b80edee98)
[115](https://explorer.pkt.cash/tx/46efcd278573052299c95819e1c630dc76358f9be8360c5c60b6a1ad86ea0c4c)
[116](https://explorer.pkt.cash/tx/93f179f82496fc81fd8807692567543418711ba84c04ad6b0761a73757d51836)
[117](https://explorer.pkt.cash/tx/0f156c6217bff5de259d03f7092bff7bab649ec6db7e92a4ad30259ae7a62c86)
[118](https://explorer.pkt.cash/tx/511cb5cb2ae68f041fe73b545ac8868573e36d3d06745ea3f5ca15263d412572)
[119](https://explorer.pkt.cash/tx/e7b4a30610f67bc151556ca5f7badd193675ae148e64204e9122a9ab5045a323)
[120](https://explorer.pkt.cash/tx/598d3f229cc2ebc38276f2f03a3ff2d4158a5f99f19d5470362bef3ed5690cd4)
[121](https://explorer.pkt.cash/tx/3aa957c54c23ee6758258fae3a6fbfa1d349e7d995289782b3fa44bb9c2e9ede)
[122](https://explorer.pkt.cash/tx/b0c655a49c4c373565c7a80cf4e6c0cf73958e73504e85dea2265f210d395283)
[123](https://explorer.pkt.cash/tx/9cec05e0320c44ed5c2efdd00ed7fe8d78c50d29cdd969f2172a35cb5a6cfd11)
[124](https://explorer.pkt.cash/tx/2582968499eab6990a097ec9256e797b2f70ceded5f2970d6ce7476760c17ffb)
[125](https://explorer.pkt.cash/tx/1baf35d2caccf4ba63600c58a4ce749db8c63194ff538d2205e7276f5aa4f7f3)
[126](https://explorer.pkt.cash/tx/84047a8c6cc2abc78555e05a30130c070ea87a58f8ac6731d1994f035d333f13)
[127](https://explorer.pkt.cash/tx/97787f4b14313ee20f79b05966558ecbf7c89d2aee39e5f0a9e6fe1d953e666f)
[128](https://explorer.pkt.cash/tx/07a4dadf29b6f81d6dc7754bbb84f8e719375c357babb31cdd466baf8e327440)
[129](https://explorer.pkt.cash/tx/6fd7274c1643e669c5072ab9e0f3c5c915022aa3df72fc8ee28f5316044e4a41)
[130](https://explorer.pkt.cash/tx/76dce7fed327c14eb3f8cec6a2fcefdb2288dfa676d8acbd8fedd249ee6a459d)
[131](https://explorer.pkt.cash/tx/d2177cd9453d46826c77ce8703a7f4d304aca663144b4769931ac63fd4beda22)
[132](https://explorer.pkt.cash/tx/37841709a0eaf4645a32e1f4270b150c6fd05d655a58ccd649d25fd7dfcc0b66)
[133](https://explorer.pkt.cash/tx/f7be4fef02d497184a34849a8ddff67992bba1596265f856f2399739d5993251)
[134](https://explorer.pkt.cash/tx/e0ecb2ff6ad70ba14fddd1104cfe71a87ffb460d0c0d7fdcf2b2145565ab1963)
[135](https://explorer.pkt.cash/tx/259474b31c2eb6835994ed1b802567c970f6b1e47e8615e7a702af860b5855aa)
[136](https://explorer.pkt.cash/tx/2f0ef0da4d6471826a51f44637b2bd47077718544227fc69a33783fd1050229d)
[137](https://explorer.pkt.cash/tx/a3b86d691657d7998f6d94f9f506d16566649fc9c31be0242027f23d51b57e49)
[138](https://explorer.pkt.cash/tx/bf1ce0f04a3f685d75daa0945258f077c028c9f224eb28c3c97701441354725f)
[139](https://explorer.pkt.cash/tx/7ff1af86c1803969cdb98821b3c1efa8dbd72e20fd26ee3f0e430c018ca68359)
[140](https://explorer.pkt.cash/tx/b80f7a6c32afa289a733c9417f0850dc7f4178ad9db14b12818ffb41170bd170)
[141](https://explorer.pkt.cash/tx/a0c7b1e1a8b062a74b8a55a885c515b554b47911044d7e930c38a85c51959dec)
[142](https://explorer.pkt.cash/tx/7259967d9fe0f040afadaa5d33cd0f8ef27c7454d25959626ca96a930ba838be)
[143](https://explorer.pkt.cash/tx/5b02d65f43c5fa43c6993be6b2c680b9ff18da8f65ad18d32841b344ac1e9913)
[144](https://explorer.pkt.cash/tx/26a0bd02cc2e9533dbe45c5898bed136a02c67f4fd6507dd12d69b5712affeee)
[145](https://explorer.pkt.cash/tx/b4f9db8375860e5c0c50fa8930e50a357b143cb4daa2af1b29519f5949152e55)
[146](https://explorer.pkt.cash/tx/f10ec28eeb2cd76891162bd84e47dfec1645291b0f69740314ed1cbeadac4669)
[147](https://explorer.pkt.cash/tx/c0a8ddeab4738855da8a830b7386e1e364899a7b0068a629c7985981738ab915)
[148](https://explorer.pkt.cash/tx/2a67a4fa92ed3ca1d4937bd59d02d40c0e523342d5138fd29d8747b272957cf5)
[149](https://explorer.pkt.cash/tx/1261b16367a281d15685b879280d4c6ffa2d48c75ce5fb9de10ca22594a970f2)
[150](https://explorer.pkt.cash/tx/d1e8ce26b938efac85ace7fdc2b2090d50e631f4dfa4d9317f0df96707f253cd)
[151](https://explorer.pkt.cash/tx/9e92537bf30cc42a53a198c0bf0748f06b502e4d7b1b76c2c713075469f83a2b)
[152](https://explorer.pkt.cash/tx/2e1e4d066b995650bb404e93d4cfa47e97ff0e05ae8c6d73f57969dde067c73e)
[153](https://explorer.pkt.cash/tx/70fbd784b3357f41e433afc43bd8313bd212da36cfb9a7f9fbfcefdb6c02273e)
[154](https://explorer.pkt.cash/tx/99ad520583161fffbac88971cb3ae76fdc6a6bbb5be793a8a4b98af715dd385e)
[155](https://explorer.pkt.cash/tx/8ac0c518d9ad182c313e2b1f7218ba8c8891b5519c27ef0e2cdce0b9501163f5)
[156](https://explorer.pkt.cash/tx/c2786d33a25dee856327bde275822c4a98b1e087cb2bc0e09a54b1801f1cb97c)
[157](https://explorer.pkt.cash/tx/5ee26393f24aabf44f3433223ad06ab1d3ea01284336e85deee731bc4c23df53)
[158](https://explorer.pkt.cash/tx/b77a840bfd4de41bdf9735801e16e0ba3959cb547cae401105dbd650e41b6f88)
[159](https://explorer.pkt.cash/tx/eec17943ec1b84b07729c18e8eafaa1d59d0c2522590647f9bd8a9cf8678f59c)
[160](https://explorer.pkt.cash/tx/76024d919e918f328a8420919db8bf6e926673c90afb2adc7cf46170174a2e2d)
[161](https://explorer.pkt.cash/tx/f0ea3b5e9487e11df1b2777ee696cd78c136f30e12a176959999b0e49459f384)
[162](https://explorer.pkt.cash/tx/895d55cfa14ca7866ceb86736991fc97265cccd0b66c7e7893a4ce57abac0d85)
[163](https://explorer.pkt.cash/tx/8f49eb1477deed9f9d2feb59fec97a41bcbb64fd7575bc4a465963129fb3b99f)
[164](https://explorer.pkt.cash/tx/e8a7fc1c39b3588904d8d32fb8bfea875a3fc8992cf9cf69a45befc5ca8a7ad2)
[165](https://explorer.pkt.cash/tx/2a9051a9a1735f0c799f472cd6580c2981f68874366504c9dce9653c29103c85)
[166](https://explorer.pkt.cash/tx/a5461e2b9f0907f761cd34b1f63fee4327774d94443f51889f256278674d78cd)
[167](https://explorer.pkt.cash/tx/0e17c383d41495de5583a621dc9c33677dec1c7682328cb6fa53f48820ae8a3c)
[168](https://explorer.pkt.cash/tx/36cf736b64228ca03a48531628130b13fc6e3660a5608a7f90910bbc6b6b8602)
[169](https://explorer.pkt.cash/tx/99f7c3cdd7beba17eea77828dcdb1cc842673234d3f49a794e5520114149a2de)
[170](https://explorer.pkt.cash/tx/9a8062e926aa883ace28b9d6f06f17dccd0616e0bd91235cb407c46831563008)
[171](https://explorer.pkt.cash/tx/8171a008d388a4bb627ecb0bb79b31162fd292817a24276c26a39eedc2598099)
[172](https://explorer.pkt.cash/tx/c1fb382d938d7e3e47ef1ce54c3b5f967e070846ff5a3e4b600e64d65b136009)
[173](https://explorer.pkt.cash/tx/5204539cc2e4bfc26749454cbce6891f3296f5ca1a7d50e676668e278c3be517)
[174](https://explorer.pkt.cash/tx/f6ad7542e3fec345e32044c4b1336fcd13c9b3c0950326a9582b780753c562ff)
[175](https://explorer.pkt.cash/tx/a18949d33ad9a4256945b7c8b5cd553ba263e86b2e8e3f1f9c7643a7d0c14423)
[176](https://explorer.pkt.cash/tx/60ccd83b68cb19843e1ee283e29ec45d721dca5e55842008f63d37fb1e3ddf4f)
[177](https://explorer.pkt.cash/tx/85a4c99a156524886d5888dd79af68081121d93d3f3e7ac7e9ae51c68e10fc3a)
[178](https://explorer.pkt.cash/tx/c7838d4322af70fa7f61298b96e0c4052b96e369e516a05c3a7abf6140dfdfb0)
[179](https://explorer.pkt.cash/tx/caf60b6584d9e3aec9517fc6eb4c33100efd411a386c5a59162ae60a73759573)
[180](https://explorer.pkt.cash/tx/2d7a3d7b512cea33ef3c0b5edfa13714baf0d19e22fad052e6b9f89c19660b0d)
[181](https://explorer.pkt.cash/tx/83f801b70335a990d983bd1675fa9ae167c6ae2af0c17ab8dd913249368971d0)
[182](https://explorer.pkt.cash/tx/d7e96c25658e5912ad5ff501a144a72ef80404e25180b441e8f685563f280a08)
[183](https://explorer.pkt.cash/tx/da20ca9858199ad4af157cde05c2ff4bce2eff3ed125546dbdd47aadc06dbd09)
[184](https://explorer.pkt.cash/tx/eb297f09703910c183d2cddcc97efbee7ddd5da2a30d73eecc148253612e83a9)
[185](https://explorer.pkt.cash/tx/954912eed3964f4f5a676b6f17d88abbd98f99a2b46cf50eeef7dd0e7e52177d)
[186](https://explorer.pkt.cash/tx/b106fb2661117761df6c043c7659c394487b654f0937da1f5ae5fde2a9d155eb)
[187](https://explorer.pkt.cash/tx/9ed2094fcb2371fc273ed8d65c12b8f1b1a8fb95c5cda61bf3dafed5927cad2d)
[188](https://explorer.pkt.cash/tx/0532e31fb1b5e1e47b990d974e07247216b7cfaa80b2df7f5acdb97d5ca21995)
[189](https://explorer.pkt.cash/tx/1948540cf55d0250f39b5e8cecf2622fe28ee89fd6652253f0b4217e150336c6)
[190](https://explorer.pkt.cash/tx/a41606ba89494e48fc8143ae1a08e14102b8d2993cb1960c37b1741ec3eb5e56)
[191](https://explorer.pkt.cash/tx/88625f397b16d361f9b9981814f1afae8ebed848633cf1d72dae7ebb435b3640)
[192](https://explorer.pkt.cash/tx/dca98b76473e7df2330aa61bb93397696c878fe8254af877bf02396116b28e56)
[193](https://explorer.pkt.cash/tx/ae4de577c753b441fb532613c10b3d6eef26d5e277c606c1f924566918b3a955)
[194](https://explorer.pkt.cash/tx/9d2c15897507438a3ffa5c002ce9b1f7104dbac3cd0f7cfc1035f0daa9bf4fe1)
[195](https://explorer.pkt.cash/tx/a946281a26556b999150b34bc0830ee05d5124f5c72f8716f9b9cdd77905a360)
[196](https://explorer.pkt.cash/tx/371a8c8b4ec5efc054b005accb4e3eeb110c3ebfedb5d6136daacd02a38a62e7)
[197](https://explorer.pkt.cash/tx/c41f9b6d3db839bef79aefe915e0af92483d058c54dd07ff4f9d741b2aef91b1)
[198](https://explorer.pkt.cash/tx/b001f23a0a4e78b4608e05d313ecdd047460486968e43b2362d021d8e780b011)
[199](https://explorer.pkt.cash/tx/ed0afd095fdaf15b4d2ef1371924e3c748cacc9f224c0517aaf54bf9bfc5c902)
[200](https://explorer.pkt.cash/tx/ea28de096f2727c1f68530415cfda221276c2a3e1505c70f02d782fbf15c0840)
[201](https://explorer.pkt.cash/tx/bdfde3ac316bbb19c5e650611f88591785b4a3e8ab7f29a78c1beb9871485ee1)
[202](https://explorer.pkt.cash/tx/156d8a154f705fee8fe3d022f0de8da70d9cd61e7279b8dc6e411f331766d1f6)
[203](https://explorer.pkt.cash/tx/62e8fbf818f97c34200530ef55b56a8422f6e69b58c881c19bbbf1a30c167628)
[204](https://explorer.pkt.cash/tx/bbbf31d64a0ea3149be493fc79c7b29c8d46b35f84c4c9f60736c7f273c2b7b9)
[205](https://explorer.pkt.cash/tx/5aa7904b63b4a1aab2729bd03496a6b2ab35aa4086fd8bdc551d949ffdf60996)
[206](https://explorer.pkt.cash/tx/da34d232730a454884594797d812c707875fd81f0152256d58e6472439e97140)
[207](https://explorer.pkt.cash/tx/90c6f8b78d1b5b1d99805298ce40cebab8dc33f6b916e070f6237c536d30963c)
[208](https://explorer.pkt.cash/tx/e8a2155de87b4cd1bcef47f484d3807e7449179c4c558220e4cfe4dff7909aff)
[209](https://explorer.pkt.cash/tx/4147fe610c3cceec5804165679111f2a979298de56e53fec59c8e030a3cc737f)
[210](https://explorer.pkt.cash/tx/cb2e9bc977d10b6c82b24440df8d4601d995e6fe7e19d2520921a65c01edfe8b)
[211](https://explorer.pkt.cash/tx/1db44a8f0ab9d7eed9b89bc1a9f86316ec851a2629bfe508ed2d018d16a1d5b2)
[212](https://explorer.pkt.cash/tx/07672e5ab4e6fbb88310c96b3e9d076e77cbdb79e2aa21282cd13a777db36437)
[213](https://explorer.pkt.cash/tx/d2d178bd5d81cfd911860bb341a05a5862b09a780dc6d4699b1de4f17de2d81b)
[214](https://explorer.pkt.cash/tx/7b959d80001bf8e325bb6ba7fe307f143b5c2e8b73911153f3dd46739df64e3d)
[215](https://explorer.pkt.cash/tx/8d2ac631e3e7e4782d94e620750561f6a5cb29eb983872d3e29e40943039041d)
[216](https://explorer.pkt.cash/tx/5e44518a18fc79a0f84dfbaa3be5141dc9f23d9c1a27c6a633302bc26a9b978e)
[217](https://explorer.pkt.cash/tx/9d0445175cd548d21e77e078b43e26b5269b2915ab0de649f975f41ab0d7a702)
[218](https://explorer.pkt.cash/tx/c1f3dd46e5712e051bf95bb5bda32976fb7e350c34e4f6faf57a7ab29f719c57)
[219](https://explorer.pkt.cash/tx/236780aee196623a442827ca3eb3376a9d155d05f0979eb2e86d4a537ae9ef0c)
[220](https://explorer.pkt.cash/tx/7ecd9ea86ced442254ac6e09a9eecf41ccc5bb7dc5d31b32daf122caf8b8badf)
[221](https://explorer.pkt.cash/tx/da374d32eedf985714f96e5efbe8207c452af804d5c0aa888246a142b476fccb)
[222](https://explorer.pkt.cash/tx/1a191e12f414c3d8c4b241c3ab2c257dc58da4c6e3a11969fbd374d1f9a9feb3)
[223](https://explorer.pkt.cash/tx/ea6809edb35d31bee687b816b82c23925bbd1bc8183ab5fa3d3e5a5a7708fd67)
[224](https://explorer.pkt.cash/tx/d5bbbae574d5f79bb58343bf9003fa47c9201b25252e66bcec5b1fb2c846b3b8)
[225](https://explorer.pkt.cash/tx/0e399ba9c79debcf7dc024e5b06a2dd86cae3cbfce9018bb96403f090d34b6ec)
[226](https://explorer.pkt.cash/tx/c5607027eda9162bfe28ea394e65c20e25efe10b2ff5e81c6b7fe7835db233cc)
[227](https://explorer.pkt.cash/tx/e57726bf8d358213f837847f9a90e915674e0f7b01ef2aa8e7546175ae87414c)
[228](https://explorer.pkt.cash/tx/14112fc4192af493746bdf7e40e9d8b5b134436ff396d01aff59ee912182d324)
[229](https://explorer.pkt.cash/tx/642de87998a5c9dc42070bdfd4d9d61e404e50fd9a45bff2ace68707dbdcc520)
[230](https://explorer.pkt.cash/tx/73dfe2fb0ab97e6e9845fdbfa107c10c244073937dc869597b808bc9d907922f)
[231](https://explorer.pkt.cash/tx/1198903a80695663c455e6f66c92966005e8b162af00c4b62c481c1de46b9719)
[232](https://explorer.pkt.cash/tx/764639738af3cdceea8ef2e130313bd2b5de9533754e04a26c851666d54cead0)
[233](https://explorer.pkt.cash/tx/7854f50a2aca08c2bc69278ced5ad1278a8363015ffd7b30e131a22dd717ceb7)
[234](https://explorer.pkt.cash/tx/00164e794f18d11d49ae603f265f1d806064536bf2f844b328edce6358e6bf2e)
[235](https://explorer.pkt.cash/tx/d6069053a2cb2046ccabbe1bb9c185c3bb46da8e31027072652af740e84e2c6a)
[236](https://explorer.pkt.cash/tx/71689256ef39cc50e760671cfdbfe0270a189905f716e247d3328ff8549e5d4b)
[237](https://explorer.pkt.cash/tx/b0376fe136cb4032dcf1c2176ad9042eede7472f76beb4658932dfad690426bf)
[238](https://explorer.pkt.cash/tx/7535e1304ad15044de4aa31efede6cd01dd681121333af3e2b615bcd572f2eb1)
[239](https://explorer.pkt.cash/tx/b9c508b749eea820c43b7156dddcee79afe2acdb4890a31e968fb5674b93925a)
[240](https://explorer.pkt.cash/tx/345c325c272ed6cf7fd5c7c58f4883d7785682a97c891b01c3717deab52e3e6d)
[241](https://explorer.pkt.cash/tx/13f31060a90d7c04711ad0b73c40cec5c2834a0444efa93a0163c7dad12bd0ac)
[242](https://explorer.pkt.cash/tx/196afac3bc6029ad6f663b2cd3f54583985b204fd6239d02d9289346aba4aa03)
[243](https://explorer.pkt.cash/tx/6c82c185c6f88c4f4183c6ba94b11184f9859d2465ba33bd02512c91117fd182)
[244](https://explorer.pkt.cash/tx/95775b33327abbe94042c1cecbacb7e17333f065d684bf2a77fd8c548e57e06b)
[245](https://explorer.pkt.cash/tx/61df7c20f6eb22837c70fdbfd18bef26762a80a5d2b53b02b6325944cfc5f39a)
[246](https://explorer.pkt.cash/tx/a0af9dbb0619e67484838ce54d8b9b67f30f1e76f20a432c6d712870b16334e5)
[247](https://explorer.pkt.cash/tx/13779ef9f4eb5f797500f7f6763693953296dfcebed6e984dafe165012c42405)
[248](https://explorer.pkt.cash/tx/df2ee8032e5e0ae827f7b7ad788414819e590bdbd32b33daa6ece28db795ff70)
[249](https://explorer.pkt.cash/tx/8dd52847b0ea94ad609b2d7e99eaf412bcca423872dc9e7d3fbeb8ac80238770)
[250](https://explorer.pkt.cash/tx/dd75a1ce418bd5ee75f546da7cf1baa02c9d3b63d54fb5f523c362a08f5bbfe4)
[251](https://explorer.pkt.cash/tx/6d08f36db3264b128eacff1b4ce5aac17ba495fcf29a275ea6832668b6d19ba2)
[252](https://explorer.pkt.cash/tx/e250b9532555176b36684c83b3664dfbf36155291fcbeae55c57485d7578ba64)
[253](https://explorer.pkt.cash/tx/195324b093964769dbbab4c13706d4ae03e80249484ba94ac62552c7ab156290)
[254](https://explorer.pkt.cash/tx/a7cca070a8b47473351196242b1685891528618ff7d8192401ac40525c7ed8b3)
[255](https://explorer.pkt.cash/tx/ea67b1c50ffbb0a7a0fde896d88d1c293d8756f8b6f87394f5b7af1c261b4ac4)
[256](https://explorer.pkt.cash/tx/1734818858b6ffa8ace006036ab4bd334fd01287a4162d29e05f7f209a3fde40)
[257](https://explorer.pkt.cash/tx/672d053f7881251f56a408209ab28430af970e6a8190f001833a4d8101aec5f6)
[258](https://explorer.pkt.cash/tx/ebafad90920a0cea78d1458e55efb2b1ddeafd2bd23a096428c317f8607c53d8)
[259](https://explorer.pkt.cash/tx/cb372c06d06f97009a419eebd98ffcc80657d0f6f010f0e6dfa2fb72d61a0474)
[260](https://explorer.pkt.cash/tx/4e748842c8b103bbbd0d17a8146a07d329b7457d924710e566148e21fa87828b)
[261](https://explorer.pkt.cash/tx/02047a74272fa1dc4ce33bb888bfc3ffc04be3cbfafa7dbadd4ce34889d9339e)
[262](https://explorer.pkt.cash/tx/2af58989afbca667b3bfdd465ee3239d6f7d81f3dab959a21716e55b8d6c19c5)
[263](https://explorer.pkt.cash/tx/bd8dc7f1d5e15ada467e177963f2c14db6c7e0df5745f166497e493809b487e2)
[264](https://explorer.pkt.cash/tx/f6ed0b83903f6dc4c7eb9b9fb26021d46600eefd6389758961de7b389d51d81e)
[265](https://explorer.pkt.cash/tx/a625b5260e1380f5d4b4e9a3ab584b44e71b08eb38e84d296a8800543112e43b)
[266](https://explorer.pkt.cash/tx/32f483d8909baec2667433841439dc48796e92ef77154c7f17ed74447771927c)
[267](https://explorer.pkt.cash/tx/6f45a2f446696d3dbc380ddeb628d87335f964b44098916036febeafeaa5020d)
[268](https://explorer.pkt.cash/tx/87ceeedc309b6ff7e5aa082a3f2db70d28fd10470958e76585f192fe9bd50b24)
[269](https://explorer.pkt.cash/tx/c2e145a0c917485fb80a4b3506b9d05ffb41dcf2bb825002258138f65df3be0d)
[270](https://explorer.pkt.cash/tx/6f03e4c02d16a0976675a502ebe66ec81a16b7add2496e5c2e53979efed8ef86)
[271](https://explorer.pkt.cash/tx/4e1bf816a9af2275f640640e15837e08b55301db9ba6388c5bac980103d7a2f0)
[272](https://explorer.pkt.cash/tx/af1fb67a4b65e714bd9e5fe5d17fae9b7069b7a34fd9159f507852d2f60e73be)
[273](https://explorer.pkt.cash/tx/498188960f8914c92dd973086eee5afff2347d4e56ad27ed3e701c4e22b7d3e2)
[274](https://explorer.pkt.cash/tx/ef23ec29837913bd83818522f3a9e6b3771dea43211407fdaf47f3d1f3fb00b8)
[275](https://explorer.pkt.cash/tx/5bd88df16d38ce94f4654899ea6884d9cdcc21064ccf8ee96bd474f08e5bb330)
[276](https://explorer.pkt.cash/tx/0daec001124d9b4efd289f5fed48068a6d4677a4a252350a32322c775c794ac3)
[277](https://explorer.pkt.cash/tx/3ebe6e58c45f8ab6ee7d2b00e2d755712eae426a29c29a24a22e7449445f80d6)
[278](https://explorer.pkt.cash/tx/56bfc7908e2368ea4a8af8fe3d4c49fe38d775bd3bd5fec1705f3937c9142b19)
[279](https://explorer.pkt.cash/tx/fcf29e7bf0c5189db0da1621fb54eac0fd51acccf4773bdf8ce459d9c9b3c3b9)
[280](https://explorer.pkt.cash/tx/59a7c865f29682a87695724a759ffc0cb9f0a46f95de57051547713b718654d7)
[281](https://explorer.pkt.cash/tx/bb9bb8883bd4f1a09e57f0c9d050bc2731fce2cfd49ce21fde818ce7b6cfbe1a)
[282](https://explorer.pkt.cash/tx/f864f70a8b9a66963ede8acd7d9cc4940788c440a33ed121d00f36e0a442be6a)
[283](https://explorer.pkt.cash/tx/ce38dcc83126caa779a3dbcc7d7a6449d7046bdae37d8a90b5b182f9576b6bc5)
[284](https://explorer.pkt.cash/tx/dd18dd1de2d4c83afb3b23743a2ebe421e9452a22c60622c65c843207294d8b8)
[285](https://explorer.pkt.cash/tx/e038a97da4f696a832888f0fb783b23e120718c77f19bffad7acf14b1f3c0812)
[286](https://explorer.pkt.cash/tx/7650a27a0d28b4e3e8febf1bc97eee1ce47351d130fe2bec2c317f1065c656cf)
[287](https://explorer.pkt.cash/tx/f2ce94fbc5779642ae3898b208987603f196e9d2b9b8b827683e7208e8cdc1be)
[288](https://explorer.pkt.cash/tx/1ac9517aa3ddc2bef4c382efe15704ba5bb2fc6c2edc5e683b5fabd2afcd7a44)
[289](https://explorer.pkt.cash/tx/00bec76f5850d4dbdd77415ab3de8b9020fb428bb9f5715fa30c77d57f8d3673)
[290](https://explorer.pkt.cash/tx/a3a3545472efc361f97ec193c84dcde66baa3d1425ae7274392b9f5a2494c171)
[291](https://explorer.pkt.cash/tx/1ecab4c53947b8acf86a3bad30a2b6ea333026857275923fce66b34128c5f68a)
[292](https://explorer.pkt.cash/tx/aae97ca11b874579aa7364bab1db19881d1b77798d3b5ddf1de2e7fb7050270b)
[293](https://explorer.pkt.cash/tx/6a78f097f2fe6854557193200e93382e92c9dde9f169fbc773d66022e75524fa)
[294](https://explorer.pkt.cash/tx/2e47c8d13d6e83687a2c5e94ae85b6d5027fd1e1a88f84163fa4142d482c7e5a)
[295](https://explorer.pkt.cash/tx/8db7e28619564ba01810b4d0d11be0eb528d3da88437b958cfa8ea49ee132706)
[296](https://explorer.pkt.cash/tx/b8d9330f12c442abc9427a8167a5fba8cc8f98a61ec865145975b9f1120d352f)
[297](https://explorer.pkt.cash/tx/989e2e694fdc73ec01f93afe309871797cefbfe6728b34d070a2e9f056ea2f35)
[298](https://explorer.pkt.cash/tx/297b943c8dbf74a6b1418c31a8154b11c65b088d3fdabc5e8f4e4c6c4d7efccc)
[299](https://explorer.pkt.cash/tx/db67cc2f82b0f32658e0cbf3493e63e5d1dc5f6b8aa52ee024985d0d5f9ac14e)
[300](https://explorer.pkt.cash/tx/7f683cb9aa9eb65324926ceba015319785c72ab5c7d32bf3290e618a910c5ce3)
[301](https://explorer.pkt.cash/tx/c84205b809e4f57cadf1e9fc54b64874692169b6715b0fe2b852701cc919094e)
[302](https://explorer.pkt.cash/tx/ff1b6e7906fd1dc55103a8f468c2096c0b99333c87142250be5f671853535f18)
[303](https://explorer.pkt.cash/tx/a22d391aaeaf8f31c828c3d8c516129605e90698c52eec5b36bae44b0dab708f)
[304](https://explorer.pkt.cash/tx/c74d3ce1ddbd4c259e3fb2252c43a92c22b71c57e88e119872948bc2c7132c55)
[305](https://explorer.pkt.cash/tx/44ccdfc2a1573732b8a020a61260a2347aae42cfe4e6817f4c0fa5542367a6c2)
[306](https://explorer.pkt.cash/tx/788b91541abbb7ece7cd5bcdac3f34477600bcc88b485fc16a4162619eebeae1)
[307](https://explorer.pkt.cash/tx/61b1d6812d6d779d518663faba48c64991795cda829ad06a82ec2e939cbfa4e1)
[308](https://explorer.pkt.cash/tx/da4ed9c46a3ecccdc53014b4f01128f67a7be63b9a9d22323818c81cdacb979a)
[309](https://explorer.pkt.cash/tx/8e41a11bfba11fba8eab8aa79f553c6b999617f5303742469985ef1f167cb72f)
[310](https://explorer.pkt.cash/tx/a18703e005257d42223f9bc26f9940b83aaea69b27b101d5cffe0e60fcbf6351)
[311](https://explorer.pkt.cash/tx/c42475e5b97119039189bc9b4b2ddc7aa3b088cdaf760019b374e0ebde12b3f2)
[312](https://explorer.pkt.cash/tx/1e6b197de41f7f04e9c35998ced2c82f85a8b9f6f87426feb200fa17a3351d16)
[313](https://explorer.pkt.cash/tx/120eefceae018af47ea753e824da14d98e5098c6a77071523ec01864a9ac70cf)
[314](https://explorer.pkt.cash/tx/feed4d5973151db162f9c6f7a403b73b24a3b697e526f8930a0a7f514c0be05a)
[315](https://explorer.pkt.cash/tx/623ab79cf1e360384b708708192251b8adf24578a427b16905d482a8a716818d)
[316](https://explorer.pkt.cash/tx/ebcd199954e751bc7b38b1c73bebfc08cd624ec476dd21041e9e5c751ff3b28c)
[317](https://explorer.pkt.cash/tx/d8774c72077a35b1bfd9b8c80c615e26cf3707ea13e98588a326cbbd06c85f16)
[318](https://explorer.pkt.cash/tx/f6693d680e6a8028c4532a954d486121ed334cb2938e8e6c54f69b8479f6232a)
[319](https://explorer.pkt.cash/tx/fc5143cf75aac027fdf1157fbe4347b89c54688604b5a976d2aa5715ef0d52bf)
[320](https://explorer.pkt.cash/tx/a3c2f669cd3dd4ce5f9482b31fa813d59ecc620dc64e64a06d0320df96c7f646)
[321](https://explorer.pkt.cash/tx/2e9d9138b7ca3ddf9036a67de41128eef8f5a5c5e09019846d93ff679a61c8eb)
[322](https://explorer.pkt.cash/tx/e13b11aaaa25a7e4e3ec582280924db2657aa11f8711558d37fb450026625f35)
[323](https://explorer.pkt.cash/tx/d98526bd94aff218ac712e84f9ec96f99207ddcbada3aca1d58065b9ffd8b008)
[324](https://explorer.pkt.cash/tx/ae7e7d127da793de0fba34ce0d7b85fa25ff0c4904861bddc7eaf1339aa9714f)
[325](https://explorer.pkt.cash/tx/4d0b67a6e8212aa8901047494c02042b18cc1d20a5bd444bcb75f0571d00405e)
[326](https://explorer.pkt.cash/tx/37d44a54877aabd15ab035478cdf90520d254389cf742472297c245c72ca710a)
[327](https://explorer.pkt.cash/tx/d36c025bcbab3230f10e82404da22d4f6f8ea885b6c6570523a431d73454bb52)
[328](https://explorer.pkt.cash/tx/3d9316f90110bcc8836c6479c3f2c716ab720690d4eb6a357a38852b70329f6d)
[329](https://explorer.pkt.cash/tx/59c321fc80e221309e81a18869e47d1bdffd1f1694cd6c32f997a999c7381fa5)
[330](https://explorer.pkt.cash/tx/6f88a9cb7af40fc44dfed1ee100c94235b44b908a3d5c2fb5c644a4fb5f7f659)
[331](https://explorer.pkt.cash/tx/880d30c5828497f2961884434a8fbd33157ffba8bee44efc5d6ecd155e40a4bf)
[332](https://explorer.pkt.cash/tx/9f3d8a6b61f097cb65ff2b9b3aa20c349b91d205a6a6522483d6a701ebbc5c2a)
[333](https://explorer.pkt.cash/tx/5ca32d27ab0e98b0e35a938565e22f057814f1921da5351ea005a4278bbc4532)
[334](https://explorer.pkt.cash/tx/a9b3a611dd31789dbe86aaf9bfa9f648394424a9cdba1b5e0838e618bd6d388a)
[335](https://explorer.pkt.cash/tx/081dac0bf1cec4a16d1d7f1d68aa0e9fefd45a99371cdff4d7be52798f1765cb)
[336](https://explorer.pkt.cash/tx/65e16e11d6ddf656e9ad6821fefc48ba7bc3d186f4a991fe865fc54716deffeb)
[337](https://explorer.pkt.cash/tx/bdd13ab028436a9038862b79aa69404da78ef611262f702f55b5fd07cab04adc)
[338](https://explorer.pkt.cash/tx/7ac6dea091a5c31dd8f1b4e13dbd2c881b6d4ff73b6cff61f40b2c600dc44a69)
[339](https://explorer.pkt.cash/tx/c16858b17a01e36f51272995f13ed2265178ab51ad91b1290cf91b3c070e729c)
[340](https://explorer.pkt.cash/tx/1db60dbe99271a63fb6951055efb26e92610f3d983c025e9bd5314e9eb6aef03)
[341](https://explorer.pkt.cash/tx/e163f86b4aeac2a469ae768908f2c2b54ab3d84a6b2a1cd2c40856137b864811)
[342](https://explorer.pkt.cash/tx/655fd88c1a572007f05256b7937bc52bd5693e64082cf330c2210bc13b8ecb5c)
[343](https://explorer.pkt.cash/tx/00996902c352c1fa0832679e24b0a228a67cb0c3f99d62a5ef001d07bc5e7569)
[344](https://explorer.pkt.cash/tx/6c42b7a72872a5f6db173f39adc58903ec770596adfb10e2dc061aa4313f5b66)
[345](https://explorer.pkt.cash/tx/a24a397b3ae0d94cb4cb9b4978b95c7c79e834db38e8f1b93611dfeabe0a4b9c)
[346](https://explorer.pkt.cash/tx/3e4dc51d944571a4a2b646983d578eb8a179be29c1943ff30fe3cbb2be034652)
[347](https://explorer.pkt.cash/tx/949bcdc2d6926eb6509d1f23bf1e924a42d00048709f464705bcf5458555a297)
[348](https://explorer.pkt.cash/tx/a76dffc562302a23b21b2dfdec3d1eb8505f170d1fd07b097913e9f9642952a7)
[349](https://explorer.pkt.cash/tx/0a87a9e281e212313c0822ce486d444e62791d6ea0a0885933d0ac2ca7e9fa44)
[350](https://explorer.pkt.cash/tx/47b295db4c27a098a3eb8af3ca0468680e1483c4403c3e3a90a7fb0fc25f2fcd)
[351](https://explorer.pkt.cash/tx/fb3c8e4e08dc47ca12bc415bb5894a5cd23f3405b4af9ba2bd0ebebcd8582fd7)
[352](https://explorer.pkt.cash/tx/090957f03549ef701c16fb5049ddc9cc551e036adabf0524ab0145b0a99fa897)
[353](https://explorer.pkt.cash/tx/bcf8d1a39885296c751a6031507b2938c4842491c0a9a750f5c50f9468777c85)
[354](https://explorer.pkt.cash/tx/969ba20b17410902bde8f5aacbe5f1f4e673105f430a6cd684f2f61bc629f18b)
[355](https://explorer.pkt.cash/tx/96f3d6cabbdb4e9b055cd5dced0f28a99feb6078e4f529382d27f0a3f7b12325)
[356](https://explorer.pkt.cash/tx/689f5a9d4ba53d837c1cbe090ba68c03c20f12eb17daf7ccd6be5e1c72311fc7)
[357](https://explorer.pkt.cash/tx/2e00c01bcc185140504bbbdd0c77911dadcda118563e9d9bd4db22fb2eecb31b)
[358](https://explorer.pkt.cash/tx/9a00721f5f4f5815e7c03b77318892c1a781b7bc88f228f0ffaf59df1a200d55)
[359](https://explorer.pkt.cash/tx/6a36820408ca45cfe92376cc5a0a636cd400656ec0a4fdd3cabce138413ce9a2)
[360](https://explorer.pkt.cash/tx/237359d0853cb402d4d47741af250b16b7ab3623d7b73bcfb43485ffc9d3d77b)
[361](https://explorer.pkt.cash/tx/efe8385c2de55db817c65ae8be846a380b29fbd0360ac0e0eda41eb4b76615c3)
[362](https://explorer.pkt.cash/tx/b70fc1c5aece4e220385f3118221a7ecc5a659e7dc9a8f65329faab4beedc9e3)
[363](https://explorer.pkt.cash/tx/99b2d1b43d44f08aaa3cd6477a2309591fb0cc7814da565968008765e117cc27)
[364](https://explorer.pkt.cash/tx/c291385c0da335d6714af99da43ba96840aa6c10c2499b1caff736baabcbccb3)
[365](https://explorer.pkt.cash/tx/87bed892807de0fe70d2f30db9915bbcbb076466d4a019184806413ac2156159)
[366](https://explorer.pkt.cash/tx/8f29cf3811bb161e48982d049226e0225b1fdaa78f2a20487cb26eeb6b9ab48a)
[367](https://explorer.pkt.cash/tx/20699dabf36a0d7bdf7fd76f2917613eb1fdef2655fd3c67192caf0f36638696)
[368](https://explorer.pkt.cash/tx/9171394046ff93240d418708d931e3b23b72a9a918f6bb06249afc3d6643922e)
[369](https://explorer.pkt.cash/tx/1a7294b383341ffe400fa6ad0bc68624595db7c15c35d7c53a750e3939e8c3ca)
[370](https://explorer.pkt.cash/tx/c2ddfabd1beff950b3a8d54191c668e4887fd2eff295add84e9b538baa632893)
[371](https://explorer.pkt.cash/tx/0be16cac101f1eb772365e38ab59f8465a36e1a169aed635eee354c9c091e001)
[372](https://explorer.pkt.cash/tx/347d7d441bdcc3fcd0e4123ff610c030828b7e1edfdcae3b206b6571e6eec501)
[373](https://explorer.pkt.cash/tx/36924dd5cb9067ea9df6c7c28fa4fddf7440ef7927a61b6c7e2675554c3d9e10)
[374](https://explorer.pkt.cash/tx/392075d1aa414d3482fa29490737db8703bb3460657f83267ec0dd9fda00e10a)
[375](https://explorer.pkt.cash/tx/1502cc4a9323bc0c628140ffdfed3eccdc8758fdd30c4da4427297482e386fe4)
[376](https://explorer.pkt.cash/tx/4a7c091018f03de7b4b35488ae8b46bc5a3e268aa09f0e950456d1ed17dc99f4)
[377](https://explorer.pkt.cash/tx/3312a568ad52941cf50f2f3d7c654b61aa9402474709da3f91715a0d0cdf4127)
[378](https://explorer.pkt.cash/tx/5df772cf7a6705b2864979435c753bbe1949f2035c04557ab916f7eb17c757ff)
[379](https://explorer.pkt.cash/tx/591f8fd3e4f886a1968c16aef599162980a1d4ebc6e689655540de8be81daa19)
[380](https://explorer.pkt.cash/tx/5c185fb3cc54e3397a278d33b001f9615af4d3d4d34524484c36b9d53286503f)
[381](https://explorer.pkt.cash/tx/3b8768dec9404be6589dd582ba8e39ace60115fea6b1071e51c46391b61e3974)
[382](https://explorer.pkt.cash/tx/a08ce5d81311236a61ddcb630f85b36d0cad3d431e3f2dc195f33fc219a0b092)
[383](https://explorer.pkt.cash/tx/e149430503dc0eda854fa3011a954630882675bdb26c304122e3e7dae89ca3d2)
[384](https://explorer.pkt.cash/tx/994a412b37c871177e3b23220fa859ca954ff5a8c2fbb75746ce1321cb404eea)
[385](https://explorer.pkt.cash/tx/b86b5c6af792bda9e2992c4a3e9d9e907c38346fa8b397f936b3b47a6f251d05)
[386](https://explorer.pkt.cash/tx/aeb96b94c095004fb26ffbc724cc7260e74b93993da878312914a39bc7bb3fbf)
[387](https://explorer.pkt.cash/tx/9c9980c96ccd840a23bff5b75672b47c6466f82f0e3ff10b6e6e19cd612be196)
[388](https://explorer.pkt.cash/tx/7a8fe2b8f8647fe4d0c2707358475ba8977098435fd2ac17bda82332b60ab792)
[389](https://explorer.pkt.cash/tx/f9de59914175e50f3b0dc50f03b09a575a2e0a2093064db2b39b1c2bc3fd0152)
[390](https://explorer.pkt.cash/tx/91601875eb9ffdae9bb76554d5998090d4c5b63c202a4851a1c4f65b3ea5133e)
[391](https://explorer.pkt.cash/tx/6e2fa4912cb0ed4af55051565cd1f166bf81d25a15819718641d724e06f27f17)
[392](https://explorer.pkt.cash/tx/6e55b03bb90c614ff2bd046c9bfa5087afe33d53030cadb52fffd1ca8f51e27f)
[393](https://explorer.pkt.cash/tx/c6d30fef3d004ddf71c0a8a8535e93cc09f0c471d888787f47645c95354f2092)
[394](https://explorer.pkt.cash/tx/df9b87f331c15141212c51bc810585484a37716b97522f7ac80284aba266055d)
[395](https://explorer.pkt.cash/tx/e915976971d6c9edbf1fc752cf4b3a0f834ddca3f29c2f9db06deb9a99ef8a39)
[396](https://explorer.pkt.cash/tx/328515ab11e28d015366f4ebcbd171f64d66711360ef45f952e624ce41065df6)
[397](https://explorer.pkt.cash/tx/dfb11038e44e6131997b995b8acec40e988e50509200f89943bba4f68d9793e3)
[398](https://explorer.pkt.cash/tx/0dcd94bbde730b06fedd206b554cbfa23323075a15b4867da8cafbe60b08dc3a)
[399](https://explorer.pkt.cash/tx/e779fc0238cc60d7f23a55c11c949aef94f4b16f83b7b875dc9cb3912f8fa79d)
[400](https://explorer.pkt.cash/tx/94705676ef33485b36cc09b4603fa0a697f3f53fc2237212a024bd4c9c282448)
[401](https://explorer.pkt.cash/tx/4a6b4f8e59d9adf007b81bc9deb60dde4019c6854a46305a40820114df3bdf5c)
[402](https://explorer.pkt.cash/tx/bf7265b719a6569c22fab28e45eb05569b0c746becb596783c76e23c6d5d3549)
[403](https://explorer.pkt.cash/tx/52761c895e485728b09bb176dd15370348e9ee6f40d1f1ca4da7127806d85093)
[404](https://explorer.pkt.cash/tx/bb7d7733a308765b6b17ac01be8007dfd829da470d097b588b9a0ea8b57aec00)
[405](https://explorer.pkt.cash/tx/19802c2b509f0d1f68debd1c045120a3627b4ec149bd006f9a5ee14a1411d9d6)
[406](https://explorer.pkt.cash/tx/44e47ab62fa379a42c2e70cca5ef00a1f56e000d656d4d773ec9c4891c26b948)
[407](https://explorer.pkt.cash/tx/bb55026f300a0b0e0489adfc4b9fbd0c8caee186e8ecbc4760ecc74b9b8de5f1)
[408](https://explorer.pkt.cash/tx/91ff1941de2f1f61dc15813aed1842b1a86635e4af5184f6dc90071b7d0ce839)
[409](https://explorer.pkt.cash/tx/4fe6d373aedb0d40675caffd9f555cd5c3cb185cca4f43071295226877284f5a)
[410](https://explorer.pkt.cash/tx/d015733799f433ff2bcd8333d1b20c4e2ebeb2534ff22a8c9a1dc3dc1a052cbb)
[411](https://explorer.pkt.cash/tx/99500850b9873a6a3bb1592a78df1fc394c5d93e59f44ba368b66616ed840c60)
[412](https://explorer.pkt.cash/tx/207dee6e45a4448f4610dd16ac3944028c2a5da7be22dd874dff7c18ded0f679)
[413](https://explorer.pkt.cash/tx/3d875c2761dfdc689dab599138637e7222207301d922bf535555e1143bb859f1)
[414](https://explorer.pkt.cash/tx/6f0e6ebafec611743b7e6ed100918cc9a90c37a6c7678ebfc5fa0242951b2208)
[415](https://explorer.pkt.cash/tx/f714ef73a827082427633d2e698ebb9528b0011ebc2b23d5363eea120127bfac)
[416](https://explorer.pkt.cash/tx/a8d202b53ee84755ff142e433802d1d0d1e5f4a48759159a21b6a2b1f993fa00)
[417](https://explorer.pkt.cash/tx/f9082115b0087ea213e5d64763921ada5ff771ac3cfc6e69817832e34ba44066)
[418](https://explorer.pkt.cash/tx/4e05a1e613b0aed0ccd00c5eac58a37f17578f64766adf92b6998672fed7841c)
[419](https://explorer.pkt.cash/tx/f933fd232396b08e1f9dc1b31a705b4b88528549ddc59facfe3f02c3331233a5)
[420](https://explorer.pkt.cash/tx/c4cb694ee4607ce0677630499459e9de7e1d21f199555a22d72bcaf05983c9e9)
[421](https://explorer.pkt.cash/tx/2f7be72b04bedc0ea87e1acbd86a0ff5ea8f288637577e2f32be2a399c2c0021)
[422](https://explorer.pkt.cash/tx/c8d73d81bcdeeec0375dc14087798f859506b31e96892d10fe2daef0b6478cc1)
[423](https://explorer.pkt.cash/tx/79c65d8038abd0db55593a07aa679274e5c2c38e47d206d90553f81dd09a7aac)
[424](https://explorer.pkt.cash/tx/b7adadf52af41c8accbcd99a0fa82389726ad3e87d438453f43318895334a4b6)
[425](https://explorer.pkt.cash/tx/1c13b96993b5a942de8f896133738c176c1b4946d869ac4621e493ef713cfc21)
[426](https://explorer.pkt.cash/tx/3764c84fda62d7cb4ac95f37c465aeb6f2d7f010efc5c9ef692fdc80e3d5e9d4)
[427](https://explorer.pkt.cash/tx/7216fb87ec77f8c6f31f7e03b11b020459b960a4993d030167a533550a6c9661)
[428](https://explorer.pkt.cash/tx/7e805ab5d32c9ed318d58132b1a0c1572d20792acec3e08a61876dc0f825b17f)
[429](https://explorer.pkt.cash/tx/3cb538047ea05004256504496187ab6f5a9d5beb9a8bbc6f55c2a92c9ec872e6)
[430](https://explorer.pkt.cash/tx/f1a1a86c6e1578d01a32d492c75facedb8c6f3b0ea8c49c2049541604a4c6a38)
[431](https://explorer.pkt.cash/tx/aefa502ac416738a6f467f3582ddac81f3f76d968d58012dba9c0c6efdc55ad7)
[432](https://explorer.pkt.cash/tx/3905a2383b79a6542257df8f3041b5d565fc748eb93f8ec8c2176832859634c2)
[433](https://explorer.pkt.cash/tx/1086dced1886cdea41ac46c922adf4b9a1ea56991f2a5271bb0a7a130606e749)
[434](https://explorer.pkt.cash/tx/eeb891a7039ee696878b6c9c827dcdb8949c5779f7a68a77c941f5c8be8344c7)
[435](https://explorer.pkt.cash/tx/41b64d41e2e5f8286d3a8eaec4dcda404a1ae34abfb6ffde0a69f7ab3a5d950b)
[436](https://explorer.pkt.cash/tx/c7050f0e4a4df77f030f1b731ac995ccec088e0f9a03b287a5899703e1a3a402)
[437](https://explorer.pkt.cash/tx/e068d91f01b71c776344ea1f80eff3505390784dabc23abf4d015fc2592158ea)
[438](https://explorer.pkt.cash/tx/3f5613cc32fccf2e18905d43cea53bb06f261ada7243e2a5af45b159c2b96fe1)
[439](https://explorer.pkt.cash/tx/aa5f397076307bc62309fdcdc856c05d2683c8b301c375730acfd0252ce0cb30)
[440](https://explorer.pkt.cash/tx/1c69a8b6131df9b67fbe4ce0d84f8b69bc7d3cf45459cc31da82cb09cebd2445)
[441](https://explorer.pkt.cash/tx/5e78471cbefc38b0ab22d38f037878f54fa06f2099831ea18062dec218c1bb0a)
[442](https://explorer.pkt.cash/tx/86ee1ec39ad515862004a212bd573ea38d53c724a96e2b0c6ed6fc8fdcfe4163)
[443](https://explorer.pkt.cash/tx/709735e3745db692dabb9bbac7e01c774d9726580666ed9676430fe8dba472fd)
[444](https://explorer.pkt.cash/tx/6cac57bacf5e3ff6be1213eec280eb91ab89ff872d4123661742e24d7e053bff)
[445](https://explorer.pkt.cash/tx/d5c5edc0527ac7c74988b40aff68a13200a7a3fdebe2272ca94257df6efc8240)
[446](https://explorer.pkt.cash/tx/452e8f3ec67825a1aaeff7654a9ab6060424205fac617244269aa75cbe9f57e1)
[447](https://explorer.pkt.cash/tx/054a38d214d5b4b233d3d5b70dff76ecb0b098675211dec8487d02f1f34b8eb7)
[448](https://explorer.pkt.cash/tx/d285bfd6285cfcaca9fa7f885568554b4aa47d7954af3448e021e440fd8a6f0b)
[449](https://explorer.pkt.cash/tx/ed6669675280fec19320e96a998520b254e306580e1b2d24c0dcbfe24efed775)
[450](https://explorer.pkt.cash/tx/e148d03f4e5f9e092ca7c672c778f1907a9c50044e31f50421db30d7cdde6490)
[451](https://explorer.pkt.cash/tx/c5ddd902f08dda7a59ff07dc706bee454273137b86b5c0900731cb95f276ead8)
[452](https://explorer.pkt.cash/tx/4cb8292cfee6d7fb25104f399aadcb16e49be0b84868391eba060f94d6672cfe)
[453](https://explorer.pkt.cash/tx/a4a90caa6fe8dda4a077e77526a2f6c0634180bde84ef07ff4e42d3b821077c9)
[454](https://explorer.pkt.cash/tx/3f02e9b7338dff4b7495f4e5e69a3c82636152af4d27a1990ea3294bbbcac1d1)
[455](https://explorer.pkt.cash/tx/3e2e669afbb4fa4f32205b1ee3eabcb8dc587556f09f558f47d3d838bb4bf493)
[456](https://explorer.pkt.cash/tx/baa70d39201ae3919baffb6e2d02f9a5a64382af0cd964c8f1d6ea092eea3f28)
[457](https://explorer.pkt.cash/tx/93a7306cb19f2c0a1872c63bbaa716851a132dcb7cc1860e785fd0ed8fca428a)
[458](https://explorer.pkt.cash/tx/1fb6c0dfbc172a235da00bb81ecc502ea16057fe6c134e5c74fbf76c1046c291)
[459](https://explorer.pkt.cash/tx/428c92638c76ba3b60a722fb9f6083a88f6b9e3e9987ac2485ba30c71e885111)
[460](https://explorer.pkt.cash/tx/5a8061578ade92560763fb557798c6755e5b7fdd5adf143a81dffd2aaec07f03)
[461](https://explorer.pkt.cash/tx/7dffe20e10be7b21b6fd11a0b05d7278d3efb05b1a68be3735a60ba0e657445d)
[462](https://explorer.pkt.cash/tx/1fbed3b36b61fc65d6bf1642b90b52d932b561299001dc289a99e0e970c47b1d)
[463](https://explorer.pkt.cash/tx/d262acc87e7339b7af272b28a72406f7bd4fe77e8fac55935c98e8b5b9c09a87)
[464](https://explorer.pkt.cash/tx/e1e5e7810ad380bca8f363a021e69436fb3ecd06b63e64638d7122cbe7d81f24)

This payment was made in more transactions than usual because the NS address had accumulated a large
amount of dust payments which needed to be folded.

This project is now done and can be moved into the "complete" directory.