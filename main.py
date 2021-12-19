import telnetlib
import json
import util
from time import sleep
import sys

f = open('config_routers.json')
config = json.load(f)
f.close()

s = config["nb_routers"]
print(f"nb_routers is {s}")

#sleep(5)

if len(sys.argv) < 2:
    print("Pas le bon nombre d'argument !")
    exit()

if sys.argv[1] == '0':

    for router in config["routers"]:
        r = telnetlib.Telnet("localhost", router["port"])
        terminal = util.Commands(r)
        print("connected to "+router["name"])
        r.read_until(b"#")
        r.write(b"\r")
        for interface in router["interfaces"]:
            terminal.config_interface(interface["name"], interface["IP"], interface["netmask"])

        terminal.config_OSPF(config, router)
        terminal.config_MPLS(config, router)

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
