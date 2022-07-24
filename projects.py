import random
import numpy as np
from random import choice
exclude_this = []
arr = [" "," "," "," "," "," "," "," "," "]
winner = 2

def demo():
    print("----------------------")
    print("|   0   |   1   |  2 |")
    print("----------------------")
    print("|   3   |   4   |  5 |")
    print("----------------------")
    print("|   6   |   7   |  8 |")
    print("----------------------")
    print("-----Enter Your Choice As Below----")

def printdata():
    print("----------------------")
    print("|  {}   |  {}   |  {}   |".format(arr[0],arr[1],arr[2]))
    print("----------------------")
    print("|  {}   |  {}   |  {}   |".format(arr[3],arr[4],arr[5]))
    print("----------------------")
    print("|  {}   |  {}   |  {}   |".format(arr[6],arr[7],arr[8]))
    print("----------------------")


def computer_choice():
    my_random_int = choice(list(set(range(0, 9)) - set(exclude_this)))
    exclude_this.append(my_random_int)
    print("Computer Choice is {}".format(my_random_int))
    arr[my_random_int]="X"


def user_choice():
    user = int(input("Enter choice of Position = "))
    arr[user] = "O"
    if(user>8):
        print('Please Enter Less Than 9')
        user = int(input("Enter choice of Position = "))
    while user in exclude_this:
        print("Please Enter Valid Choice")
        user = int(input("Enter choice of Position = "))
    else:
        exclude_this.append(user)
    
    


def comp_winner():
    global winner
    if(arr[0]=="X" and arr[1]=="X" and arr[2]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[3]=="X" and arr[4]=="X" and arr[5]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[6]=="X" and arr[7]=="X" and arr[8]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[0]=="X" and arr[3]=="X" and arr[6]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[1]=="X" and arr[4]=="X" and arr[7]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[2]=="X" and arr[5]=="X" and arr[8]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[0]=="X" and arr[4]=="X" and arr[8]=="X"):
        print("Computer is Winner")
        winner = 1
    elif(arr[2]=="X" and arr[4]=="X" and arr[6]=="X"):
        print("Computer is Winner")
        winner = 1

def user_winner():
    global winner
    if(arr[0]=="O" and arr[1]=="O" and arr[2]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[3]=="O" and arr[4]=="O" and arr[5]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[6]=="O" and arr[7]=="O" and arr[8]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[0]=="O" and arr[3]=="O" and arr[6]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[1]=="O" and arr[4]=="O" and arr[7]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[2]=="O" and arr[5]=="O" and arr[8]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[0]=="O" and arr[4]=="O" and arr[8]=="O"):
        print("You are Winner")
        winner = 0
    elif(arr[2]=="O" and arr[4]=="O" and arr[6]=="O"):
        print("You are Winner")
        winner = 0

# def choice():
    

def main():
    x = 1
    while(winner!=0 or winner!=1):
        demo()
        if(x==1):
            user_choice()
            x = 1 - x
        elif(x==0):
            computer_choice()
            x = 1 - x
        else:
            print("Code Block")
        printdata()
        comp_winner()
        user_winner()
        if(winner==0 or winner==1):
            print("--------------------Game Over-------------------")
            exit()
main()