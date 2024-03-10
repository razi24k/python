import random


def game():
    user_count = 0
    computer_count = 0
    for i in range(3):
        computer_choice = str(random.choice(("r", "p", "s")))
        print((computer_choice))

        user_choice = str(input("Please select one of the options r/p/s. "))

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

    if user_count == computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "Tie")
        return 2

    elif user_count > computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "// User wins.")
        return 0

    elif user_count < computer_count:
        print(f"user: {user_count} vs computer: {computer_count}", "// computer wins.")
        return 1


user_answer = input("Do you want to continue the previous game?")
if user_answer == 'yes':
    file = open('res.txt', 'r')
    content = file.read()
    list_a = content.split(",")
    total_computer_wins = int(list_a[0])
    total_user_wins = int(list_a[1])
    total_tie = int(list_a[2])
    empty_dict = {'computer': int(list_a[0]), 'user': int(list_a[1]), 'tie': int(list_a[2])}
    print(content)
    file.close()
else:
    empty_dict = {'computer': 0, 'user': 0, 'tie': 0}
    file = open("res.txt", "w")
    file.write(f"{str((empty_dict.get('computer')))},{str((empty_dict.get('user')))},{str((empty_dict.get('tie')))}")
    file.close()
    total_computer_wins = 0
    total_user_wins = 0
    total_tie = 0

flag = True
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

if total_user_wins > total_computer_wins:
    print("User won!")

elif total_user_wins < total_computer_wins:
    print("Computer won!")
else:
    print("tie")


empty_dict.update({'user': total_user_wins})
empty_dict.update({'computer': total_computer_wins})
empty_dict.update({'tie': total_tie})

file = open("res.txt", "w")
file.write(f"{str((empty_dict.get('computer')))},{str((empty_dict.get('user')))},{str((empty_dict.get('tie')))}")
file.close()