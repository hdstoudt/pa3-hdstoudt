def menu():
    print("What type of sport: football, quidditch, gymnast:")
    menu_choice = input("Please enter a valid sport type.")
    return menu_choice.lower()


def int_check(int):
    int_check
    if int_check == int
        return true
    else:
        print("Error, invalid entry!")
        return 0


def football(interceptions, completions, attempts, passing_yards, touchdown_passes):
    interception = int(input("Please enter your number of interceptions made."))
    int_check()
    completion= int(input("Please enter your number of completions made."))
    int_check()
    attempt = int(input("Please enter your number of attempts made."))
    int_check()
    passing_yard = int(input("Please enter your number of passing yards made."))
    int_check()
    touchdown_passess = int(input("Please enter your number of touchdown passes made."))
    int_check()
    football_score = (100 * [5 (completion / attempt - 0.3) + 0.25(passing_yard / attempt - 3) + 20 (touchdown_passess
                    / attempt) + 2.375 - (25 * interception / attempt)] / 6)
    return football_score


def quidditch(goals, snitch):
    goals = int(input("Please enter your number of goals made."))
    int_check()
    quidditch_score = 10(goals)
    snitch = int(input("Did you catch the golden snitch? yes or no?"))
    int_check()
    if snitch == "yes":
        quidditch_score += 30
    elif snitch =="no":
        quidditch_score += 0
    else:
        print("Error! Invalid Answer.")
        snitch = int(input("Did you catch the golden snitch? yes or no?"))
    return quidditch_score


def gymnast(difficulty, execution1, execution2, execution3, execution4, execution5):
    difficulty = float(input("Please enter difficulty score."))
    int_check()
    execution1 = execution()
    int_check()
    execution2 = execution()
    int_check()
    execution3 = execution()
    int_check()
    execution4 = execution()
    int_check()
    execution5 = execution()
    int_check()
    min_value = min_value()
    max_value = max-value()
    average_executions = ((execution1 + execution2 + execution3 + execution4 + exeuction5) - (min_value + max_value)) / 5
    calculate_gym = (difficulty) + (average_executions)
    return calculate_gym

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
    return main

# Run the Program
main()