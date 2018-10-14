def menu():
    print("What type of sport: football, quidditch, gymnast:")
    sport = str(input("Please enter a valid sport type.")
    return menu_choice


def error_check_menu():
    if menu_choice == "football":
        return true
    elif menu_choice == "quidditch":
        return true
    elif menu_choice == "gymnast":
        return true
    else:
        return false

def football(interceptions, completions, attempts, passing_yards, touchdown_passes):
    interception = interceptions()
    completion = completions()
    attempt = attempts()
    passing_yard = passing_yards()
    touchdown_passess = touchdown_passes()
    football_score = (100 * [5 (completion / attempt - 0.3) + 0.25(passing_yard / attempt - 3) + 20 (touchdown_passess
                    / attempt) + 2.375 - (25 * interception / attempt)] / 6)
    return football_score

def interceptions():
    interceptions = int(input("Please enter your number of interceptions made."))
    return interceptions

def completions():
    completions = int(input("Please enter your number of completions made."))
    return completions

def attempts():
    attempts = int(input("Please enter your number of attempts made."))
    return attempts

def passing_yards():
    passing_yards = int(input("Please enter your number of passing yards made."))
    return passing_yards

def touchdown_passes():
    touchdown_passes = int(input("Please enter your number of touchdown passes made."))
    return touchdown_passes


def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu = menu()
    error_check_menu = error_check_menu()
    if error_check_menu == false
        print("Sorry your answer is invalid, please try again.")
        ## go back to menu step 2
    if menu_choice == "football"
        football()
        print("Your football QB rating is", football_score)
        if football_score == 158.3
            print("You are a perfect passer.")
        else:
            print("Sorry, you are not considered a perfect passer.")
    elif menu_choice == "quidditch"
        quidditch()
        print("Your score for Quidditch is", quidditch_score)
    else:
        gymnast()
        print("Your final score is", gym_score)
    print("Thank you for using this program")

