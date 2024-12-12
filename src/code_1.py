# I used Harlowe in Twine, so I had to make sure the code was formatted in a way that would work with Harlowe's syntax.

# Here is the python version:

# 1. Initialize the points
positive_points = 0
neutral_points = 0
negative_points = 0

# 2. Define a function to simulate the choices and track points
def make_choice(choice):
    global positive_points, neutral_points, negative_points
    
    if choice == "Positive":
        positive_points += 1
    elif choice == "Neutral":
        neutral_points += 1
    elif choice == "Negative":
        negative_points += 1

# 3. Calculate the final ending
if positive_points > neutral_points and positive_points > negative_points:
    final_ending = "Positive Ending"
elif negative_points > positive_points and negative_points > neutral_points:
    final_ending = "Negative Ending"
else:
    final_ending = "Neutral Ending"

# By calculating the ending, the code will automatically give you the ending based on the points your choices have accumulated.