"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""
def main():
    """
    Takes two integer inputs from the user, calculates their product,
    and prints the result. Follows specific prompt and output formats.
    """
    # Print the introductory message
    print("This program multiplies two numbers.")

    # 1. Prompt the user to enter the first number and 2. Read and convert to integer
    num1_str = input("Enter first number: ")
    num1 = int(num1_str) # Convert the string input to an integer

    # 3. Prompt the user to enter the second number and 4. Read and convert to integer
    num2_str = input("Enter second number: ")
    num2 = int(num2_str) # Convert the string input to an integer

    # 5. Calculate the value of multiplying the two numbers
    product = num1 * num2

    # 6. Print the value
    print(product)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()