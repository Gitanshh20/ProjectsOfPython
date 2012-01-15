import os
os.system('cls' if os.name == 'nt' else 'clr')

print("Quiz Game!!")

Ask_user = input("Are You Ready to Play game Yes/No: ")

def First_Que():
    if Ask_user == "Yes":
        Que1 = input("\nQue.1 What is The Captial of India?\nAns: ")
        if Que1 == "Delhi":
            print("Correct!, The Capital of India is Delhi")
        else:
            print("Wrong Answer..")

First_Que()

def Second_Que():
    if Ask_user == "Yes":
        Que2 = input("\nQue.2 Who is the National Animal of India?\nAns: ")
        if Que2 == "Tiger":
            print("Correct!, The National Animal of India was Tiger")
        else:
            print("Worng Answer...")

Second_Que()

def Third_Que():
    if Ask_user == "Yes":
        Que3 = input("\nQue.3 What is the capital of Australia?\nAns: ")
        if Que3 == "Canberra":
            print("Correct!, The Capital of Australia is Canberra")
        else:
            print("Worng Answer...")

Third_Que()

def Fourth_Que():
    if Ask_user == "Yes":
        Que4 = input("\nQue.4 What gas do plants absorb from the atmosphere during Photosynthesis?\nAns: ")
        if Que4 == "Carbon dioxide":
            print("Correct!, Gas absorbed during Photosynthesis → Carbon dioxide (CO₂)")
        else:
            print("Worng Answer...")

Fourth_Que()

def Fifth_Que():
    if Ask_user == "Yes":
        Que5 = input("\nQue.5 Which planet is known as the “Red Planet”?\nAns: ")
        if Que5 == "Mars":
            print("Correct!, “Red Planet” → Mars")
        else:
            print("Worng Answer...")

Fifth_Que()

def Sixth_Que():
    if Ask_user == "Yes":
        Que6 = input("\nQue.6 What is 12 x 8?\nAns: ")
        if Que6 == "96":
            print("Correct!, 12 x 8 is 96.")
        else:
            print("Worng Answer...")

Sixth_Que()