import random

random_number = random.randrange(1, 100)

user_guessing_number =  int(input("Enter number What you guess(1-99)... "))
attempt = 1

while(user_guessing_number != random_number):
    if(user_guessing_number > random_number):
        print("Your guess number is greater than the random number...")
    elif(user_guessing_number < random_number):
         print("Your guess number is less than the random number...")
    user_guessing_number =  int(input("Enter number What you guess... "))
    attempt += 1

print(f"Congrats! 🥇 You guess the correct number only in {attempt} attempt... 🎊")