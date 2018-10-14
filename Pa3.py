def menu():
    print("What type of sport: football, quidditch, gymnast:")
    sport = input("Please enter a valid sport type.")
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



#1. Tell the user the purpose of the program: "This program will calculate various sports statistics for the user, based
#on the user’s choice of sport."
#2. Call menu
#3. Call error_check_menu
#4. If error_check_menu is equal to "false":
    #a. Output error message: "Sorry your answer is invalid, please try again."
   # b. Go back to Step 2 #In main function
#5. If menu_choice is equal to "football":
    #a. Call football
    #b. Output: ("Your football QB rating is", Calculation_QB)
    #c. If Calculation_QB is equal to 158.3
       # i.Output: "You are a perfect passer."
    #d. Otherwise:
     #   a. Output: "Sorry, you are not considered a perfect passer."
#6. Otherwise/If menu_choice is equal to "quidditch":
  #  a. Call quidditch
 #   b. Output: ("Your score for Quidditch is", Calculation_Quid)
#7. Otherwise:
  #  a. Call gymnast
  #  b. Output: ("Your final score is", Calculation_Gym)
#8. Output: "Thank you for using this program."