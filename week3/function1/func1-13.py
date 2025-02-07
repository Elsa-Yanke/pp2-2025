import random   
def guess_number():
    num = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    count = 0

    while True:
        guess = input("Take a guess.\n")

        if guess.lower() == 'q': 

            print("You have quit the game. See you next time!") 
            break 

        try: 

            guess = int(guess) 
        except ValueError: 
            print("Please enter a valid number or 'q' to quit.") 
            continue 
        
        
        if guess > num: 
            print("Too high!") 
            count+=1
        elif guess < num: 
            print("Too low!") 
            count+=1
        else: 

            print(f"Congratulations! You won! You guessed my number in {count+1} guesses") 
            break 

guess_number()