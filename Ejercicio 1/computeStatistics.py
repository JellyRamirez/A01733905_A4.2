"""
computeStatistics.py

This script calculates descriptive statistics (mean, median, mode, variance, 
and standard deviation) for a given file containing numerical data.
"""

import sys
import time
from collections import Counter

def compute_mean(numbers):
    """Calculates the mean (average) of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0

def compute_median(numbers):
    """Calculates the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    mid = count // 2
    if count % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def compute_mode(numbers):
    """Calculates the mode of a list of numbers."""
    frequency = Counter(numbers)
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    return modes

def compute_variance(numbers, mean):
    """Calculates the variance of a list of numbers."""
    count = len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / count if count > 0 else 0

def compute_std_dev(variance):
    """Calculates the standard deviation from variance."""
    return variance ** 0.5

def process_file(input_file, output_file):
    """Processes the file, computes statistics, and saves results."""
    start_time = time.time()
    try:
        with open(input_file, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    numbers = []
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        try:
            numbers.append(float(line))
        except ValueError:
            print(f"Error in line {line_number}: '{line}' is not a valid number.")
        

    if not numbers:
        print("No valid numbers found. Exiting.")
        sys.exit(1)

    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(variance)
    elapsed_time = time.time() - start_time

    results = (
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Execution Time: {elapsed_time:.2f} seconds\n"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(results)

    print(results)

def main():
    """Main function that reads a file from the command line, 
    computes descriptive statistics, and writes the results to a file."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "StatisticsResults.txt"
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
