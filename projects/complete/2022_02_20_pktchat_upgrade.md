# Upgrade pkt.chat software

* Project Name: pkt.chat software version upgrade
* Contact Email: delivery [ a t ] marianne [ d o t ] io
* Project participants:
  * Thierry Marianne (@thierrymarianne in [pkt.chat](https://pkt.chat)) will work 100% of fulltime
* Projected duration: from 2 to 2.5 weeks 
to be put in perspective with 14 days required to have [v5.36.1 PR merged](https://github.com/thierrymarianne/contrib-matterfoss/pull/1) before excluding minor fixes like [restoring emojis](https://github.com/cjdelisle/MatterfossWeb/pull/4) or [replacing favicons](https://github.com/cjdelisle/MatterfossWeb/pull/6)) and also 
by including optional post-release maintenance hours / days (the last half-week)
* Projected effort: 1 person/week
* Total requested contribution: 4675 EUR
* Requested rate: 53.38 EUR / hour
* Pre-project effort: half a day involving 2 person: @cjd as pkt.chat hosting provider and I
* Maximum requested PKT contribution: 275K PKT
* PKT address to pay to: `pkt1qpcnlzcam8gcka4mrjwdlzdgkyngwazjrtan24n`

## Project summary

Matterfoss was [recently](https://github.com/cjdelisle/Matterfoss/commit/b61323db6e7de9344db8ac7bf566bd48dba13540) upgraded to support native mobile applications compatible with Mattermost™ v5.36.1 tag.  

Given than more recent iOS and Android mobile applications versions have been rolled out to further support latest stable versions of [Mattermost™ upstream server-side API project](https://github.com/mattermost/mattermost-server/releases/tag/v6.6.1) (v6.6.1 being the latest major version at the moment),  
and to prevent being reminded of the pending intermediate software upgrades   
for each and every time the latest version available of the native app is opened,  
integrating upstream changes into Matterfoss makes sense. 

Please see below a screenshot of the warning message being displayed for Android:

![unsupported-software](https://user-images.githubusercontent.com/1053622/154851334-31799dbc-17c5-4f19-ab03-4964fce14424.png)

## Team and Past Work

As an independant solo contractor, I have worked in the service of PKT ecosystem before,  
especially in the context of the [European LEDGER project](https://www.ngi.eu/ngi-projects/ledger/) with [SafePKT](https://ledgerproject.github.io/home/#/teams/SafePKT) developments.

Besides having worked on the Matterfoss instance hosted at https://pkt.chat in the past,  
this project would present relatively few unknowns  

## Project deliverables

* [ ] New open source software
    * Which license(s) which you will use:
      * [ ] [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
      * [ ] [MIT](https://spdx.org/licenses/MIT.html)
      * [ ] [GPL-2.0-only](https://spdx.org/licenses/GPL-2.0-only.html)
      * If your license(s) is/are not shown, please add them using the [SPDX license list](https://spdx.org/licenses/)
    * The maintainer of this software will be: *project participant*
    * The software will be hosted in: *software repository location*
* [x] Contributions to existing software
  * List software projects
    * [ ] [cjdns](https://github.com/cjdelisle/cjdns)
    * [ ] [yggdrasil-go](https://github.com/yggdrasil-network/yggdrasil-go)
    * [ ] [PacketCrypt](https://github.com/cjdelisle/PacketCrypt)
    * [ ] [pktd](https://github.com/pkt-cash/pktd)
    * [x] [Matterfoss API](https://github.com/cjdelisle/Matterfoss)
    * [x] [Matterfoss Single-Page Application (SPA)](https://github.com/cjdelisle/MatterfossWeb)
* [x] Other deliverables
    * [x] Active support during version migration in production
    * [x] Hotfix implementations

Matterfoss has become one of [PKT ecosystem communication pillars](https://pkt.cash/community) in the shape of an instance hosted at https://pkt.chat when it comes to 
 - bringing support to newcomers and also, 
 - streamlining project organization.

Since this platform serves as a host for a significant portion of all community-dependent operations, and innovations happening at the heart of PKT project and responding to its long-term vision, I'd argue that the tools offered to community members should be of pristine quality,  
hence the need for a software upgrade policy consistent with industrial standards.

As PKT project lead @cjd stated himself in [The Tao of Information Security](https://youtu.be/ek2bGVBdeBs) video:
[...] "you may fall victim to vulnerabilities that everybody already know about" [...] without making a consistent habit of [updating software](https://www.youtube.com/watch?v=ek2bGVBdeBs&t=1s).

## Success criteria

The most critical and final evaluation criteria is the release of those changes in production (and pkt.chat instance services recycling). 

Such release in production will be fairly easy to validate by having the Android client application not displaying anymore the unsupported version message previously attached to this proposal until the next major version of Mattermost™ incompatible with its native mobile apps is released.

## Milestones

  1. Define which tags will need to be targeted for integration from upstream projects during kickoff 
  2. ✅ Upgrade [Matterfoss API](https://github.com/cjdelisle/Matterfoss) to [`v6.6.1`](https://github.com/cjdelisle/Matterfoss/pull/9)
  3. ✅ Upgrade [Matterfoss SPA](https://github.com/cjdelisle/MatterfossWeb) 
  4. ✅ Replace favicons to accommodate to software licencing differences.
  See this past [issue](https://github.com/cjdelisle/MatterfossWeb/pull/6)
  5. ✅ Generate emoji fonts and matching images along with static files.
  See this past [issue](https://github.com/cjdelisle/MatterfossWeb/pull/4)
  6. ✅ Communicate upfront to community members about upcoming maintenance mode with minimal disturbance affecting their discussions
  7. ✅ Recycle Matterfoss API service 
  8. 🎯 Communicate to community members regarding likely requirement for hard-refresh of https://pkt.chat pages possibly cached by their browser 
  9. ✅ Replace Matterfoss SPA static files re-exported since latest merge in production before recycling web server
 10. [ ] ~~(Optional) Offer support to project maintainer up to half a week worth of post-release maintenance (hourly billed)~~

### Milestone 1 (Kickoff)

Upon agreement during the kickoff meeting regarding tagged versions to be targeted for integration from upstream,  
1/10 of the total requested contribution in PKT (**51,027 PKT**) ~~or **To be determined on milestone submission date** PKT / hour~~.

 * The cost of this milestone is 467.5 EUR (4675 EUR / 10) and  
 I declare that the current trading price is **0.0088** EUR per PKT (0.9 EUR/USD / 100 PKT/USD) on the **3rd of April 2022**
 * Therefore, I will request a transfer of **51,027 PKT**

### Milestone 2

#### Success criteria

A pull-request being merged into Matterfoss API repository and/or commits have been added to its main branch so that  
the server-side API becomes ready for testing with the SPA software and future deployment in production

#### Payout

After a report is delivered on this milestone, and it is approved by the NS,  
the NS **would have** sent 3/20 of the total PKT contribution (**41,250 PKT**) ~~or **To be determined on milestone submission date** PKT / hour~~.

 * ~~Since first payment was about 18% of `maximum requested PKT contribution` (`51,027  PKT / 275,000 PKT`),~~
   ~~it makes sense that payment request for milestones 2 would be decreased accordingly as [mentioned in first payment request](https://github.com/pkt-cash/ns-projects/pull/110#issue-1190899590)~~
 * ~~Besides and since Milestone 1 through 9 payments were evaluated for up to 80%~~
   ~~of maximum requested PKT contribution as follows:~~
   - ~~Milestone #1       - 1/10~~
   - ~~Milestone #2       - 3/20~~
   - ~~Milestone #3       - 3/20~~
   - ~~Milestone #4       - 1/20~~
   - ~~Milestone #5       - 1/20~~
   - ~~Milestone #6 to #9 - 3/10~~  
   ~~so that a pre-provisioned budget would be available for additional fixes,~~  
   ~~the remaining 20% of `maximum requested PKT contribution` can now be distributed back through Milestone #1 to #9~~
 * ~~Therefore, I will request a transfer of **(1/10 + 3/20 - 18/100 + 20/(9 * 100)) * 275,000** PKT for Milestone 2,~~
   ~~i.e. (**25,361 PKT**)~~

~~`1/10 + 3/20` being the sum of original Milestone #1 and Milestone #2 payouts.~~  
~~`18/100` being the actual Milestone #1 payment given the evolution of PKT price on the **3rd of April 2022**.~~
~~`20/(9 * 100))` being the remaining 20% of the optional Milestone (#10) divided by the number of total milestones (9).~~

See [Project Status](#project-status) for final payout

### Milestone 3

#### Success criteria

A pull-request has been merged into Matterfoss SPA repository and/or commits have been added to its main branch so that  
the client-side application becomes ready for testing with the API software and future deployment in production.

#### Payout

After a report is delivered on this milestone and it is approved by the NS,  
the NS will send 3/20 of the total PKT contribution (**To be determined on milestone submission** PKT) or **To be determined on milestone submission date** PKT / hour.

 * ~~The cost of this milestone is 701.25 EUR and~~  
 ~~I declare that the current trading price is **to be determined on milestone submission** EUR per PKT on the **milestone submission date**~~
 * ~~Therefore, I will request a transfer of **to be determined on milestone submission** PKT~~

See [Project Status](#project-status) for final payment request

### Milestone 4

All favicons are ready to be served.  
Special cases exist for macos and iOS native app applications, we might need to go back and forth with testing in staging environment.

#### Payout

After a report is delivered on this milestone and it is approved by the NS,  
the NS will send 1/20 of the total PKT contribution (**To be determined on milestone submission** PKT) or **To be determined on milestone submission date** PKT / hour.

 * ~~The cost of this milestone is 233.75 EUR and~~
 ~~I declare that the current trading price is **to be determined on milestone submission** EUR per PKT on the **milestone submission date**~~ 
 * ~~Therefore, I will request a transfer of **to be determined on milestone submission** PKT~~

See [Project Status](#project-status) for final payment request

### Milestone 5

Emoji fonts and images have been generated and are ready to be served.  
There is a ruby script requiring specific libraries from a linux system to be installed in order to generate these assets. 

See this [pull-request description](https://github.com/cjdelisle/MatterfossWeb/pull/2).

Both API and SPA are affected by [system emojis generation](https://github.com/cjdelisle/Matterfoss/pull/5/files).

#### Payout

After a report is delivered on this milestone and it is approved by the NS,  
the NS will send 1/20 of the total PKT contribution (**To be determined on milestone submission** PKT) or **To be determined on milestone submission date** PKT / hour.

 * ~~The cost of this milestone is 233.75 EUR and~~
   ~~I declare that the current trading price is **to be determined on milestone submission** EUR per PKT on the **milestone submission date**~~
 * ~~Therefore, I will request a transfer of **to be determined on milestone submission** PKT~~

See [Project Status](#project-status) for final payment request

### Milestones 6 to 9

Even though those last milestones are the most critical ones since they are all about releasing to production the software changes, there is no way for me to implement them on my own for privacy reason towards community members by accessing services to be recycled or their logs in case of unforeseen incident occurring in production.

That's why migrations for both API and SPA will need to be conducted with full collaboration between @cjd, who is responsible for hosting pkt.chat as far as I know and myself so that we could deploy potential hotfixes.

Both release dates will need to be defined at the time of the kickoff so that we can schedule all necessary communication as soon as possible.

#### Payout

After a report is delivered on this milestone and it is approved by the NS,  
the NS will send 3/10 of the total PKT contribution (**To be determined on milestone submission** PKT) or **To be determined on milestone submission date** PKT / hour.

 * ~~The cost of this milestone is 1,402.5 EUR and~~   
   ~~I declare that the current trading price is **to be determined on milestone submission** EUR per PKT on the **milestone submission date**~~
 * ~~Therefore, I will request a transfer of **to be determined on milestone submission** PKT~~

### ~~Milestones 10 (optional)~~

See [Project Status](#project-status) for final payment request

Hotfixes and additional patches could be applied and prepared for deployment in production on an hourly basis up to the pre-provisioned budget.

#### Payout

After a report is delivered on this milestone and it is approved by the NS,  
the NS will send 1/5 of the total PKT contribution (**To be determined on milestone submission** PKT) or **To be determined on milestone submission date** PKT / hour.

 * ~~The cost of this milestone is 935 EUR at most considering an hourly rate of 53.38 EUR and~~
 ~~I declare that the current trading price is **to be determined on milestone submission** EUR per PKT on the **milestone submission date**~~
 * ~~Therefore, I will request a transfer of **to be determined on milestone submission** PKT~~

See [Project Status](#project-status) for final payment request

## Disclosure

I hereby submit this application in good faith and I attest that I have made no effort, nor do I intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
    1. [ ] An organization is receiving the funds  
        1. [ ] Organization has financial relationships with one or more reviewers: N/A  
        2. [ ] Organization has no financial relationships with any reviewers  
    2. [x] An individual is receiving the funds
        1. [ ] Individual works for same organization as one or more reviewers: N/A  
        2. [x] Individual has *had* other financial relationships with one or more reviewers: @cjd (I used to be an employee of CJDNS SASU until December 2021)  
        3. [x] Individual does not work for the same organization as any reviewer  
2. No Pumping  
    1. [ ] Project results will present information which might lead to PKT price speculation  
       * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially   misleading the public.  
    2. [x] Project results will not present information which might lead to PKT price speculation  

## Use of Resources

Each milestone report will be accompanied by:

* [x] Itemization of project expenditures, including description, date and price (in national currency)
  * [ ] Justification of this itemization in an audit certificate
* [x] Dates when PKT was converted to national currency
  * [ ] Justification of this conversion in an audit certificate
* [ ] An audit certificate from a qualified financial auditor
  * *If yes, please provide name of the auditor*: ___________

### Partial milestones

If it happens that I have satisfied all of the criteria for a milestone but have not provided justification of all resources allocated:

* [x] I will deduct the un-justified amount from the amount requested for the milestone
* [ ] I will request the milestone be paid in full anyway

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

 - [x] guidance requested (especially regarding Use of Resources section)
 - [x] Milestone 1 payment requested  
   - `51,027 PKT` for `467.5 EUR` i.e. `467.5 EUR / ( 0.90 EUR / USD * 0.0088 USD / PKT )`
     considering [1 USD = 0.90 EUR](https://finance.yahoo.com/quote/USDEUR=X/) and [1 PKT = 0.0088 USD](https://global.bittrex.com/Market/Index?MarketName=USDT-PKT)
     * CALEB: I have personally advanced this payment to the project in transaction https://explorer.pkt.cash/tx/ffec379725a8b1319c18d71978c088f3e53ece49b923139be2ec6c2fac237fe5 and I hereby request the payment be redirected to pkt1qtu5y64ln9n9mw3e88ydt28jgmu327ygme8y54t
     * June 10, 2022: Payment of 51027 (refund) executed in transaction: [1](https://explorer.pkt.cash/tx/3c79bc9a04b9dac1be332540d818de4b9359d0d6355a527999c230e96b9d1876)
 - [x] ~~Milestone 2 payment requested~~
   - ~~`25,361 PKT` for `216.22 EUR` i.e. `216.22 EUR / ( 0.94 EUR / USD * 0.00907 USD / PKT )`~~
     ~~considering [1 USD = 0.94 EUR](https://finance.yahoo.com/quote/USDEUR=X/) and [1 PKT = 0.00907 USD](https://global.bittrex.com/Market/Index?MarketName=USDT-PKT)~~
 - [x] Milestones 2 through 9 payment requested
   - `223,973 PKT` for `1068.62 EUR` i.e. `1068.62 EUR / ( 0.96 EUR / USD * 0.00497 USD / PKT )`
     considering [1 USD = 0.94 EUR](https://finance.yahoo.com/quote/USDEUR=X/) and [1 PKT = 0.00497 USD](https://global.bittrex.com/Market/Index?MarketName=USDT-PKT)
   - June 10, 2022: Payment of 223973 executed in transactions:
    [1](https://explorer.pkt.cash/tx/5223e98672303b9ede1949a3f6be733749cc7d35523830e81e0990c097fa845c)
    [2](https://explorer.pkt.cash/tx/3e6372a5a434a7388a94b2123836bb90bf0a37e3570735bb9996eca32fb932a3).
- June 10, 2022: This project is now complete.