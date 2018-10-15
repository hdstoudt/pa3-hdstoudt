def menu():
    print("What type of sport: football, quidditch, gymnast:")
    menu_choice = input("Please enter a valid sport type.")
    if menu_choice  == "football":
        menu_choice = football
    elif menu_choice == "quidditch":
        menu_choice = quidditch
    else:
        menu_choice = "gymnast"
    return menu_choice


def error_check_menu(menu_choice):
    if menu_choice.lower() == "football":
        return true
    elif menu_choice.lower() == "quidditch":
        return true
    elif menu_choice.lower() == "gymnast":
        return true
    else:
        return false


def int_check(int):
    int_check
    if int_check == int
        return true
    else:
        return false


def football(interceptions, completions, attempts, passing_yards, touchdown_passes):
    interception = interceptions()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    completion = completions()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    attempt = attempts()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    passing_yard = passing_yards()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    touchdown_passess = touchdown_passes()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
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


def quidditch(goals, snitch):
    goals = goals()
    int_check()
    if int_check == "true":
        quidditch_score = 10(goals)
    else:
        print("Error! Invalid Answer.")
        return 0
    snitch = snitch()
    if snitch == "yes":
        quidditch_score += 30
    elif snitch =="no":
        quidditch_score += 0
    else:
        print("Error! Invalid Answer.")
        return 0
    return quidditch_score

def goals():
    goals = int(input("Please enter your number of goals made."))
    return goals

def snitch():
    snitch = int(input("Did you catch the golden snitch? yes or no?"))
    return snitch


def gymnast(difficulty, execution1, execution2, execution3, execution4, execution5):
    difficulty = difficulty()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    execution1 = execution()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    execution2 = execution()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    execution3 = execution()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    execution4 = execution()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    execution5 = execution()
    if int_check() == true:
        continue
    else:
        print("Error! Invalid Answer.")
        return 0
    min_value = min_value()
    max_value = max-value()
    average_executions = ((execution1 + execution2 + execution3 + execution4 + exeuction5) - (min_value + max_value)) / 5
    calculate_gym = (difficulty) + (average_executions)
    return calculate_gym

def difficulty():
    difficulty = int(input("Please enter difficulty score."))
    return difficulty

def execution():
    execution = int(input("Please enter execution score."))
    return execution

def calculate_min(execuation1, execuation2, execuation3, execuation4, execuation5):
    min_value = execution1
    if execuation2 < min_value:
        min_value = execuation2
    if execuation3 < min_value:
        min_value = execuation3
    if execuation4 < min_value:
        min_value = execuation4
    if execuation5 < min_value:
        min_value = execuation5
    return min_value

def calculate_max(execuation1, execuation2, execuation3, execuation4, execuation5):
    max_value = execution1
    if execuation2 > max_value:
        max_value = execuation2
    if execuation3 > max_value:
        max_value = execuation3
    if execuation4 > max_value:
        max_value = execuation4
    if execuation5 > max_value:
        max_value = execuation5
    return max_value


def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu_choice = menu()
    error_check_menu = error_check_menu()
    if error_check_menu == false:
        print("Sorry your answer is invalid, please try again.")
        ## Go back to menu_choice ##
    if menu_choice == "football":
        football()
        print("Your football QB rating is", football_score)
        if football_score == 158.3:
            print("You are a perfect passer.")
        else:
            print("Sorry, you are not considered a perfect passer.")
    elif menu_choice == "quidditch":
        quidditch()
        print("Your score for Quidditch is", quidditch_score)
    else:
        gymnast()
        print("Your final score is", gym_score)
    print("Thank you for using this program")


# Run the Program
main()