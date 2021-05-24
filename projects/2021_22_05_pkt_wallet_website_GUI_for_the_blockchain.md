# *PKT Wallet GUI with mining from your browser*

* Project Name: *PKT Wallet GUI with mining from your browser*
* Contact Email: *maarten@vantwout.net*
* Project participants:
  * *Maarten van 't Wout(maarten@vantwout.net) will work 100% of fulltime* (name in pkt.chat: @mavantwout)
  * *Gijs Overgaag (gijs.overgaag@hotmail.com) will work 100% of fulltime* (name in pkt.chat: @gijs_83a)
  * *Other participants will be added as needed.*
* Projected duration: *e.g. 5 months*
* Projected effort: *e.g. 10 person/months*
* Requested PKT contribution: *21M PKT*
* PKT address to pay to: *pkt1q2qlnu9lp6g86q4vdjgfkh0kjxc4l6qtduwy3ya*

## Project summary

At the moment, it is still difficult for the average Jane and Joe to interact with the PKT blockchain. Over time the PKT network should be used by everyone in a decentralized manner and therefore everybody should be able to send and recieve PKT, but also have the possibility to announcement mine without having coding knowledge. This will ensure decentralization of the PKT network. Therefore, our plan is to create a website with an easy to use graphical user interface on which people can make an account and from the account interact with the blockchain. First, we will add the account functionality, then the option to receive PKT's and after that we will add the option to send PKT from this webwallet by providing the private key of the people. We will never store your private key and therefore everyone will always keep complete control of their own PKT funds. Lastly, we will add the more advanced option to mine PKT through the browser. This will make the PKT network much stronger and more decentralized.

## Team and Past Work

Our team consists of software developers and blockchain and webdevelopment experts. They have worked at blockchain and web development companies and other companies that manage automated decentralized systems. Our team shares the same values. We all pay a lot of attention to detail and are all  dedicated to make this project a success.

https://github.com/vantwoutmaarten


## Project deliverables

* __Deliverable 1:__ A website with a well designed easy to use front-end.
* __Deliverable 2:__ A website with a secure user authentication system. People will be able to register an account. Then, the users will be able to login and logout in a secure manner. On top of that, the user will be able to view their wallets history and status that is retrieved from the blockchain.
* __Deliverable 3:__ Add a QR code and another copy option to make it easy to get the wallet addresses from accounts on the website.
* __Deliverable 4:__ Add the option to use your private key to send funds from the website.
* __Deliverable 5:__ Add the option to announcement mine from your browser.


* [X] New open source software
    * Which license(s) which you will use:
      * [X] [MIT](https://spdx.org/licenses/MIT.html)
    * The maintainer of this software will be: *Maarten van 't Wout*
    * The software will be hosted in: *First, on google cloud, later on IPSF and ENS to also make the site decentralized*

## Milestones

> **Instructions:** What are the milestones that will be delivered, and at each milestone:
> 1. What new things will be delivered which the Network Steward can use to verify that the milestone was a success?
> 2. How much of the budget should be paid out?
>
> If you have already done work on the project, create *negative* milestones and write success criteria for
> these milestones in order to justify what has already been done.

### Milestone 0 (Kickoff)

> **Instructions:** Document anything which you did on the project before the project began, any prototypes,
> mockups, planning or useful work which was done. This should correspond to the **Pre-project effort**
> defined at the beginning of the document.
>
> Then explain how much PKT must be provided at the beginning of the project. **NOTE:** Projects which ask for larger advances with less pre-project work will be regarded as more risky, for details see the [acceptance_process](https://github.com/pkt-cash/ns-projects/blob/master/acceptance_process.md).

>* In advancement of the project, we have already made a similar website for bitcoin to test how this would work on a more established blockchain.
>* On top of that, we have done in depth research on the PKT ecosystem, including optimizing a mining strategy that considers both block and announcement miners.

After the project is accepted, the Network Steward will pay 1,000,000 PKT

### Milestone 1
__A working website with a well designed easy to use front-end.__

* Setup the project
* Designing the frontend
* Host the website

#### Success criteria
> * The Front-End has to be easy to use and everything should be in one style.
> * The website will be hosted on google cloud and coupled to a adequate domain name.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send 1,000,000 PKT.

### Milestone 2
__A website with a secure user authentication system. People will be able to register an account. Then, these users will be able to login and logout in a secure manner. On top of that, the user will be able to view their wallets history and status that is retrieved from the blockchain.__

* creating a PKT wallet from within your account.
* Apply user authetication, make registration, login and logout possible in a secure manner.
* Setup Django Admin Interface
* Get the wallet addres details from your account.
...

#### Success criteria
> * A wallet address should clearly coupled to a user account and this should be displayed.
> * The User-authentication system will work adequately.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send 2,000,000 PKT.

### Milestone 3
__Add a QR code and another copy option to make it easy to get the wallet addresses from accounts on the website.__

* Add options to recieve pkt in your account.
* -- By copying the address.
* -- By scanning a QR code.

#### Success criteria
> * It should be possible to receive funds in your wallet and this should be displayed on the website.
> * It should be possible to send funds to an account by copyin the addresss.
> * It should be possible to copy an address by scanning a QR-code.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send 2,000,000 PKT.

### Milestone 4
__Add the option to use your private key to send funds from the website.__

* Add options to send PKT from wallet by providing your private key from within your account account on the website. 


#### Success criteria
> * If it is possible to send funds trough the website the milestone is completed.

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send 4,000,000 PKT.


### Milestone 5
__Add the option to announcement mine on from your browser.__

* It will be possible to do announcement mining from within the website within one click. It will be possible to mine to the accounts wallet or it will be possible to send the mining rewards to another wallet address of choice. This will be done by loading mining code within the browser though javascript. This will be done by using the original Rust pkt mining files and use WebAssembly to use these files with javascript in the browser.


#### Success criteria
> * It will be possible to announcement mine from within your account on the website. 

#### Payout
After a report is delivered on this milestone and it is approved by the NS, the NS will send 11,000,000 PKT.


## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I
intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
  1. [ ] An organization is receiving the funds
    1. [ ] Organization has financial relationships with one or more reviewers: *specify whom*
    2. [ ] Organization has no financial relationships with any reviewers
  2. [ ] An individual is receiving the funds
    1. [ ] Individual works for same organization as one or more reviewers: *specify whom*
    2. [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [ ] Project results will present information which might lead to PKT price speculation
    * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially misleading the public.
  2. [ ] Project results will not present information which might lead to PKT price speculation

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

* Can be ready to release the first 3 milestones within 1 month.
