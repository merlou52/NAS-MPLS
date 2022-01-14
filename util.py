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

    def config_OSPF(self, config, router, num_router):
        self.command(f'configure terminal')
        self.command(f'router ospf {config["process_ID"]}')
        self.command(f'router-id {router["OSPF_ID"]}')
        self.command(f'end')

        for interface in router["interfaces"]:
            if (interface["is_loopback"] == True):
                self.command(f'configure terminal')
                #self.command(f'router ospf {config["process_ID"]}')
                self.command(f'interface {interface["name"]}')
                self.command(f'ip address {num_router}.{num_router}.{num_router}.{num_router} 255.255.255.255')
                self.command(f'ip ospf {config["process_ID"]} area 1')
                self.command(f'end')

            else:
                if (interface["is_core"] == True):
                    self.command(f'configure terminal')
                    self.command(f'interface {interface["name"]}')
                    self.command(f'ip address 1.0.{interface["num"]}.2 255.255.255.0')
                    #self.command(f'ip ospf {config["process_ID"]} area 1')
                    #self.command('duplex full')
                    self.command(f'end')
                else:
                    self.command(f'configure terminal')
                    self.command(f'interface {interface["name"]}')
                    self.command(f'ip address 1.0.{interface["num"]}.2 255.255.255.252')
                    self.command(f'ip ospf {config["process_ID"]} area 1')
                    #self.command('duplex full')
                    #self.command(f'passive-interface {interface["name"]}')
                    self.command(f'end')

            self.command('conf t')
            self.command(f'router ospf {config["process_ID"]}')
            self.command(f'router-id {num_router}.{num_router}.{num_router}.{num_router}')
            self.command(f'network {num_router}.{num_router}.{num_router}.{num_router} 0.0.0.0 area 0')
            if(router["is_border"]):
                for interface in router["interfaces"]:
                    if(interface["is_core"] == False):
                        self.command(f'passive-interface {interface["name"]}')
            self.command('end')
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

        if(router["is_border"]):
            self.command('router bgp 111')
            #self.command('no sync')
            self.command(f'bgp router-id 1.1.1.{num_router}')
            self.command('bgp log-neighbor-changes')
            for interface in router["interfaces"]:
                if(interface["is_core"] == False):
                    self.command(f'neighbor 1.{interface["num_client"]}.0.1 remote-as 11{interface["num_client"]}')
            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} remote-as 111')
                    self.command(f'neighbor {num}.{num}.{num}.{num} update-source Loopback0')
            self.command('address-family ipv4')
            self.command(f'network 1.0.{interface["num"]}.0 mask 255.255.255.0')
            for interface in router["interfaces"]:
                if(interface["is_core"] == False):
                        self.command(f'network 1.{interface["num_client"]}.0.0 mask 255.255.255.252')
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 activate')
            self.command(f'network {num_router}.{num_router}.{num_router}.{num_router} mask 255.255.255.255')

            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} activate')
            self.command('exit-address-family')

        else:
            self.command('router bgp 111')
            #self.command('no sync')
            self.command(f'bgp router-id {num_router}.{num_router}.{num_router}.{num_router}')
            self.command('bgp log-neighbor-changes')
            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} remote-as 111')
                    self.command(f'neighbor {num}.{num}.{num}.{num} update-source Loopback0')
            self.command('address-family ipv4')
            self.command(f'network {num_router}.{num_router}.{num_router}.{num_router} mask 255.255.255.255')

            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} activate')
            self.command('exit-address-family')


#        for interface in router["interfaces"]:
#            if not interface["is_core"]:
#                self.command(f'neighbor 1.{num_router}.0.2 remote-as 21{num_router}')
#                self.command(f'neighbor 1.{num_router}.0.2 activate')

        self.command('end')
        self.write()
