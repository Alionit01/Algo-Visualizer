import random
import time
from sorting import bubble_sort, quick_sort, merge_sort
from searching import linear_search, binary_search


def measure_sort_time(algorithm, data):
    start = time.perf_counter()
    algorithm(data.copy())
    end = time.perf_counter()
    return end - start


def measure_search_time(algorithm, data, target):
    start = time.perf_counter()
    algorithm(data, target)
    end = time.perf_counter()
    return end - start


def generate_data(size, mode="Random"):
    if mode == "Sorted (Best Case)":
        return list(range(size))
    elif mode == "Reversed (Worst Case)":
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, 10000) for _ in range(size)]


def analyze_sort_algorithms(mode="Random"):
    input_sizes = [10, 100, 1000, 2000]
    results = {
        "Bubble Sort": [],
        "Quick Sort": [],
        "Merge Sort": []
    }

    for size in input_sizes:
        data = generate_data(size, mode)
        results["Bubble Sort"].append(measure_sort_time(bubble_sort, data))
        results["Quick Sort"].append(measure_sort_time(quick_sort, data))
        results["Merge Sort"].append(measure_sort_time(merge_sort, data))

    return input_sizes, results


def analyze_search_algorithms(mode="Random"):
    input_sizes = [10, 100, 1000, 2000]
    results = {
        "Linear Search": [],
        "Binary Search": []
    }

    for size in input_sizes:
        data = generate_data(size, mode)
        data.sort()  # Required for Binary Search
        target = random.choice(data)
        results["Linear Search"].append(measure_search_time(linear_search, data, target))
        results["Binary Search"].append(measure_search_time(binary_search, data, target))

    return input_sizes, results
