import time


class Commands:

    def __init__(self, tn):
        self.tn = tn

    def command(self, string):
        self.tn.write(f'{string}\r'.encode("utf-8"))
        # print(self.tn.read_until(b"#"))
        time.sleep(0.1) # pour permettre que le routeur soit pas submergé par les commandes

    def write(self):
        self.command('write')
        for i in range(10): # pour etre sur que le routeur capte bien qu'on lui dise 'yes'
            self.command('')
            time.sleep(0.1)

    def config_interface(self, name, ip, mask):
        self.command('configure terminal')
        self.command(f'interface {name}')
        self.command(f'ip address {ip} {mask}')
        self.command('no shutdown')
        self.command('end')
        self.write()

    def config_loopback(self, num_router):
        self.command('configure terminal')
        self.command('interface Loopback0')
        self.command(f'ip address {num_router}.{num_router}.{num_router}.{num_router} 255.255.255.255')
        self.command('no shutdown')
        self.command('end')
        self.write()

    def config_OSPF(self, config, router):
        self.command(f'configure terminal')
        self.command(f'router ospf {config["process_ID"]}')
        self.command(f'router-id {router["OSPF_ID"]}')
        self.command(f'end')

        for interface in router["interfaces"]:
            if (interface["is_loopback"] == True):
                self.command(f'configure terminal')
                self.command(f'router ospf {config["process_ID"]}')
                self.command(f'network {interface["addr_loopback"]} area 0')
                self.command(f'end')

            else:
                if (interface["is_core"] == True):
                    self.command(f'configure terminal')
                    self.command(f'interface {interface["name"]}')
                    self.command(f'ip ospf {config["process_ID"]} area 0')
                    self.command(f'end')
                else:
                    self.command(f'configure terminal')
                    self.command(f'router ospf {config["process_ID"]}')
                    self.command(f'passive-interface {interface["name"]}')
                    self.command(f'end')

            self.write()

    def config_MPLS(self, config, router):
        self.command('configure terminal')
        self.command('mpls ip')
        self.command('mpls label protocol ldp')

        for interface in router["interfaces"]:
            if (interface["is_core"]):
                self.command(f'interface {interface["name"]}')
                self.command('mpls ip')
                self.command('exit')

        self.command('end')
        self.write()

    def config_BGP(self, config, router, num_router, nb_routers):
        self.command('configure terminal')
        self.command('router bgp 111')
        self.command('no sync')
        self.command(f'bgp router-id 1.1.1.{num_router}')

        for i in (range(nb_routers)):
            num = i + 1
            if i + 1 != num_router:
                self.command(f'neighbor {num}.{num}.{num}.{num} remote-as 111')
                self.command(f'neighbor {num}.{num}.{num}.{num} update-source Loopback0')
                self.command(f'neighbor {num}.{num}.{num}.{num} activate')
                self.command('network 1.1.1.0')

        self.command('address-family ipv4')

        for interface in router["interfaces"]:
            if not interface["is_core"]:
                self.command(f'neighbor 1.{num_router}.0.2 remote-as 21{num_router}')
                self.command(f'neighbor 1.{num_router}.0.2 activate')

        self.command('end')
        self.write()
