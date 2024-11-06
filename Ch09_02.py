import random

# Dictionary of U.S. states and their capitals
states_and_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

def quiz_user():
    correct_count = 0
    incorrect_count = 0
    
    while True:
        # Select a random state
        state = random.choice(list(states_and_capitals.keys()))
        capital = states_and_capitals[state]
        
        # Ask the user to input the capital of the selected state
        user_answer = input(f"What is the capital of {state}? (or type 'exit' to stop): ").strip()

        if user_answer.lower() == "exit":
            break
        elif user_answer.lower() == capital.lower():
            correct_count += 1
            print(f"Correct! Running count - Correct: {correct_count}, Incorrect: {incorrect_count}")
        else:
            incorrect_count += 1
            print(f"Incorrect. The capital of {state} is {capital}.")
            print(f"Running count - Correct: {correct_count}, Incorrect: {incorrect_count}")

    # Final result display
    print(f"\nQuiz Ended.\nTotal Correct Answers: {correct_count}\nTotal Incorrect Answers: {incorrect_count}")


quiz_user()
