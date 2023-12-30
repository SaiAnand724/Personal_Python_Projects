import random
import os

MYPROJECTFOLDER = "modifiedHangmanProject"
# Function to load the list of words from a text file
# Each word should be on a separate line.
# Leading and trailing whitespace should be removed from each line.
# The words should be in uppercase format.
def load_words():
    #with open("C:\\Users\saiud\OneDrive\Documents\Python_Projects\modifiedHangmanProject\words.txt", "r") as file:
    directory = os.getcwd()
    print("The Current working directory is :", directory) 
    myFile = directory + "\\" + MYPROJECTFOLDER + "\words.txt"
    print("My file:", myFile)
    with open(myFile, "r") as file:
        words = file.readlines()
    words = [word.strip().upper() for word in words]
    return words

# Function to select a random word from the list
def get_word():
    words = load_words()
    word = random.choice(words)
    return word

# Function to play the game
def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print("\nNumber of tries: ", tries)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        # isalpha() method returns True if all the characters are alphabet letters (a-z)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word correctly!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Try Again!")

# Function to display the hangman image based on the number of tries remaining
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |
                   -
                """ ]
    return stages[tries]
    
# Main function to run the game
def main():
    print("Welcome to Hangman!\n")
    word = get_word()
    play_game(word)

if __name__ == "__main__":
    main()
