import telnetlib
import json
import util
from time import sleep

f = open('config_routers.json')
config = json.load(f)
f.close()

s = config["nb_routers"]
print(f"nb_routers is {s}")

#sleep(5)

for router in config["routers"]:
    r = telnetlib.Telnet("localhost", router["port"])
    terminal = util.Commands(r)
    print("connected to "+router["name"])
    r.read_until(b"#")
    r.write(b"\r")
    for interface in router["interfaces"]:
        terminal.config_interface(interface["name"], interface["IP"], interface["netmask"])

    terminal.config_OSPF(config, router)


print("end")
