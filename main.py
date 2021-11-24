import telnetlib
from time import sleep

r1 = telnetlib.Telnet("127.0.0.1", "5003")
print("connected")
print(r1.read_until(b"#"))
r1.write(b"\r\n")
r1.write(b'show ip route\r\n')
print(r1.read_until(b"#"))
print("end")
