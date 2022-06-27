import socket
from IPy import IP
from termcolor import colored

def convert_ip(ip):
	try:
		IP(ip)
		return ip
	except ValueError:
		return socket.gethostbyname(ip)

def port_scan(ipadress, port):
	try:
		s = socket.socket()
		s.settimeout(0.5)
		s.connect((ipadress, port))
		print(colored(f"[+] The port {port} is open.", 'green'))
	except:
		print(colored(f"[-] The port {port} is closed",'red'))

host = input("[+] Enter the host to scan: ")
converted_ip = convert_ip(host)

for port in range(75,85):
	port_scan(converted_ip, port)
