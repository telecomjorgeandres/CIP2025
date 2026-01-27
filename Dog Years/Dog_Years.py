# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    """
    Prompts the user for an age in human years and converts it to dog years,
    using a conversion factor of 7.18 dog years per human year.
    Reports the result using Python's default float-to-string conversion
    to dynamically handle decimal places as per the expected output formats.
    """
    # Define the conversion factor
    DOG_YEARS_PER_HUMAN_YEAR = 7.18

    # Get input from the user for age in human years
    # The prompt must be exactly "Enter an age in calendar years: "
    human_years_str = input("Enter an age in calendar years: ")

    # Convert the input string to a float
    human_years = float(human_years_str)

    # Calculate the age in dog years
    dog_years = human_years * DOG_YEARS_PER_HUMAN_YEAR

    # Report the result to the user.
    # Using str(dog_years) naturally handles removing trailing zeros
    # when they are not significant (e.g., 71.8 instead of 71.80).
    print(f"That's {str(dog_years)} in dog years!")



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()