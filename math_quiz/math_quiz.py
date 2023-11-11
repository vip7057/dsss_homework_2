import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive)
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random mathematical operator (+, -, *)
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculate the result of the mathematical operation
    Returns a tuple containing the problem string and the answer
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    # Format the problem string
    problem = f"{num1} {operator} {num2}"

    return problem, result


def math_quiz():
    """
    Main function to conduct a math quiz game
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Calculate the result of the mathematical operation
        problem, answer = calculate_result(num1, num2, operator)

        # Display the question
        print(f"\nQuestion: {problem}")

        try:
            # Get user input as an answer
            user_answer = int(input("Your answer: "))
        except ValueError:
            # Handle invalid user input
            print("Invalid input. Only integer input is valid.")
            continue  # Start the quiz again for invalid user input

        # Check if the user's answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
