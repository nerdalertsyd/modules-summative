#--------------------------------
#Library and Modules Summative
#Sydney Loerzel
#April 5, 2020
#Module 1, The intro and cleaning the room
#--------------------------------

#-------------Lists---------------

art_supplies = ["paint", "brushes", "paper", "canvas", "pencil", "tape"]
others = ["poster", "model cars", "books", "garbage", "bag"]

#-----------Functions-------------

def intro():
    print("You have a spare art room that has become a mess")
    print("You know you are going shopping later and can buy more supplies")
    print("BUT first. You need to clean the room and see what all you have in there")
    print("You start by putting everything into 2 piles. Supplies and other stuff")
    print("After a going through everything you look at what all is in each pile")
    print(art_supplies)
    print(others)
    print("You notice a random deck of cards and toss it into the other pile")
    others.append("cards")
    
def art_pile():
    print("You decide to deal with the art supplies pile first")
    print("You begin to put everything up onto the empty shelf")
    print("You notice the tape is the wrong kind of tape")
    print("It belongs not in your art room but in a junk drawer")
    print("You take it out of your room")
    art_supplies.remove("tape")
    print("Once the art pile has been organized onto shelves you move onto the others")
    print("First you make a note of how many different art things you have")
    print(len(art_supplies))

def other_pile():
    print("This pile doesn't look fun at all...")
    print("Lets use a bag and get rid of all the garbage")
    others.remove("garbage")
    others.remove("bag")
    print("lets look at how many other things you have to deal with")
    num = len(others)
    print(num)
    print("That's", num, "too many")
    print("You decide to worry about that pile later and push it to the side")