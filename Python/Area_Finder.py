import os
os.system('cls' if os.name == 'nt' else 'clear')

print("____Area Finder____".center(110))

print("1.Trapezium\n2.Square\n3.Hexagon\n4.Rectangle\n5.Paralllelogram\n")

Ask_user = input("Enter Your Choice:- ")

def Choice1():
    if Ask_user == 1 or "Trapezium".lower():
        class Area1:

            def __init__(self, A, B, Height):
                self.A = A
                self.B = B
                self.Height = Height

            @property
            def clac_area1(self):
                print("Area of Trapezium =",(1/2 * (self.A + self. B) * self.Height))

        Trapezium = Area1(float(input("\nEnter Your A's Base:- ")),float(input("Enter Your B's Base:- ")),float(input("Enter Your Height:- ")))
        
        Trapezium.clac_area1

Choice1()

def Choice2():
    if Ask_user == 2 or "Square".lower() :
        class Area2:

            def __init__(self, side):
                self.side =side

            @property
            def clac_area2(self):
                print("Area of Square =", 4 * self.side)

        Square = Area2(float(input("\nEnter Your Side:- ")))

        Square.clac_area2

Choice2()

def Choice3():
    if Ask_user == 3 or "Hexagon".lower():
        class Area3:

            def __init__(self, side2):
                self.side2 = side2

            @property
            def clac_area3(self):
                print(6 * 1.732/4 ** float(self.side2))

        Hexagon = Area3(input("\nEnter Your Side:- "))

        Hexagon.clac_area3

Choice3()

def Choice4():
    if Ask_user == 4 or "Rectangle".lower():
        class Area4:
            
            def __init__(self, length, breadth, height):
                self.length = length
                self.breadth = breadth
                self.height = height

            @property
            def clac_area4(self):
                print("Area of Rectangle =",self.length * self.breadth * self.height)

        Rectangle = Area4(float(input("\nEnter Your Length:- ")),float(input("Enter Your Breadth:- ")),float(input("Enter Your Height:- ")))

        Rectangle.clac_area4()


Choice4()

def Choice5():
    if Ask_user == 5 or "Parllelogram".lower():
        class Area5:

            def __init__(self, base, height):
                self.base = base
                self.height = height

            @property
            def clac_area5(self):
                print("Area of Parllelogram =",self.base * self.height)

        Parallelogram = Area5(float(input("\nEnter Your Base:- ")), float(input("Enter Your Height:- ")))

        Parallelogram.clac_area5

Choice5()

