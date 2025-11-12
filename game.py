import random

print("Welcome to Rock-Paper-Scissors!")

# list of choices
moves = ['Rock', 'Paper', 'Scissors']

# verify that input is valid
def verify_input(input):

    # verified is false by default
    verified = False

    # if input in title format = any item in moves, verified is true
    for m in moves:
        if input.title() == m:
            verified = True
    
    return verified
    
        
def play_game():
    # ask player for input
    user_input = input("Choose Rock, Paper, or Scissors: ")

    # verify input with function
    verified = verify_input(user_input)

    # if input is valid
    if verified = True:
        print(f"You chose: {user_input}")

    # if input is invalid, exit the function
    else:
        print(f"{user_input} is not valid")
        return
    
    # generate a random number from 0 to 2
    print("Welcome to Rock-Paper-Scissors!")

    computer_choices = ['Rock', 'Paper', 'Scissors']

    computer_input = random.choice(computer_choices)

    print(f"Computer chose: {computer_input}")

    # see if user won or lost
    


