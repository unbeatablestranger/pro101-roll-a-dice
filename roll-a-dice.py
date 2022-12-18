import random

response = input("Do you want to roll the dice? (press y for yes and n for no):")

def dice(response):

    while response == "y":
        no = random.randint(1,6)

        if no == 1:
            print("[   ]\n[ 0 ]\n[   ]")

        elif no == 2:
            print("[0  ]\n[   ]\n[  0]")     

        elif no == 3:
            print("[0  ]\n[ 0 ]\n[  0]")         

        elif no == 4:
            print("[0 0]\n[   ]\n[0 0]")  

        elif no == 5:
            print("[0 0]\n[ 0 ]\n[0 0]")    

        else:
            print("[0 0]\n[0 0]\n[0 0]")  

        response = input("Do you want to roll the dice? (press y for yes and n for no):")

    while response == "n":
        quit()        
    
Diiice = dice(response)                