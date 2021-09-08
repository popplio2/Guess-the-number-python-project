from random import randrange
chosen_number = int(input("Choose a number from 1-100. "))
range_bottom = 1
range_top = 101
guess_counter = 0
def guess_number():
    global range_bottom
    global range_top
    global guess_counter
    guess_counter += 1
    return randrange(range_bottom, range_top)

guessed_number = guess_number()
print("Guess #" + str(guess_counter)+ ": " + "My guess is " + str(guessed_number))

while chosen_number != guessed_number:
    if chosen_number > guessed_number:
        range_bottom = guessed_number + 1
        guessed_number = guess_number()
        print("Guess #" + str(guess_counter)+ ": " + "My guess is " + str(guessed_number))
    else: # if chosen number < guessed number
        range_top = guessed_number
        guessed_number = guess_number()
        print("Guess #" + str(guess_counter)+ ": " + "My guess is " + str(guessed_number))
print("Aha! Your number was " + str(guessed_number) + "!")
    