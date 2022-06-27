import socket
from IPy import IP
from termcolor import colored

def scan(ip):
	print(f"[*] Scanning the target {ip} ")
	converted_ip = convert_ip(ip)

	for port in range(1,100):
		port_scan(converted_ip, port)

def convert_ip(ip):
	try:
		IP(ip)
		return ip
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(sock):
	return sock.recv(1024)

def port_scan(ipadress, port):
	try:
		s = socket.socket()
		s.settimeout(0.5)
		s.connect((ipadress, port))

		try:
			banner = get_banner(s)
			print(colored("[+] Open port " + str(port) + ": " + str(banner.decode().strip("\n"))))
		except:
			print(colored(f"[+] Open port {port} "))
	except:
		pass

targets = input("[+] Enter the target/s to scan (seperate multiple targets by ,): ")

if "," in targets:
	for ip_addr in targets.split(","):
		scan(ip_addr.strip())
else:
	scan(targets)
