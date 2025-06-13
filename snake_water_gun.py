import random
options = ("Snake", "Water", "Gun")
random_number = random.randrange(0,3)
computer_output = options[random_number]
again = input("Want to play this game...?(yes/no)").capitalize()

while(again == "Yes"):
    print("************Welcome to this game************")
    user_input = input("Choose an option to play game(Snake, Water, Gun)... ").capitalize()

    if user_input == computer_output:
        result = "Tie"
    elif user_input == "Snake" and computer_output == "Gun" or user_input == "Gun" and computer_output == "Water" or user_input == "Water"  and computer_output == "Snake":
        result = f"You loose! Computer win because computer choosed {computer_output}"
    else:
        result = f"You win! Computer loose because computer choosed {computer_output}"

    print(result)

    again = input("Do you want to play again...?(yes/no)  ").capitalize()

    