phonebook = {}

name = input("Your name?")
phone = input("Phone?")
email = input("Email?")

phonebook[phone] = {"name": name, "email": email}
print(phonebook)