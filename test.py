from collections import deque

# Function to solve water jug problem
def water_jug(jug_x, jug_y, target):
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        current_state, sequence = queue.popleft()

        if current_state[0] == target or current_state[1] == target:
            return sequence

        if current_state in visited:
            continue

        visited.add(current_state)

        # Fill jug X
        fill_x = ((jug_x, current_state[1]), sequence + [(jug_x, current_state[1])])
        if fill_x[0] not in visited:
            queue.append(fill_x)

        # Fill jug Y
        fill_y = ((current_state[0], jug_y), sequence + [(current_state[0], jug_y)])
        if fill_y[0] not in visited:
            queue.append(fill_y)

        # Empty jug X
        empty_x = ((0, current_state[1]), sequence + [(0, current_state[1])])
        if empty_x[0] not in visited:
            queue.append(empty_x)

        # Empty jug Y
        empty_y = ((current_state[0], 0), sequence + [(current_state[0], 0)])
        if empty_y[0] not in visited:
            queue.append(empty_y)

        # Pour from X to Y
        pour_x_to_y = min(current_state[0], jug_y - current_state[1])
        x_to_y = ((current_state[0] - pour_x_to_y, current_state[1] + pour_x_to_y), sequence + [(current_state[0] - pour_x_to_y, current_state[1] + pour_x_to_y)])
        if x_to_y[0] not in visited:
            queue.append(x_to_y)

        # Pour from Y to X
        pour_y_to_x = min(current_state[1], jug_x - current_state[0])
        y_to_x = ((current_state[0] + pour_y_to_x, current_state[1] - pour_y_to_x), sequence + [(current_state[0] + pour_y_to_x, current_state[1] - pour_y_to_x)])
        if y_to_x[0] not in visited:
            queue.append(y_to_x)

    return None

# Example usage
jug_x = int(input("Enter the capacity of Jug X:"))  # Capacity of jug X
jug_y = int(input("Enter the capacity of Jug X:"))  # Capacity of jug Y
target = int(input("Enter the target"))  # Target amount of4= water


result = water_jug(jug_x, jug_y, target)
if result:
    print(f"All sequences of steps for obtaining {target} liters:")
    for i, step in enumerate(result):
        print(f"Step {i + 1}: {step}")
else:
    print(f"Target amount of {target} liters cannot be obtained with the given jugs.")
