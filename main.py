from random import randint

coins = 10


while True:
    new_game = input("Start a New Game? (1 - Yes / 0 - No): ")

    match new_game:
        case "1":

            random_number = randint(1, 100)
            tries = 10
            used_hint = False

            print("\nGuess a number from 1 to 100. \nYou have", tries, "tries")

            while tries > 0:

                if tries < 2 and used_hint == False:
                    print("\n--- HINT AVAILABLE ---")
                    print("\nCoins available:", coins)

                    while True:
                        hint_request = input("\nDo you want to find out the last digit of the number for 10 coins? (1 or 0): ")

                        if hint_request == "1":
                            if coins >= 10:
                                coins -= 10
                                last_digit = random_number % 10
                                print("\n💡 Hint: The last digit of the number is ->", last_digit)

                            else:
                                print("\n❌ Not enough coins! Win to earn more.")
                            used_hint = True
                            break
                        elif hint_request == "0":
                            used_hint = True
                            print("Hint rejected.")
                            break
                        else:
                            print("\nInput error! \nPlease enter 1 or 0.")
                            continue

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
                    tries -= 1
                else:
                    print("\nInput error! \nPlease enter an integer from 1 to 100. This attempt does not count.")
                    continue


                if num == random_number:
                    if tries == 9:
                        coins += 10
                        print("\n🎉 Congratulations! \nYou guessed the number:", random_number, "in 1 attempt.","\n\nGreat intuition! \nBonus: +10 coins!")

                    elif tries == 7:
                        coins += 6
                        print("\n🎉 Congratulations! You guessed the number:", random_number, "\nYou guessed the number in 3 attempts. Great result!")
                    else:
                        coins += 5
                        print("\n🎉 Congratulations! You guessed the number:", random_number)

                    tries = 0
                    used_hint = False

                elif num > random_number and tries > 0:
                    print("\n📉 The number you are guessing is less than yours.")
                elif num < random_number and tries > 0:
                    print("\n📈 The number you are guessing is greater than yours.")
                elif tries == 0:
                    used_hint = False

                    print("\n💀 Game over. Remaining attempts: 0")

        case "0":
            print("🌚 You have opted out of the game!")
            break
        case _:
            print("\n🛑 Input error! \nPlease enter 1 or 0.\n")
            continue