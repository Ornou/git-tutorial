#! /usr/bin/python3
import random
def guess_loop():
    number_to_guess = random.randint(1,100)
    essais = 0
    nom = input ("First,what is your name ?: ")
    print ("Okay",nom)
    print ("I have in mind a number in between 1 and 100, can you find it ?")
    while True:
        try:
            guess = int(input())
            if guess > number_to_guess :
                 print ("The number to guess is lower")
                 essais = essais + 1
            elif guess < number_to_guess :
                 print ("The number to guess is higher")
                 essais = essais + 1
            else :
                 print ("You just found the number , it was indeed",guess)
                 print ("Congratulations",nom,"You found it in",essais,"trials")
                 
                 return
        except ValueError as err :
            print ("Invalid input,please enter an integer")
guess_loop()


