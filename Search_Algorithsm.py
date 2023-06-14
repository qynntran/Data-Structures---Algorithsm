def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (target - arr[low]))

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


arr = [10, 20, 30, 40, 50]
target = 30
index = linear_search(arr, target)
#index = interpolation_search(arr, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found in the array")
