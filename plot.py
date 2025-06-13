import matplotlib.pyplot as plt

def plot_sorting_results(input_sizes, results):
    plt.figure(figsize=(10, 6))
    for algo, times in results.items():
        plt.plot(input_sizes, times, marker='o', label=algo)

    plt.title("Sorting Algorithm Performance")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_searching_results(input_sizes, results):
    plt.figure(figsize=(10, 6))
    for algo, times in results.items():
        plt.plot(input_sizes, times, marker='o', label=algo)

    plt.title("Searching Algorithm Performance")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
