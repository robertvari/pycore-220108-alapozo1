phonebook = {
    "+36 20 234 5678": {
        "name": "Robert",
        "address": "Budapest",
        "email": "robert@gmail.com",
        "age": 34,
        "kids": 2
    },
    "+36 20 653 7865": {"name": "Csaba", "address": "Pécs", "email": "csaba@gmail.com", "age": 19}
}

print(phonebook["+36 20 653 7865"]["name"])
print(phonebook["+36 20 653 7865"]["address"])
print(phonebook["+36 20 653 7865"]["email"])
print(phonebook["+36 20 653 7865"]["age"])

print(phonebook.keys())

# cast dictionary to list
print( list(phonebook) )