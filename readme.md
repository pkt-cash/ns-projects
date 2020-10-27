# Projects Supported by The Network Steward

* **CURRENT DEADLINE**: Midnight UTC on November 14, 2020
* **CURRENT ROUND BUDGET**: 70mn

## Not a gravy train
When you begin thinking about writing proposals, the first thing you need to understand is that
writing Network Steward project proposals is not meant to be a profitable endevor. When you mine
PKT, you're mining against all of the other miners, when you buy it in a private trade you're
bidding against all of the other buyers, and when you apply for projects, you're competing against
all of the other applicants.

Therefore you should think of making a project proposal as a partnership which allows you to
expand your contributions to the PKT ecosystem.

## 1. Read old projects and their feedback
The existing projects, both those accepted and those rejected provide a valuable resource for
learning what the Network Steward is looking for. You can go to all of the
[projects which have been accepted](https://github.com/pkt-cash/ns-projects/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+label%3Aproject)
and [projects which failed](https://github.com/pkt-cash/ns-projects/pulls?q=is%3Apr+is%3Aclosed+is%3Aunmerged+label%3Aproject) and you'll find the project proposal in the
[Files changed](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-comparing-branches-in-pull-requests)
tab and you'll find the review information in the comments.

## 2. Pick a project idea
The Network Steward maintains a list of
[project ideas](https://github.com/pkt-cash/ns-projects/blob/master/project_ideas.md) which are in
the overall plan for the PKT project. However, this list is not exhaustive and the Network Steward
will consider ideas not on the list nonetheless. If your idea is not listed, https://pkt.chat/ and
talk about what what your idea in the `#network-steward` room. Nobody *has* to reply, but you may
start some useful conversations.

## 3. Check for "unfair advantage"
The Network Steward process requires that a project must help the PKT ecosystem as a whole without
giving any unfair advantage to anyone in it. Unfair advantage can look like any of the following:

* Charging for inflated labor costs or hours
* Using project funds to develop intellectual property which give you competitive advantage
* Using project funds to grow your business

A simple recipe for a project which does not have unfair advantage is to develop software at a
competitive price and release it to the PKT community under an open source license. If this recipe
doesn't work for you, there are other solutions but they will require more extensive documentation
to prove that the proposal is fair.

## 4. Use the template
There is a [template](https://github.com/pkt-cash/ns-projects/blob/master/projects/template.md) for
project proposals, use it. Make a first pass and fill in everything you're sure of, then take
everything you're not sure of and make a todo list.

## 5. Establish success criteria
This is super important, if an applicant requests in a project without adaquate success criteria,
the Network Steward cannot be sure that they plan on doing much of anything, and when it comes time
to submit a milestone report, the Network Steward will be unable to effectively argue that the work
was not done because the work was so vaguely specified that almost anything counts as success.

Success criteria should be *specific* and *measurable*: when you file your milestone report, the
Network Steward will compare the results to the success criteria in order to determine whether you
have achieved your objectives.

Good success criteria include:
* A user will be able to connect to a cjdns VPN from an app in the Android app store
* The address page on the block explorer will have a chart showing income per day
* With the wallet, a user will be able to pay multiple addresses in a single transaction

Bad success criteria include:
* The app works on Android
  * This is completely unclear about whether the Android needs to be rooted to work, or what
  "works" even means at all, so as a result, a project with this criterion could technically
  succeed at this without doing nearly any actual work
* The block explorer will show income
  * Without specifying that there is a chart, saying it will show income could just mean you can
  look at transactions which every block explorer supports
* The wallet will allow payment to multiple addresses
  * Without specifying "in a single transaction", any wallet imaginable would support this

## 6. Do your time estimate
After you have defined the project, you will need to estimate how much time it will take. This is
very important because the Network Steward will be comparing the time it takes to your success
criteria in order to determine if a project is properly planned and properly specified as well as
to filter out anyone who is trying to take advantage of the system by reporting inflated hours.

## 7. Disclose conflicts
Currently, the Network Steward multi-sig team is also the team who does the actual evaluation of
the proposals, so it is important to disclose any interactions with these people which might
present a conflict of interest. There is a form in the template document to fill out in order to
disclose whether there is any conflict or to affirm that there isn't.

## 8. Show your capabilities
A good project is a low-risk project, one executed by a person or team who already has plenty of
experience on the topic at hand. There are three ways you can show that the risk of the project is
low:

1. Team qualifications: A short bio on the people involved in the project showing their
qualifications for this type of work.
2. Prior work: Provide examples of work done by the people involved in the application to justify
that they have the capability to do this type of work, links to code projects in places like github
are highly valued.
3. Pre-project effort: Any plans, mockups, prototypes or other pre-project work will not only
contribute to the specification of the project but will also serve to demonstrate the team's
capacity to deliver the rest of the project. You can do as much pre-project work as you want and
describe your work in *Milestone 0 (Kickoff)* which will be written as an milestones but you are
writing success criteria for a success which you already achieved. If the project is accepted then
pre-project work will be payable.

## 8. Evaluate your own project
The Network Steward team doesn't just make decisions on a whim, there is a clearly defined process
which the evaluators follow so you can evaluate your own project before they do.

1. Read the [acceptance process](https://github.com/pkt-cash/ns-projects/blob/master/acceptance_process.md)
2. Review your project while asking the questions in the
[evaluation criteria](https://github.com/pkt-cash/ns-projects/blob/master/acceptance_process.md#evaluation-criteria)

## 9. Get competitive
If you've done a good job on everything above, you will have a good project, but the difference
between good and great is your willingness to make the project a better deal for the community
than other applicants. There are 2 key ways you can do this:

1. **Reduce your person-month cost**: If you can get the work done cheaper, or if you consider PKT
to be worth more, then your project will stand out ahead of the others.
2. **Reduce the "front-loading" of the project**: Asking for PKT before the first milestone is
completed makes the project more risky and difficult to accept, the Network Steward will tend
to prefer projects which ask for the least amount in the first period and push the majority of
the payment back until after success-criteria are met.

## 10. Submit
After you have everything put together, your success criteria are awesome, your time estimates
are on target, conflicts are disclosed and you have decided how hard you want to compete, it's
time to submit your project.

* Use a github
[pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
to submit the project to this repository
* The file should be placed in the `/projects` folder
* The name of the file should conform to
[the naming convension](https://github.com/pkt-cash/ns-projects/tree/master/projects)

### Early submission
If you submit early then the Network Steward team might provide feedback but others can also see
your project proposal. If you submit at the deadline then the project will be secret up until
the end, but it will be evaluated as it is.

