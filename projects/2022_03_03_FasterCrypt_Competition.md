# FasterCrypt Competition
FasterCrypt is a competition to optimize 3 encryption algorithms which are used in the PacketCrypt bandwidth hard proof of work. These encryption algorithms are also used in many other software programs so the results of this competition will benefit the entire internet ecosystem.

* Contact Email: tomas@leitecastro.com
* Project participants:
  * Tomás Leite de Castro (tomas@leitecastro.com and @tomas347 - https://pkt.chat)
  * Judges 
  * Contestants
* I ask the network stewards a contribution of the value equivalent of 17 000€ to help me cover the costs associated with hosting the competition. I will also have to develop the test harness, and use the hardware to benchmark the competitors code. (This value was estimated considering the competition will be hosted for 3 months, I intend to return the rest if the competition ends sooner). I only ask for my PKT contribution to be paid by the NS after the competition is over, in order to reduce risks. 
x
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
The total hardware list is:
> 2x Dell PowerEdge R730xd (E5-2699v4, 512GB DDR4) - Used as block miners
> 3x Dell PowerEdge R720 (E5-2650v2, 96GB DDR3) - Will be used as handlers for The Lab's pool
> 8x Supermicro x10DRT-H Blades (Mixed CPUs between E5-2699v4 / E5-2698v4 / E5-2673v4 / E5-2620v3) - Will be used as ann miners to generate all announcements necessary for the test environment. 
> 1x Dell PowerEdge R730xd (Storage server)
> All other machines required will be hosted as VMs such as the Pools Master, blk handler, and pktd node.

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
    * Contestants are expected to know the rules and 
4. After results have been published, the fastest proposed implementation will now become **the mark to beat** and applicants will have Five (5) days to re-submit.
  * Re-submission will return the process to step 2.
5. When there is only 1 candidate remaining, they will be declared the winner and the embargo on their submission will end.

### Possibility for further rounds
If it is agreed between the winning candidate and the competition administrators, another round may be added:
  * The process will return to step 2, but with anyone from the public able to enter
  * The bounty for final win will be raised
  * The current winning candidate's submission will remain under embargo

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
