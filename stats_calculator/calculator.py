
import math

def get_class_marks(class_intervals):
    """Calculates the class marks from class intervals."""
    class_marks = []
    for interval in class_intervals:
        lower, upper = map(int, interval.split('-'))
        class_marks.append((lower + upper) / 2)
    return class_marks

def get_mean(class_intervals, frequencies):
    """Calculates the mean from grouped data."""
    class_marks = get_class_marks(class_intervals)
    sum_of_products = sum(f * x for f, x in zip(frequencies, class_marks))
    total_frequency = sum(frequencies)
    return sum_of_products / total_frequency if total_frequency > 0 else 0

def get_median(class_intervals, frequencies):
    """Calculates the median from grouped data."""
    total_frequency = sum(frequencies)
    median_index = total_frequency / 2
    
    cumulative_frequency = 0
    median_class_index = -1
    for i, f in enumerate(frequencies):
        cumulative_frequency += f
        if cumulative_frequency >= median_index:
            median_class_index = i
            break
            
    if median_class_index == -1:
        return None # Should not happen with valid data

    lower_boundary, upper_boundary = map(int, class_intervals[median_class_index].split('-'))
    class_width = upper_boundary - lower_boundary
    
    cumulative_frequency_before = sum(frequencies[:median_class_index])
    median_frequency = frequencies[median_class_index]
    
    median = lower_boundary + ((median_index - cumulative_frequency_before) / median_frequency) * class_width
    return median

def get_mode(class_intervals, frequencies):
    """Calculates the mode from grouped data."""
    modal_class_index = frequencies.index(max(frequencies))
    
    lower_boundary, upper_boundary = map(int, class_intervals[modal_class_index].split('-'))
    class_width = upper_boundary - lower_boundary
    
    f1 = frequencies[modal_class_index]
    f0 = frequencies[modal_class_index - 1] if modal_class_index > 0 else 0
    f2 = frequencies[modal_class_index + 1] if modal_class_index < len(frequencies) - 1 else 0
    
    if (2 * f1 - f0 - f2) == 0:
        # Handle the case where the denominator is zero,
        # which can happen in a bimodal or multimodal distribution.
        # A simple approach is to return the midpoint of the modal class.
        return (lower_boundary + upper_boundary) / 2

    mode = lower_boundary + ((f1 - f0) / (2 * f1 - f0 - f2)) * class_width
    return mode

def main():
    """Main function to get user input and calculate stats."""
    print("Enter the class intervals (e.g., 10-20), one per line. Type 'done' when finished:")
    class_intervals = []
    while True:
        interval = input()
        if interval.lower() == 'done':
            break
        class_intervals.append(interval)

    print("\nEnter the corresponding frequencies, one per line:")
    frequencies = []
    for _ in range(len(class_intervals)):
        frequency = int(input())
        frequencies.append(frequency)

    mean = get_mean(class_intervals, frequencies)
    median = get_median(class_intervals, frequencies)
    mode = get_mode(class_intervals, frequencies)

    print("\n--- Results ---")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode:.2f}")

if __name__ == "__main__":
    main()
