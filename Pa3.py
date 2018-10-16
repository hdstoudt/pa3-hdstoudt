# Programmers: Hannah Stoudt
# Course: CS151, Dr.Olsen
# Date: 10/17/18
# Pa Assignment: Number 3
# Problem Statement: "This program will calculate various sports statistics for the user, based on the user’s choice of
# sport."
# Data In: sport type, football(interceptions, completion, attempt, passing yards, touchdown passess), quidditch(goals,
#snitch), gymnast(difficulty score, execuation1 score, execuation2 score, execuation3 score, execuation4 score,
# execuation5 score).
# Data Out: Hogwarts House (Gryffindor, Hufflepuff, Ravenclaw, and Slytherin)
# Other files needed: None
# Credits: Programmers, the template for comments given by Dr. Olsen, and Harry Potter books for reference.


def menu():
    menu_choice = input("Please enter a valid sport type: football, quidditch, or gymnast.")
    return menu_choice.lower()


def int_check():
    value = input("Please enter an integer.")
    while not value.isdigit():
        print("Error! Not an integer!")
        value = input("Please enter an integer.")
    value = int(value)
    return value


def football():
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


def gymnast(min_value, max_value):
    difficulty = float(input("Please enter difficulty score."))
    execution1 = float(input("Please enter execution1 score."))
    execution2 = float(input("Please enter execution2 score."))
    execution3 = float(input("Please enter execution3 score."))
    execution4 = float(input("Please enter execution4 score."))
    execuation5 = float(input("Please enter execution5 score."))
    min_value = min_value()
    max_value = max_value()
    average_executions = ((execution1 + execution2 + execution3 + execution4 + execuation5) - (min_value + max_value)) / 3
    calculate_gym = (difficulty) + (average_executions)
    return calculate_gym

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


def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu_choice = menu()
    if menu_choice.lower() == "football":
        football = football()
        print("Your football QB rating is", football_score)
        if football_score == 158.3:
            print("You are a perfect passer.")
        else:
            print("Sorry, you are not considered a perfect passer.")
    elif menu_choice.lower() == "quidditch":
        quidditch = quidditch()
        print("Your score for Quidditch is", quidditch_score)
    else:
        gymnast = gymnast()
        print("Your final score is", gym_score)
    print("Thank you for using this program")

# Run the Program
main()