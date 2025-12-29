#shuffle while preserving some order
import random
numbers = [1, 2, 3, 4, 5]
fixed_positions = [2, 4]
# Create a list of positions that can be shuffled (not fixed)
shufflable_positions = [i for i in range(len(numbers)) if i not in fixed_positions]
for i in range(len(numbers)):
    if i not in fixed_positions:
        # Only swap with other non-fixed positions
        j = random.choice(shufflable_positions)
        numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)



