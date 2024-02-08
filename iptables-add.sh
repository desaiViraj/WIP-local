#!/bin/bash

port_venet0=<port1>
port_br0=<port2>

iplist_output=$(iplist | grep -Eo "192\.168\.200\.[0-9]+")

while read -r ip; do
    echo "-A DNAT ! -i venet0 -p tcp -m tcp --dport $port_venet0 -j DNAT --to-destination $ip:$port_venet0"

    # Increment port number for venet0
    port_venet0=$((port_venet0+1))

    echo "-A DNAT -i br0 -p tcp -m tcp --dport $port_br0 -j DNAT --to-destination $ip:22"

    # Increment port number for br0
    port_br0=$((port_br0+1))
done <<< "$vzlist_output"
