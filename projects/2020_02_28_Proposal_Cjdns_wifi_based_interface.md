
# Cjdns wifi based interface #

* Project Name: 
* Contact Email: alexlightman@me.com
* Project participants:
  * Kirill
  * Vsevolod
  * Dmitry
* Projected duration: 6-7 months
* Projected effort: 12 person/months
* Requested PKT contribution: 36M PacketCrypt tokens (3M tokens per man month)
* PKT address: pKHsMf6Eg8YB2jTJUpdRbCj7RpvpMpYRkU
* We suggest to pay contribution for every milestone
* Project status: PROPOSED

## Project participants ##

### Kirill Varlamov, Architect ###
Distributed systems and decentralized services аrchitect. Cloud computing and network technologies expert. Kirill graduated from the University of NRU MIET. Together with his colleagues he developed a p2p network for 
His specialty is Telecommunications. From 2010 to 2015 worked in Cisco Systems as a systems engineer in computational and cloud computing area. 
 
From 2010 to 2017 Kirill was a systems architect in Brain4Net where he had conducted the research in Software Defined Networks (SDN).
 
 ### Vsevolod Mikhalevsky ### 
Vsevolod graduated from the NRU MIET. His specialty is secure communication systems. Since 2008 he worked in the leading system integrators as an information security engineer, took part in the development of IS subsystems for large customers. Was also involved in the development and support of the CISCO teaching laboratory (MIET TU). For a long time Vsevolod worked in Digital. Since 2017  has been studying protocols and was engaged in DApp development
 
 ### Dmitry Suldin ### 
Smart contracts, decentralized applications (DApps) and web services developer. Key technology stack: Python, Django, JavaScript, Solidity, web3.py and Truffle.

 ## Project summary  ##

Create cjdns wifi based interface for the PKT network. PKT ecosystem includes a special broadcasting network and a protocol, that can be used for building decentralized VPN services and Web 3.0. PKT team is going to create a worldwide online community of PKT protocol adopters and unite all supporters of decentralized web. Also PKT is a bandwidth market based on cjdns protocol, which rewards its members for bandwidth delegation. 

 ## Project deliverables  ##
This project will deliver:
* Contributions to existing software: https://github.com/cjdelisle/cjdns
* Note on delivery: the team 
 * would plan to set up the software development process in two week long spring
 * would be ready to discuss the current spring results and plans for next sprint every two weeks with the Stewards and other stakeholders


 ## Success criteria  ##

Verify that cjdns wifi interface is working. 

## Milestones  ##
Creation of cjdns wifi based interface. Here are milestones for the progress of the project by which the network steward can evaluate the success of the project.

### Milestone 0: Kickoff
At the beginning of the project, the Network Steward will pay out 9M of PKT to the applicant.

Features expected to be completed include:
   * Server: Creates a WPA access point which is able to negotiate a different key per client (e.g. using an EAP protocol)
   * It is important that keys are negotiated so that the protocol is not subject to Evil Twin attack
   * Ideally the AP should not appear in wifi scans, if it does then it should have a common prefix (e.g. "cjdns-" followed by a random string which can be a public key)
   * Dependence on installed hostapd/wpa_supplicant for the server component is OPTIONAL
   * Android + iPhone demo apps
     * Simple demo app which can connect to said WPA server with one button
     * no UX design necessary, the app is purely for proving that the technology works
     * Application must be able to connect with one click, no special procedure such as downloading certificates
     * Application must enable the installation via the normal route from the app store. It is not required that the app be published on the app store, it is just necessary that it can be installed from an app store context
     * Application must not violate the guidelines of the app store
 
Upon the completion of this milestone, a report will be made for the Network Steward and if the Network Steward accepts this report, 9M of PKT will be paid out.

### Milestone 2: Upgrades to server component  ##
Features expected to be completed include:
   * Able to connect to or disconnect from an AP on demand
   * Able to create an AP on demand

Upon the completion of this milestone, a report will be made for the Network Steward and if the Network Steward accepts this report, 9M of PKT will be paid out.
  

 ### Milestone 3: Integration with cjdns  ##

Features expected to be completed include:

* WLANInterface.c or WLANInterface.rs (C or Rust)
* Access point mode should be considered equal to ETHInterface beacon mode (anyone can connect)
* Information traditionally stored in the beacon message might be included in the SSID or otherwise
* The WPA-Enterprise shared secret must be computed based on secret information resulting from the cjdns CryptoAuth encrypted session
* Exposes admin RPC calls:
 * WLANInterface_new(ifaceName: string) -> number (same API as ETHInterface_new)
 * WLANInterface_getInfo(ifNum: number) -> object (returns info such as channel number, mode, connection quality, etc)
 * WLANInterface_setChannel(ifNum: number, channel: number)
 * WLANInterface_setMode(ifNum: number, mode: number)

 + mode values:
  * 0 disabled
  * 1 manual connection only
  * 2 automatically connect to any discovered access point
  * 3 create an access point
  * WLANInterface_scan(ifNum: number) -> Array<object> (returns an array of detected access points, include whether the access point appears to be using the same cjdns protocol)
  * WLANInterface_beginConnection(ifNum: number, ssid: string)

This constitutes the end of the project, at the end of Milestone 3, a report will be made for the Network Steward and if the Network Steward accepts this report, 9M of PKT will be paid out.

&nbsp;
&nbsp;
&NewLine;
&NewLine;
## Legal ## 

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.
