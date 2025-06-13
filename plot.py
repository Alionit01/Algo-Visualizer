import matplotlib.pyplot as plt

def plot_sorting_results(input_sizes, results):
    fig, ax = plt.subplots(figsize=(10, 6))
    for algo, times in results.items():
        ax.plot(input_sizes, times, marker='o', label=algo)

    ax.set_title("Sorting Algorithm Performance")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Time (seconds)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig  # ✅ return the figure

def plot_searching_results(input_sizes, results):
    fig, ax = plt.subplots(figsize=(10, 6))
    for algo, times in results.items():
        ax.plot(input_sizes, times, marker='o', label=algo)

    ax.set_title("Searching Algorithm Performance")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Time (seconds)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig  # ✅ return the figure
