import time

class Commands

    def _init(self, tn):
        self.tn = tn

    def command(self, string):
        self.tn.write(f'{string}\r\n'.encode("utf-8"))
        #print(self.tn.read_until(b"#"))
        sleep(0.1)

    def config_interface(self, name, ip, loopback):
        r.command('configure terminal')
        r.command(f'interface {name}')
        r.command(f'ip address {ip} {loopback}')
        r.command('no shutdown')
        r.command('end')
