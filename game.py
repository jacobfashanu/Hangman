import random
from words import words_lst

def print_game(wrong_guess):
    if wrong_guess == 0:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-")
    elif wrong_guess == 1:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("-")
    elif wrong_guess == 2:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|            |")
        print("|")
        print("|")
        print("-")
    elif wrong_guess == 3:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           \|")
        print("|")
        print("|")
        print("-")
    elif wrong_guess == 4:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           \|/")
        print("|")
        print("|")
        print("-")
    elif wrong_guess == 5:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           \|/")
        print("|            |")
        print("|")
        print("-")
    elif wrong_guess == 6:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           \|/")
        print("|            |")
        print("|           /")
        print("-")
    else:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           \|/")
        print("|            |")
        print("|           / \\")
        print("-")
        
def get_word():
    word = random.choice(words_lst)
    return word

def main():
    wrong_guess = 0
    print_game(wrong_guess)
    word = "hi"
    guesses = ["_"] * len(word)
    cont = True 
    while(wrong_guess < 7):
        print(" ".join(guesses))
        guess = input("\nPlease guess a letter: ")
        if len(guess) != 1:
            print("You must type a letter\n")
            
        elif guess.lower() in guesses:
            print("You already guessed \"{}\" before \n".format(guess))
            
        elif guess.lower() in word.lower():
            print("Great Job, \"{}\" is in the word\n".format(guess))
            new_word = word.lower()
            for i in range(len(word)):
                if new_word[i] == guess.lower():
                    guesses[i] = guess
        else:
            print("Sorry, \"{}\" is not in the word\n".format(guess))
            wrong_guess += 1
        
        if "_" not in guesses:
            print(" ".join(guesses))
            print("Congratulations, you won!!!")
            return
        print_game(wrong_guess)
        
    print("\n\nSorry, you lost the game.")
    print("The word was: \"{}\"".format(word))  
        
             
main()