def arithmetic_arranger():
    problems = []
    num_problems = int(input("How many problems would you like to calculate? "))

    for _ in range(num_problems):
        problem = input("Enter a problem (e.g., '32 + 698'): ")
        problems.append(problem)

    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    middle_line = ""
    bottom_line = ""
    result_line = ""  # Line to display results

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        # Format the lines
        top_line += f"{operand1:>{width}}    "
        middle_line += f"{operator} {operand2:>{width - 2}}    "
        bottom_line += "-" * width + "    "

        # Calculate the result
        if operator == '+':
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        result_line += f"{result:>{width}}    "

    return f"{top_line.rstrip()}\n{middle_line.rstrip()}\n{bottom_line.rstrip()}\n{result_line.rstrip()}"

# Call the function to get user input and calculate problems
print(arithmetic_arranger())
