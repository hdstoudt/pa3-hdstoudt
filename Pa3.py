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


def error_check_menu(menu_choice):
    if menu_choice == "football":
        return true
    elif menu_choice == "quidditch":
        return true
    elif menu_choice == "gymnast":
        return true
    else:
        return false


def int_check(int):
    if int_check == int
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

def quidditch(goals, snitch):
    goals = goals()
    int_check()
    if int_check == "true":
        quidditch_score = 10(goals)
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
    goals = int(input("Please enter your number of goals made."))
    return goals

def snitch():
    snitch = int(input("Did you catch the golden snitch? yes or no?"))
    return snitch

def gymnast(difficulty, execution1, execution2, execution3, execution4, execution5):

Function Name: gymnast
Parameters: difficulty, execution1, execution2, execution3, execution4, execution5
Return: Calculation of Parameters
Algorithm:
1. Ask user to input Parameter: "difficulty"
2. Call int_check to check for valid interger
3. If valid:
    a. Continue on
4. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
5. Ask user to input Parameter: "execution1"
6. Call int_check to check for valid interger
7. If valid:
    a. Continue on
8. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
9. Ask user to input Parameter: "execution2"
10. Call int_check to check for valid interger
11. If valid:
    a. Continue on
12. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
13. Ask user to input Parameter: "execution3"
14. Call int_check to check for valid interger
15. If valid:
    a. Continue on
16. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
17. Ask user to input Parameter: "execution4"
18. Call int_check to check for valid interger
19. If valid:
    a. Continue on
20. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
21. Ask user to input Parameter: "execution5"
22. Call int_check to check for valid interger
23. If valid:
    a. Continue on
24. Otherwise:
    a. Output: "Error! Invalid Answer."
    b. return 0
25. Check for min_value for calculation
26. Check for max-value for calculation
27. Calculate average_executions: "((execution1 + execution2 + execution3 + execution4 + execution5) - (min_value +
max_value)) / 5 "
28. Calculate_Gym = "(difficulty) + (average_executions)"
29. Return Calculation_Gym

def difficulty():
    difficulty = int(input("Please enter difficulty score."))
    return difficulty


def main():
    print("This program will calculate various sports statistics for the user, based on the user’s choice of sport.")
    menu_choice = menu()
    error_check_menu = error_check_menu()
    if error_check_menu == false
        print("Sorry your answer is invalid, please try again.")
        ## Go back to menu_choice ##
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