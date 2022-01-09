min_number = 1
max_number = 10
max_tries = 3

magic_number = 5

# show game intro
print("="*50, "MAGIC NUMBER", "="*50)
print(f"There is a number between {min_number} and {max_number}. Can you guess it?")
print(f"You have {max_tries} tries.")

user_guess = input("Your guess?")

while user_guess != magic_number:
    # bad guess
    max_tries -= 1

    # check if we have tries
    if max_tries == 0:
        print("You have no more tries :(")
        break

    print(f"Wrong answer. You have {max_tries} tries lef.")
    user_guess = input("Your guess?")