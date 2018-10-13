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

def football_cost():
    interceptions = interceptions()
    completion = completions()
    attempts = attempts()
    passing_yards = passing_yards()
    touchdown_passes = touchdown_passes()
    football_cost = (100 * [5 (completion / attempts – 0.3) + 0.25(passing_yards / attempts - 3) + 20 (touchdown_passes
                    / attempts) + 2.375 – (25 * interceptions / attempts)] / 6)
    return football_cost