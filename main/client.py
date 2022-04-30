import requests
import time

HOST = ["127.0.0.1", "192.168.1.24", "192.168.1.50"]
PORT = [8080]
DIRECCIONES = []
for host in HOST:
    for port in PORT:
        DIRECCIONES.append("http://" + host + ":" + str(port) + "/")

offset = lambda t0, t1, t2, t3: (t1 - t0 + t2 - t3) / 2
delay = lambda t0, t1, t2, t3: (t1 - t0 + t3 - t2)


def main():
    mejorPar = {"address": None, "d": 999999, "o": 999999}
    for direccion in DIRECCIONES:
        print("\nProbando " + direccion)
        print("{:^10} {:^25} {:^25}".format("Iteracion", "Offset", "Delay"))
        for i in range(8):
            t0 = time.time()
            data = requests.get(direccion + "tiempo")
            data = data.json()
            t1 = data["t1"]
            t2 = data["t2"]
            t3 = time.time()
            o = round(offset(t0, t1, t2, t3), 18)
            d = round(delay(t0, t1, t2, t3), 18)
            print("{:^10} {:^25} {:^25}".format(i + 1, o, d))
            if d < mejorPar["d"]:
                mejorPar["address"] = direccion
                mejorPar["d"] = d
                mejorPar["o"] = o
    print("\nMejor par:" + str(mejorPar))


if "__main__" == __name__:
    main()