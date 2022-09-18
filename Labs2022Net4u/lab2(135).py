'''
writing the program that will receive a shopping basket from outside and calculate its cost...
tomato (per kg) - 5 nis
cucumber (per kg) - 3 nis
Coca-Cola - 5 nis
chicken wings (per kg) - 30 nis
The program will calculate the price after tax of 17%, with no remainder
'''

from time import sleep

name = input("Hello! Enter your name please\n")
print("Welcome to our market " + name + "\nNow we will calculate your shopping basket.\n------------\nPrices:\ntomato=5 nis (per kg)\ncucumber=3 nis (per kg)\nCoca-Cola= 5 nis\nchicken wings=30 nis (per kg)\nPlease select the items you would like to bay: ")
sleep(1)
tomatoes = int(input("How many tomatoes?\n"))
cucumbers = int(input("How many cucumbers?\n"))
Coca_Cola = int(input("How many bottles of Cola?\n"))
chicken_wings = int(input("How many chicken_wings (in kg)?\n"))
sum1 = tomatoes * 5
sum2 = cucumbers * 3
sum3 = Coca_Cola * 5
sum4 = chicken_wings * 30
sleep(1)
print("Summary of your order:\ntomatoes- " + str(tomatoes) + "\ncucumbers- " + str(cucumbers) + "\nCoca-Cola- " + str(
    Coca_Cola) + "\nchicken wings- " + str(chicken_wings))
summary = sum1 + sum2 + sum3 + sum4
sleep(1)
print("You have to pay(plus tax): " + str("%.2f" % (summary * 1.17)) + "NIS\n...\nThank you for your visit!")
