# Detecting suspicious behavior in network traffic indicating a zombie bot
def detect_zombie_activity(network_traffic):
    if "high frequency requests" in network_traffic and "to unknown IPs" in network_traffic:
        return "Zombie bot detected! Suspicious activity in network."
    else:
        return "Network traffic seems normal."

network_traffic = "high frequency requests to unknown IPs"
print(detect_zombie_activity(network_traffic))