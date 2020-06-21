"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MAX_RANGE = 99
MIN_RANGE = 10
REQUIRED_CORRECT_ANSWER = 3


def main():
    """
    This program is simple mathematics test series  for students of primary school. In the program, the addition,
     multiplication, subtraction and division of randomly  generating two digit numbers ranging from 10 to 99 is done
     and the answer given by the user is checked. the user is given a choice to take the test of operators he want to
     practice. If the user gives a wrong answer, the right answer is displayed and If the user gives a right answer,
    he is appreciated with a  congratulatory statement. The user needs to give three consecutive right answers,
     to pass the test. If the user wants to practice more, he can take the test again for as many times as he wants.
     And he can switch to different test series too.
    """
    # the user is asked what he wants to practice
    print("Which test series you want to take- 1. Addition")
    print("                                  - 2. Subtraction")
    print("                                  - 3. Multiplication")
    print("                                  - 4. Division")
    test = int(input("Type- 1, 2, 3 or 4: "))
    if test == 1:
        addition_test_series()
    elif test == 2:
        subtraction_test_series()
    elif test == 3:
        multiplication_test_series()
    elif test == 4:
       division_test_series()
    else:
        print("Ïnvalid Input")

    another_test()


# if the user chooses addition test series
def addition_test_series():
    # the number of correct answer until now
    correct_answer = 0
    # two numbers are randomly generated and their addition is performed
    num1 = random.randint(MIN_RANGE, MAX_RANGE)
    num2 = random.randint(MIN_RANGE, MAX_RANGE)
    total = num1 + num2
    # the below line is displayed
    print("What is " + str(num1) + " + " + str(num2) + " ? ")
    # the user is asked to give his answer
    your_answer = int(input("Your answer: "))
    # the program checks if the answer matches to the right answer or not
    while your_answer:
        if your_answer == total:
            correct_answer = correct_answer + 1
            print("Correct! You've gotten " + str(correct_answer) + " correct in a row.")
            # if the number of correct answer is 3, the test completes and loop breaks
            if correct_answer >= 3:
                print("Congratulations! You mastered addition.")
                another_test()
            # another set of numbers are generated
            else:
                num1 = random.randint(MIN_RANGE, MAX_RANGE)
                num2 = random.randint(MIN_RANGE, MAX_RANGE)
                total = num1 + num2
                print("What is " + str(num1) + " + " + str(num2) + " ? ")
                your_answer = int(input("Your answer: "))
        else:
            # if the user gives wrong answer
            print("Incorrect. The expected answer is " + str(total))
            while your_answer != total:
                addition_test_series()


# if the user chooses subtraction test series
def subtraction_test_series():
    # the number of correct answer until now
    correct_answer = 0
    # two numbers are randomly generated and their subtraction is performed
    num1 = random.randint(MIN_RANGE, MAX_RANGE)
    num2 = random.randint(MIN_RANGE, MAX_RANGE)
    total = num1 - num2
    # the below line is displayed
    print("What is " + str(num1) + " - " + str(num2) + " ? ")
    # the user is asked to give his answer
    your_answer = int(input("Your answer: "))
    # the program checks if the answer matches to the right answer or not
    while your_answer:
        if your_answer == total:
            correct_answer = correct_answer + 1
            print("Correct! You've gotten " + str(correct_answer) + " correct in a row.")
            # if the number of correct answer is 3, the test completes  and the person is asked for another test
            if correct_answer == 3:
                print("Congratulations! You mastered subtraction.")
                break
            # another set of numbers are generated
            else:
                num1 = random.randint(MIN_RANGE, MAX_RANGE)
                num2 = random.randint(MIN_RANGE, MAX_RANGE)
                total = num1 - num2
                print("What is " + str(num1) + " - " + str(num2) + " ? ")
                your_answer = int(input("Your answer: "))
        else:
            # if the user gives wrong answer
            print("Incorrect. The expected answer is " + str(total))
            while your_answer != total:
                subtraction_test_series()


# if the user chooses multiplication test series
def multiplication_test_series():
    # the number of correct answer until now
    correct_answer = 0
    # two numbers are randomly generated and their multiplication is performed
    num1 = random.randint(MIN_RANGE, MAX_RANGE)
    num2 = random.randint(MIN_RANGE, MAX_RANGE)
    total = num1 * num2
    # the below line is displayed
    print("What is " + str(num1) + " * " + str(num2) + " ? ")
    # the user is asked to give his answer
    your_answer = int(input("Your answer: "))
    # the program checks if the answer matches to the right answer or not
    while your_answer:
        if your_answer == total:
            correct_answer = correct_answer + 1
            print("Correct! You've gotten " + str(correct_answer) + " correct in a row.")
            # if the number of correct answer is 3, the test completes  and the person is asked for another test
            if correct_answer == 3:
                print("Congratulations! You mastered Multiplication.")
                break
            # another set of numbers are generated
            else:
                num1 = random.randint(MIN_RANGE, MAX_RANGE)
                num2 = random.randint(MIN_RANGE, MAX_RANGE)
                total = num1 * num2
                print("What is " + str(num1) + " * " + str(num2) + " ? ")
                your_answer = int(input("Your answer: "))
        else:
            # if the user gives wrong answer
            print("Incorrect. The expected answer is " + str(total))
            while your_answer != total:
                multiplication_test_series()


# if the user chooses division test series
def division_test_series():
    # the number of correct answer until now
    correct_answer = 0
    # two numbers are randomly generated and their division is performed
    num1 = random.randint(MIN_RANGE, MAX_RANGE)
    num2 = random.randint(MIN_RANGE, MAX_RANGE)
    total = num1 / num2
    # it gives a round off answer to two decimal places
    total = round(total, 2)
    # the below line is displayed
    print("What is " + str(num1) + " / " + str(num2) + " ? ")
    # the user is asked to give his answer
    your_answer = float(input("Your answer: "))
    # the program checks if the answer matches to the right answer or not
    while your_answer:
        if your_answer == total:
            correct_answer = correct_answer + 1
            print("Correct! You've gotten " + str(correct_answer) + " correct in a row.")
            # if the number of correct answer is 3, the test completes  and the person is asked for another test
            if correct_answer == 3:
                print("Congratulations! You mastered Division.")
                break
            # another set of numbers are generated
            else:
                num1 = random.randint(MIN_RANGE, MAX_RANGE)
                num2 = random.randint(MIN_RANGE, MAX_RANGE)
                total = num1 / num2
                # it gives a round off answer to two decimal places
                total = round(total, 2)
                print("What is " + str(num1) + " / " + str(num2) + " ? ")
                your_answer = float(input("Your answer: "))
        else:
            # if the user gives wrong answer
            print("Incorrect. The expected answer is " + str(total))
            while your_answer != total:
                division_test_series()


def another_test():
    # if the user wishes to take another test
    test_again = input("Do you want to take the test again? type- yes or no:   ")
    if test_again == "yes":
        while test_again == "yes":
            main()
    else:
        print("See you next time!")




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
