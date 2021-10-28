import platform
import os
import time
import secrets
import random

sysInfo = f'''----------------------------------
System Information
OS: {platform.platform()}
Version: {platform.release()}
Machine Type: {platform.machine()}
System Name: {platform.node()}
Processor: {platform.processor()}
----------------------------------
'''

print(sysInfo)

if os.path.isfile("config.txt"):
	readFile = open("config.txt", "r")
	readContent = readFile.read().split("/")
	while True:
		for x in range(random.randint(1,4)):
			print(f"New job received from: {readContent[3]} Target: 000000{secrets.token_hex(5)} Difficulty: 6")
			time.sleep(1)
		print(f"Solving job... Average speed: {random.randint(50,60)} mh/s")
		time.sleep(random.randint(1,3))
		print(f"Job solved. Reward: {random.randint(5000,10000)/10000000} Wallet: {readContent[5]}")

else:
	print("Creating first time setup files...")
	f = open("config.txt", "w")
	f.write("minerhash/0B70AD6F/pool/BTCPool.asia1/wallet/bc1q9jynwaxz2gm6elyy5h6vmnwp7svzcuvuf5s5yc")
	f.close()
	time.sleep(1)
	print("'config.txt' successfully created. (DO NOT DELETE THIS FILE)")
	print("Please restart the miner.")
	time.sleep(3)
	quit()
