import random

def main():
    """
    Prompts the user for the number of sides on a dice,
    simulates a roll, and prints the outcome with the exact required prefix.
    """
    # Prompt the user for the number of sides on the dice (exact format as previously corrected)
    sides_str = input("How many sides does your dice have? ")

    # Convert the input to an integer
    num_sides = int(sides_str)

    # Simulate rolling the dice from 1 up to the number of sides
    roll_outcome = random.randint(1, num_sides)

    # Print the outcome of the roll with the exact required prefix "Your roll is "
    print(f"Your roll is {roll_outcome}") # <--- This line is changed



if __name__ == '__main__':
    main()