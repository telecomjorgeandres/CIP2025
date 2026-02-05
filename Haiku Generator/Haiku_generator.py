from ai import call_gpt # This function is used to interact with an AI model

def main():
    """
    Prompts the user for their name and a topic, then generates a haiku
    on that topic, incorporating the name, using an AI model.
    """
    # Get the user's name
    user_name = input("Enter your name: ")
    # Get the topic for the haiku
    haiku_topic = input("Enter a topic: ")

    # print("Creating your haiku...") # Removed this line for a simpler, more direct beginner style

    # Construct the prompt for the AI using basic string concatenation
    # A beginner might use this approach rather than f-strings.
    ai_prompt = "Please write a haiku (5-7-5 syllables) about '" + haiku_topic + "'.\n"
    ai_prompt = ai_prompt + "The haiku should subtly include the name '" + user_name + "' if possible,\n"
    ai_prompt = ai_prompt + "or simply be inspired by the sentiment of someone named " + user_name + "\n"
    ai_prompt = ai_prompt + "contemplating the topic.\n"
    ai_prompt = ai_prompt + "Ensure it strictly follows the 5-7-5 syllable structure for three lines.\n"
    ai_prompt = ai_prompt + "Do not include any introductory or concluding remarks, just the haiku lines."

    # Call the AI model to generate the haiku
    # The 'call_gpt' function sends the prompt to the AI and returns its response.
    generated_haiku = call_gpt(ai_prompt)

    # Print the generated haiku
    print(generated_haiku)

if __name__ == "__main__":
    main()