# rock paper scissors, 3, 5, or 7 match series

from random import randint

#print(random_num)

try:
    series_modes = [3, 5, 7]
    choose_series = int(input("Enter matches in the series (3, 5, or 7): "))


    if choose_series == 3:
        choose_series = series_modes[0]
    elif choose_series == 5:
        choose_series = series_modes[1]
    elif choose_series == 7:
        choose_series = series_modes[2]
    else:
        choose_series = series_modes[0]
        print("Invalid input. Default option is selected. ")
except ValueError:
    choose_series = series_modes[0]
    print("Invalid input. Default option is selected. ")


print("This is a " + str(choose_series) + " match series. ")
rsp = ["Rock", "Paper", "Scissors"]

matches_count = 0
computer_win = 0
user_win = 0



while matches_count < choose_series:
    print("\n")
    user_select = input("Select from R, P, S: ")
    computer_select = rsp[randint(0, 2)]

    if user_select == computer_select[0]:
        print("Match drawn. ")
        print("Computer also selected " + computer_select)
    elif user_select == "R" and computer_select[0] == "P":
        computer_win += 1
        print("Computer selected " + computer_select)
    elif user_select == "R" and computer_select[0] == "S":
        user_win += 1
        print("Computer selected " + computer_select)
    elif user_select == "P" and computer_select[0] == "S":
        computer_win += 1
        print("Computer selected " + computer_select)
    elif user_select == "P" and computer_select[0] == "R":
        user_win += 1
        print("Computer selected " + computer_select)
    elif user_select == "S" and computer_select[0] == "R":
        computer_win += 1
        print("Computer selected " + computer_select)
    elif user_select == "S" and computer_select[0] == "P":
        user_win += 1
        print("Computer selected " + computer_select)
    else:
        print("Invalid input. Game ends. ")
        break
    matches_count += 1
    print("Overall score is " + str(user_win) + "-" + str(computer_win))

    matches_remain = choose_series - matches_count
    if matches_remain < abs(user_win - computer_win):
        break

    if user_win > computer_win:
        print("You are winning. ")
    elif user_win < computer_win:
        print("Computer is winning. ")
    else:
        print("No one has the lead.")

if user_win > computer_win:
    print("Congratulations. You won the series. ")
elif user_win < computer_win:
    print("Computer won the series. Better luck next time. ")
else:
    print("Series drawn.")
