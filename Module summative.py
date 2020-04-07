#--------------------------------
#Library and Modules Summative
#Sydney Loerzel
#April 5, 2020
#Main code
#--------------------------------

import cleaning
import listing
import shopping

def start():
    cleaning.intro()
    cleaning.art_pile()
    cleaning.other_pile()
    
def make_list():
    listing.paints()
    listing.tape()
    listing.canvas()
    listing.add_more()
    
def purchase():
    shopping.items()
    shopping.outro()

def main():
    start()
    make_list()
    purchase()
    
main()