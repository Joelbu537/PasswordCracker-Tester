from random import *
import time
attempts = 0

userPass = input("\nEnter your password: ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

guessPass = ""

start = time.perf_counter()

while(guessPass != userPass):
    guessPass = ""
    for letter in range(len(userPass)):
        guessLetter = password[randint(0, 25)]
        attempts = attempts + 1
        guessPass = str(guessLetter) + str(guessPass)
    print(guessPass)

print("Your password is: ", guessPass)
end = time.perf_counter()
print(attempts , " attempts were needed to crack your password")
print(f"The process took {end - start:0.3f} seconds")
end = input("Press enter to exit")
