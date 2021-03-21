import pickle

#exampleDict = {1:"69", 2:"420"}

#pickleOut = open("dictionary.pickle", "wb")
#pickle.dump(exampleDict, pickleOut)
#pickleOut.close()

pickleIn = open("dictionary.pickle", "rb")
exampleDict = pickle.load(pickleIn)

print(exampleDict)
input()
