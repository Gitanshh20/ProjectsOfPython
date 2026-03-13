import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Simple Interest Calculator...\n")

class SI_Clac:

    def __init__(self, Principal, Rate, Time):
        self.Principal = Principal
        self.Rate = Rate
        self.Time = Time

    @property
    def Answer(self):
        print("\nYour SI =₹",(self.Principal * self.Rate * self.Time / 100))

    @property
    def Total_Amount(self):
        print("Total Amount is:₹", self.Principal+(self.Principal * self.Rate * self.Time / 100))


SI = SI_Clac(float(input("Enter Your Principal: ")),float(input("Enter Your Rate: ")),float(input("Enter Your Time: ")))

SI.Answer
SI.Total_Amount