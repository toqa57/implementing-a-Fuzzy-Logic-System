def get_valid_input(prompt, min_value, max_value, value_type):
    while True:
        try:
            value = value_type(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
