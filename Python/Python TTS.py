from gtts import gTTS
import os

welcome = '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄─▄▄─█▄─█─▄█─▄─▄─█─█─█─▄▄─█▄─▀█▄─▄███─▄─▄─█─▄─▄─█─▄▄▄▄█
██─▄▄▄██▄─▄████─███─▄─█─██─██─█▄▀─██████─█████─███▄▄▄▄─█
█▄▄▄████▄▄▄███▄▄▄██▄█▄█▄▄▄▄█▄▄▄██▄▄████▄▄▄███▄▄▄██▄▄▄▄▄█
'''

print(welcome)

while True:
	text = str(input("Text to convert: "))
	soundFile = gTTS(text)

	soundFile.save("python_tts.mp3")
	os.system("python_tts.mp3")