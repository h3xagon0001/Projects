import random
import pyperclip

wordlist = ["HAHAHA", "GG EZ", "MALD", "COPE", "GG", "EZ",  "SHIVER", "SO", "BADXDX", "XD", "XD", "XD", "XD", "DXE", "Z", "EZZE",  "ZEZEGET", "GOOD", "IMAGINE", "X", "DX", "DX", "DX", "DX", "XRATIOE", "GET COUNTER", "GET", "COUNTER", "REAIO", "S", "DZ", "ZD", "ZDEZD", "XDEZ", "ZE", "LOL", "SO BAD", "SO", "BAD", "SKILL ISSUE",  "MALD MORE", "CRY ABOUT IT", "LOLOLO", "COPE", "UR MOMEZ"]
completedText = ""


words = int(input("Words: "))

for x in range(words):
	completedText += random.choice(wordlist) + " "

pyperclip.copy(completedText)

print(completedText)
print("Copied to clipboard.")
input()
