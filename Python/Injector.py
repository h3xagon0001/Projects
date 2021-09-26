def inject(mode,filename,text):

	if mode == "inject":
		file = open(filename, "ab")
		file.write(bytes(text, encoding="utf-8"))
		file.close()

	elif mode == "read":
		file = open(filename, "rb")
		splitContent = file.read().split(b"<identifier>")
		print(splitContent[1])
		file.close()

# inject or read
mode = "read"

# name of file
filename = "mozambique.png"

# text that will be appended
text = "<identifier>"+"Terraria is a land of adventure! A land of mystery! A land that's yours to shape, defend, and enjoy. Your options in Terraria are limitless. Are you an action gamer with an itchy trigger finger? A master builder? A collector? An explorer? There's something for everyone.Start by building basic shelter, then dig for ore and other resources. Discover and craft over 500 weapons of magic, ranged, melee and summon varieties, as well as armor, and use them to battle hundreds of different enemies. Soon you'll be going head-to-head with any of a dozen enormous bosses. Go fishing, ride a mount, find Floating Islands, build houses for helpful NPCs, and much, much more."

inject(mode, filename, text)