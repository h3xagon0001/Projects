import random
import time

responseFeeling = ["I'm fine.", "I'm fine, how about you?", "Fine, how about you?", "I'm good.", "I'm good, how about you?", "Good, how about you?", "I'm feel great.", "I'm feel great, how about you?", "Great, how about you?"]
responseAge = ["I don't think I have an answer to that.", "I don't know my age, do you?", "I don't know my how old I am, do you?", "I'm just a computer program, I don't have an age", "I'm not sure I can grow old."]
responseSport = ["I don't have a physical body so I can't play.", "I would have one if I had a physical body", "I am unable to play any sports.", "I would like to play basketball if I could.", "I would like to play tennis if I could.", "I would like to play soccer if I could."]
responseInvalid = ["Sorry, I'm unable to answer your question.", "I'm unable to answer your question.", "Sorry, I don't seem to understand your question.", "I don't seem to understand your question.", "Please rephrase your question."]

while True:
	userInput = input()

	if "how" in userInput.lower() and "day" in userInput.lower():
		print(random.choice(responseFeeling))

	elif ("how" in userInput.lower() and "old" in userInput.lower()) or ("what" in userInput.lower() and "age" in userInput.lower()):
		print(random.choice(responseAge))

	elif "what" in userInput.lower() and "sport" in userInput.lower():
		print(random.choice(responseSport))

	elif "what" in userInput.lower() and "time" in userInput.lower():
		print("The time is", time.strftime("%H:%M:%S", time.localtime()))

	elif "what" in userInput.lower() and "date" in userInput.lower():
		print("The time is", time.strftime("%d/%m/%Y", time.localtime()))

	elif "what" in userInput.lower() and "launch" in userInput.lower() and "code" in userInput.lower():
		print("66AB7G")

	elif userInput == "66AB7G":
		print("Tranfering to secure line...")
		time.sleep(3)
		print("Verifying SHA256 signature...")
		time.sleep(3)
		for x in range(40):
			print(hash(random.uniform(0,1000)), "	|	", hash(random.uniform(0,1000)))
			time.sleep(0.1)

		print("Verified using '80c5e536eec8387cccad28b8b17b933832244998d85918abf18cc9bada5d4fe9'")
		time.sleep(3)
		print("Locating target...")
		time.sleep(3)
		print("Target located at 14.008041 9.120700 241.041920")
		time.sleep(3)
		print("Fueling Javelin ICBM in Silo 4...")
		time.sleep(5)
		print("Priming missle...")
		time.sleep(3)
		print("Launching in 3...")
		time.sleep(1)
		print("2...")
		time.sleep(1)
		print("1...")
		time.sleep(1)
		print("Missle has been successfully launched and is now headed towards the upper atmosphere.")
		time.sleep(7)
		print("Missle has reached peak altitude and is heading towards the target.")
		time.sleep(5)
		print("Missle has made contact with target.")
		time.sleep(3)
		print("Estimated Casualties\nDead:", random.randint(20, 100), "Injured:", random.randint(200, 1000))
		time.sleep(3)
		print("Target has been completely destroyed in initial blast. Target area will be affected by nuclear fallout for", random.randint(20, 60), "years until safe for human activities.")
		
		

	else:
		print(random.choice(responseInvalid))
