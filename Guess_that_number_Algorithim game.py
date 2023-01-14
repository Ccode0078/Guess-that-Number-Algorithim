import random
'''
 GUESS THAT NUMBER !
  INSTRUCTIONS
 1. The computer will generate a random number, then User will try to guess it.
 2. The computer will generate a random number, then the computer will try to guess it using linear search.
 3. The computer will generate a random number, then the computer will try guess it using binary search.
 '''
print('        ----------- Guess That Number --------')
print('        -----------   Welcome         --------')


def guess_random_number(tries, start, stop):
    # Use the ranmdom module to generate a number between the start and stop numbers.
    random_num = random.randint(start, stop)
    print(random_num)
    while tries:
        print("Number of tries left", tries)
        user_input = int(input("guess a number between" +
                         str(start) + " and " + str(stop)))   # User being asked by CPU to guess a number between example(3 - 10).
        if user_input == random_num:
            print('You guessed the correct number')
            return
        # If the integer the User picked was lower than the random number you will need to guess a higher number.
        if user_input < random_num:
            print("guess Higher")
        else:
            print("Guess lower")
        tries -= 1
        # Every try the the User does, takes away 1 "try" at a time.
        print("Number of tries left :", tries)
        if tries == 0:
            print("program failed to guess the number", random_num)

  # task 1 drive

# guess_random_number(5, 0, 10)     <---- Try output example

#     ---- Guess Random Number using Linear search ----
def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop) 
    computer_choice = int(                        # The CPU must guess the random number correctly
        input("The number for the program to guess is: "))
    print("Number of tries: ", tries)
    for computer_choice in range(random_number):
        if computer_choice == random_number:
            print("The program has found the random number:", random_number)
        elif computer_choice != random_number:
            print("The program is guessing...", random_number)   # CPU trying to guess the number.
        else:
            print("The ")
        tries = tries - 1
        if tries == 0:
            print("The program didnt find the right number") #The CPU failed to guess the correct number
            break

 # task 2 drive
#guess_random_num_linear(5, 0, 10)      <----- Try output example


#   ---- Guess Random Number Using Binary Search ----
def guess_random_number_binary(tries, start, stop): # Set the Parameters.
    num = random.randint(start, stop)
    print(f"The random number to find is: ", num) # Every time the code runs, it will generate a new random number to guess.

    def binary_search(stop, start, num):
        lower_bound = start
        upper_bound = int(stop) - 1
        tries = 5
        while tries != 0:

            while lower_bound <= upper_bound:
                pivot = (lower_bound + upper_bound) // 2
                pivot_value = pivot - 1

                if pivot_value == num:
                    print(f"Found it! {num}")
                    return num
                elif pivot_value > num:
                    upper_bound = pivot - 1
                    print("Guessing higher!")
                    tries -= 1
                elif pivot_value < num:
                    lower_bound = pivot + 1
                    print("Guessing lower!")
                    tries -= 1
                if tries == 0:
                    print("Your program failed to find the number")
                    return
    binary_search(stop, start, num)


    # Task 3 test driver
#guess_random_number_binary(5, 0, 100) TRIES,START,NUM     <---- TRY OUTPUT EXAMPLE
