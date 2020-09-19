#!/usr/bin/python2.7
# iptables --flush
# iptables -I INPUT -j NFQUEUE --queue-num 0
# iptables -I FORWARD -j NFQUEUE --queue-num 0
import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
