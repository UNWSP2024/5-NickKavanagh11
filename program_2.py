# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# import random


def generate_numbers():
    """
    Generates two random integers between 100 and 999.
    
    Returns:
        tuple: two random integers
    """
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    return num1, num2


def check_answer(num1, num2, user_answer):
    """
    Checks whether the user's answer is correct.
    
    Parameters:
        num1 (int): first number
        num2 (int): second number
        user_answer (int): student's answer
        
    Returns:
        bool: True if correct, False otherwise
    """
    correct_answer = num1 + num2
    return user_answer == correct_answer


def main():
    print("=== Welcome to the Math Quiz ===")
    
    num1, num2 = generate_numbers()
    
    print(f"   {num1}")
    print(f"+  {num2}")
    print("------")
    
    try:
        user_answer = int(input("Enter your answer: "))
        
        if check_answer(num1, num2, user_answer):
            print("Congratulations! That is correct! 🎉")
        else:
            print(f"Sorry, that is incorrect.")
            print(f"The correct answer is {num1 + num2}.")
    
    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Program execution starts here
if __name__ == "__main__":
    main()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
