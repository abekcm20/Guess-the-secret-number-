import random

print("Hello,What is your name")
name = input()
secretnumber = random.randint(1,20)
print("well"+name+"Im thinking a number between 1 to 20")

for guess in range(1,7):
    print("Enter the number")
    number = int(input())
    if number > secretnumber:
        print("Your guess is too high")
    elif number < secretnumber:
        print("Your guess is too low")
    else:
        break
if number == secretnumber:
    print("Good jon"+name+"You guessed my number")
else:
    print("the number was i thinking of was",secretnumber)
