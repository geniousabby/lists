# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
# Create an empty list to store the shifted characters  
# Loop through each character in the string:
#    If the character is a letter (A-Z or a-z):
#        Shift the letter by adding the shift value to its ASCII code (use the ord function)
#        Convert the new ASCII code back to a character (use the chr function)
#        Add the shifted character to the list
#    If the character is not a letter:
#        Add the character unchanged to the list
# After the loop, join the list into a string and return it  
# Get user input for the message and shift value  
# Call the function with the inputs and display the result


# TASK: Create a high score tracker that keeps the top 5 scores.

# Define a function that takes a list of scores and a new score
# Append the new score to the list
# Sort the list in descending order
# Keep only the top 5 scores
# Return the updated list
# Start with an empty high scores list
# Use a loop to let the user enter scores until they type -1
# Call the function with each new score and display the updated top 5 scores


# TASK: Create an interactive grocery list manager.

# Define a function to add an item to the list
# Append the item to the list and return it

# Define a function to remove an item from the list
# If the item exists, remove it
# If not, display a message saying the item is not in the list

# Define a function to display the grocery list
# If the list is not empty, print all items with numbers
# If the list is empty, display a message

# Start with an empty grocery list
# Use a loop to let the user choose an action:
# (1) Add an item
# (2) Remove an item
# (3) View the list
# (4) Exit the program
# Call the corresponding function based on user input
# Continue looping until the user chooses to exit