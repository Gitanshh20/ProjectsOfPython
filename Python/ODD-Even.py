# Even And ODD Identifier...

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Odd and Even Finder..")

num = int(input("\nEnter Your Number: "))

def Even_Odd():
    if num % 2 == 0:
        print("\nYour Number is Even.")

    else:
        print("\nYour Number is ODD.") 

Even_Odd()