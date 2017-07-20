import ipaddress

def every_ip_in_range(ip_range):
    net4 = ipaddress.ip_network(line)
    for ipv4 in net4.hosts():
        print(ipv4)

with open("fi.zone") as f:
    for line in f:
        line = line.strip()
        if line:
            every_ip_in_range(ip_range)
