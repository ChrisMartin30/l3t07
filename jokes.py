# Task: Create a random joke generator. 

# Import random library.
import random

# Create list of jokes.
jokes = ["What's brown and sticky?\nA stick.", 
    "Two goldfish are in a tank. One says to the other \"Who's driving this thing\"", 
    "I met the bloke who invented crosswords today. I can't remember his name, it's P something T something R.",
    "Two sharks are eating a clown. One say to the other\"Does this taste funny to you\".",
    "Why was six afraid of seven? \nBecause 7 8 9.",
    "Knock knock\nWho's there?\nLettuce\nLettuce who?\nLettuce in.",
    "What's the best thing about Switzerland? \nI don't know, but the flag is a big plus.",
    "A magician was walking down the street. \nThen he turned into a grocery store.",
    "Why do scuba divers fall backwards into the water? \nBecause if they fell forwards they'd still be in the boat." ]

# Use random.choice() function, and print result.
print("Random Joke Generator\n")
print(random.choice(jokes))