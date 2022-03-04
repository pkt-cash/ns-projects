# FasterCrypt Competition
FasterCrypt is a competition to optimize 3 encryption algorithms which are used in the PacketCrypt bandwidth hard proof of work. These encryption algorithms are also used in many other software programs so the results of this competition will benefit the entire internet ecosystem.

* Contact Email: tomas@leitecastro.com
* Project participants:
  * Tomás Leite de Castro (tomas@leitecastro.com and @tomas347 - https://pkt.chat)
  * Judges 
  * Contestants
* I ask the network stewards a contribution of the value equivalent of 16 000€ plus 518€ per month to help me cover the costs associated with hosting the competition. I will also have to develop the test harness, and use the hardware to benchmark the competitors code. (This value was estimated considering the competition will be hosted for 3 months, I intend to return the rest if the competition ends sooner). I only ask for my PKT contribution to be paid by the NS after the competition is over, in order to reduce risks.
* The total cost of this project will be the prize of 5 Million PKT or 7.5 Million PKT (with the extra round) plus the cost of hosting the competition [described bellow on mmilestone 1 and milestone 5] plus the initial funding minus the depreciation of the sell of the aquired hardware.


## Algorithms
The FasterCrypt competition will focus on optimization of three key encryption algorithms used in the popular [libsodium](https://libsodium.gitbook.io/doc/) encryption library.

* [ChaCha20 stream cipher](https://libsodium.gitbook.io/doc/advanced/stream_ciphers/chacha20)
  * crypto_stream_chacha20_ietf
  * crypto_stream_chacha20_ietf_xor_ic
* [Poly1305 authenticator](https://libsodium.gitbook.io/doc/advanced/poly1305)
  * crypto_onetimeauth_poly1305_init
  * crypto_onetimeauth_poly1305_update
  * crypto_onetimeauth_poly1305_final
* [Blake2b hashing algorithm](https://libsodium.gitbook.io/doc/hashing/generic_hashing)
  * crypto_generichash_blake2b

Performance will be verified using the [PacketCrypt](https://github.com/cjdelisle/packetcrypt_rs) proof of work algorithm's [CryptoCycle](https://github.com/cjdelisle/packetcrypt_rs/blob/024debf273b4be8efac6a5bfa7f66ba323e074eb/packetcrypt-sys/packetcrypt/src/CryptoCycle.c#L44) function which runs the above encryption operations on random length pieces of data roughly the size of an internet packet. Also the [Hash_compress32](https://github.com/cjdelisle/packetcrypt_rs/blob/02c00a9fefcd8ebbd5d39b559d27863bcfe2bd2e/packetcrypt-sys/packetcrypt/src/Hash.c) function is heavily used, which triggers use of Blake2b hashing.

## Process
* The administrator of the FasterCrypt competition, will be Tomás Leite de Castro. He will host the necessary components to benchmark the block miner.
* The hardware for the block miners will be 2x Dell PowerEdge R730xd.
    Specifications:
        > 2x Xeon E5-2699v4 (44C/88T)
        > 512GB DDR4 ECC
        > 1x Nvidia Tesla V100
        > 10GbE Intel x520
* The Administrator will have to provide the test harness and open-source it. 
* The test OS is Debian (Kernel 5.16.12).
* As we want the competition to the fairest possible, and generating 10Gbps of announcements internally is very costly. I will create a test environment starting with a given block height. I will generate announcements at a fixed difficulty, which will be stored in a storage server. After that, we subject the block miner to a staged pool configuration. A modified version of the annhandler will then read the announcements from the SSDs and send a continous flow of 10Gbps of announcements to the miners for a set period of time (I suggest 4 hours). Every 60 seconds, the block height is increased by one, and the handler will send a different queue of announcements considering the block hash it fetches from the Pool's Master. The pools Master role, will be to increase block height every 60 seconds and deliver the block hashes. Every team's miner will be subjected to the same height, block hash and announcements.

## Hardware List
* 2x Dell PowerEdge R730xd (E5-2699v4, 512GB DDR4) - Used as block miners
* 3x Dell PowerEdge R720 (E5-2650v2, 96GB DDR3) - Will be used as handlers for The Lab's pool
* 8x Supermicro x10DRT-H Blades (Mixed CPUs between E5-2699v4 / E5-2698v4 / E5-2673v4 / E5-2620v3) Will be used as ann miners to generate all announcements necessary for the test environment. 
* 1x Dell PowerEdge R730xd (Storage server)
* All other machines required will be hosted as VMs such as the Pools Master, blk handler, and pktd node.

## Steps
1. Administrators will test the unmodified algorithms on **the target hardware** and publish the resulting performance, this will become **the mark to beat**.
2. Applicants submit their improved algorithms to the competition judges by the **Deadline March 31st 2022 23:59 GMT**.
  * Proposals will remain under embargo until the applicant has won, or is eliminated from the competition
  * Applicants MAY submit before the deadline for validation from the judges of the correctness of their application.
3. After the deadline, Administrators will test the applications on **the target hardware** and publish the results of testing
  * All submissions which:
    1. Are in violation with the rules of the competition, or
    2. Do not test better than **the mark to beat**
  * will be eliminated from the competition and the embargo on release of their code will end.
  * If a submission is deemed to be *slightly* outside of the rules, for example a deficiency of code style, the judges **may** at their sole descretion tenatively accept the submission, allowing the contestant to cure deficiencies in the following round.
    * Contestants are expected to know the rules of the competition. 
4. After results have been published, the fastest proposed implementation will now become **the mark to beat** and applicants will have Five (5) days to re-submit.
  * Re-submission will return the process to step 2.
5. When there is only 1 candidate remaining, they will be declared the winner and the embargo on their submission will end.

### Possibility for further rounds
If it is agreed between the winning candidate and the competition administrators, another round may be added :
  * The process will return to step 2, but with anyone from the public able to enter
  * The bounty for final win will be raised by 1.5x the current bounty
  * The current winning candidate's submission will remain under embargo
If at the end of the round no submissions can beat **the mark to beat** the bounty will be payed at the original value

## Milestones
> 0. Lab setup
> 1. Submission phase X (one milestone per round)
> 2. Evaluation phase X
> 3. Final round
> 4. Extra round (optional)
> 5. Announcement of the winner

### Milestone 0
This part will be fairly easy. The PKT team will use their main channels to get the word out that there is a 5 Million PKT reward for a block miner. 

After 3 weeks should the Network Stewards accept this proposal, the hardware will be available for the teams to check, try and benchmark. The Test round software will not be available immediately, but I'll set up a pool, and ask the community to send announcements so there will be announcements flowing (Much less than in the test and final round). I will create the staged test environment, and when I deem it's ready to be deployed I'll inform the community and allow them to test the same way they will be judged. 

The hardware will be "offered" to the community similarly as a dedicated server hosting. After each team finishes their tests, the server will be erased and a clean OS install will be performed. There will be a system to reserve the hardware for an X period of time (To be defined). Most of the interaction will happen on the dedicated pkt.chat channel. 
All reservations will be public, with a calendar. So every team will now how much time the others are spending on benchmarking the code.
I may have to put an hourly limit on how much time each team can spend with the servers. 
No team is obligated to use the test lab, but it will be very much suggested as not everyone has the access to this kind of machines for benchmarking crypto mining software. 

I reserve the right to block any further reservations should I see that the teams were using the servers for other purposes than to develop their block miner. (Huge spikes in bandwidth usage to a current PKT pool is a high suspicion of abuse)

This is the reason I will ask for a contribution from the network steward. Hosting a fair, and long, software development competition with this hardware is expensive. And I will ask for the Network Steward to offset my costs.

#### Payout

> In order to reduce risk for the Network Steward I will only ask for payment after Milestone 1 is achieved.

### Milestone 1 + x

> This is the test phase. (8 weeks before submission at most) the contestants will now be able to put their miners through their final test phase. I will host several rounds of the same test they will be presented on the final challenge. Of course the final challenge will be with different block height as to prevent cheating. They will have enough time to make some last minute changes and modifications before the last final round.
> Deadline for this milestone is 29 May 2022

#### Payout
    > The Network Steward will pay to my address the EURO equivalent for the total time that The Lab was on and served to the community, from the time it was delivered access up until the date of this Milestone. This value should be the Average usage per month predicted as 518€/Month (I intend to deduct the excess amount of power usage).

### Milestone 2
> This is the Evaluation phase the judges will annount the mark to beat and the competition will move to the next round.
> Each round from here will be held for a week.

### Milestone 3
> This is the last round. The judges will announce the **the mark to beat**
> If there is interest from the community in participating, the competition administrators may discuss with the winner the possibility of an extra round for a 1.5x bigger bounty.

### Milestone 4
> This is the extra round. Any participant will be able to submit their code for a 1.5x bigger bounty.
> The duration of this round will be decided by the competition administrators.

### Milestone 5
> The judged will announe the final **score**.
> The competition administrators will announce the winner.
#### Payout
    > The Network Steward will pay to the winning developers address the sum of 5 Million PKT or 7.5 Million PKT in case there was an extra round.
    > The Network Steward will pay to my address the EURO equivalent for the total time since the last payout that The Lab was on and served to the community.
    > Estimated EURO value for the payment 8000€ (This value is an overestimate of the depreciation of the hardware) I intend to only ask for the actual depreciation with proof of purchase and sale.


## Submission Rules
1. Submissions must consist only of modifications to existing software:
  * [packetcrypt_rs](https://github.com/cjdelisle/packetcrypt_rs/),
  * [libsodium](https://github.com/jedisct1/libsodium/), and
  * [sodiumoxide](https://github.com/sodiumoxide/sodiumoxide/)
2. All modifications of software shall bear the same open source license as the software that is being modified.
3. No judge shall disclose any information regarding the code or techniques used in any of the submissions under embargo to any other person who is not a judge, including to administrators of the competition.
4. When embargo is lifted on a submission, the submission shall be published by the judge to a public git repository.
5. All modifications of software must adhere to the coding convensions of the software which they modify, this is subjective and will be decided by the judges but the following are some guidelines to inform the definition of compliance:
  * They must compile using the same compilation process as the original software
  * No tests should fail which previously were passing and no tests should be removed
  * The software should work on the same operating systems and processor architectures that it worked on before, any use of assembly instructions which are not available on all processors should use runtime checks to enable itself where available
  * Code style convensions should be adhered to
6. No applicant can submit his code to an Administrator.
