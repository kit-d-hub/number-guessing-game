from random import randint

# Global economy system
coins = 10

# --- MAIN GAME LOOP & MENU HANDLING ---
while True:
    new_game = input("Start a New Game? (1 - Yes / 0 - No): ")

    if new_game == "1":
        # Initialize a new game session with random number and full tries
        random_number = randint(1, 100)
        tries = 10
        used_hint = False

        print("\nGuess a number from 1 to 100. \nYou have", tries, "tries\n")

        # --- ACTIVE ROUND LOOP ---
        while tries > 0:

            # --- HINT SYSTEM ---
            # Offer a hint if the player is running out of tries (less than 2 left)
            if tries < 2 and used_hint == False:
                print("\n--- HINT AVAILABLE ---")
                print("\nCoins available:", coins)

                # Prompt user for hint and validate their choice (1 or 0)
                while True:
                    hint_request = input("\nDo you want to find out the last digit of the number for 10 coins? (1 or 0): ")

                    if hint_request == "1":
                        if coins >= 10:
                            coins -= 10
                            last_digit = random_number % 10
                            print("\n💡 Hint: The last digit of the number is ->", last_digit)

                        else:
                            print("\n❌ Not enough coins! Win to earn more.\n")

                        used_hint = True
                        break

                    elif hint_request == "0":
                        used_hint = True
                        print("\n❌ Hint rejected.\n")
                        break

                    else:
                        print("\n🛑 Input error! \nPlease enter 1 or 0.")

            # --- USER INPUT & VALIDATION ---
            # Continuously prompt for a guess until a valid integer between 1 and 100 is entered
            while True:
                check_input_num = input("Enter your guess: ")

                if check_input_num.isdigit() and int(check_input_num) in range(1, 101):

                    num = int(check_input_num)
                    tries -= 1
                    break

                print("\n🛑 Input error! \nPlease enter an integer from 1 to 100. This attempt does not count.")

            # --- GAME LOGIC & RESULT CHECK ---
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



                break

            elif num > random_number and tries > 0:
                print("\n📉 The number you are guessing is less than yours.")
            elif num < random_number and tries > 0:
                print("\n📈 The number you are guessing is greater than yours.")
            elif tries == 0:

                print("\n💀 Game over. Remaining attempts: 0\n")
                break

    elif new_game == "0":
        print("\n🌚 You have opted out of the game!")
        break
    else:
        print("\n🛑 Input error! \nPlease enter 1 or 0.\n")

