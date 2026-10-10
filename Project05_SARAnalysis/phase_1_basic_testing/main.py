from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)

def run_test(values, target, desc):
    print(f"\n=== {desc} ===")
    print(f"List: {values}")
    print(f"Target: {target}")

    rec = recursive_binary_search(values, target, 0, len(values) - 1)
    print(f"Recursive binary -> index={rec}, found={rec != -1}")

    itr = iterative_binary_search(values, target)
    print(f"Iterative binary -> index={itr}, found={itr != -1}")

    seq = sequential_search(values, target)
    print(f"Sequential search -> index={seq}, found={seq != -1}")

def main():
    values = [1, 3, 5, 6, 10, 13, 22]
    values.sort()

    run_test(values, 6, "Middle integer found")
    run_test(values, 2, "No integer found")
    run_test(values, 1, "First integer found")
    run_test(values, 22, "Last integer found")
    run_test([7], 7, "List present found")
    run_test([7], 5, "List absent found")
    run_test([], 1, "List empty found")
    run_test([3, 4, 4, 7], 4, "Duplicate integers found")

if __name__ == "__main__":
    main()
