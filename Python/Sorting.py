import time

data = [361, 32, 300, 300, 150, 384, 310, 79, 361, 402, 32, 322, 67, 167, 403, 45, 226, 158, 103, 271, 162, 199, 48, 74, 166, 452, 206, 223, 215, 173, 82, 201, 218, 49, 457, 407, 85, 34, 317, 37, 174, 43, 466, 396, 32, 183, 271, 396, 113, 52, 408, 141, 64, 270, 226, 433, 27, 355, 290, 303, 291, 429, 77, 146, 383, 223, 424, 464, 131, 277, 420, 443, 173, 268, 195, 50, 377, 496, 288, 6, 500, 209, 397, 413, 122, 52, 151, 120, 110, 289, 403, 261, 276, 104, 103, 303, 480, 189, 410, 438]
index1 = 0
index2 = 1
temp = 0

time.sleep(5)

while True:
	if index2 > len(data)-1:
		index1 = 0
		index2 = 1

	if data[index1] > data[index2]:
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp
	
	print(data)
	index1 += 1
	index2 += 1