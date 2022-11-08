secret_word = "goat"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")
print("You win!")



secret_word1 = "giraffe"
guess1 = ""

while guess1 != secret_word1:
    guess1 = input("Enter guess1: ")
    if guess1 == secret_word1:
        print("you win1")
    else:
        print("wrong choice, try again")


secret_word2 = "sheep"
guess2 = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess2 != secret_word2 and not (out_of_guesses):
    if guess_count < guess_limit:
        guess2 = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lose")
else:
    print("You win!")