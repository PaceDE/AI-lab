from collections import deque

def water_jug(jug_x, jug_y, target):
    visited = set()
    queue = deque([((0, 0), [])])  # Initial state is (0, 0) with empty sequence

    while queue:
        current_state, sequence = queue.popleft()

        if target in current_state:
            return sequence

        if current_state in visited:
            continue

        visited.add(current_state)

        actions = [
            ((jug_x, current_state[1]), "Fill X"),
            ((current_state[0], jug_y), "Fill Y"),
            ((0, current_state[1]), "Empty X"),
            ((current_state[0], 0), "Empty Y"),
            ((max(0, current_state[0] - (jug_y - current_state[1])), min(jug_y, current_state[0] + current_state[1])), "Pour X to Y"),
            ((min(jug_x, current_state[0] + current_state[1]), max(0, current_state[1] - (jug_x - current_state[0]))), "Pour Y to X")
        ]

        for next_state, action in actions:
            if next_state not in visited:
                queue.append((next_state, sequence + [(next_state, action)]))

    return None

# Example usage
jug_x = int(input("Enter the capacity of Jug X:"))  # Capacity of jug X
jug_y = int(input("Enter the capacity of Jug Y:"))  # Capacity of jug Y
target = int(input("Enter the target:"))  # Target amount of water

result = water_jug(jug_x, jug_y, target)
if result:
    print(f"All sequences of steps for obtaining {target} liters:")
    print(f"Step 1: State=(0,0), Action = (Initial State)")
    for i, (state, action) in enumerate(result):
        print(f"Step {i + 2}: State={state}, Action={action}")
else:
    print(f"Target amount of {target} liters cannot be obtained with the given jugs.")
