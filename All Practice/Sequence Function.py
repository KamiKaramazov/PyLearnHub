##Fibonacci Sequence Function
#Create a Python function called fibonacci that takes an integer n as an argument and returns the first n Fibonacci numbers as a list. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, 8, ...).

# Ask the user if they want to generate a Fibonacci sequence
start = input("If you want to generate a Fibonacci sequence, press 'y'. To quit, press 'q': ")
number = input("Please define the number of terms to generate: ")

# Check if the user wants to generate the Fibonacci sequence
if start == 'y':
    # Define a function to generate the Fibonacci sequence
    def fibonacci(n):
        # Initialize the sequence with the first two Fibonacci numbers
        fib_sequence = [0, 1]
        
        # Continue generating numbers until reaching the desired count 'n'
        while len(fib_sequence) < n:
            # Calculate the next Fibonacci number by adding the last two numbers
            next_number = fib_sequence[-1] + fib_sequence[-2]
            
            # Append the next number to the sequence
            fib_sequence.append(next_number)
        
        # Return the generated Fibonacci sequence
        return fib_sequence

    # Call the fibonacci function to generate the first 'number' Fibonacci numbers
    result = fibonacci(int(number))
    
    # Print the generated Fibonacci sequence
    print("Generated Fibonacci Sequence:", result)
else:
    print("Goodbye!")



