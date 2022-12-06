import time
import sys
import random


# For formatted printing
class colors:
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'


# Read in list of sentences from sentences.txt file
sentences = set()
with open("sentences.txt",'r') as sentences_file:
    sentences = set(sentences_file.read().splitlines())

# Keep track of statistics across different sentences
total_words = 0
total_minutes = 0
total_correct_characters = 0
total_characters = 0

def start_typing_test():
    # Access global variables
    global total_words, total_minutes, total_correct_characters, total_characters

    # Print divider between sentence typing tests
    print('─' * 50 + "\n")

        # Randomly select a sentence and remove it from the sentence bank
    sentence = random.choice(list(sentences))
    sentences.remove(sentence)

    # Print the sentence for the user to type
    print(colors.HEADER + "Prompt: " + colors.NORMAL + sentence)

    # Start a timer to track how long it takes for the user to type the sentence
    start_time = time.time()

    # Get the user's input and store it in a variable
    user_input = input(colors.HEADER + "Go: " + colors.NORMAL)

    # End the timer
    end_time = time.time()
    
    # Calculate the time it took for the user to type the sentence
    time_elapsed = end_time - start_time
    minutes_elapsed = time_elapsed / 60
    total_minutes += minutes_elapsed

    # Number of characters correctly typed by the user
    characters_correct = 0

    # Number of characters in the sentence
    sentence_characters = len(sentence)
    total_characters += sentence_characters

    # Compare the user's input to the original sentence
    for i in range(len(sentence)):
        if i < len(user_input) and user_input[i] == sentence[i]:
            # If character is correct, print in green and increment the # of characters correctly typed
            print(colors.GREEN + sentence[i], end='')
            characters_correct += 1
        else:
            # If character is incorrect, print in red
            print(colors.RED + sentence[i], end='')

    total_correct_characters += characters_correct

    # Calculate the number of words inputted
    num_words = len(user_input.split())
    total_words += num_words

    # Reset color
    print(colors.NORMAL + "\n")

    # Print statistics
    print(colors.BOLD + "Accuracy: " + colors.NORMAL + '%.2f' % (100 * characters_correct / sentence_characters) + "%")
    print(colors.BOLD + "Total Time: " + colors.NORMAL + '%.2f' % time_elapsed + "s")
    print(colors.BOLD + "Words Per Minute: " + colors.NORMAL + '%.2f' % (num_words / minutes_elapsed) + "\n")

    while True:
        user_input = input("Keep playing? (y/n) ")
        if user_input.lower() == "y":
            break
        elif user_input.lower() == "n":
            # If user is exiting, print their overall stats
            print("\n" + colors.BOLD + colors.GREEN + "OVERALL STATS:" + colors.NORMAL)
            print(colors.BOLD + "Accuracy: " + colors.NORMAL + '%.2f' % (100 * total_correct_characters / total_characters) + "%")
            print(colors.BOLD + "Words Per Minute: " + colors.NORMAL + '%.2f' % (total_words / total_minutes))
            print("\n" + colors.BOLD + "Thanks for playing!")
            sys.exit(0)
        else:
            print("Sorry, I didn't understand that.")
            continue


def typing_masterclass():
    print(colors.BOLD + colors.GREEN + "Welcome to Typing Masterclass!" + colors.NORMAL)
    input(colors.BOLD + "Press any key to continue...\n" + colors.NORMAL)

    while len(sentences) > 0:
        start_typing_test()

    print("\n" + colors.RED + "Uh-oh, ran out of sentences. Goodbye!" + colors.NORMAL)

if __name__ == "__main__":
    typing_masterclass()
