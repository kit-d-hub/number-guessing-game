from random import randint

while True:
    new_game = input("Start a new game? (1/0): ")

    match new_game:
        case "1":

            random_number = randint(1, 100)

            trys = 10

            print("\nGuess a number from 1 to 100. \nYou have", trys, "trys")

            while trys > 0:

                check_num = input("Enter your guess: ")

                test_number = 1
                valid = False

                while test_number <= 100:

                    if check_num == str(test_number) :
                        valid = True
                        break
                    test_number += 1

                if valid:
                    num = int(check_num)
                    trys -= 1
                else:
                    print("\nInput error! \nPlease enter an integer from 1 to 100. This attempt does not count.")
                    continue


                if num == random_number:
                    if trys == 9:
                        trys = 0
                        print("\nCongratulations! \nYou guessed the number:", random_number, "in 1 attempt.","\n\nExcellent result! Great intuition! \nYou guessed it on the first try!")

                    elif trys == 7:
                        trys = 0
                        print("\nCongratulations! You guessed the number:", random_number, "\nYou guessed the number in 3 attempts. Great result!")
                    else:
                        trys = 0
                        print("Congratulations! You guessed the number:", random_number)

                elif num > random_number and trys > 0:
                    print("The number you are guessing is less than yours.")
                elif num < random_number and trys > 0:
                    print("The number you are guessing is greater than yours.")
                elif trys == 0:
                    print("\nGame over. Remaining attempts: 0")

        case "0":
            print("You have opted out of the game!")
            break
        case _:
            print("\nInput error! \nPlease enter 1 or 0.\n")
            continue