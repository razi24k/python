# Q 06
import random


def game():
    user_count = 0
    computer_count = 0
    for i in range(3):
        computer_choice = str(random.choice(("r", "p", "s")))
        user_choice = str(input("Please select one of the options r/p/s. "))
        print((computer_choice))
        if user_choice in ('r', 'p', 's'):
            if computer_choice == user_choice:
                continue
            else:
                if (computer_choice == "r") and (user_choice == "p"):
                    user_count += 1
                elif computer_choice == "p" and user_choice == "s":
                    user_count += 1
                elif computer_choice == "s" and user_choice == "r":
                    user_count += 1
                else:
                    computer_count += 1
        else:
            print("wrong choice!")

        print(f"user: {user_count} computer: {computer_count}")
    count_user_win = 0
    count_computer_win = 0

    if user_count == computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "Tie")
        return 2

    elif user_count > computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "// User wins.")
        return 0

    elif user_count < computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "// computer wins.")
        return 1


flag = True
total_computer_wins = 0
total_user_wins = 0
total_tie = 0
while flag:
    a = game()
    if a == 1:
        total_computer_wins += 1
    elif a == 0:
        total_user_wins += 1
    elif a == 2:
        total_tie += 1

    user_flag = input("Do you want to play again? ")
    if user_flag.lower() != 'yes':
        flag = False

empty_dict = {}
if total_user_wins > total_computer_wins:
    print("User won!")
    empty_dict.update({'user': total_user_wins})

elif total_user_wins < total_computer_wins:
    print("Computer won!")
    empty_dict.update({'computer': total_computer_wins})
else:
    print("tie")
    empty_dict.update({'tie': total_tie})

print(empty_dict)
