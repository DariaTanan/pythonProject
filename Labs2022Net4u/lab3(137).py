'''
Create 2 variables: string of my full name, another string of my mail.
Create variable of my age(integer)
Print all that to the screen.
Then, print my name from the end to the start and print it only with my age*3
Then, check if my full name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"
'''
n = "Daria Tanan"
m = "das.gmail.com"
a = 31
print("Full name: " + n + "\nEMail: " + m + "\nAge: " + str(a) + "\n-------------")

print("Full name: " + n[::-1] + "\nAge: " + str(a*3) + "\n-------------")

print(n in "idan ben dudu yuval shimon yael gal adam shahar yana")
print("Your name doesn`t match with the string")
