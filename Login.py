
# init varibles
username = "johndoe"
password = "jd123"


print("Please login to continue.")

# init function
def login():
    u = input("Username: ")
    p = input("Password: ")
    if u == username and p == password:
        print("Login Successful.")
        input()
    else:
        print("Invalid username or password.")
        print("Please try again.")
        login()

login()

    