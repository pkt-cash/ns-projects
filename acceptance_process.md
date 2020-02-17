# Network Steward project acceptance process
The following is an approval process for PKT Network Steward funded projects. Firstly the NS will publish a budget and a deadline for proposals. The deadline will be Step 0 in the following process.

* **Step 0**
  * Deadline for project proposals
* **Step 1** (1 week after step 0)
  * NS provides a ranking of proposals, winners are selected starting from the best and counting down the list, skipping any which cause the sum to go over the budget, and adding projects until the sum reaches at least 90% of the total budget or there are no more acceptable projects.
    * **Note**: The reason to fill only 90% of the budget is to avoid incentivising a mass submission of micro-projects which bring little to no value. Remaining coins go to the next proposal window.
  * Deadline for submission of "significantly similar" counter-proposals
    * **Note**: Counter-proposals are submitted without knowledge of whether the project which they are countering will in fact be accepted
* **Step 2**: (1 week after step 1)
  * NS evaluates each counter-proposal according to evaluation criteria and compares it to the relevant original proposal, any counter-proposal which is not significantly similar and a significant improvement over the original proposal is eliminated and the original proposal wins.
    **Note**: If there are multiple counter-proposals, they are ranked and all are immediately eliminated except for the best one
  * Original applicants to provide amendments to original proposals to make them better than counter-proposals.
    **Note**: Amendments to original applications are submitted without knowledge of whether the counter-proposal will be considered better
    **Note 2**: If the counter-proposal is not accepted then the original project the one that wins, not the amendment.
* **Step 3**: (1 week after step 2)
  * NS evaluates amended original proposals and compares them to counter-proposals, any amended proposal which is not significantly similar and a significant improvement over the relevant counter-proposal is eliminated and the counter-proposal wins.
  * Counter-proposers provide amendments to their counter-proposals, if a winner has not been selected at this point, the process continues at step 2.

Once all competing proposals have been eliminated, the remaining proposal is deemed accepted and is funded. This happens even if other proposals remain in the amendment loop.

If all involved applicants, counter-applicants and the NS team are in agreement, the amendment loop can happen faster than a 1 week period, but in case of non-response, 1 week is the deadline after which a participant is deemed to have failed to file an amendment to their proposal or counter-proposal.

## Example of process
1. Deadline 1: Alice submits a proposal
* Deadline 2:
    * Bob and Charlie, both thinking they can do the same project better/cheaper, submit counter-proposals
    * The NS team provides their ranking and indicates that Alice's proposal has not been eliminated
* Deadline 3:
    * Alice submits an amended proposal which takes into account some of the improvements in the counter-proposals of Bob and Charlie
    * The NS indicates that Bob's proposal is better than Alice's, Charlie's proposal being not better than Bob's is immediately eliminated
* Deadline 4:
    * Bob submits an amended counter-proposal
    * The NS indicates that Alice's amended proposal is better than Bob's counter-proposal
* Deadline 5:
    * Alice submits a second amendment of her initial proposal
    * The NS indicates that Alice's first amendment of her proposal is better than bob's amended counter-proposal, thus Bob's counter-proposal is eliminated and Alice's first amendment of her proposal wins

