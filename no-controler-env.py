from mininet.net import Mininet
from mininet.node import OVSSwitch, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link

def createNetwork():
    net = Mininet(switch=OVSSwitch)

    info('*** Adding hosts\n')
    host = net.addHost('host', ip='10.0.0.1/24')
    at1 = net.addHost('at1', ip='10.0.0.3/24')
    at2 = net.addHost('at2', ip='10.0.0.2/24')
    at3 = net.addHost('at3', ip='10.0.0.3/24')
    at4 = net.addHost('at4', ip='10.0.0.4/24')
    at5 = net.addHost('at5', ip='10.0.0.5/24')
    usr = net.addHost('usr', ip='10.0.0.6/24')

    info('*** Adding switches\n')
    s1 = net.addSwitch('s1', failMode='standalone')
    s2 = net.addSwitch('s2', failMode='standalone')

    info('*** Creating links\n')
    net.addLink(host, s1)
    net.addLink(usr, s1)
    net.addLink(at1, s1)
    net.addLink(at2, s1)
    net.addLink(at3, s2)
    net.addLink(at4, s2)
    net.addLink(at5, s2)

    info('*** Adding router\n')
    router = net.addHost('r0', cls=Node, ip='10.0.0.254/24')
    router.cmd('sysctl -w net.ipv4.ip_forward=1')
    net.addLink(s1, router)
    net.addLink(s2, router)

    info('*** Starting network\n')
    net.build()
    net.start()

    info('*** Configuring hosts\n')
    at1.cmd('ip route add default via 10.0.0.254')
    at2.cmd('ip route add default via 10.0.0.254')
    at3.cmd('ip route add default via 10.0.0.254')
    at4.cmd('ip route add default via 10.0.0.254')
    at5.cmd('ip route add default via 10.0.0.254')
    usr.cmd('ip route add default via 10.0.0.254')
    host.cmd('ip route add default via 10.0.0.254')

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()
