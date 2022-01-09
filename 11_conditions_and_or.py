username = "robert"
password = "testpas123"

#        True                       True
if username == "robert" and password == "testpas123":
    print("Wellcome Robert. You are logged in.")
else:
    print("Bad username or password")


#          False                   True
if username == "robert" or password == "testpas123":
    print("username or password was correct")