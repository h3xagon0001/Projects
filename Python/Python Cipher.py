
# write message into file
def write(filename, message):
	with open(filename, "rb") as openfile:
		split = filename.split(".")
		newfile = open(split[0] + "_ciphered." + split[1], "wb")
		newfile.write(openfile.read())
		newfile.write(bytes("<s>" + message, encoding="utf-8"))

# read message from file
def read(filename):
	with open(filename, "rb") as openfile:
		split = openfile.read().split(b"<s>")
		print(split[1])


print("\n[    Python Cipher and Decipher Tool    ]\n")

c = int(input("Enter:\n(1) to Cipher\n(2) to Decipher\n"))

if c == 1:
	filename = input("Enter name of file to cipher (include file extension): ")
	message = input("Enter message to cipher: ")
	write(filename, message)
	input("Completed successfully")

elif c == 2:
	filename = input("Enter name of file to decipher (include file extension): ")
	read(filename)
	input("Completed successfully")

# Thanks to thegamecracks#1317 for having a mountain of pantience and helping me