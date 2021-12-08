import telnetlib
import json
#import util
from time import sleep

f = open('config_routers.json')
config = json.load(f)
f.close()

s = config["nb_routers"]
print(f"nb_routers is {s}")


for router in config[routers]:
    r = telnetlib.Telnet(router["loopback"], router["port"])
    terminal = util.Commands(r)
    print("connected to "+router["name"])
    print(r.read_until(b"#"))
    r.write(b"\r\n")
    for interface in r[interfaces]:
        terminal.config_interface(interface["name"], interface["IP"], interface["loopback"])

print("end")
