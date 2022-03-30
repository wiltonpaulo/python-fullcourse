calculation_to_units = 24  # global vars
name_of_unit = "hours"  # global vars


def days_to_units(num_of_days, custom_message):
    # num_of_days and custom_message  are local vars inside function
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


def scope_check(num_of_days):
    # num_of_days is another local vars and is different than the one used in function days_to_units
    my_var = "var inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)


scope_check(20)
