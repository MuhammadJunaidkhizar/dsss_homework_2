import random

def get_random_integer(min_value, max_value):
    """
    Returns a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def pick_random_math_operator():
    """
    Selects a random math operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def generate_math_question(num1, num2, operator):
    """
    Creates a math question and computes the correct answer.
    """
    question = f"{num1} {operator} {num2}"
    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    
    return question, correct_answer

def math_quiz_game():
    """
    Runs a math quiz game with 5 questions. Tracks score and displays at the end.
    """
    score = 0
    total_questions = 5  # Number of questions in the game

    print("Welcome to the Math Quiz Game!")
    print("Solve the math problems correctly to earn points.")

    for _ in range(total_questions):
        # Generate numbers and operator
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 10)
        operator = pick_random_math_operator()

        # Generate problem and correct answer
        question, correct_answer = generate_math_question(num1, num2, operator)
        
        print(f"\nQuestion: {question}")
        
        try:
            user_answer = int(input("Your answer: "))  # Get user input
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip to next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1  # Increase score if correct
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")

    # Show final score
    print(f"\nGame over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
