from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Extracting unique letters from the puzzle
    unique_letters = set([char for char in puzzle if char.isalpha()])
    letters_count = len(unique_letters)
    if letters_count > 10:
        print("Invalid puzzle: More than 10 unique letters")
        return

    # Generate all permutations of digits from 0 to 9
    digit_permutations = permutations(range(10), letters_count)
    attempts = 0

    for digit_assignment in digit_permutations:
        attempts += 1
        assignment = dict(zip(unique_letters, digit_assignment))
        # Check if the assignment satisfies the puzzle
        if satisfies_puzzle(puzzle, assignment):
            return assignment, attempts

    return None, attempts

def satisfies_puzzle(puzzle, assignment):
    # Replace letters in the puzzle with digits
    for letter, digit in assignment.items():
        puzzle = puzzle.replace(letter, str(digit))
    
    # Format the puzzle expression to remove leading zeros
    puzzle = puzzle.replace(" 0", " ")
    
    # Evaluate the arithmetic expression
    try:
        return eval(puzzle)
    except ZeroDivisionError:
        return False

# Example usage:
puzzle = input("Enter words and their sum format(x + y == z) : ")
solution, attempts = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for letter, digit in sorted(solution.items()):
        print(f"{letter}: {digit}")
    print(f"Total attempts: {attempts}")
else:
    print("No solution found.")
    print(f"Total attempts: {attempts}")
