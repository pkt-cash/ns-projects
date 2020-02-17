# Projects Supported by The Network Steward

* **CURRENT DEADLINE**: Midnight February 29, 2020 UTC
* **CURRENT ROUND BUDGET**: 90mn PKT - Please see [Acceptance Process](https://github.com/pkt-cash/ns-projects/tree/master/acceptance_process.md) for more information

The [Network Steward](https://pkt-cash.github.io/www.pkt.cash/steward/) of the PKT project is interested in the following topics. This list is not exhaustive and not every feature of every idea needs to be in a proposal for it to be accepted. These are just general topics which the Network Steward has an interest in seeing open source development.

In order to create a project, fork this repository, create a new file in the projects directory which is a copy of the [template.md](https://github.com/pkt-cash/ns-projects/tree/master/projects/template.md) file. Then make a pull request to add your project proposal to this repository.

Projects will be evaluated in accordance with the process defined in [Acceptance Process](https://github.com/pkt-cash/ns-projects/tree/master/acceptance_process.md)

* Open source graphical SPV PKT wallet
  * Checking the authenticity of the blockchain by verifying the PacketCrypt proofs on a configurable number of the most recent blocks and verifying only the connectedness of all earlier headers
  * Ability to issue, transfer and validate [colored coins](https://en.bitcoin.it/wiki/Colored_Coins)
  * Ability to validate a message as signed by the current holder of a given colored coin
  * Ability to offer a colored coin for sale in a swap and ability to take such a swap transaction and accept it
  * Future interoperability with Lightning Network
  * Compatibility with Android, iOS, Linux, OSX, Windows
  * Graphical, command line and library modes
  * Low resource footrpint
* Cjdns using Wireguard for encryption
  * Replacement of cjdns CryptoAuth protocol with Wireguard
  * Detection of "new nodes" who speak Wireguard vs. "old nodes" who speak CryptoAuth
  * Replacement for peering and also for end-to-end
* Cjdns kernelspace implementation
  * Using Wireguard kernel module to perform encryption
  * Only needs to speak Wireguard based protocol, legacy CryptoAuth is not necessary
  * Maximum feasible code-reuse between kernel module and userland code
* Cjdns key rotation
  * Allow changing the keypair each restart for non-server nodes
* Packet prioritization system in cjdns
  * Ability to allocate virtual switches and bandwidth leases
  * Ability to associate a bandwidth lease with a virtual switch
  * Further thoughts in [cjdns packet priority spec](https://cryptpad.fr/code/#/2/code/view/TXyEJbs1UQ9yQWvqPcSRoyhFGMdcQY0FjCOHAcjUzz4/present/)
* Open source high performance cjdns Route Server
  * High performance language such as Rust or Elixir
  * Network coordination functionality of [cjdnsnode](https://github.com/cjdelisle/cjdnsnode)
  * Ability to coordinate cjdns nodes to configure VPN tunnels
  * Collection and publication of link quality data
  * Gossip protocol so that other route servers can inter-operate
* Example usage of PacketCrypt announcements for pub/sub
  * A simple tweet-like interface where people can send messages by mining announcements
  * WebAssembly compiled version of PacketCrypt
  * Static code only which interacts directly with a PacketCrypt mining pool
  * Pool updates to allow subscription to different types of announcements
* Creation and maintanence of a repository of packages of mesh software
  * Packages to be easily installed in major operating systems which do not have support already such as Debian, OSX and Windows
  * Packaging of meshnet software including cjdns and yggdrasil
* Cjdns wifi based interface
  * Automatic peering when a compatible wireless device is in range
  * Lower CPU consumption using encryption offload
  * Compatibility with Android and iPhone devices