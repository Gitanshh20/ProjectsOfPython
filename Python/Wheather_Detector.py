import os
os.system ('cls' if os.name == 'nt' else 'clr')

print("..Wheather Detector..\n".center(160))

Contine_or_Not = input("If You Want to Know about Wheather Type Yes or No for denied: ")

if (Contine_or_Not == "Yes" or "yes"):
    Ask_Celsius = int(input("\nEnter Your Temperature in °C: "))

    def Check_Wheather():
        if Ask_Celsius >= 30 and 45<= Ask_Celsius:
            print("\nIn Your Area Wheather was Sunny/Hot.\n")
            print("Description:-")
            print("Very warm or hot weather with strong sunlight. Common in summer.")

        if Ask_Celsius >= 20 and 30<= Ask_Celsius:
            print("\nIn Your Area Wheather was Mild/Pleasent.\n")
            print("Description:-")
            print("Comfortable weather, not too hot or cold.")

        if Ask_Celsius >= 0 and 15<= Ask_Celsius:
            print("\nIn Your Area Wheather was Cold.\n")
            print("Description:-")
            print("Cool to very cold weather. Below 0°C water can freeze.")
        
        if Ask_Celsius >= 22 and 32<= Ask_Celsius:
            print("\nIn Your Area Wheather was Monsoon/Rainy.\n")
            print("Description:-")
            print("Warm but humid with frequent rain and clouds.")

    Check_Wheather()
        
else:
    print("Ok, We can Tomorrow if You want..")

Ask_Table_of_Celsius = input("\nIf You Want The Simple Understanding of Celsius so Type Yes or No for Denied: ")

if Ask_Table_of_Celsius == "Yes" or "yes":
    print('''
Simple understanding

0°C – 10°C → Very cold 🧊

10°C – 20°C → Cool 🌬️

20°C – 30°C → Pleasant 🙂

30°C – 40°C+ → Hot ☀️
''')

else:
    print("Ok, That's Your Choice.")