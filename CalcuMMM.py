def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_dataset = sorted(data)
    n = len(sorted_dataset)

    mid = n // 2
    if n % 2 == 0:
        return (sorted_dataset[mid - 1] + sorted_dataset[mid]) / 2
    else:
        return sorted_dataset[mid]


def mode(data):
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1

    max_count = max(counts.values())
    modes = [value for value, counts in counts.items() if counts == max_count]

    return modes[0] if len(modes) == 1 else modes

def value_range(data):
    r = sorted(data)
    return r[-1] - r[0]


def variance(data, sample=True):
    m = mean(data)
    squared_diffs = [(x - m) ** 2 for x in data]
    divisor = len(data) - 1 if sample else len(data)
    return sum(squared_diffs) / divisor

def deviation(data, sample=True):
    return variance(data, sample) ** 0.5

dataset = [34, 4565, 3434, 667, 343, 345, 56, 34, 57, 23, 45, 56, 5]

print("Mean: ", mean(dataset))
print("Median: ", median(dataset))
print("Mode: ", mode(dataset))
print("Variance: ", variance(dataset))
print("Sample Std Dev: ", deviation(dataset, sample=True))
print("Population Std Dev:: ", deviation(dataset, sample=False))
print("value_range: ", value_range(dataset))
