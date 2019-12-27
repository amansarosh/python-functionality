
secret_word = "dog"  # word that needs to be guessed
guess = ""  # variable used to store users guess
guess_count = 0  # keeps track of guesses
guess_limit = 3  # how many guesses a user can do
out_of_guesses = False  # starting amount of guesses

while guess != secret_word and not out_of_guesses:  # read as while guess is not equal to the secret word
    if guess_count < guess_limit:  # if the guess count is less than the guess limit then we continue
        guess = input("Enter Guess: ")  # every time we give the guess
        guess_count += 1  # we count it onto the rounds
    else:
        out_of_guesses = True  # if out of guesses then mark as true

if out_of_guesses:
    print("You Lost")  # if out of guesses then print you loose
else:
    print("You Win!")  # if NOT out of guesses then you win
