"""
Example of a Fill in the Blank program, like the one from the lesson.
The user will enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story.
"""
def main():
    """
    Prompts the user for a color, an adjective, and a goal repeatedly,
    then fills them into a predefined story template and prints the result.
    The program will continue to ask for inputs until an empty string is
    entered for the 'color' prompt.
    """
def fill_in_the_blank_story_once():
    """
    Prompts the user for a color, an adjective, and a goal,
    then fills them into a predefined story template and prints the result.
    This function runs only once.
    """
    # Request the three strings from the user with exact prompts
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    # Construct the story using the provided template and user inputs
    story = f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}."

    # Print the complete story
    print(story)

# Call the function to run the program just once
fill_in_the_blank_story_once()



    

if __name__ == "__main__":
    main()