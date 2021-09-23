email = input("Enter your email address: ")

slicedString = email.split("@")

username = slicedString[0]
domain = slicedString[1]

print(f"Username: {username}\nDomain: {domain}")
input()