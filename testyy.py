from collections import deque

def water_jug(jug_x, jug_y, target):
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        current_state, sequence = queue.popleft()

        if target in current_state:
            return sequence

        if current_state in visited:
            continue

        visited.add(current_state)

        actions = [
            ((jug_x, current_state[1]), (jug_x, current_state[1])),
            ((current_state[0], jug_y), (current_state[0], jug_y)),
            ((0, current_state[1]), (0, current_state[1])),
            ((current_state[0], 0), (current_state[0], 0)),
            ((max(0, current_state[0] - (jug_y - current_state[1])), min(jug_y, current_state[0] + current_state[1])), (max(0, current_state[0] - (jug_y - current_state[1])), min(jug_y, current_state[0] + current_state[1]))),
            ((min(jug_x, current_state[0] + current_state[1]), max(0, current_state[1] - (jug_x - current_state[0]))), (min(jug_x, current_state[0] + current_state[1]), max(0, current_state[1] - (jug_x - current_state[0]))))
        ]

        for next_state, step in actions:
            if next_state not in visited:
                queue.append((next_state, sequence + [step]))

    return None

jug_x = int(input("Enter the capacity of Jug X:"))  # Capacity of jug X
jug_y = int(input("Enter the capacity of Jug Y:"))  # Capacity of jug Y
target = int(input("Enter the target:"))  # Target amount of water

result = water_jug(jug_x, jug_y, target)
if result:
    print(f"All sequences of steps for obtaining {target} liters:")
    for i, step in enumerate(result):
        print(f"Step {i + 1}: {step}")
else:
    print(f"Target amount of {target} liters cannot be obtained with the given jugs.")
