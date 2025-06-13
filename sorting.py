def bubble(list):
    index= len(list)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list
print("bubble sort:",bubble([2,1,6,3,4]))

def quick_sort(list):
    lenght= len(list)

    if lenght <= 1:
        return list
    else:
        pivot = list.pop()

    list_greater=[]
    list_lesser=[]

    for item in list:
        if item > pivot:
            list_greater.append(item)
        else:
            list_lesser.append(item)
    return quick_sort(list_lesser) + [pivot] + quick_sort(list_greater)

print("quick sort:",quick_sort([1,45,6,2,5,67,7,34,7,8,9,10]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("merge sort:",merge_sort([1, 45, 6, 2, 5, 67, 7, 34, 7, 8, 9, 10]))
