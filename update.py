import telnetlib
import json
import util
from time import sleep
import sys

if len(sys.argv) != 2:
    print("Syntax is: python3 update.py *new_router.json*")
    exit()

f = open('config_routers.json', "r")
config = json.load(f)
f.close()

f2 = open(sys.argv[1], "r")
new_routers = json.load(f2)
f2.close

for new_router in new_routers["router"]:
    num_router = config["nb_routers"]+1

    r = telnetlib.Telnet("localhost", new_router["port"])
    terminal = util.Commands(r)
    print("connected to "+new_router["name"])
    r.read_until(b"#")
    r.write(b"\r")
    terminal.config_loopback(num_router)
    for interface in new_router["interfaces"]:
        terminal.config_interface(interface["name"], interface["IP"], interface["netmask"])

    terminal.config_OSPF(config["proccess_ID"], new_router, num_router)
    terminal.config_MPLS(new_router)

    terminal.config_BGP(new_router, num_router, num_router)
    terminal.config_route_map(new_router)


    for router in config["routers"]:
        r2 = telnetlib.Telnet("localhost", router["port"])
        terminal2 = util.Commands(r2)
        print("connected to "+router["name"])
        r.read_until(b"#")
        r.write(b"\r")
        terminal2.update_BGP(router, num_router)


    # updates file
    config["nb_routers"]++
    config["routers"].append(new_router)
    f = open('config_routers.json', "w")
    json.dump(config, f)
    f.close()


print("end")
