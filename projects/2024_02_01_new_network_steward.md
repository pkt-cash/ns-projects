# New Network Steward Vote

* Project Name: New Network Steward Vote
* Contact Email: cjd@cjdns.fr
* Project participants:
  * Caleb James DeLisle
  * Whoever wins the vote
* Projected duration: 10 weeks
* Projected effort: I don't expect payment for this
* Pre-project effort: About 2 person/months, but I don't expect payment for this
* Requested PKT contribution: 16 million PKT
* PKT address to pay to: pkt1qkx7feflncphh4hqchueqln3k8vts60g3lwtz9j

The object of this proposal is to establish the new Network Steward voting system prior to
implementing a soft fork in the chain.

I have already developed:
1. A vote counting system: https://github.com/cjdelisle/Electorium / https://github.com/cjdelisle/Electorium_go
2. Ability to cast a vote with PKT-Lightning-Wallet: https://github.com/cjdelisle/PKT-Lightning-Wallet/blob/master/proto/rpc_pb/rpc.proto#L4140
3. Ability to cast a vote with (old) pktwallet: https://github.com/pkt-cash/pktd/blob/dfc2b99e9226b70ec108738962138a7179744690/CHANGELOG.md?plain=1#L6
4. Vote computation system in pktd based on Electorium_go https://github.com/pkt-cash/PKT-FullNode/pull/3/files

As of now, it is possible to cast votes, and to count them. There are currently 4 voting
addresses, 2 of them are mine and 2 are from other community members.

Currently the Network Steward address is yielding 1.596 million PKT per week. If the new
system were in place now, this is how much would go to the winner of the election each week.

What I would like to do is take custody of 16 million PKT up-front and then begin paying it
out in batches of 1.6 million each week from the start of the project.

The project will begin when I have received the coins and when there are over 100 million PKT
currently being used for voting. This sets a simple target threshold which is easily
achievable if there is any amount of community engagement.

My long term plan is that we use this project, and consider extending it over time, in order
to manage the Network Steward on a go-forward basis. When we have reached a high level of
confidence in the correct operation of the new voting system, we will pursue a *soft fork*
which imposes an additional rule, namely, that the *old system* Network Steward, i.e.
pkt1q6hqsqhqdgqfd8t3xwgceulu7k9d9w5t2amath0qxyfjlvl3s3u4sjza2g2, is forbidden from making
payments to anyone except the *new system* Network Steward, i.e. the winner of the vote.

After the soft fork, the *old* Network Steward will not be capable of awarding funds to
anyone except for the winner of the vote in the new system - but will still be capable of
halting the funding in case of a major incident such as a security exploit.

Then at some point in time after we have become adaquately comfortable that the soft fork
is stable and the chance of some incident is neglegable, I will envite my colleagues to
publish your private keys such that the old Network Steward address will become a simple
pass-through.

## Milestones

### 1. Funding event
When the coins have been received and are in my custody, milestone 2 cannot take place
until this milestone has completed.

### 2. Election concludes with over 100 million votes
This event will take place when there has been an election with 100 million coins counted
as votes. Elections in the new system take place at a period (once per week), if there
are 100 million coins in votes before the election but then some of those coins are spent
or the votes withdrawn, it will not count. Furthermore, if there are 100 million coins in
votes but then after the election, they are spent of withdrawn, the project will not halt.

### 3. Funds exhausted
Each week after the election takes place and has been counted, I will transfer 1.6mn PKT
to the winner.

## Project Halt Conditions
It is my greatest intention to ensure that this project follows, as closely as possible,
how the new Network Steward will behave in real life. To that end, I do not intend to
make any value judgements on how the coins are being used. If one believes in democracy
then one must believe in democracy even when they disagree with the outcome.

There are, however, two possible conditions over which I will halt the project:

1. If I believe that the transfer of coins to the winner would constitute a crime: For
example if the winner is an OFAC designated terrorist organization.
2. If I believe that the vote counting code has malfunctioned and is either not able to
produce a result at all, or produces a result that does not match the result that should
be expected from manually computing the delegated voting process over the duely cast
votes.

In case of a project halt, I will re-start the project once I believe the condition has
been remediated, or I will refund the coins to the original Network Steward address if
I do not foresee remediation within what I consider a reasonable timeframe.


## Disclosure
I hereby submit this application in good faith and I attest that I have made no effort, nor do I
intend to make effort, influence the Network Steward to accept this or any other project I have
submitted.

*Please check one or more:*

1. Conflicts
  1. [ ] An organization is receiving the funds
    1. [ ] Organization has financial relationships with one or more reviewers: *specify whom*
    2. [ ] Organization has no financial relationships with any reviewers
  2. [x] An individual is receiving the funds
    1. [x] Individual works for same organization as one or more reviewers: Myself, I will not review my own propsal.
    2. [ ] Individual has other financial relationships with one or more reviewers: *specify whom*
    3. [ ] Individual does not work for the same organization as any reviewer
2. No Pumping
  1. [x] Project results will present information which might lead to PKT price speculation
    * If selected, please attach a paragraph detailing the information which will be presented and any steps which will be taken to prevent this from potentially misleading the public.
  2. [ ] Project results will not present information which might lead to PKT price speculation

## No Pumping
100% of the funds allocated in this project will be forwarded to the winner of the vote to
do what they see fit with them, so the indirect communications are beyond my control. There have
been and will be direct communications in order to encourage PKT holders to understand the system
and to vote, but they do not encourage or discourage the purchase or sale of any asset.

## Legal

The applicant understands that the network steward is not a legal entity and no part of this
project constitutes any form of legal agreement. The applicant accepts that the network steward
exists thanks to the effort of volunteers and the applicant has no reasonable expectation of any
action, payment or communication from the network steward at any time. For their part, the
applicant has no binding commitment or obligation at any time as a result of their participation
in this project.

## Project Status

Accepted with payment of 15mn. NOTE: I initially planned to request 19.2mn then I updated it to
16mn, but when making the funding txn it was 15mn. In any case the project will progress by the
same rules.