## Evaluation criteria
Each of the NS team members will score the proposals for each one of the evaluation criteria and then the [Reweighted Range Voting](https://www.rangevoting.org/RRV.html) algorithm (example counter provided here: [rrv_vote.py](https://github.com/pkt-cash/ns-projects/tree/master/rrv_vote.py)). This is done by scoring each proposal based on the criteria given below, with a combined score being calculated from.

Until the agreed upon deadline, no NS team member shall converse about their rankings with anyone at all, even other NS team members, unless such statements are made publicly. Thus it is ensured that nobody has insider information about which proposals will be accepted and should be counter-proposed. Furthermore, as the criteria for evaluation are public, those making counter-proposals are able to make their own evaluations and choose which projects they expect to be the winners.

### 1. Short term impact
Short term impact constitutes the project's capability to help the achievement of the PKT project's immediate objectives. For example, a project to search for breakthroughs in wireless technology may be well aligned with PKT's objectives in the long term but will not bear fruit for a significant amount of time. Specific questions useful for evaluating short term impact:

* Will this project facilitate the use of PKT for micro-payments ?
* Does this project align with the PKT bandwidth market strategy ?
* Will this project help PKT to distinguish itself from other blockchains ?
* Does this project provide a piece of infrastructure which is considered necessary for any blockchain ?

### 2. Long term impact
Long term impact constitutes a project's capability to pay dividends to the PKT ecosystem over the long term. For example, a project such as the block explorer is quite important in the short term because without it, the blockchain would lack an important central piece of infrastructure, however the block explorer is not a key component to the long term strategy of the PKT project. Long term impact is important because it fosters a snowball effect of returns on the investment from the NS. Specific questions useful for evaluating long term impact:

* Will this project help advance the separation of "network administrator" from "infrastructure operator" roles ?
* Will this project provide key infrastructure/institutions necessary to the emergence of a healthy bandwidth market ecosystem ?
* Does this project bypass a tragedy-of-the-commons problem which blocks the natural emergence of a piece of key infrastructure ?

### 3. Scope and use of resources
Use of resources is the question of how "expensive" a project is and its ability to fit within the budget. Short and long term impact will be evaluated with attention to the impact/cost ratio. Note that volunteer time/effort spent by the NS team in order to oversee the project will be taken into account, so all other things being equal, a few large projects are preferable to a large number of smaller ones. Some questions which may be useful for evaluating scope and use of resources include:

* Do the metrics for success justify the amount of effort placed on the project ?
* Does the cost for effort seem to be a good deal (attention shall be given to the skill sets of declared participants) ?
* Are there competitive aspects between the project to promote efficient use of resources ?

### 4. Risk control
Risk control is about the question of how likely a project is to fail at delivering the expected result. Projects which are inherently more risky will be evaluated more stringently on their proposed risk control. Specific questions useful to the evaluation of risk control include:
* How evenly is the effort spaced over the milestones of the project ?
* How evenly is the payment spaced over the milestones of the project ?
* To what extent are the risks defined and planned for in the project proposal ?
* To what extent are the difficulties and potential blockers moved to the early parts of the project ?
* What evidence is there that the project owner is capable of delivering ?

### 5. Hazard control
The objective of the Network Steward is to make funding available for projects which benefit the entire PKT ecosystem equally without unfairly benefitting any one participant over any other. Hazard control is about preventing any incentive or the perception of an incentive which would promote a corruption of the process from its objective. Public perceptions are almost as important as the real thing because the perception of hazard discourages new participants from joining the PKT ecosystem and encourages existing participants to submit projects which are at least as corrupt as they imagine the average project to be. Some questions which may be useful to the evaluation of hazard control include:

* To what extent is the project safe from any real or perceived conflicts of interest with the NS team ?
* To what extent are the results of this project equally advantageous to all participants in the PKT ecosystem ?
* To what extent does the proposal structure the project such that success will be more advantageous to the applicant than failure ?
  * The use of milestones, deliverables and evenly spaced payments conditioned on deliveries is encouraged.
* To what extent does the project control the risk of arbitrage profit opportunity for the applicant ?
  * An example of arbitrage profit opportunity appears when there is a lack of market agreement on the cost of the deliverables which the project will produce. Logo design is a good example of a deliverable for which there lacks market agreement on the cost. While PepeiCo saw fit to spend one million dollars on their logo, the Nike logo was bought for a mere $35. In the case of such an expenditure, the NS team and overall community are unable to verify whether a project constitutes a million dollars worth of diligent effort or a $35 drawing sold at a markup.

## Counter-proposal and Amendment Criteria
Counter-proposals and amendments to existing proposals are compared using the 5 evaluation criteria but in addition, they must achieve the status of significantly similar and a significant improvement.

### Significantly similar
A counter-proposal or amendment should be considered to be significantly similar in the event that it targets the same objectives as the original proposal. Some questions which may be useful to the evaluation of significantly similar status include:
* Do the two proposals have the same short and long term impacts ?
* Assuming both projects were funded, would it be nonsensical for a single entity to use the results of both projects ?

### A significant improvement
The definition of a significant improvement is designed to prevent "stealing projects" by submission of proposals which are trivially less costly. While the exact definition of a significant improvement will be left to the discretion of the NS team, applicants can generally consider that:
* A proposal of otherwise equal value but at more than 5% less cost is a significant improvement
* A proposal which is not only better than the original, but in fact also better than another project which is better than the original is a significant improvement
Counter-proposers should be aware that a copy/paste counter-proposal will generally not be considered to be equal to the original without a justification of domain knowledge equal to that which is justified by the original applicant through the text of the proposal.

### Unacceptable projects
Some projects may be judged by the Network Steward to be unacceptable under any conditions. An intuitive example would be a proposal to build an assasination market which is blatantly illegal and contrary to the objectives of the project. These judgements will be made by each member of the NS team individually and projects which are not deemed acceptable by at least 3 of the 5 team members will not be funded, even if that means burning coins. Some questions which are useful in the evaluation of acceptability:

* Does the project seem more likely to benefit the PKT ecosystem than to harm it ?
* Does the project seem unlikely to cause significant damage to the perceived legitimacy of the Network Steward ?
* Does the project seem likely to be a better use of resources than burning the coins ? (note that burning coins causes deflation which increases the value of all existing coins)

