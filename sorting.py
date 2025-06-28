def bubble_sort(data, key=lambda x: x):
    data = data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key(data[j]) > key(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def quick_sort(data, key=lambda x: x):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]  # Middle pivot helps prevent worst-case
    pivot_key = key(pivot)

    lesser = [x for x in data if key(x) < pivot_key]
    greater = [x for x in data if key(x) > pivot_key]
    equal = [x for x in data if key(x) == pivot_key]

    # ⚠️ Only recurse when input is smaller than original
    if len(lesser) == len(data) or len(greater) == len(data):
        return data  # Avoid infinite recursion on equal elements

    return quick_sort(lesser, key) + equal + quick_sort(greater, key)


def merge_sort(data, key=lambda x: x):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
