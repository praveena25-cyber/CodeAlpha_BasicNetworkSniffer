print("Starting Network Sniffer...")

packets = [
    {"src":"192.168.1.10","dst":"142.250.183.14","protocol":"TCP"},
    {"src":"192.168.1.10","dst":"8.8.8.8","protocol":"UDP"},
    {"src":"192.168.1.10","dst":"1.1.1.1","protocol":"ICMP"}
]

for p in packets:
    print("\n===== Packet Captured =====")
    print("Source IP:", p["src"])
    print("Destination IP:", p["dst"])
    print("Protocol:", p["protocol"])