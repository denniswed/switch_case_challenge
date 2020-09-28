from classynumbers import Switcher
"""using if/elif to emulate switch/case - also adding in other methods I am finding on the all knowing googles to help me"""

def _error_messages(first, second, third):
    """Function for error messages"""
    # If first is true, then the input is a digit, but not a 1, 2 or 3
    if first:
        print(f"\nYou are not following directions. Pick a number from 1, 2 or 3.")
    
    # Input selects a non-digit
    if second:
        print(f"\nThis is a numbers game, pick a NUMBER between one, two or three.")

    #Giving a copout from the game. 
    if third:
        print(f"\nIf you are getting tired, just hit 'q' and it will all end.")

def _success_messages(the_selection):
    """Function for success messages, but there really is only one winner"""
    # using a "switcher" for this just to demonstrate, in normal circumstances I would probably have this has a main capture of the input
    the_switcher_options = {
        1: "one",
        2: "two",
        3: "three"
    }
    return the_switcher_options.get(the_selection, "what what")


active = True
while active:
    user_choice = input("\nPlease select a number 1, 2 or 3: ")
    thenumber = Switcher()
    
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            print(f"\nNice choice: {_success_messages(user_choice)}")
            print(thenumber.indirect(1))
        elif user_choice == 2:
            print(f"\nWell done: {_success_messages(user_choice)}")
            print(thenumber.indirect(1))
        elif user_choice == 3:
            print(f"\nSpectaculor!: {_success_messages(user_choice)}")
            print(thenumber.indirect(1))
        else:
            _error_messages(True, False, True)
    else:
        if user_choice == 'q':
            active = False
        else:
            _error_messages(False, True, True)


