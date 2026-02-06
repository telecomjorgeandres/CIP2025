def main():
    """
    Asks the user for a number, then repeatedly doubles it and prints only the
    doubled result as an integer, until the value is 100 or greater.
    """
    while True:
        try:
            initial_number_str = input("Enter a number: ")
            initial_number = int(initial_number_str) # Use int for integer input
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    curr_value = initial_number

    if curr_value >= 100:
        # If the initial number is already 100 or greater, no output needed per example
        pass
    else:
        while curr_value < 100:
            curr_value = curr_value * 2
            print(curr_value) # Print only the doubled value
            if curr_value >= 100: # Break after printing if it's 100 or more
                break

if __name__ == '__main__':
    main()