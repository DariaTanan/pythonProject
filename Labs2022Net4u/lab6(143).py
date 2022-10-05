'''
Write a code that will show a menu.
Menu:
1.Insert number and ** it by 3
2.Insert 4 IPs to a list and print it
3.Insert 4 entries to DNS_DICT and print it
4.Check if a string is PALINDROME
is a user will not choose from 1-4, he will be told to insert 1-4 only.
'''
from time import sleep

choice = input(
    "Menu:\n1.Insert number and raise it to the 3rd power.\n2.Insert 4 IPs to a list and print it.\n3.Insert 4 "
    "entries to DNS_DICT and print it.\n4.Check if a string is PALINDROME.\n")
if choice == '1':
    num = (int(input("Enter a number: ")) ** 3)
    sleep(1)
    print("New number is: " + str(num))
    sleep(2)
elif choice == '2':
    list_ip = []
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    sleep(1)
    print(("New IP List is: " + str(list_ip)))
    sleep(2)
elif choice == '3':
    my_dict = {}
    my_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    my_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    my_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    my_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    sleep(1)
    print("New DNS DICTIONARY is: " + str(my_dict))
    sleep(2)
elif choice == '4':
    word = (input("Welcome to a PALINDROME check station!\nEnter a word: "))
    sleep(1)
    if word == word[::-1]:
        print("This is palindrome!")
    else:
        print("False")
        sleep(2)
else:
    sleep(1)
    print("please choose 1-4 only")

print("bay bay!!!")
