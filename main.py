import telnetlib
import json
import util
from time import sleep
import sys

# Chargement des données du fichier .json
f = open('config_routers.json')
config = json.load(f)
f.close()

s = config["nb_routers"]
print(f"nb_routers is {s}")

if len(sys.argv) < 2:
    print("Pas le bon nombre d'argument !")
    exit()

# Configuration classique 
if sys.argv[1] == '0':

    num_router = 1

    for router in config["routers"]:
        r = telnetlib.Telnet("localhost", router["port"])
        terminal = util.Commands(r)
        print("connected to "+router["name"])
        for i in range(5):
            r.write(b"\r")
            sleep(1)
        terminal.config_loopback(num_router)
        for interface in router["interfaces"]:
            terminal.config_interface(interface["name"], interface["IP"], interface["netmask"])

        terminal.config_OSPF(config["process_ID"], router, num_router)
        terminal.config_MPLS(router, config["process_ID"])

        terminal.config_BGP(router, num_router, config["nb_routers"], config["clients_as"])
        num_router += 1
        sleep(5)

# Configuration ligne de commande par ligne de commande 
else :

    if len(sys.argv) < 3:
        print("<port> <commande>")
        exit()

    r = telnetlib.Telnet("localhost", sys.argv[1])
    terminal = util.Commands(r)
    com = ""

    for i in range(len(sys.argv) - 2):
        com = com + sys.argv[i+2] + " "

    terminal.command(com)
    print("On a pas encore implémenté")

print("end")
