# Programmers: Hannah Stoudt
# Course: CS151, Dr.Olsen
# Date: 10/17/18
# Pa Assignment: Number 3
# Problem Statement: "This program will calculate various sports statistics for the user, based on the user’s choice of
# sport."
# Data In: sport type, football(interceptions, completion, attempt, passing yards, touchdown passess), quidditch(goals,
# snitch), gymnast(difficulty score, execuation1 score, execuation2 score, execuation3 score, execuation4 score,
# execuation5 score).
# Data Out: Score for all sports, and for football whether or not you are a perfect passer
# Other files needed: None
# Credits: Ti-84 for test cases, the template for comments given by Dr. Olsen, and sports websites for reference.


# Purpose: menu, this function allows the user to input what type of sport they want to calculate
# Parameter: None
# Return: menu_choice.lower()
def menu():
    menu_choice = input("Please enter a valid sport type: football, quidditch, or gymnast.")
    return menu_choice.lower()


# Purpose: int_check, this function checks to make sure that what the user inputs is an int value
# Parameter: value
# Return: value
def int_check(value):
    while not value.isdigit():
        print("Error! Not an integer!")
        value = input("Please enter an integer.")
    value = int(value)
    return value

# Purpose: football, this is the function for football if they pick it from menu, then the user inputs the following
# parameters
# Parameter: None
# Return: football_score
def football():
    interception = input("Please enter your number of interceptions made.")
    int_check(interception)
    interception = int_check(interception)
    completion = input("Please enter your number of completions made.")
    int_check(completion)
    completion = int_check(completion)
    attempt = input("Please enter your number of attempts made.")
    int_check(attempt)
    attempt = int_check(attempt)
    passing_yard = input("Please enter your number of passing yards made.")
    int_check(passing_yard)
    passing_yard = int_check(passing_yard)
    touchdown_passess = input("Please enter your number of touchdown passes made.")
    int_check(touchdown_passess)
    touchdown_passess = int_check(touchdown_passess)
    football_score = 100 * ((5 * (completion / attempt - 0.3)) + (0.25 * (passing_yard / attempt - 3)) +
                    (20 * (touchdown_passess/attempt)) + 2.375 - (25 * interception / attempt))/ 6
    return football_score

# Purpose: quidditch, this is the function for quidditch if they pick it from menu, then the user inputs the following
# parameters
# Parameter: None
# Return: quidditch_score
def quidditch():
    goals = input("Please enter your number of goals made.")
    int_check(goals)
    goals = int_check(goals)
    quidditch_score = 10 * (goals)
    snitch = input("Did you catch the golden snitch? yes or no?")
    if snitch == "yes":
        quidditch_score += 30
    elif snitch =="no":
        quidditch_score += 0
    else:
        print("Error! Invalid Answer.")
        snitch = input("Did you catch the golden snitch? yes or no?")
    return quidditch_score

# Purpose: gymnast, this is the function for gymnast if they pick it from menu, then the user inputs the following
# parameters
# Parameter: None
# Return: gymnast_score
def gymnast():
    difficulty = float(input("Please enter difficulty score."))
    execuation1 = float(input("Please enter execuation1 score."))
    execuation2 = float(input("Please enter execuation2 score."))
    execuation3 = float(input("Please enter execuation3 score."))
    execuation4 = float(input("Please enter execuation4 score."))
    execuation5 = float(input("Please enter execuation5 score."))
    minimum = calculate_min(execuation1, execuation2, execuation3, execuation4, execuation5)
    maximum = calculate_max(execuation1, execuation2, execuation3, execuation4, execuation5)
    average_executions = ((execuation1 + execuation2 + execuation3 + execuation4 + execuation5) - (minimum + maximum)) / 3
    gymnast_score = (difficulty) + (average_executions)
    return gymnast_score

# Purpose: calculate_min, this function is for finding the min value so it can be used for the gymnast_score
# Parameter: execuation1, execuation2, execuation3, execuation4, execuation5
# Return: min_value
def calculate_min(execuation1, execuation2, execuation3, execuation4, execuation5):
    min_value = execuation1
    if execuation2 < min_value:
        min_value = execuation2
    if execuation3 < min_value:
        min_value = execuation3
    if execuation4 < min_value:
        min_value = execuation4
    if execuation5 < min_value:
        min_value = execuation5
    return min_value

# Purpose: calculate_max, this function is for finding the max value so it can be used for the gymnast_score
# Parameter: execuation1, execuation2, execuation3, execuation4, execuation5
# Return: max_value
def calculate_max(execuation1, execuation2, execuation3, execuation4, execuation5):
    max_value = execuation1
    if execuation2 > max_value:
        max_value = execuation2
    if execuation3 > max_value:
        max_value = execuation3
    if execuation4 > max_value:
        max_value = execuation4
    if execuation5 > max_value:
        max_value = execuation5
    return max_value


# Purpose: main, this function basically leads the program through all of the steps
# Parameter: None
# Return: none
def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu_choice = menu()
    if menu_choice.lower() == "football":
        football_QB = football()
        print("Your football QB rating is", football_QB)
        if football_QB >= 158.3:
            print("You are a perfect passer.")
        else:
            print("Sorry, you are not considered a perfect passer.")
    elif menu_choice.lower() == "quidditch":
        quidditch_q = quidditch()
        print("Your score for Quidditch is", quidditch_q)
    else:
        gymnast_gym = gymnast()
        print("Your final score is", gymnast_gym)
    print("Thank you for using this program")

# Run the Program
main()