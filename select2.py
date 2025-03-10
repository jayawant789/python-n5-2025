username = input("Please enter your username: ")
password = input("Please enter your password: ")
if username == "ian" and password == "letmein":
    print("Logon accepted")
else:
    print("Password incorrect")

    #username=IAN, password=letmein-password incorrect 
    #username=ian, password=letmein-password correct
    #username=ian, password=LETMEIN-password incorrect 
