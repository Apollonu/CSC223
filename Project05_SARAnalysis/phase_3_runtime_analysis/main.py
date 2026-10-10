import csv, statistics, time, random
from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search
)

DATA_SIZES = [5_000, 50_000, 100_000, 150_000, 1_000_000]
TRIALS = 10

def median(list):
    return statistics.median(list)

def time_search(function, *arguments):
    start = time.perf_counter()
    id = function(*arguments)
    elapsed = (time.perf_counter() - start) * 1_000_000
    return id, elapsed

def validate_result(values, target, id):
    if target in values:
        assert id != -1 and values[id] == target, "Positive result"
    else:
        assert id == -1, "Negative result"

def run_trial(values, target):
    recursive_s, recursive_time = time_search(recursive_binary_search, values, target, 0, len(values) - 1)

    iterative_s, iterative_time = time_search(iterative_binary_search, values, target)

    sequential_s, sequential_time = time_search(sequential_search, values, target)

    validate_result(values, target, recursive_s)
    validate_result(values, target, iterative_s)
    validate_result(values, target, sequential_s)

    return recursive_time, iterative_time, sequential_time

def main():
    results = []

    for size in DATA_SIZES:
        recursive_times, iterative_times, sequential_times = [], [], []

        for _ in range(TRIALS):
            values = sorted(random.randint(1, 1_000_000) for _ in range(size))

            if random.random() < 0.5:
                target = random.choice(values)
            else:
                target = 1_000_001

            recursive, iterative, sequential = run_trial(values, target)

            recursive_times.append(recursive)
            iterative_times.append(iterative)
            sequential_times.append(sequential)

        recursive_median = median(recursive_times)
        iterative_median = median(iterative_times)
        sequential_median = median(sequential_times)

        results.append((size, recursive_median, iterative_median, sequential_median))
        print(
            f"Size {size:>7}: "
            f"Rec={recursive_median:8.2f} microseconds "
            f"It={iterative_median:8.2f} microseconds "
            f"Seq={sequential_median:8.2f} microseconds"
        )

    csv_path = "results.csv"
    with open(csv_path, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["data_size", "recursive_binary_us", "iterative_binary_us", "sequential_us"])
        writer.writerows(results)
    print(f"\nResults written to {csv_path}")

if __name__ == "__main__":
    main()
