# returns the index of the target, else returns -1
def bin_search(array ,low, high, target):
    
    # finding the middle of array
    if high >= low:
        mid = (high + low) // 2
        
        # check if target is in the middle
        if target == array[mid]:
            return mid
            
        # check if target is smaller than mid
        elif target < array[mid]:
            return bin_search(array, low, mid - 1, target)
            
        # check if target is bigger than mid
        else:
            return bin_search(array, mid + 1, high, target)
    # target is not present in array  
    else:
        return -1

# test array
testarray = [2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 18, 20]
# int to find in array
target = int(input("What number do you want to search for:\n"))

# call func
answer = bin_search(testarray, 0, len(testarray) - 1, target)

if answer != -1:
    print(f"Target is at index {answer}")
else:
    print("Target is not in array")
input()
