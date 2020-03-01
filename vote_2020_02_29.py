#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 90.0
costs = {
  'repo': 4.0,
  'price_display': 8.0,
  'faucet': 16.0,
  'cloud': 30.0,
  'vpn': 30.0,
  'route_server': 30.0,
  'cjdns_wifi': 36.0,
  'cjdns_wireguard': 24.0
}
votes = []

### Fill in your values here, you can run this code but don't share it until 2020-03-08
votes.append({
  'repo':            { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'price_display':   { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'faucet':          { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cloud':           { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'vpn':             { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'route_server':    { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wireguard': { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
})

## This is filler so that the algoritm works. When other team members have their data it will go here.
votes.append({
  'repo':            { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'price_display':   { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'faucet':          { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cloud':           { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'vpn':             { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'route_server':    { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wireguard': { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
})
votes.append({
  'repo':            { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'price_display':   { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'faucet':          { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cloud':           { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'vpn':             { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'route_server':    { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wireguard': { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
})
votes.append({
  'repo':            { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'price_display':   { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'faucet':          { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cloud':           { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'vpn':             { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'route_server':    { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wireguard': { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
})
votes.append({
  'repo':            { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'price_display':   { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'faucet':          { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cloud':           { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'vpn':             { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'route_server':    { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wifi':      { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
  'cjdns_wireguard': { 'short': 0.5, 'long': 0.5, 'scope': 0.5, 'risk': 0.5, 'hazard': 0.5 },
})
print "RESULTS NOT YET FINAL - winners: %s" % getApprovedProjects(budget, costs, votes)