# global variable
import random

USER_CHOICES = ("rock", "paper", "scissor")


# pick user input
def get_user_input():
    user_choice = input('pick your choice ["rock", "paper", "scissor"]:')

    while user_choice not in USER_CHOICES:
        user_choice = input('pick your choice["rock", "paper", "scissor"]:')
    print(f"your choice is: {user_choice}")
    return user_choice


# pick pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f"pc choice was: {pc_choice}")
    return pc_choice


# detemine_winner(user,pc)
def detemine_winner(user, pc):
    if user == pc:
        return "draw"

    elif (
        (user == "rock" and pc == "scissor")
        or (user == "scissor" and pc == "paper")
        or (user == "paper" and pc == "rock")
    ):
        print("user you woon!!!!")
    else:
        print("pc  wooon!!!!")


# handler
def main():
    detemine_winner(get_user_input(), get_pc_input())


# loop always run
answer = "y"
while answer == "y":
    main()
    answer = input("do you want to continue? (y/n):")
