def mean(data):
    if not data:
        return 0
    total = sum(data)
    return total / len(data)

def median(data):
    if not data:
        return 0
    sorted_numbers = sorted(data)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid = n // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def mode(data):
    if not data:
        return 0
    counts = {}
    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    if all(value == 1 for value in counts.values()):
        return 0
    max_count = max(counts.values())
    mode_numbers = [num for num, count in counts.items() if count == max_count]
    return min(mode_numbers)

if __name__ == "__main__":
    data = []
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
