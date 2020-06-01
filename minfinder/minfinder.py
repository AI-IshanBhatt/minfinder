def _find_minimum(arr, low, high):
    # Only one element
    if low == high:
        return arr[low]

    # Two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low]
        else:
            return arr[high]
    else:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
            return _find_minimum(arr, low, mid - 1)
        else:
            return _find_minimum(arr, mid + 1, high)


def minimum(arr):
    if not arr:
        raise ValueError("Empty Array supplied")
    elif len(arr) == 1:
        return arr[0]
    else:
        return _find_minimum(arr, 0, len(arr) - 1)
