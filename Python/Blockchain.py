import random
import hashlib
import pickle
import json
import time

firstNames = ['Anna', 'John', 'James', 'Emily', 'Michael', 'Emily', 'David', 'Sarah', 'William', 'Christopher', 'Elizabeth', 'Ryan', 'Robert', 'Mark', 'Jessica']
lastNames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris']

class Block:

    def __init__(self, blockHash, previousHash, data):
        self.blockHash = blockHash
        self.previousHash = previousHash
        self.data = data

def main(blocks):
    
    previousHash = 0
    
    with open("blockchain.txt", "w") as f:
        f.write("")
    
    for i in range(blocks):

        data = {
            "name": f"{random.choice(firstNames)} {random.choice((lastNames))}",
            "age": random.randint(18, 40),
            "uid": random.randint(100000000000, 999999999999)
        }
        blockHash = hashlib.sha256(pickle.dumps(data)).hexdigest()
        block = Block(blockHash, previousHash, data)
        blockDetails = {
            "Hash": block.blockHash,
            "Previous Hash": block.previousHash,
            "Data": block.data
        }

        with open("blockchain.txt", "a") as f:
            f.write(json.dumps(blockDetails, indent=4))
            f.write("\n")

        previousHash = blockHash
    
start = time.process_time()
main(10)
print(time.process_time() - start)