import os
import random


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# The Global Variables Unite
WORD_LIST = []
WORD_LEN = 5
tries = 5


# Extracts Words from the Dictionary File
def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as dictionary:
            for word in dictionary.readlines():
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File Not Found")
    print(WORD_LEN)
    print(WORD_LIST)
    # target = WORD_LIST[random.randint(0,len(WORD_LIST))]
    return random.choice(WORD_LIST)


# Gameplay Function
def banana():
    letters_used = set()  # Tracks the letters that are not in the word
    letters_correct = set()  # Hopefully Tracks the letters in the word...
    global tries
    life = tries
    target = extract_words()  # Gets Random Word from List
    print("Welcome to Wordle 3.0!")
    print(f"You have {life} attempts to guess the {WORD_LEN}-letter word.")
    while life > 0:
        player_guess = input("Enter your guess: ").strip().lower()
        # Checks for correct guess
        if player_guess == target:
            print("You guess the word! GGS Lil Player!")
            break
        # Checks for correct length
        elif len(player_guess) != WORD_LEN:
            print(f"?. Entere a {WORD_LEN}-letter word.")
            continue


        # Checks if word is a ENGLISH word
        elif player_guess not in WORD_LIST:
            print("Bro What? This word is not in dictionary. Try again.")
            continue

        # Checks each letter to the target word
        print(f"Your guess: {player_guess}")
        for i in range(WORD_LEN):
            if player_guess[i] == target[i]:
                print(f"{player_guess[i]} - Chophy")  # Correct letter and spot
                letters_correct.add(player_guess[i])
            elif player_guess[i] in target:
                print(f"{player_guess[i]} - Storts")  # Correct letter, but wrong spot
            else:
                print(f"{player_guess[i]} - Bascat")  # Incorrect letter, not even in the word
                letters_used.add(player_guess[i])

        life -= 1
        print(f"You have {life} attempts left.")
        print(f"Letters Correct: {' '.join(sorted(letters_correct))}")
        print(f"Letters Not In Word: {' '.join(sorted(letters_used))}")
    # Ends games with loss
    else:
        print(f"GGS Lil Player, the correct word was: {target}")

    # Option to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        banana()
    else:
        print("Thanks for playing Wordle 3.0!")


# Menu Function
def minecraft():
    global WORD_LEN, tries

    while True:
        clear_console()

        print("[-] 0. Exit\n"
              "[-] 1. Change Word Length\n"
              "[-] 2. Change Difficulty\n"
              "[-] 3. Play Game\n" \
              "[-] 4. View Current Settings")
        selection = int(input("[-] Please Select an Option: "))

        if selection == 0:
            print("Quiting Game")
            exit()
        elif selection == 1:  # Change Word Length
            print("Choose Difficulty:\n" \
                  "[-] 1. Easy (4-Letter Words\n" \
                  "[-] 2. Standard (5-Letter Words)\n" \
                  "[-] 3. Hard (6-Letter Words)\n" \
                  "[-] 4. Challenging (7-Letter Words)")
            WORD_LEN_DIFF = input("Select an Option: ")

            if WORD_LEN_DIFF == '1':
                WORD_LEN = 4
            elif WORD_LEN_DIFF == '2':
                WORD_LEN = 5
            elif WORD_LEN_DIFF == '3':
                WORD_LEN = 6
            elif WORD_LEN_DIFF == '4':
                WORD_LEN = 7
            else:
                print("Invalid Option Selected")


        elif selection == 2:  # Change Amount of Tries
            print("Choose Difficulty:\n" \
                  "[-] 1. Easy (10 Tries)\n" \
                  "[-] 2. Standard (5 Tries)\n"
                  "[-] 3. Hard (4 Tries)\n"
                  "[-] 4. Challenging (3 Tries)")
            tries_diff = input("Select an Option: ")

            if tries_diff == '1':
                tries = 10
            elif tries_diff == '2':
                tries = 5
            elif tries_diff == '3':
                tries = 4
            elif tries_diff == '4':
                tries = 3
            else:
                print("Invalid Option Selected")


        elif selection == 3:  # Starts Game
            banana()


        elif selection == 4:  # Examine Current Settings
            print(f"Current Word Length: {WORD_LEN}\n"
                  f"Current Number of Tries: {tries}")
            input("Press Enter to Continue...")


        else:
            input("Value isn't an option. Press Enter to Continue...")


def main():
    minecraft()


if __name__ == "__main__":
    main()
