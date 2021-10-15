import random

def hangman(word): #define function to store the game
    wrong = 0 #store incorrect guesses
    print(word)
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ] #list of strings, when printed in a new line, a picture of a hangman forms
    rletters = list(word) #remaining letters, keeps track of which letters are left to guess
    board = ["__"] * len(word) #list of strings, use it keep track of the game board to display like ["__", "__", "__"] for word cat
    win = False #won or not
    print("Welcome to Hangman") #start the game to 
    while wrong < len(stages) - 1: #loop to keep the game going, continues until wrong is less than the stages list -1, game will continue
            #until the player 2 has guesses more wrong letter than the number fo strings it takes to create the hanghman
            #subtract 1 to compensate for the fact, that the stages list counts from zero, and wrong starts at 1
        print("\n") #print blank space to make the game looknice
        msg = "Guess a letter" #print msg to player
        char = input(msg) #collect the char guessed by player
        if char in rletters: #check if player geussed correctly, if the guess is in the list of letters
            cind = rletters.index(char)
            board[cind] = char #if it is, update the board list
            rletters[cind] = '$' #replace the letter guessed with a dollar sign, so its not anymore in the remaining list, its easier than removing
        else:
            wrong += 1 #if guessed incorrectly increment wrong by +1
        print((" ".join(board))) #print board, call join to make the next guess
        e = wrong + 1 #
        print("\n".join(stages[0: e])) #slice the stages list, start at 0 to slice up to stage we are depending on 'e', gives at begin 0 slice to 1
        if "__" not in board: #check if underscores are left in the board
            print("You win!")
            print(" ".join(board)) #print winned board
            win = True #win true, break the loop
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word)) #print lose with the word they could not guess

words = ["apple", "pear", "ananas", "blueberry", "watermelon"] #create list with words
random_word = random.choice(words) #use the random choice to pick randomly from list

hangman(random_word)

