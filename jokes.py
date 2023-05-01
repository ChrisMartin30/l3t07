# Task: Create a random joke generator. 

# Import random library.
import random

# Create list of jokes.
jokes = ["What's brown and sticky?\nA stick.", 
    "Two goldfish are in a tank. One says to the other \"Who's driving this thing\"", 
    "I met the bloke who invented crosswords today. I can't remember his name, it's P something T something R.",
    "Two sharks are eating a clown. One say to the other\"Does this taste funny to you\".",
    "Why was six afraid of seven? \nBecause 7 8 9.",
    "Knock knock\nWho's there?\nLettuce\nLettuce who?\nLettuce in." ]

# Use random.choice() function, and print result.
print("Random Joke Generator\n")
print(random.choice(jokes))