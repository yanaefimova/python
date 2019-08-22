import string

print("-Some Game-")
user_data = {"name": {"question": "Enter your name: ", "answer": None},
             "age": {"question": "Enter your age: ", "answer": None},
             "gender": {"question": "Enter your gender (m/f) : ", "answer": None},
             "pet_name": {"question": "Enter your pet's name: ", "answer": None},
             "like_game": {"question": "Do you like to play games (y/n)? ", "answer": None}
             }
for itm in user_data:
    user_data[itm]["answer"] = input(user_data[itm]["question"])

    # Check AGE format
    if itm == "age" and user_data[itm]["answer"].isdigit():
        user_data[itm]["answer"] = int(user_data[itm]["answer"])
    elif itm == "age":
        print("Incorrect! Use the number format!")
        user_data[itm]["answer"] = int(input(user_data[itm]["question"]))

    # Check AGE confirm
    if itm == "age" and user_data[itm]["answer"] >= 18 and user_data[itm]["answer"] <= 90:
        print("Ok,", user_data["name"]["answer"], "let's play")
    elif itm == "age" and user_data[itm]["answer"] < 18:
        print("Forbidden to play the game! Your age is less than 18")
        break
    elif itm == "age" and user_data[itm]["answer"] >= 90:
        temp_question = (
        'This game can be tiring. Do you really want to play? (y/n) ', 'Again...Do you really want to play? (y/n) ')
        for itmp in temp_question:
            confirm = input(itmp).lower()
            if confirm == "y":
                continue
            elif confirm == "n":
                break
            else:
                print("Incorrect! Use 'y' or 'n'!")
                confirm = input(itmp).lower()
        if confirm == "y":
            print("Ok,", user_data["name"]["answer"], "let's play")
            continue
        else:
            print("This is the right decision. Games are an evil! Bye!")
            break

    # Check GENDER format
    if itm == "gender":
        while not (user_data[itm]["answer"].lower() == "m" or user_data[itm]["answer"].lower() == "f"):
            user_data[itm]["answer"] = input("Incorrect! Enter 'm' for male or 'f' for famele!: ")

    # Make LIKE_GAME is bool
    if itm == "like_game":
        while not (user_data[itm]["answer"].lower() == "y" or user_data[itm]["answer"].lower() == "n"):
            user_data[itm]["answer"] = input("Incorrect! Enter 'y' or 'n': ")
        if user_data[itm]["answer"].lower() == "y":
            user_data[itm]["answer"] = True
        else:
            user_data[itm]["answer"] = False

# Print other letters of NAME
user_name_dif = []
ascii = string.ascii_lowercase

for lett_a in ascii:
    if lett_a not in user_data["name"]["answer"].lower():
        user_name_dif.append(lett_a)
print("\nThese letters are not in your name:\n", user_name_dif)