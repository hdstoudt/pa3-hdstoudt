def menu():
    print("What type of sport: football, quidditch, gymnast:")
    sport = input("Please enter a valid sport type.")
    return menu_choice


def error_check_menu():
    if menu_choice = "football":
        return true
    elif menu_choice = "quidditch":
        return true
    elif menu_choice = "gymnast":
        return true
    else:
        return false


def football():


def interceptions():
    interceptions = int(input("Please enter your number of interceptions."))
    return interceptions

# Function Name: football
# Parameters: interceptions, completions, attempts, passing_yards, touchdown_passes
# Return: Calculation of Parameters
# Algorithm:
# 1. Ask user to input Parameter: "interceptions"
# 2. Ask user to input Parameter: "completions"
# 3. Ask user to input Parameter: "attempts"
# 4. Ask user to input Parameter: "passing_yards"
# 5. Ask user to input Parameter: "touchdown_passes"
# 6. Calculation_QB: "100 * [5(completions/attempts – 0.3) + 0.25(passing_yards/attempts-3) + 20(touchdown_passes/attempts)
# + 2.375 – (25 * interceptions/attempts)]/6"
# 7. Return Calculation_QB