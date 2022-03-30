calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


user_input = input(
    "Hey, enter a number of days and I'll convert it to hours!\n")  # input always returns a string

calculated_value = days_to_units(int(user_input))
print(calculated_value)
