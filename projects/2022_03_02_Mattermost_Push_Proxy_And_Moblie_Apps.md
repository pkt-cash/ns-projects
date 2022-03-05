
# PKT Mattermost Push Proxy and Mobile Apps

-   Project Name: PKT Mattermost Push Proxy and Mobile Apps
-   Contact Email: soricine@gmail.com
-   Project participants:
    -   Christofer Koutelieris (soricine@gmail.com) will work 50% of full time
    -   Adonis Gaitatzis (backupbrain@gmail.com) will work 50% of full time
    -   _Other participants will be added as needed_
-   Requested rate: 68 EUR / hour
-   Total requested contribution: 15640 EUR
-   Maximum requested PKT contribution: 600000 PKT
-   PKT address to pay to: pkt1quxegcaslkacj75vu7kdhadm72dyu2kkt2axljn
-   Repository with software which will be improved: e.g. https://github.com/soricine/pkt.chat-mattermost-utils
- Project status: **PROPOSED**

## Project summary

Currently, there exists a chat software for the PKT community at [http://pkt.chat](http://pkt.chat). It is browser-based, but users can install the Mattermost mobile app to connect with it.

However, with the base Mattermost chat app,  push notifications are not supported, so users aren’t alerted when someone messages them.

We would like to implement the push notification system that will enable smartphone users to to receive these notifications, improving the user experience of the PKT chat ecosystem.

## Team and Past Work

The team includes [Christofer Koutelieris](mailto:soricine@gmail.com) and [Adonis Gaitatzis](http://github.com/backupbrain). Christopher and Adonis have both worked on PKT mobile software for iOS before an as-yet-unreleased software, and Adonis has worked directly on the PKT blockchain as well as the VPN Utility project, the Telegram trading bot, and the PKT price ticker.

Examples of past open-source contributions by team members are as follows:

**Christofer Koutelieris**
Is:

* [x] The lead maintainer of the software
* [ ] A regular contributor to the software
* [ ] An occasional contributor to the software
* [x] Not a contributor yet

_Has only work on closed source projcets up until this point_

**Adonis Gaitatzis**
Is:

* [ ] The lead maintainer of the software
* [ ] A regular contributor to the software
* [ ] An occasional contributor to the software
* [x] Not a contributor yet

He is an avid open source contributor and technology educator.

Open source projects include:
* [Python/Django Utility to Add Secure Headers to HTTP Headers](https://github.com/backupbrain/drf-keypair-permissions)
* [Javascript (browser and server) Utility to Add Secure Headers to HTTP Headers](https://github.com/backupbrain/client-http-keypair-authorization-headers)
* [Browser-based Programmable Quantum Computer Simulator](https://github.com/backupbrain/quantum-compiler-simulator)
* [The first Ripple Wallet for Android](https://github.com/backupbrain/android-ripple-wallet)
* [A browser-based REST API client Test Tool](https://github.com/backupbrain/thimiama)

## Project Deliverables

When the project is complete, we will deliver to the pkt.cash operators:

-   A working push-notification server configuration
-   A PKT-branded Android APK and source code
-   A PKT-branded iOS IPA and source code

These deliverables are broken down by milesstone, so time and cost will be addressed for each deliverable in its corresponding milestone.

The project includes sensitive information including private keys, which should not be revealed to the public. Therefore our deliverables must be handed over to a verified pkt.cash operator rather than open source to the public.

## Success criteria

At the end of this project, we will have:

-   Push notification service running that enables PKT chat users to receive message alerts on their smartphones when they are not using the app.

-   PKT-branded Android and iOS Mattermost apps, which interact with the PKT chat server and the push proxy.

## Milestones

1.  Push Notification Software
2.  Push Notification service running online
3.  Customize and build Android app
4.  Customize and build iOS app

### Milestone 0 (Kickoff)

We have found the Mattermost instructions for deploying a push notification server, including testing the mobile app on an Android smartphone.

### Milestone 1

#### Push notification software running on a server

At this step we will have the Mattermost push notification software running on a server, but will not be yet connected to a public website.

Estimated time: 15 hours
Estimated cost: 1020 EUR

After delivery, we will be able to demonstrate by screenshot that the push notification is running in console.

### Milestone 2

#### Push notification software running on a server

At this step we will connect a web server, likely NGINX to the Mattermost push proxy software, so that the push proxy can operate on the public Internet over secure HTTPS.

Estimated time: 15 hours
Estimated cost: 1020 EUR

After delivery, a lay person wil be able to visit the web server and display a simple  "Mattermos push proxy" web site. Additionally we expect to be able to send test notifications into the server using the `curl` program.

### Milestone 3

#### PKT-branded Android App

At this step we will have an unsigned APK file that we can distribute for testing which is securely connected to the Mattermost proxy server and which uses PKT-themed colors and icons

Estimated time: 100 hours
Estimated cost: 6800 EUR

After delivery, PKT.chat maintainers will be able to install and test an Android App that sends and receives messages to the [pkt.chat](http://pkt.chat) server, as well as receiving push notifications.

### Milestone 4

#### PKT-branded iOS App

At this step we will have an unsigned IPA file that we can distribute for testing which is securely connected to the Mattermost proxy server and which uses PKT-themed colors and icons.

Estimated time: 100 hours
Estimated cost: 6800 EUR

After delivery, PKT.chat maintainers will be able to install and test an iOS App that sends and receives messages to the [pkt.chat](http://pkt.chat) server, as well as receiving push notifications.

## Disclosure

I hereby submit this application in good faith and I attest that I have made no effort, nor do I intend to make effort, influence the Network Steward's decision making process.

* Conflicts
  * [ ] An organization is receiving the funds
    * [ ] Organization has financial relationships with one or more reviewers: *Adonis Gaitatzis*.
    * [ ] Organization has no financial relationships with any reviewers
  * [x] An individual is receiving the funds
    * [x] Individual works for same organization as one or more reviewers: *Adonis Gaitatzis*
    * [x] Individual has other financial relationships with one or more reviewers: *Adonis Gaitatzis*
    * [ ] Individual does not work for the same organization as any reviewer
* No Pumping
  1. [x] The applicant declares that they understand the community's
  [Ethical Communication Guidelines](https://docs.pkt.cash/en/latest/communication/)
  and will strive to follow these guidelines and represent the PKT community in the best way possible.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

* **PROPOSED**