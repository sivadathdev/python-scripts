import scapy.all as scapy
import sys
import time

def get_mac_address(ipaddr):
	broadcast_layer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_layer = scapy.ARP(pdst=ipaddr)
	# Basically we are sending a broadcast msg to the n/w asking for the MAC address of the given IP.
	get_mac_packet = broadcast_layer/arp_layer
	answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0] # sending the packet & recieving answers.
	return answer[0][1].hwsrc # extracting MAC address from the answer
	# This is how we grab the MAC address, refer the networking screenshot for better understanding.


def main():
	if len(sys.argv) != 3:
		print(f" Usage : {sys.argv[0]} <router_ip> <target_ip>")
	else:
		router_ip = str(sys.argv[1])
		target_ip = str(sys.argv[2])

		target_mac = str(get_mac_address(target_ip))
		router_mac = str(get_mac_address(router_ip))

		print(router_mac)
		print(target_mac)


if __name__ == "__main__":
    main()
