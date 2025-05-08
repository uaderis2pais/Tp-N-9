import os

class Ping:
    def execute(self, ip):
        if not ip.startswith("192."):
            print("Dirección IP no válida.")
            return
        for _ in range(10):
            os.system(f"ping -c 1 {ip}")

    def executefree(self, ip):
        for _ in range(10):
            os.system(f"ping -c 1 {ip}")

class PingProxy:
    def __init__(self):
        self._ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self._ping.executefree("www.google.com")
        else:
            self._ping.execute(ip)
