import random

response = input("Do you want to roll the dice? (press y for yes and n for no):")

def dice(response):

    while response == "y":
        no = random.randint(1,6)

        if no == 1:
            print("[   ]\n[ 0 ]\n[   ]")

        if no == 2:
            print("[0  ]\n[   ]\n[  0]")     

        if no == 3:
            print("[0  ]\n[ 0 ]\n[  0]")         

        if no == 4:
            print("[0 0]\n[   ]\n[0 0]")  

        if no == 5:
            print("[0 0]\n[ 0 ]\n[0 0]")    

        if no == 6:
            print("[0 0]\n[0 0]\n[0 0]")  

        response = input("Do you want to roll the dice? (press y for yes and n for no):")

    while response == "n":
        quit()        
    
Diiice = dice(response)                