#--------------------------------
#Library and Modules Summative
#Sydney Loerzel
#April 5, 2020
#Module 3, buying the stuff
#--------------------------------

import listing

def items():
    print("Now you are at the store buying everything")
    print("You remember everything that you need to get")
    print("But you already forget how much stuff you need to get")
    for values in listing.to_buy:
        buy = listing.to_buy[values]
        print(buy)
        
def outro():
    print("Eventually you get everything and it is time to go home")
    print("Now time to put all the new things away....")