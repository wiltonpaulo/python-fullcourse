calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input_number))
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive value")
        else:
            print("you entered a negative number.")
    except ValueError:
        print("your input is not an integer number.")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey, enter a number of days and I'll convert it to hours!\n")  # input always returns a string
    validate_and_execute()
