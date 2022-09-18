'''
How to reprisent a number as a segments...
we got a number 4567
our outcome should be:
alafim=4
meot=5
asarot=6
ahedot=7
'''
num=4567
print("Our number is " + str(num) + "\nLets subtract it by segments...")
alafim=num//1000
# print("alafim=" + str(alafim))
meot=num%1000//100
# print("meot=" + str(meot))
asarot=num%100//10
# print("asarot=" + str(asarot))
ahadot=num%10
# print("ahadot=" + str(ahadot))

print(str(alafim) + " alafim" + "\n" + str(meot) + " meot" + "\n" + str(asarot) + " asarot" + "\n" + str(ahadot) + " ahadot")


