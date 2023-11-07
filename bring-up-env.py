#!/usr/bin/python
'''
Test environment
 - Ryu as simple switch
 - no attack
'''
import logging

from datetime import datetime
import os
import time

# Create "logs" folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log filename based on the current timestamp with "env1-" prefix
log_filename = datetime.now().strftime("logs/env1-%Y-%m-%d_%H-%M-%S.log")

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def scenario_basic():
    net = Mininet(topo=None, build=False, link=TCLink)

    logging.info('*** Controller (Ryu) ***\n')
    c0 = net.addController(name='c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    logging.info('*** Add 2 switches ***\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

    logging.info('*** Add Hosts ***\n')
    host = net.addHost('host', cls=Host, ip='10.0.0.1', defaultRoute=None)
    usr = net.addHost('usr', cls=Host, ip='10.0.0.2', defaultRoute=None)
    at1 = net.addHost('at1', cls=Host, ip='10.0.0.3', defaultRoute=None)
    at2 = net.addHost('at2', cls=Host, ip='10.0.0.4', defaultRoute=None)
    at3 = net.addHost('at3', cls=Host, ip='10.0.0.5', defaultRoute=None)
    at4 = net.addHost('at4', cls=Host, ip='10.0.0.6', defaultRoute=None)
    at5 = net.addHost('at5', cls=Host, ip='10.0.0.7', defaultRoute=None)

    logging.info('*** Add links ***\n')
    net.addLink(s1, host, bw=10)
    net.addLink(s1, usr, bw=10)
    net.addLink(s1, at1, bw=10)
    net.addLink(s1, s2, bw=5, max_queue_size=500)
    net.addLink(s2, at2, bw=10)
    net.addLink(s2, at3, bw=10)
    net.addLink(s2, at4, bw=10)
    net.addLink(s2, at5, bw=10)

    logging.info('\n*** Build it ***\n')
    net.build()

    logging.info('*** Start the controller ***\n')
    for controller in net.controllers:
        controller.start()

    logging.info('*** Start switches and associate with controller ***\n')
    s1.start([c0])
    s2.start([c0])

    logging.info('*** Post-startup configuration ***\n')
    # Any post-startup configuration goes here

    logging.info('*** Run Mininet\'s CLI ***\n')
    CLI(net)



if __name__ == '__main__':
    setLogLevel('info')
    scenario_basic()

