import time


class Commands:

    def __init__(self, tn):
        self.tn = tn

    # Fonction lançant une commande
    def command(self, string):
        self.tn.write(f'{string}\r'.encode("utf-8"))
        time.sleep(0.5) # Pour permettre que le routeur soit pas submergé par les commandes

    # Fonction lançant la commande "write"
    def write(self):
        self.command('write')
        for i in range(7): # Pour être sûrs que le routeur ait reçu le write et ait fini de le traiter
            self.command('')
            time.sleep(0.5)

    # Configure une interface d'un routeur
    def config_interface(self, name, ip, mask):
        self.command('configure terminal')
        self.command(f'interface {name}')
        self.command(f'ip address {ip} {mask}')
        self.command('no shutdown')
        self.command('end')
        self.write()

    # Configure une interface de Loopback
    def config_loopback(self, num_router):
        self.command('configure terminal')
        self.command('interface Loopback0')
        self.command(f'ip address {num_router}.{num_router}.{num_router}.{num_router} 255.255.255.255')
        self.command('no shutdown')
        self.command('end')
        self.write()

    # Configure OSPF
    def config_OSPF(self, process_ID, router, num_router):
        self.command(f'configure terminal')
        self.command(f'router ospf {process_ID}')
        self.command(f'router-id {router["OSPF_ID"]}')
        self.command(f'end')

        for interface in router["interfaces"]:
            if (interface["is_loopback"] == True):
                self.command(f'configure terminal')
                self.command(f'interface {interface["name"]}')
                self.command(f'ip ospf {process_ID} area 1')
                self.command(f'end')

            else:
                if (interface["is_core"] == True):
                    self.command(f'configure terminal')
                    self.command(f'interface {interface["name"]}')
                    self.command(f'ip ospf {process_ID} area 1')
                    self.command(f'end')
                else:
                    self.command(f'configure terminal')
                    self.command(f'interface {interface["name"]}')
                    self.command(f'ip ospf {process_ID} area 1')
                    self.command(f'end')

            self.command('conf t')
            self.command(f'router ospf {process_ID}')
            self.command(f'router-id {num_router}.{num_router}.{num_router}.{num_router}')
            if(router["is_border"]):
                for interface in router["interfaces"]:
                    if(interface["is_core"] == False):
                        self.command(f'passive-interface {interface["name"]}')
            self.command('end')
            self.write()

    # Configure MPLS
    def config_MPLS(self, router, process_ID):
        self.command('configure terminal')
        self.command(f'router ospf {process_ID}')
        self.command(f'mpls ldp autoconfig')
        self.command('end')
        self.write()

    # Met à jour la configuration BGP des routeurs à l'ajout d'un autre /!\ ne fonctionne pas encore
    def update_BGP(self, router, num_new_router):
        self.command('configure terminal')
        self.command('router bgp 111')
        self.command(f'neighbor {num_new_router}.{num_new_router}.{num_new_router}.{num_new_router} remote-as 111')
        self.command(f'neighbor {num_new_router}.{num_new_router}.{num_new_router}.{num_new_router} update-source Loopback0')
        if(router["is_border"]):
            self.command(f'neighbor {num_new_router}.{num_new_router}.{num_new_router}.{num_new_router} send-community')
        self.command(f'neighbor {num_new_router}.{num_new_router}.{num_new_router}.{num_new_router} activate')
        self.command('end')
        self.write()

    # Configure BGP
    def config_BGP(self, router, num_router, nb_routers, clients_as):
        self.command('configure terminal')

        if(router["is_border"]):
            self.command('router bgp 111')
            self.command(f'bgp router-id 1.1.1.{num_router}')
            self.command('bgp log-neighbor-changes')
            for interface in router["interfaces"]:
                if(interface["is_core"] == False): # si c'est une interface vers un AS voisin, donc hors de notre réseau
                    self.command(f'neighbor 1.{interface["num_client"]}.0.2 remote-as {interface["client_as"]}')
                    # Configuration des route-map
                    if(interface["client_type"] == "provider"):
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 route-map PROVIDER_IN in')
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 route-map PROVIDER_OUT out')
                        self.command('end')
                        self.command('conf t')
                        self.command('route-map PROVIDER_OUT permit 10')
                        self.command('match community 10')
                        self.command('continue')
                        self.command('end')
                        self.command('conf t')
                        self.command('route-map PROVIDER_IN permit 30')
                        self.command('match community 1')
                        self.command('set local-preference 50')
                        self.command(f'set community {interface["client_as"]}:50')
                        self.command('end')
                        self.command('conf t')
                        for client in clients_as:
                            self.command(f'ip community-list 10 permit {client}:150')
                        self.command('access-list 1 permit any')
                    elif(interface["client_type"] == "peer"):
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 route-map PEER_IN in')
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 route-map PEER_OUT out')
                        self.command('end')
                        self.command('conf t')
                        self.command('route-map PEER_OUT permit 10')
                        self.command('match community 10')
                        self.command('continue')
                        self.command('end')
                        self.command('conf t')
                        self.command('route-map PEER_IN permit 30')
                        self.command('match community 1')
                        self.command('set local-preference 100')
                        self.command(f'set community {interface["client_as"]}:100')
                        self.command('end')
                        self.command('conf t')
                        for client in clients_as:
                            self.command(f'ip community-list 10 permit {client}:150')
                    elif(interface["client_type"] == "client"):
                        self.command(f'neighbor 1.{interface["num_client"]}.0.2 route-map CLIENT_IN in')
                        self.command('end')
                        self.command('conf t')
                        self.command('route-map CLIENT_IN permit 10')
                        self.command('match community 1')
                        self.command('set local-preference 150')
                        self.command(f'set community {interface["client_as"]}:150')

            self.command('end')
            self.command('conf t')
            self.command('ip community-list 1 permit internet')
            self.command('router bgp 111')
            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} remote-as 111')
                    self.command(f'neighbor {num}.{num}.{num}.{num} update-source Loopback0')
                    self.command(f'neighbor {num}.{num}.{num}.{num} send-community')
            self.command('address-family ipv4')

            for interface in router["interfaces"]:
                if(interface["is_core"] == False):
                    self.command(f'network 1.{interface["num_client"]}.0.0 mask 255.255.255.252')
                    self.command(f'neighbor 1.{interface["num_client"]}.0.2 activate')
                elif(interface["is_loopback"] == False):
                    self.command(f'network 1.0.{interface["num"]}.0 mask 255.255.255.0')


            self.command(f'network {num_router}.{num_router}.{num_router}.{num_router} mask 255.255.255.255')

            for i in (range(nb_routers)):
                num = i + 1
                if i + 1 != num_router:
                    self.command(f'neighbor {num}.{num}.{num}.{num} activate')
            self.command('exit-address-family')

        else:
            self.command('router bgp 111')
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

        self.command('end')
        self.write()
