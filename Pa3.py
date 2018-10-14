def menu():
    print("What type of sport: football, quidditch, gymnast:")
    menu_choice = input("Please enter a valid sport type.")
    if menu_choice.lower() == "football":
        menu_choice = football
    elif menu_choice.lower() == "quidditch":
        menu_choice = quidditch
    else:
        menu_choice.lower() = "gymnast"
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
    int_check()
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

def quidditch():
    goal = goals()
    int_check()
    if int_check == "true":
        quidditch_score = 10(goal)
    else:
        print("Error! Invalid Answer.")
        return 0
    snitch = snitch()
    if snitch == "yes"
        quidditch_score += 30
    elif snitch =="no":
        quidditch_score += 0
    else:
        print("Error! Invalid Answer.")
        return 0
    return quidditch_score

def goals():
    goal = int(input("Please enter your number of goals made."))
    return goal

def snitch():
    snitch = int(input("Did you catch the golden snitch? yes or no?"))
    return snitch


def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu_choice = menu()
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


# Run the Program
main()