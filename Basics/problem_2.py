"""Install an external module and use it to perform an operation of your interest."""

import pyjokes

# Fetch and print a random joke
# If you want to get one joke at a time
joke = pyjokes.get_joke()
print(f"Here's a joke for you: {joke}")


# If you want to get multiple jokes at once

jokes = pyjokes.get_jokes()
number_of_jokes = int(input("How many jokes would you like to hear? "))
for i in range(number_of_jokes):
    print(f"Joke {i + 1}: {jokes[i]}")