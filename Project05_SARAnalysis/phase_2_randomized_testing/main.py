import random
from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)

def validate_index(values, target, id):
    if id == -1:
        return target not in values
    return 0 <= id < len(values) and values[id] == target

def run_random_trial():
    values = sorted(random.randint(1, 100) for _ in range(20))

    if random.random() < 0.5:
        target = random.choice(values)
        expected = "present"
    else:
        target = 101
        expected = "absent"

    recursive_id = recursive_binary_search(values, target, 0, len(values) - 1)
    iterative_id = iterative_binary_search(values, target)
    sequential_id = sequential_search(values, target)

    recursive_validate = validate_index(values, target, recursive_id)
    iterative_validate = validate_index(values, target, iterative_id)
    sequential_validate = validate_index(values, target, sequential_id)

    print("-" * 60)
    print(f"List ({len(values)} elements): {values}")
    print(f"Target: {target}    (expected {expected})")
    print(f"Recursive binary -> index={recursive_id}    {'OK' if recursive_validate else 'FAIL'}")
    print(f"Iterative  binary -> index={iterative_id}  {'OK' if iterative_validate else 'FAIL'}")
    print(f"Sequential binary -> index={sequential_id}  {'OK' if sequential_validate else 'FAIL'}")
    print("-" * 60)
    return expected, recursive_validate and iterative_validate and sequential_validate

def main():
    success, failure = False, False
    trial = 0

    while not (success and failure):
        trial += 1
        expected, passed = run_random_trial()

        if expected == "present" and passed:
            success = True
        if expected == "absent" and passed:
            failure = True
        if trial >= 20:
            break

    print("\nCompleted randomized testing")
    print(f"Present case: {'yes' if success else 'no'}")
    print(f"Absent case: {'yes' if failure else 'no'}")

if __name__ == "__main__":
    main()
