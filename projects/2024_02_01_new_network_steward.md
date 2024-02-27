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