def pad_right(string: str, targetLength: int):
    if len(string) < targetLength:
        for i in range(targetLength - len(string)):
            string += " "
    
    return string