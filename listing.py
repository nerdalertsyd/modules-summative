#--------------------------------
#Library and Modules Summative
#Sydney Loerzel
#April 5, 2020
#Module 2, making a list of what you have and need to buy
#--------------------------------

#--------------Dicts--------------
paint = {}
to_buy = {}

#-----------Functions-------------

def paints():
    print("Lets look at the paint you have")
    print("You see a lot of blues, reds, greens, and white. Plus one black")
    paint["blues"] = "6"
    paint["reds"] = "5"
    paint["greens"] = "7"
    paint["white"] = "4"
    paint["black"] = "1"
    print(paint)
    print("You should probably get some other colours and more black")
    print("A few purple, pink, and yellow should be good")
    print("Just a couple bottles of each. So 8 in total with the black")
    to_buy["paint"] = "8"
    
def tape():
    print("You remember the tape you tossed aside earlier")
    print("That makes you think about buying painters tape")
    print("Best to buy a couple to have on hand")
    to_buy["tape"] = "2"
    
def canvas():
    print("To paint you need canvas'. You only have one")
    key = input("How many canvas' do you want to buy?")
    to_buy["canvas"] = key
    
def add_more():
    done = False
    while done == False:
        key = input("Would you like to add anything else? Type 'done' to exit.").lower()
        if key == "done":
            done = True
        elif key != "done":
            value = input("How many?")
            to_buy[key] = value