Transactions:
[1](https://explorer.pkt.cash/tx/dbdb73166cfb72b22e04c2f392819e84a9caddb56ed0bfe7cf716e3f15a0e401)
[2](https://explorer.pkt.cash/tx/ab8bf3eb9ca8c802ae4cf8c99ebd6205293a95220c7cc6cb4be2721e7bd1c966)
[3](https://explorer.pkt.cash/tx/7688fb5687f9ec9d51bef7da1c20ebe9daca294dd65702e54ff933250ebf4e6b)
[4](https://explorer.pkt.cash/tx/e09d6ee6fb20170273545cf1b07415eb86c6fbbffc4ad8b0fb73afffdaa5ca05)
[5](https://explorer.pkt.cash/tx/5392e5f6cc302c43db274cb4183aa4acc5c5a248173fba9d7ff9385c92e1bca1)
[6](https://explorer.pkt.cash/tx/ca38f57268e23f0cf17c12633f3e74440a6966cdd71a166b502ae94947c1070c)
[7](https://explorer.pkt.cash/tx/4cc1a9ad97a939080c4b0254acfcce951d411c2f3d8634d35604b48c0021d2d4)
[8](https://explorer.pkt.cash/tx/1b0a7ad7cd2d3df661cc10283c3d855e4b16f07501228a03b1d362f688e6b5b7)
[9](https://explorer.pkt.cash/tx/27ab6d35a52a0ea09e14133b83d70eef228ede471fa259d96b6b58d8b87909c5)
[10](https://explorer.pkt.cash/tx/ffcb730a46d7511cfe538bbb04b48c4e37264e89359bbe689df5113f785b7400)
[11](https://explorer.pkt.cash/tx/04f247fc101da9bc1b4b51e95c06e884cb4641e368acaac583b38fc7969352ed)
[12](https://explorer.pkt.cash/tx/bc2c08589037db069f981db762ea851c991c1448173ede054b87b944055c982b)
[13](https://explorer.pkt.cash/tx/33f54a512a7aaf62a5182081ebec08f910b38eaf17c4004af91aad15adbaa41b)
[14](https://explorer.pkt.cash/tx/8a7d0a472d31ef38617efbc114391f4e381755d794ede0caffe5ec271f235cc5)
[15](https://explorer.pkt.cash/tx/71ee8d138e58087bc848423ae43450a44dba545c0106140d388f6ee3a18a4a75)
[16](https://explorer.pkt.cash/tx/4c9d866f3938edff3982f561f9e79a2a9b919ec1f814839e88cf2d0b2599dabc)
[17](https://explorer.pkt.cash/tx/43d7065e8a286cc6f4a8e2bfdb67876510a37f0eb06299e5bad9c6cdee4fb352)
[18](https://explorer.pkt.cash/tx/ed088210081f74f65ca634fdd7fb77c7e9dca4bb8e227d3cd73be90d4c28cb60)
[19](https://explorer.pkt.cash/tx/1bf0cd2c173dad9d48a6d98ff5e2378d590e5a4f295da04940bde2e49f135085)
[20](https://explorer.pkt.cash/tx/36a468feecd78241f1f21eec6c327981110b2b465da9df21529f0817fd93622c)
[21](https://explorer.pkt.cash/tx/846f2dc4cc7a2051708c6e560976e4de90e9743aac73a8c80f3020644658ae79)
[22](https://explorer.pkt.cash/tx/72329d93acd0f9179346f42389141fe5077debade7fb842acec1c695331ef50c)
[23](https://explorer.pkt.cash/tx/3076ddec1455f5f8c1a8305f8e84b046f09ef456f600deaa5ba0b42599492595)
[24](https://explorer.pkt.cash/tx/e3a42bdc0b5c026918e17b3877159e2eae198bd26649bd32f257a94cceefc316)
[25](https://explorer.pkt.cash/tx/5d6df6b462c87edb58188aa44d1e7e2149bfe5602839aa44c3b4b5ef11e6971e)
[26](https://explorer.pkt.cash/tx/afe0acf056bc40da17288526ba17d8de562bc63309f1e9cb65694e8de1f25713)
[27](https://explorer.pkt.cash/tx/76f54f9f32b885eda6929f203ef9bb2551becb3dea881429827a26a3ef58c68a)
[28](https://explorer.pkt.cash/tx/8884d5a33f6002704f35e08a6a0e3ab563f78af418b7dc36211643deeb8d6855)
[29](https://explorer.pkt.cash/tx/3b027ad593d4454541b5737dc14eefdcc80989b534ef768a1ce2b4248910fd2a)
[30](https://explorer.pkt.cash/tx/a89e1d06256384ba18e060afd87adc9dc29bfd7c67f34fa73b87d5cdedab8313)
[31](https://explorer.pkt.cash/tx/51573695a3bb1d179eb81679f06e66abb6267e859efa8dc1739c78050c6a602a)
[32](https://explorer.pkt.cash/tx/a8bdd655469cf72588a98abf8d6b8d92ec85c1775c989aa2d12cc182659c996c)
[33](https://explorer.pkt.cash/tx/2b86caaac473de2224bb3021573fa4588d2a0dffb0520e22b2bcc4a3f9395310)
[34](https://explorer.pkt.cash/tx/27e5f3e5bb8c2df983fe962043c2e386b8ba8e86f00f7ae14336ecb41ca6becf)
[35](https://explorer.pkt.cash/tx/175259302771e93d8db1d44b36fe41fc91ca64392ab3aa7ab2c285c12a9e4c76)
[36](https://explorer.pkt.cash/tx/94665cbef93bfcefb15ce0637dd095245ec71fd93d39dac26c101532a4624f33)
[37](https://explorer.pkt.cash/tx/4270a259a7d758a0e8a8a5e3e83bb881ae3170b938ebfc0b697648ae9039c438)
[38](https://explorer.pkt.cash/tx/3b7fd34c810ce6fc7513ad58038e0cf6e66ccd9843b7a520f5b2a5571cbc7614)
[39](https://explorer.pkt.cash/tx/535378c0f51b2c55b60fec74c16a2c6f482ad50065e2c50604c7450a22514fc1)
[40](https://explorer.pkt.cash/tx/aeab7e1af89b07c27cc0725a4b495dac2b6ad2053ad4621abb1036454cce8af6)
[41](https://explorer.pkt.cash/tx/e3821febd1775e8c16657967d7d00ad61aa95247e1088b5bccc1b45b2cc94b69)
[42](https://explorer.pkt.cash/tx/24418f67ce65fac27c0ab9d5fec646de9a6c0ec1a0c3072935c350d92a0e5a70)
[43](https://explorer.pkt.cash/tx/cdf39ad72752366c4fe785b1edd3504b492f23e08ab4da86f8fbfd1a70f1ccfe)
[44](https://explorer.pkt.cash/tx/2eb20efc7c3a5f88fb5e2d7f2605fb5f60b9b99f2275ba68f089062647834ce9)
[45](https://explorer.pkt.cash/tx/069a5c12c1a9b50ef3b3416d22eed8b3f25b7584a798adcd4e524cfde6c7114c)
[46](https://explorer.pkt.cash/tx/8dc007ddefe1408fe78b71ec6516db485468de0e50cf8bce7f3e6a84d4849b3c)
[47](https://explorer.pkt.cash/tx/4b13aa8f5d483fe03735e5fd0630734a30ce0f6d73a0b15c08abbd4b0f70cb66)
[48](https://explorer.pkt.cash/tx/0879cf1fe6491a1d8d9097d665cc5a73fe3ab8cb6a5a128641f78701e09842ba)
[49](https://explorer.pkt.cash/tx/15da5558967cc334156bde97f9d25f71f9c7c4c09b74c987d063b23ef14479fa)
[50](https://explorer.pkt.cash/tx/88634793cff2190a725a6bf7dfb80c5d2765c312c85c08b1eb1b0a2e475ef711)
[51](https://explorer.pkt.cash/tx/5697b55c067310ef0ca0df461fbcd1f57a0bf48728daf510518255d407c7274b)
[52](https://explorer.pkt.cash/tx/82c718361f4d7bc30b5b567d4ecc1876a17aa376420eafbaaf0189beb6048766)
[53](https://explorer.pkt.cash/tx/2b491a6e3f381753a1b277b0293fe0afbbeff5055b648f0d8a919afb78f799a7)
[54](https://explorer.pkt.cash/tx/9d90f91c96e186a32bbece22adbbb02b43a6d6a195300ae21ada7187d2eb0f1c)
[55](https://explorer.pkt.cash/tx/37e1d483ba2ad080a213729d7f852188fdec1f1152136469811496c4c0831974)
[56](https://explorer.pkt.cash/tx/4e03bf81800c23fcd41e4b4692b743a6fd3d56e3bee8c94958d3d3dcd1c640d6)
[57](https://explorer.pkt.cash/tx/cec13a6c346ef7509f46a4039b0a981e44ce439480d9a606c90b54623b353f6a)
[58](https://explorer.pkt.cash/tx/a4cf120c1a871f8f069aca8cabf3090c30f9cbf0f260738c177823b074498a83)
[59](https://explorer.pkt.cash/tx/023c23416875595a8554d5db8a319188e1bc443f90e98604a391fd9d8b8f17a1)
[60](https://explorer.pkt.cash/tx/77e71b22ebf2241b9d4fc30b1ac343f3b3c3f42cdc4720d0850a553e1aa9cc92)
[61](https://explorer.pkt.cash/tx/7b701d026646b4a38ab18e2cc646e13771b83066761ba7b09d1c2084d632441a)
[62](https://explorer.pkt.cash/tx/3f9888e6e34255cd69b313548db6523aa32af38ab082487e186a2517e61d59c7)
[63](https://explorer.pkt.cash/tx/5cd7e2ad7ef9517df6b0b40317e2e521904e047dabafd2579bf431ed92bebd0d)
[64](https://explorer.pkt.cash/tx/45da9b3ee1108ebec96d59a11254ee1acc0453c1d3fbba2c72241f8bce0ded5d)
[65](https://explorer.pkt.cash/tx/0acffeda93cbc9248e112df6f1ed3a34fdcea642e324125a479c2f0c77dd4649)
[66](https://explorer.pkt.cash/tx/84be6a83dcd0b8c770ff365164dd3870c911cc614bc96e487fbd093d3f429911)
[67](https://explorer.pkt.cash/tx/c97baaba3f2c59236b4ffc5b7337e4f96966338821f64fa90f69fef73613eaea)
[68](https://explorer.pkt.cash/tx/42b185ae05b35ff01d70b3ac30fcb612bcc82b4f9b3871e8a2f8dae28333df53)
[69](https://explorer.pkt.cash/tx/c12f56b9891e95a14ea7a165f89699f388b71bff053dc4779629f1eb307059a4)
[70](https://explorer.pkt.cash/tx/c8f3b15d6fc8610fbd8fbe520fba1864189a3ba3194a195ae2a611185585219c)
[71](https://explorer.pkt.cash/tx/023bf1c95bfeb39e0aa2795588d6b55f8ae4bd3c77372b58c2b110ccb5233602)
[72](https://explorer.pkt.cash/tx/5eb21889a5f48acd7a0d510c5608f82459590c46c80adebc19d56b1e36fda2ea)
[73](https://explorer.pkt.cash/tx/202d0eb0bfb8573ea5665d12b3d24209d5a30cffe224e0a3af8efb1a817cbc57)
[74](https://explorer.pkt.cash/tx/1c19ce496d83ecec0389dabb8ad9d94755dd85eb9d43174864b862a76735d43d)
[75](https://explorer.pkt.cash/tx/c2828956e196bc4ba324a96f2f7ba5f937a0288d7b7369d15119c321171377e9)
[76](https://explorer.pkt.cash/tx/da04cd369b24459246b3dd9c9c2f89c5d07e1fd719d475f49beba6fd4d3db492)
[77](https://explorer.pkt.cash/tx/c52cf220c1adad1d897d842b1a213d73352a700bfeb903cca630e8b58d22ad46)
[78](https://explorer.pkt.cash/tx/b493c022051dcc4665550bb47a79cc71cff4c5e3dd7f467881870c005708d494)
[79](https://explorer.pkt.cash/tx/0e708f7db6f16456dcffca79fa7ce3188d36c5f8db12d1b426d36efbcbb705b3)
[80](https://explorer.pkt.cash/tx/7a01c8b31acd5fb2a94b1b3c259a1b514dae25ac76aaaab68b2d446f32a319ea)
[81](https://explorer.pkt.cash/tx/3a9e69fb19594fb1f7c682ebef8ca934b4e0618e4f5ef0576f050b1c4324be80)
[82](https://explorer.pkt.cash/tx/b9c8ef9b7b8e59fb4b76b00190bcb80b42211ce05edfa677af0acbf1dae38e22)
[83](https://explorer.pkt.cash/tx/d0efcb9185818d2c923a259076fb00f468d870fd4ee8333d2001cb94c324ce59)
[84](https://explorer.pkt.cash/tx/fc34e1989bc712f21865c34533ca64381557e8bc4bbbb1b5e0b3533183bb944e)
[85](https://explorer.pkt.cash/tx/2f36fa27d5ca9610ef5b0162224f5e35618012da962f7bfd4829f3a26faaf048)
[86](https://explorer.pkt.cash/tx/7dc113ad873f1bec9af56698b9372144d9bbe9665ad37111074e4c8ac95ce979)
[87](https://explorer.pkt.cash/tx/60d87bbeac08034ccf7075f24819bfc1ce904e9e2996f5999c40aad2817e9fb3)
[88](https://explorer.pkt.cash/tx/9f8a0a2410b8646767723e12c6dc1d2475de7d47d6a8c25ba782588c5b24a680)
[89](https://explorer.pkt.cash/tx/54343b29326b978664f9a89afb57b60b623021450cb2b9c2d7c671e1c77cbbec)
[90](https://explorer.pkt.cash/tx/2d3097cdf27cd1e29764f070d3d71abab1c1c73b394adbff6fc546f0d19b5e7e)
[91](https://explorer.pkt.cash/tx/33b1e51a31fbac592142e43063c8c7f0ee2308d7cbd8d27a6a8caf0ebbe082c7)
[92](https://explorer.pkt.cash/tx/336b19c06d48e68c1b81659aa858bb8a5804506712b789c910f54d00fbd3ed28)
[93](https://explorer.pkt.cash/tx/de33367726934698ddf4fbf7ef73813fd9adcb5eb39dbcef9d4654af4bb4af50)
[94](https://explorer.pkt.cash/tx/78f5071004358a507091baaeac1e9add361a73f83a0d0b1a1b789d75c8c2d4a4)
[95](https://explorer.pkt.cash/tx/e3119769acbe8ed23ce6f6e1c6902183028ea364da571dad07a4776cd31f5d80)
[96](https://explorer.pkt.cash/tx/f609cf0ebaae45669e2d0d2da15f967cbbabaee50236c05600494001d05875c6)
[97](https://explorer.pkt.cash/tx/98ce91e37d513673d8083469a2c46ddcafe8637e51eed107d4543d95c2bdc98e)
[98](https://explorer.pkt.cash/tx/fd7c523e4452d0dc5344fed90f299f3ee85fcf03206d8330e424319b64d4baee)
[99](https://explorer.pkt.cash/tx/339668bd8d078af085d51f2b5bfea250196cc2aa73063c03a809af9833912c01)
[100](https://explorer.pkt.cash/tx/245b71a178a18cba6ea77401ae9a9dc3d0c3d4342ad5d96e805a17167c52b340)
[101](https://explorer.pkt.cash/tx/0b6666912abe2bc5b5ca44edbf5e79c34a64b0103b08531eae16c1a9bc363ac8)
[102](https://explorer.pkt.cash/tx/094991667783e514ec9686a46717b113566efc722e36a639eee71a285d17ec1e)
[103](https://explorer.pkt.cash/tx/b6538ed709542b5863da7752e7a9fb78f69834d6305ad1c2f30b9ce12343246f)
[104](https://explorer.pkt.cash/tx/989998494100c36dd252f91f68c0ee2edf4a54777c898559932f33043202eb85)
[105](https://explorer.pkt.cash/tx/ad7f9ee8d09e43788f86d310860c90aa43dc3f74138e26206f80cacacc0adc14)
[106](https://explorer.pkt.cash/tx/0f95a8e03de3347abdbf99708b38227b7b797f0fbb091b9068d07bec85e14c6d)
[107](https://explorer.pkt.cash/tx/f89e4c8614b264a8520ce53898210758b15135ea7fdb4f22ed5879bf5d6ded01)
[108](https://explorer.pkt.cash/tx/f02a7b84a849f414e3cdaae4ebc20dda19d14e68c875b58d818a7f03e069d879)
[109](https://explorer.pkt.cash/tx/db3d1b0d168e1b869c29520ab29aa4b923b0f94c997434df0be71e11b7278d5f)
[110](https://explorer.pkt.cash/tx/a668e42ae016ab989267b9ff6a0ebc55a112fa9b92fd28cf0029d0fab9a59359)
[111](https://explorer.pkt.cash/tx/6acf6dc9bdc386c2aef8e1b21272eb7523557d1f8eb720f8d3fc8cb59d1578a1)
[112](https://explorer.pkt.cash/tx/8a2c1db3d6a44b3fd1b0ff0871e93b180952cea7b01ec775e5b50e621672f493)
[113](https://explorer.pkt.cash/tx/4c27d57d7589a197aa1372273ceca88396fb77cb2a496d2847f2da811ae9f1aa)
[114](https://explorer.pkt.cash/tx/e8e64eb56349bd5d5ef4f3fb4879bd0384261be6679cdb49288e1a85d8c1f538)
[115](https://explorer.pkt.cash/tx/64cc8cf72e06aea6a66243ab05e832990e072af769b52ca21bb1d7587575f76d)
[116](https://explorer.pkt.cash/tx/04f15642e1acd42732a4b37d5f502f04dcbde19f39ca31a7aa15b03961b61f8a)
[117](https://explorer.pkt.cash/tx/df9b10ffefe2e49074f640781f33805908ed387e419d7a1bf6ba3daa3c79034e)
[118](https://explorer.pkt.cash/tx/ecc951bb859f4c055927c4d04291fe3d88add9af0d44a3ebf43422b665448a4a)
[119](https://explorer.pkt.cash/tx/71c7d93a8491a54c44eb7d58891d1ba2627999aec99cbb44e84fa68fb180a847)
[120](https://explorer.pkt.cash/tx/922707df657aa3cbbdcef818b23e799c37a3cc1545ec1c6edd7d5d825f07dc6a)
[121](https://explorer.pkt.cash/tx/88684dadd98efdbaca0993a17a9ef86c3986847a6a3af82262beb2dbfdfd5d41)
[122](https://explorer.pkt.cash/tx/d2aca7cc29a3a465d2ba70374477184ced859ea7d94230b15add8b41c506e0b7)
[123](https://explorer.pkt.cash/tx/e2821061b383c298c7fa465bd3b38f7995f2910e8c0f5e526e4f8ed1dfea2796)
[124](https://explorer.pkt.cash/tx/b4897960220d5dbbfda507367921e2a8d921dd9ea14c30e9787018c056f3150d)
[125](https://explorer.pkt.cash/tx/0502c8d8af647833d580b3433553bf24bad70a9258b20a2df32f25cb8120dee9)
[126](https://explorer.pkt.cash/tx/001d04c07879ab4347531a75b954bef3d20e06cf1b0daec095510ef4d9d870d2)
[127](https://explorer.pkt.cash/tx/b03177a75bf3100bc2fd155087882f437a278cc1624f0736459268399add850a)
[128](https://explorer.pkt.cash/tx/a6897b6dcc553beeddbf7ebb237a8ec6f87d9ce65d7a3410f745941ecc35f759)
[129](https://explorer.pkt.cash/tx/81a593bc57b9a02f3aae28fc6cc9af010a653ce642b3063df17829de60d0959b)
[130](https://explorer.pkt.cash/tx/8efd3a2ca5a6639f55e7a7280158a8e8037a727c8d70d40247a0b0ab0c7ca645)
[131](https://explorer.pkt.cash/tx/b5914ae8621c4c5d20d9e0e50f796b854d6fe82a6441ca2b7fc18062f6f8c77a)
[132](https://explorer.pkt.cash/tx/7ad9b45f5b87caab9d100215c3e6d7cc94257bab18d5eec4cb9134570fd36dad)
[133](https://explorer.pkt.cash/tx/f5b472552d910179777736f160610d5965cdede9e788c5046cd76837a2a04b84)
[134](https://explorer.pkt.cash/tx/8e05d60e721a0e365fecc9075e6ad0ba99c55427bfc6cd089f98504a5d0935eb)
[135](https://explorer.pkt.cash/tx/9ff98c0a4bdddb2f02538d663d83b3d408b86443fac2a3333822b20e6034a670)
[136](https://explorer.pkt.cash/tx/ea1747c9ecc4cbfba0619c668673565674c39ae00d3ac1d7581cd82fb4e930b8)
[137](https://explorer.pkt.cash/tx/12bdb3545269ee84e398f9ef457675728178c0358fc8c323a1176c6bd74a202a)
[138](https://explorer.pkt.cash/tx/79db7abdbe50fb4eff348e960146b580e3f8cb43776a4a227bd8cc302319bbd4)
[139](https://explorer.pkt.cash/tx/4db2c13dc26c95329395621d7b39e399fa4a38107fd84c4dd46a30734a993c94)
[140](https://explorer.pkt.cash/tx/c1040a40e0773881d379af591e4a1d4a78366abf39df5e23416f53ee1aec2468)
[141](https://explorer.pkt.cash/tx/4153a34a53f8af01169bef3d7e031c5ec7a7c26ba4ee99e7162937585b151e91)
[142](https://explorer.pkt.cash/tx/32968c451180e937f6833dc0391dca9595529236df1f491de70745c282c639e9)
[143](https://explorer.pkt.cash/tx/36e6397b622db3432194ef85419988c929998e5b6388cf42526fc02c22e4b828)
[144](https://explorer.pkt.cash/tx/14a039da210effc8f076c0e279089693811fb38c9aec6d0a8baa21008004c213)
[145](https://explorer.pkt.cash/tx/c9af8d20d981d164dff31b7dac2ac50538c945cea72211b05219bbd961128c2a)
[146](https://explorer.pkt.cash/tx/926ec52df8ffbaf10d98743f820d691bcabc7502ed1cbe0aa90184517e477f2b)
[147](https://explorer.pkt.cash/tx/09bd509ad3252b73d3dad432d1f62b3673611a837a215325bf18474342396b8f)
[148](https://explorer.pkt.cash/tx/26f7748193eec572b61b16eb45897e16d8dc7c4a7e9c7c672b4eec249bbeb5bd)
[149](https://explorer.pkt.cash/tx/24e2377bdbd5528b115aafe0e04dabc7c8355d4d54ab20d732cbe4c5c1e385a1)
[150](https://explorer.pkt.cash/tx/b1e7dcec2b9475d937352f482fe48998848866b7d3b3eab9274a9ec2ab3877ab)
[151](https://explorer.pkt.cash/tx/bd053fe40e019cb4a3ac17d77d79ae9ec4f1f35a545a34e195a512769097acbc)
[152](https://explorer.pkt.cash/tx/fc342741031ed5927da6ef19872e213575537f164c6e7a7fa9d095be990f2c2f)
[153](https://explorer.pkt.cash/tx/2e2143c53cab0249be4f4fdc3cc5d5c34a7c62f5f0669208daa1064131cedc39)
[154](https://explorer.pkt.cash/tx/6c08d6b03512aae25327e23c292111f1a6bb8b1a1262e5605ae6f3f30cc85858)
[155](https://explorer.pkt.cash/tx/d93b88e4e145bc9c5dabf8138b12376b7a410370a98e0b488e489e803cf2fc49)
[156](https://explorer.pkt.cash/tx/e946a36e949cf4aa2f45c21528cbb25d5ddc4357a3f3f71ccc79a67c9f2cfb03)
[157](https://explorer.pkt.cash/tx/52c40183c3afb7f58b8e1f1440b66ed8f9aad5f08cf8dc4214a812c8de8e4e9f)
[158](https://explorer.pkt.cash/tx/ae750962192a2f5c48c95a74bca7302f24c2c34609e2e3654314acd3c82e72e1)
[159](https://explorer.pkt.cash/tx/a4268ef882180756ac19571df27aa0bbfc9b89b666844a4b03e84f225ce27be3)
[160](https://explorer.pkt.cash/tx/74bbaa052315f0b63a92500d2c0531ce4f7bb90a44653cc08ec683a8d0f29fe7)
[161](https://explorer.pkt.cash/tx/620419db66be9fa087fee769e09372469d7c09688ca77be7fcac9f4da2f08a03)
[162](https://explorer.pkt.cash/tx/8472d130499aa6ed2d35158575a62d3fb5c282d9e9f24c5cb1f2c453c4710630)
[163](https://explorer.pkt.cash/tx/db32f775f2ee15793b35bc6169a152b898075e3c87fb71ddb35f09ac344c2d89)
[164](https://explorer.pkt.cash/tx/3d30f53463e16058bfd7a51df433ac55cb81b34471f07a7f054fc6e047d051fc)
[165](https://explorer.pkt.cash/tx/3ae99c01b161f1c5308c18502deeed85fe81f9c868a0ed413c98a3036bb28979)
[166](https://explorer.pkt.cash/tx/d906834560b91fe54a7211a823c28a65b64b213fb861e6451cea528f0a695ef7)
[167](https://explorer.pkt.cash/tx/7de9275daa91d7a1c8406ecaa89b1ce24af72811ef082a20a6a6020b665846b4)
[168](https://explorer.pkt.cash/tx/be291a90e4417148766636f6dddb5553a742d1d6cfa9a6f8bd9702445220830c)
[169](https://explorer.pkt.cash/tx/f8d4341d965a3743cb65e4b54e21d3bf9f7d1b05b9422e119e41521c349083f6)
[170](https://explorer.pkt.cash/tx/c78171429485324fb5a84a7708fec14c64f8de1713d03999d3623c3dd276da8c)
[171](https://explorer.pkt.cash/tx/99bb1310da00a2c53818f7c1c40bd077fc3ad218b0505fbe33b23000dd459714)
[172](https://explorer.pkt.cash/tx/17ac3527a1fa1c9f9951b3906da7d20aeff3e7b46669eb95178821b7e04cee31)
[173](https://explorer.pkt.cash/tx/1f97c4050cfb0063d60d002cdc206b086bd7a38c4fba72a7723c088bca650e00)
[174](https://explorer.pkt.cash/tx/c3ff6776bec4d3e3b62ac016180b1cb4b2c15c6bfed1d54eeaf2433b1a8515d9)
[175](https://explorer.pkt.cash/tx/27fd0bbbdafea5055cf1c511db8a36283dba32eefca4c71362cbd7b057cb9111)
[176](https://explorer.pkt.cash/tx/0d2eec22182e13dfeca4e0dd2b776e4596a27407718d9c0f075f099f09dbcd11)
[177](https://explorer.pkt.cash/tx/89218ec7bf10c70c07383a144a60170c4753cca93dadbb04939846a97ca0131e)
[178](https://explorer.pkt.cash/tx/68cf3640a7f87b3959cce350b9fe24cccf076715a025dbe71ac43c18c2cf6181)
[179](https://explorer.pkt.cash/tx/90d9d91ac05ddcef60f6088c9d23bd5e0eecedfbc45c3e8f081d538989edaa4b)
[180](https://explorer.pkt.cash/tx/6b01c0f70cd8ec2b741e5f6ba0a39fc08e8a054a1b9f0f81254075f789b742d7)
[181](https://explorer.pkt.cash/tx/d7fb6a6c65a8cf8d14acd4668259cb3e9e23426ee5a5b70cc950bad3c31f2503)
[182](https://explorer.pkt.cash/tx/fa7cdc5d32dc2d3c07cf2cf10c80d3dd418256a425cbcfbd424ed6b7b8aa615f)
[183](https://explorer.pkt.cash/tx/227c3189ea2a3ff4649503728b70fbf828c4da8460c88b127d42b102a3267ca7)
[184](https://explorer.pkt.cash/tx/01ced8fcf56d79600bab67859f8d51e077432e7401eae265b0429e884017a333)
[185](https://explorer.pkt.cash/tx/496181b8b007ad789d5ce502f0b6a65b5700caf02b4461db44091bab7c4f916b)
[186](https://explorer.pkt.cash/tx/0a69a136f5cbcea9df11e502963d6419c556ba80ea36ada824ddcd3f0f036e23)

### Update and request for extension: Apr 28 2024
As of today, this project has successfully sent out transactions to the winners of the Electorium vote.

* 2/29/2024 -> pkt1q6sj0mchq7ltwm8c9tpm2wteqmeldr2ye5lcr60 [1](https://packetscan.io/tx/70c6f3b1c5d73244787b133ae496d426bf3594b9bcfec037a47377b6cbfd28d1)
* 3/8/2024 -> pkt1q6sj0mchq7ltwm8c9tpm2wteqmeldr2ye5lcr60 [2](https://packetscan.io/tx/a430d8f06f2dd4c6540f71e62a205ca03df5fa79faf7f4e42da9dc16f1762199)
* 3/14/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [3](https://packetscan.io/tx/768366708cb84af646128687d6397b46807f61b8deb67e29cb0908b6137f0141)
* 3/22/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [4](https://packetscan.io/tx/f6e7273a97dd7dbaa3302a294ee0f748d037e2146221cc5099f2539a7f0162c4)
* 3/28/2024 ->  pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [5](https://packetscan.io/tx/52c391e3298181118e3f439ab399d2c2cc803eece125d4ffb8c60971313b2d4d)
* 4/4/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [6](https://packetscan.io/tx/44d6e0920a73bcc2e246e32d0128a19a1bf2481a0115c95362e9626a0ae07a04)
* 4/11/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [7](https://packetscan.io/tx/c0fb378b54a83bdb1c2519812bed7fc443e18369088325844d7a5e46415ba55b)
* 4/19/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [8](https://packetscan.io/tx/ddbfa5fd078a3666805d7d3ea8242fb3d0c835f34b11bc43d252bda5da61c9a6)
* 4/25/2024 -> pkt1qnm94ypvfvjwe0mnk9z356m7waa7jtpzvkm4fhy [9](https://packetscan.io/tx/085000e3b012380333dcd2f9fad185b43b68a333d966a7b005906d54a9ee7c41)

The winner is currently holding 145 million delegated votes which appear to come from a wide variety
of sources. There is no evidence of significant community rejection of the vote outcome, it seems
that the vast majority of community members have voted for either the winner, or someone who
delegated their votes to the eventual winner. I have no reason to believe that the system is not
working as intended.

I would like to request a top-up of an additional 16mn PKT so that the project can continue. The
payout wallet has less than 1.6 million PKT so it will not be able to provide a full payout this
coming week, and after that it will have zero PKT.

## Status Apr 29 2024
A total of 15mn PKT was paid out to continue the project, it was paid in the following transactions

[1](https://packetscan.io/tx/f5c09a2cff613d1601b7bb3d3886df2678997a17f9877009dcc7e49044c714c0)
[2](https://packetscan.io/tx/7ea0f2fc0913366a52c600688b4121117e45a2c3403d7d55f36773c5d747c24a)
[3](https://packetscan.io/tx/409f3a8b7007c3c0d13dbafc29d0bc61c44c676dd9a86caa4d755b5fbc89bf7f)
[4](https://packetscan.io/tx/758203be2682156e9aafe4b479218a38b45af48c898a6aa8a13e577c14f4b99c)
[5](https://packetscan.io/tx/1f30e6431d01cc07e611ef87f9bca0bf473f93245ec7dac67cf294801d88d146)
[6](https://packetscan.io/tx/e5cfdff0d5cbb1248033b71b23f9c345643caa23858a0311e2c80c0e5056fa25)
[7](https://packetscan.io/tx/d173d91f760713c6ae5c03dbcc064d4f5408202e2b3c40d27b1a9f908151f473)
[8](https://packetscan.io/tx/1304ed1d5132ec15dfb215676c42682db4e61173abafe87414cfe68dc5821e07)
[9](https://packetscan.io/tx/9712a0ebf27162235db5711d2e0dfbe6707680b281de93c715c4f37bcb33d447)
[10](https://packetscan.io/tx/ca0640d681274231b9b54588e2bd14174754aa26448a7acf25d1601385b65067)
[11](https://packetscan.io/tx/562762a0bcba7f46c286050525880a339341a86d5869d8d2a9a2c1a3e1d865c1)
[12](https://packetscan.io/tx/897c12068cb1f758a56b49ea2a461c61b151d03dd0fac8214b401fcadcea4270)
[13](https://packetscan.io/tx/455907bd42ca8240d7c42b3683b375afd2d8bc6fcd5f90232b220fb3e91b6558)
[14](https://packetscan.io/tx/158a6d84a25b71e12c87509865916179fc673956164be454af6ed5f93f69b67b)
[15](https://packetscan.io/tx/5af591012c10fe0126824d7b11f66637040b30aa400e1ae9cf96ed4c67149af3)
[16](https://packetscan.io/tx/cdd999b748e8e6c6bc22091cd76488db23bd916b5df73e117ab6c1bf3ee0a0a1)
[17](https://packetscan.io/tx/0316a95572cc872b962a61ddf9760d73e136512e9eae0e6089b879484388e504)
[18](https://packetscan.io/tx/d9ae4efbb20b78ee0b6e454bf60d4d7f6c5f12702acc01795fefd5887d99a603)
[19](https://packetscan.io/tx/a1d833a21a060b4691b334c41a520b85fe8acb705db585fd3a2e121007d383e9)
[20](https://packetscan.io/tx/4fc5dc06b6694af7e1ecf38abfda7fba0841020c9d5cb4155e4a3b77d4be3859)
[21](https://packetscan.io/tx/678b0af7be4346d58aa49620329326f5046b25702c2c23a5707d784fcf7e77ad)
[22](https://packetscan.io/tx/916e099fe6dbfdbae585deea9d34d1b0e673ad13769393ff3484f07412243e79)
[23](https://packetscan.io/tx/8a976949d99e7459cc11b695101ff1ca4fa24842b768e007c899329d57ca97a9)
[24](https://packetscan.io/tx/6f0d45dc0de8a24e4c1a90c874250e41d3ca337acfbbcaae5983adc2feb7dfac)
[25](https://packetscan.io/tx/0ce38d17513c12eb95891618a0b91b32e1a58a74301b46b0937cd7b3a2df1a1c)
[26](https://packetscan.io/tx/ed564cb5722bb4c5d04463813809ee413e91ee2bd3f5a3a43eb894ae06b007b1)
[27](https://packetscan.io/tx/db0f8979a2401f9545b515cbe0031d217fab2d503b152098a047e7e1d2292054)
[28](https://packetscan.io/tx/525200ec706eb738ac009f72cbb964b74848446301627d2f8c1adb9a5c1975c4)
[29](https://packetscan.io/tx/d4d905fa1fd8e50c6cb0f85cd037609f9075cf25274fa4bfe9a9a926db51cf61)
[30](https://packetscan.io/tx/34f8abc4fb8539cbc13aa7278dd6ecc50d1a2d70a1649342df4672e59f09e79a)
[31](https://packetscan.io/tx/9aeb847deb60b3596f8fcc684b4c1434133d8c9d06746dc39bbb00a0117b5377)
[32](https://packetscan.io/tx/c3a81a7e5fe4e05e667edc5f0f29fc35742f5dfa8729d8c423261b791215dd7b)
[33](https://packetscan.io/tx/59ebca83126bcd8f94aa8369a87454be2106770e222e088d79f20c67d2cea0b2)
[34](https://packetscan.io/tx/e3b5f21bd3957eda3122e4f38b45411ba7dbacb81c67d52d277ba7c97397fcdf)
[35](https://packetscan.io/tx/f1ef42d0ce8ad72eef12bdbb763e3f11bbab9b1abe67a18506c9404c8e90e001)
[36](https://packetscan.io/tx/f13d40f34e326d98d9e7ceceb1a4a5f98c83e001e964618579d8978f64d234f6)
[37](https://packetscan.io/tx/d6ce55750788e9ee108c9fe586b5538b14772baebf9f1f5f4a5a3184f6003123)
[38](https://packetscan.io/tx/84bb9b390833b0889b131c97205e4805fdedb1f50d9c1982daebe9697a8df1e6)
[39](https://packetscan.io/tx/a0867ab6eee3b87cfc021df7fdecdd506030646cbfe71c5fac7da0831fd94053)
[40](https://packetscan.io/tx/5ca8a7e7ac23f6f9c7d963b1b769617629321f31f8b97721135a55ac8ff1ad07)
[41](https://packetscan.io/tx/6f5e52450169e0f81d7a2728cf0d10eafb284c4335c04a8d7d9bbd3faa67c60f)
[42](https://packetscan.io/tx/666852dbbd162f3e51c01dc86f88f77f713f165ebb7b3795cde7812037b6a689)
[43](https://packetscan.io/tx/814a507601306a2ebbf0d6036396e11073280ec90c21b6b4502cf552f10a74d3)
[44](https://packetscan.io/tx/fec1f6e12a1c0333acd2fd684a873ce3e6156b1b4cf84be970d67aec241c663c)
[45](https://packetscan.io/tx/d52cee98d38a619a1c5d8a8347c6866757924fd84f24b9858ef1ebb20d209e35)
[46](https://packetscan.io/tx/737c2c4a691ccd89a2398865add0c7f5108391fd267d51a959bd6143dded5c22)
[47](https://packetscan.io/tx/1f20e9cb1e86ad9070e2e74035d966745975a571cbe8a46ff96e57a06957c6b1)
[48](https://packetscan.io/tx/ce27feeedc6be20cb1fe2b2ed0aa25bbe27191773d686fcbf9abc15f9a8a4ed5)
[49](https://packetscan.io/tx/6e18760203f480ef6c98df7f4861df377224508a780bc8930b622d60daf8ef6a)
[50](https://packetscan.io/tx/f283061fc9381bbe847f75036aad6e10c080a173b9f76616d2d1156e02ab2405)
[51](https://packetscan.io/tx/0e9e1a51ef2522c09a25df1d670bc55f9d3e686ff09511b14bbd82ddcb299649)
[52](https://packetscan.io/tx/b577eab89ae0dd6f5dd5d0d4a6f07551973328e826d1e6f2f53be0b5c47b3198)
[53](https://packetscan.io/tx/0595062adc16bccd652c1abf1f3419131ea5adc1de192439268ebcbca9d456fc)
[54](https://packetscan.io/tx/28abf77df955dd5120ec11a9392b9f287bed04d15810f52e00e40fde630fec83)
[55](https://packetscan.io/tx/a928ccc0c8b3265fcf72e26556943b584bbd8f35dfbd652060c32b24b57f96d8)
[56](https://packetscan.io/tx/ec00bfa2af19a0ee1c61cec7c3ffa9e603d5ee6a8390f689b97edf5ddd4475df)
[57](https://packetscan.io/tx/eb374c296684cbaca9b0d2fec67836ff5c71e3fc35f9c04ecbfff26a234ed2a6)
[58](https://packetscan.io/tx/7c99111494073ca9f73b6bc7a4fe0d4264707c4bcfed0a474a5a11abc52452f8)
[59](https://packetscan.io/tx/e479fb1dff8ec4c1bf2204dc3275d0bc055e363caf5e4d22a6da445a80f608df)
[60](https://packetscan.io/tx/eb1c5aa790903e4e5bdcb7c3f794b67088f1989fb37293c2867cfe06cd637af2)
[61](https://packetscan.io/tx/9c1144a8280f62ec121e24b67179dbfe8f98d7535c74a2048d468e16d61b8f98)
[62](https://packetscan.io/tx/e5ed15210a486ee63b1c8738fd7cc6a062aff321479d34cdb1d00b2f7ae238d4)
[63](https://packetscan.io/tx/7449fc77302d3b670ae0fbf67cd20876c5206f56389e51c2f220f9d7d5edc633)
[64](https://packetscan.io/tx/25be6995e13d3f8087c5661d34b919ffc9e41c3fb94648aa68421822d12f004b)
[65](https://packetscan.io/tx/e6d311afc772201e91eaf63d68cbde88bc8d2c502398ae28f957c5118014c8cf)
[66](https://packetscan.io/tx/55dbf102d84b774c0222589b296fe021dad126ca79dd053cb5d8cfdc80f2ad71)
[67](https://packetscan.io/tx/33979f9f87e266f5e1f6d367c2a0886b6ac631574364ac114869d92f13bec111)
[68](https://packetscan.io/tx/27944fe7e8ebb9da7c66926ac5f9110b3ea940b40d0aaa8ce57125fcb7943c7e)
[69](https://packetscan.io/tx/8912862f6c5681012c9dfe3e89d1f2c06197b0190eae6e7a550fba8ccc524ec6)
[70](https://packetscan.io/tx/f731e09e651032b2a6af2017122dd7d6ccb0c7b6cf1b564f55883210910c200b)
[71](https://packetscan.io/tx/a86bcff58a4de3f8b42ec1b568ad47276af533d98284ff9aa7ca397a0092cdf5)
[72](https://packetscan.io/tx/b18afb012affa7a629d475d8723dd3bb3c593d5b27a0bdba358084240e5f5d2f)
[73](https://packetscan.io/tx/b175a46dc7247ec3b558bf0b877c32be4504395a92fee0bca0e5fec52fba555f)
[74](https://packetscan.io/tx/a4f49ac26cc8b3c226388fcfcf644c9e1ac5fe30becfd082f34fae59d9e1a358)
[75](https://packetscan.io/tx/9802fef2cb26971e2818ef332ad4128fe72178eed67e5d881d85461fa7e986f5)
[76](https://packetscan.io/tx/a29d0eb8eab9354c8a8eb0014e81630020b75786b8d49e11420ed5cf9d218b83)
[77](https://packetscan.io/tx/9f655e207e8d6b6bb2e3d75a4a71d57e46e69f9e07fcac06f6563ae693ab5a6e)
[78](https://packetscan.io/tx/459e19e8e8ff141d98013b5ee44a7f29a747a3eb154e2c7ac169a3fe704eea7f)
[79](https://packetscan.io/tx/112dd307fd765b42fd7e8808da9fa0f8d28bebf0733d44e2e9c846d9efe427e8)
[80](https://packetscan.io/tx/6add8c4edfda39620146c6145a2daf79a7e04326364bd32a9ee4148593ccfed5)
[81](https://packetscan.io/tx/54a829da2d56ff560a99e233587d155fab0ba99d724adb3b2f782017906f91f7)
[82](https://packetscan.io/tx/05910991ddc8edb748055d7079f49a8deed9623fca261a94408c41d4aaf622a7)
[83](https://packetscan.io/tx/5098f4af12262c1ebbfd84e40a294760d9979412b77505b17cfb35537e915a31)
[84](https://packetscan.io/tx/c7985d41124214b5acfcef08f63df889e3f2d32c28827e3f15f2c2cf7b6a62c7)
[85](https://packetscan.io/tx/4354a1dda94630ddf8e58e80a1e3c0e1765389991652318b105048477f4da24b)
[86](https://packetscan.io/tx/d5e9de18b9cc5213dcd6c6c0029c0560751fc10b16598c4e621b1e860494d01b)
[87](https://packetscan.io/tx/f82205373448057f1a4f94271c3b4a082dc2d9738cb6561a7450e7f12f3e1fbe)
[88](https://packetscan.io/tx/66a636d5bb98a3d16c486510c1a7dad1f4582f8e97170e0e9a2a4a9cfe763c9e)
[89](https://packetscan.io/tx/e83f62223f26943d3948e13c5102c1f55ff67ee76cfccb5b557699f89b38dcbe)
[90](https://packetscan.io/tx/ceb77d4ef78eff6ab879ce92112b9d1024b140f98306a8c22694dff9b0c0ff84)
[91](https://packetscan.io/tx/0754076a7d47551b36a2315d89b78a113482e4ceed92e1caf2f5800922d6c6f9)
[92](https://packetscan.io/tx/41dc9d10e3e57bd84313140e361cf69a861fc9cb2407272e3ddf7d3ecbd159fe)
[93](https://packetscan.io/tx/962294ccf93784f79372877707c6b7311497405a3ad9ebb4f81ec905a262c8ff)
[94](https://packetscan.io/tx/3c7cca49fda3dd5f2fe0e353b5580442b8eca32a0e8d5b3f254a0c6ced774d4f)
[95](https://packetscan.io/tx/d26f7a2a9cf37b8bb1832cd56d3bbf5b4bad8522d1e2de703680bfad96b81a70)
[96](https://packetscan.io/tx/6ab939fd90754c3554adc73ec86f1158db6621566b9f5853cc58af4fdf7e0302)
[97](https://packetscan.io/tx/490c83ff0fa9eb170af445de0d70b0955d595123a9a7b5f490c4641b17e13a10)
[98](https://packetscan.io/tx/db1ebb7314a9e13292b59f0e0a59e65904af43dfd63c83203f4c5af381b80c5e)
[99](https://packetscan.io/tx/29af90a98f38684009cb30a6af9ceb911761fbed28e71887ba44fbd8316ff7d5)
[100](https://packetscan.io/tx/60cccf71c51ec952066c5ba24de3b930791d2ff448ffdc8881ee708d336e24fc)
[101](https://packetscan.io/tx/2a11e660f16e4db333060c883427f47d080375718e6a31518a80725d36f5e296)
[102](https://packetscan.io/tx/f53e7f04fbb93472faeb00186229ff5c4bf7059899abe03c86d0d8ff83c768b5)
[103](https://packetscan.io/tx/a4e0d38877eae1b257c1e574cc4ebd3d275628510bcc49f78a7b21bdc9d4d86e)
[104](https://packetscan.io/tx/7d526782d3376f24957deead6195b872a6f52c7da58f9766cd294867d1d8c284)
[105](https://packetscan.io/tx/243b1428586040363aae6f7a08c06e6bb3a303c8512892c868662ad149213359)
[106](https://packetscan.io/tx/bc8ed3ac8df6cc76b1771462e1dc6f097179c407185d21eadf145ecb35f7684e)
[107](https://packetscan.io/tx/953c4221902cfaefef068c6418cbbd2c0ef1823e4fb898246993245d41a113de)
[108](https://packetscan.io/tx/f4c16b84d2e270fd9bef6e33272022e6b35a9bcb1bae3354d5a121e306bb5528)
[109](https://packetscan.io/tx/f4b8d9e004ab547738d905136b20d1811af7b43935bb80c416973364fba30fdc)
[110](https://packetscan.io/tx/a0076164144883e94e11f0d9171abed143a5c3a2d5aba3718f38b697399769d2)
[111](https://packetscan.io/tx/8fbcdc702b3fc3f13509959e927943319d967c81f33acc0b73a2cfc2eb5ce271)
[112](https://packetscan.io/tx/0e5bc39ea0d6c400d8c51478b8095e9f3a6e866f95df08f2df89a1a88e91308a)
[113](https://packetscan.io/tx/004a8b42c381e63db09ef83b2408f21a8c7a08c6da8e31756d2084efac639258)
[114](https://packetscan.io/tx/edd6381e41c76aa7e14776d8bcdaa34e7767f247692c06a7d5ceddb56b26b16f)
[115](https://packetscan.io/tx/cf79501c6c024166096c777280df4527a17a2009d68c0a5cc41b5ab9d27a8182)
[116](https://packetscan.io/tx/cf77e23573cbd979b0030672e2e3d35f80c623a76d6c26d5befc464a186e89aa)
[117](https://packetscan.io/tx/64bfedfab39e9742aef792fe83269236cd99bec4cf9d9089368e78188df78cde)
[118](https://packetscan.io/tx/fffc36ca39126284d509b20b6b5e751385ea4d00adea28a4736bf5bf60c888ac)
[119](https://packetscan.io/tx/bd9f205e3b9746b94b27d574e762804776e40e9bbc19d6879b5c08022944807d)
[120](https://packetscan.io/tx/9633c0382dea62720e02f281f487f6b55da0348375f627ed4bdb526b63f40b24)
[121](https://packetscan.io/tx/6ea642a75f6c2b698c577296efb51041b6220a470692bddfb84b7a4ae6116ee8)
[122](https://packetscan.io/tx/b6cc963fdbb68046cc8f412ba0cffaf34f20b26688e8baf5d90199f241276c3f)
[123](https://packetscan.io/tx/7143e6b0fa2cb07b2cf1b93ae36561a0d30972f2ecd46c4d1e3bda1c53588542)
[124](https://packetscan.io/tx/7936e60687cc12c54552e457a8865c6b1c77d0e303e17f37930b66efe2d5c0d5)
[125](https://packetscan.io/tx/5ad304a64ecc1a287c188f5be27800728db2244f0a962e9c97ce2b18296a5164)
[126](https://packetscan.io/tx/26fd526d4fb2733e6f276dbbd2041d5d6d9bc85cbdb434a769b12f62c36bfbd3)
[127](https://packetscan.io/tx/43d5867c4929912e20d3428aff23e3de136ea1ed3dc1d3ceb9d77339b89f63c1)
[128](https://packetscan.io/tx/af5fb836fef0b23497d173dbb46386ec9418bcaadd531ba86f52720a2f909fb2)
[129](https://packetscan.io/tx/b02e7caff10373f6b179f898cd77a1abfb97262e2e7e2f38144a44cb53f7d20c)
[130](https://packetscan.io/tx/3e4f81d6c64cb745e32bae403d04fcb5dee2d0f2f82fea9b554b354b3826b8d0)
[131](https://packetscan.io/tx/b379e185b26d8e16598a45bbd7577f84968c962b33e0eaa1338262b2a3e3b593)
[132](https://packetscan.io/tx/0a7cef5d47c2cbcb2f3f48e50cfee9d88cef7c5ee67cf11f0b8c2ab4b0844e82)
[133](https://packetscan.io/tx/1de33ed99ad906d5868ec1bbafb3fd914fb7746826604b378d7ffe85b771d98a)
[134](https://packetscan.io/tx/3f1fb7a84dd7558f912804939f9cdf53aa2259dd46a1bdcc643bec3714187242)
[135](https://packetscan.io/tx/b9968ff0527c751ee1ccaf39d312f14738ce6877d5288b6fc6f8b2f16d0f3368)
[136](https://packetscan.io/tx/e63caeeeca846cb20993637380d2c18333bba2676c0d58d77d268bf72a43103a)
[137](https://packetscan.io/tx/330bfec15d26717442f02dd08abec5fcf87712e53f2111c3c777d4f5a50a9614)
[138](https://packetscan.io/tx/4322416883242e658bc680d5bcb3348279f3f984580bd69297a8ba1af0541dd0)
[139](https://packetscan.io/tx/a2b4da4226f955dde7d8f0009d8c6d45f07e6a49cc6a8b5212c8331f82c21b00)
[140](https://packetscan.io/tx/f4e5131904ddd2d7e4899b675fc366bd1cb45afd5ba24d7a1cae1873d6714756)
[141](https://packetscan.io/tx/99f6f7888f5fbdb94e64c1e289ab3ff3c7c5e1c8892bab235574f6641c6313f9)
[142](https://packetscan.io/tx/8fd8e9dd536531e0ee42dd96ad98f29cf93ce715d4bdab1d5aa10d342d8cd2f6)
[143](https://packetscan.io/tx/c3620979809315f738f4be8712d4e36e2a07202838bb021157c8cefd32e6bece)
[144](https://packetscan.io/tx/350bacade2162dcfd8cefbbb7cc10d6ce8a52c5fff1c2c08d434c028d8f02103)
[145](https://packetscan.io/tx/a6d975112c60941fcf911a5764ee548cf04671424e684836ea7d04a83eaaf827)
[146](https://packetscan.io/tx/308dada67b91025e45107a943f4b9a92a241b44dd81ae1f261000adf7c7e42bb)
[147](https://packetscan.io/tx/4eced36653694f37ec9ea9e1e7aa5b4df1891d3e206eb84b1007cdb56aabc839)
[148](https://packetscan.io/tx/6d3a3962b105cafb5221064c6115fd3ee4a00894c6e22bd81734c703f6cf19aa)
[149](https://packetscan.io/tx/a92e2176bbb5001b56662660f2e309b97d29e2c714a0f4484f141f758a976a02)
[150](https://packetscan.io/tx/082deca8388a75b5a65517bd2a6e3f1bf50fdc6522a039c5379aee8ed3f3e6f5)
[151](https://packetscan.io/tx/0c6821df0261a5d6b42fb4b8c00fefca3b704e55ad57f8e346a5bfd847db4259)
[152](https://packetscan.io/tx/1571fc85e0d826d274616ebe23b816ff8539392cc54592da04cabc7a453f5d52)
[153](https://packetscan.io/tx/658f70907de9e4be47713c78c6a050a51a4c09624da2563b6ebb494099e2a8ba)
[154](https://packetscan.io/tx/85d2040b77a71f1704b767887c2a28e57692f390eddaf753149b8bdb23072e22)
[155](https://packetscan.io/tx/d45e53d883936ae5c4b3d80791a531ea3ca5ff2dde243bb8d121fb3348eaa8be)
[156](https://packetscan.io/tx/d354d91e4a28a576448912da39d11d6f456cddab0f6b891a7da848f57b7b31d0)
[157](https://packetscan.io/tx/35f8db955cc143eaf24094918d299a4efa58009e65decc53fb734301bf4ea28c)
[158](https://packetscan.io/tx/b495b48ba9cfcce3b3e1814637d0b49221541668df2e7b8aa280dbbf9647d8c8)
[159](https://packetscan.io/tx/abdf34ef99e7bc4fca3336ed3eba878410546cf606e9d637c28204afdef09241)
[160](https://packetscan.io/tx/ad841f4efe905dadb53b049896f31ef49fbf0f490fde12201b601d69a80c17e1)
[161](https://packetscan.io/tx/ae2471cf3f0d6756b9de89653316c42d449ac9b4d918f9ea0cc9d510256eacb6)
[162](https://packetscan.io/tx/c98162833a4fb83c4bd7aa4ecc14b4ad8c698ec3e3d9072d2efffb5e117d85db)
[163](https://packetscan.io/tx/e7cd1502f9e7310731a76d558dd1d6aeeee9eb5bda10a2736d041526b91adb15)
[164](https://packetscan.io/tx/bafa24edb2ee6c190abaa9e2d774faad00b6e364c21cad724df6bb5a3e726674)
[165](https://packetscan.io/tx/f6d01d9904717b05c1f092f09404fa8b6c364a613acec14932ed8e9b5585e1a8)
[166](https://packetscan.io/tx/ccca9c1e883887b8ad936d303cf0f92d0d98b7a55e8cebf3c7b59de34f7b9457)
[167](https://packetscan.io/tx/aa5e138699c4de876e266d23826fbe760be33e9b76669881433cf8c6d48f7eaf)
[168](https://packetscan.io/tx/26459850312770badab5116baff14efce77bfed717884b52ee899945eb425930)
[169](https://packetscan.io/tx/d9aad074c5ede78d5b0129f91e3dc3fe43d7004260c686e763ebba6682e0f255)
[170](https://packetscan.io/tx/f5758b912364c6a0cc4caba98927e0a0461c22c8e7c5a8426b9f763b591095ca)
[171](https://packetscan.io/tx/ff0e6178c67d0205a783abfb3e5d6e169015214a07cd1080fc7f807a95cad609)
[172](https://packetscan.io/tx/dd0841adc1ad9a8212f418e889f3b868b864b6c8363efb2c52031e3b3d83b469)
[173](https://packetscan.io/tx/f16c00e10cda6e130bfd052a45e605302d4af919914d22a08c840e9d1fbe837d)
[174](https://packetscan.io/tx/77716b25da0c47429688378eac038cad6a92acc572cb4c8e9809ffe2423b6ce3)
[175](https://packetscan.io/tx/35d8bf69b11544e4466f4e5018910034678f905274d1f6b6f44b4366907e5262)
[176](https://packetscan.io/tx/75fd67c25a9ec9f0600b1e1676383d055f9fe9bc18c917dab448b88ad4b0d2d6)
[177](https://packetscan.io/tx/3ee352d561cda6142898e5ddcde80816e1901f3fa8662f753bed56dfb1128db7)
[178](https://packetscan.io/tx/f6d7b489a34f5a9510f1110626680c438ff45d19196a6418df45b5b68982cdc3)
[179](https://packetscan.io/tx/5d3064e9ec7d36a29b4e11d2e122b643df41cdd17e40f5101dec0113622615de)
[180](https://packetscan.io/tx/34610fa35618fa9651d2462a392dede9f7f8e17398fd7d8d4209984ff7029057)
[181](https://packetscan.io/tx/b85a029716a9af970f4ad800bda97fce4758c0c86dd27f07202568e2e961bd6e)
[182](https://packetscan.io/tx/57eeb4e1281a24527de6452739504802d4172bdd902be9a516f4fdc625ade0f2)
[183](https://packetscan.io/tx/5cab6f27a3b3ca150aa62a592981b5f8c6378b3129db16aaa6bd167700a7e13a)
[184](https://packetscan.io/tx/1990705d973659af2907c04181a4bbaf528b1d1668ae5049bba4f46010d54012)
[185](https://packetscan.io/tx/f05ab175e10c3b990c918bb35b7c2e50df8ae5501a6c31096888734f71c57175)
[186](https://packetscan.io/tx/2bd577b4698198d03de5637f4bb8c432658d8b13513fc6961bfdd31012e823f5)
[187](https://packetscan.io/tx/54b413e9986cca23f9f9a0c51969156abc203d56c8cba71e85b542612430e817)
[188](https://packetscan.io/tx/57bdf9cd7d44c9eec3c1222496cfa15d786fa4b8ad04b08fd3296dae0de728ca)
[189](https://packetscan.io/tx/24697b0fd6588620e83f3be15c117de3387e11c6d9ba84ddf399cb858e9353b8)
[190](https://packetscan.io/tx/486b8fae2338bea05249476b5e02d6c95408b987ff4ffc8939fabb0190da7cec)
[191](https://packetscan.io/tx/c5d2be1b2bbda0dbb8ad80b2ffe582f69194ef7533909325c34e1740760917cf)
[192](https://packetscan.io/tx/f39ce7839981ceee97381634e20a5e359eda4f79d99617611fd8759b6d32078f)
[193](https://packetscan.io/tx/36847cc026fa88bff5ca2008bc1f9db992cc0bb64913c4ddde40a0ba00422058)
[194](https://packetscan.io/tx/91edfcb593fa026e99234b75c1ef6e89ea5e1ebda536e834d4b4ceff8ea471ba)
[195](https://packetscan.io/tx/c4549dfb06332ff40a57902fa96633770e0dd71226e8251b89f83be38520639d)
[196](https://packetscan.io/tx/193f61092e7a2a16eecd836e184c70cf0ebbb2c9443271ef0d9b2a83db4c58e4)
[197](https://packetscan.io/tx/7f28da31a6e93df7b451bbb8a75ab47cc5650cdcb3b96667878cdbf05ce65333)