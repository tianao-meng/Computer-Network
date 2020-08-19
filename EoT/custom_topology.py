from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):

        defaultIP_Robert = '10.1.1.14/24'
        Robert = self.addNode( 'Robert', cls=LinuxRouter, ip=defaultIP_Robert)
        s1 = self.addSwitch('s1', failMode='standalone')
        self.addLink( s1, Robert, intfName2='Robert-eth1',
                      params2={ 'ip' : defaultIP_Robert } )

        Alice = self.addHost( 'Alice', ip='10.1.1.17/24',
                           defaultRoute='via 10.1.1.14' )

        self.addLink(Alice, s1)

        s2 = self.addSwitch('s2', failMode='standalone')
        self.addLink( s2, Robert, intfName2='Robert-eth4',
                      params2={ 'ip' : '10.4.4.14/24' } )

        Bob = self.addHost( 'Bob', ip='10.4.4.48/24',
                           defaultRoute='via 10.4.4.14')

        self.addLink(Bob, s2)

        defaultIP_Richard = '10.4.4.46/24'
        Richard = self.addNode('Richard', cls=LinuxRouter, ip=defaultIP_Richard)

        self.addLink( s2, Richard, intfName2='Richard-eth4',
                      params2={ 'ip' : '10.4.4.46/24' } )

        s3 = self.addSwitch('s3', failMode='standalone')
        self.addLink( s3, Richard, intfName2='Richard-eth6',
                      params2={ 'ip' : '10.6.6.46/24' } )

        defaultIP_Rupert = '10.6.6.254/24'
        Rupert = self.addNode('Rupert', cls=LinuxRouter, ip=defaultIP_Rupert)

        self.addLink( s3, Rupert, intfName2='Rupert-eth6',
                      params2={ 'ip' : '10.6.6.254/24' } )

        Carol = self.addHost( 'Carol', ip='10.6.6.69/24',
                           defaultRoute='via 10.6.6.46' )
        self.addLink(Carol, s3)


def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo, controller=None )
    net.start()
    info( '*** Routing Table on Router:\n' )
    print net[ 'Robert' ].cmd( 'route' )
    print net['Richard'].cmd('route')
    print net['Rupert'].cmd('route')
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
