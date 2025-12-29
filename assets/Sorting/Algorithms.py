"""
    Sorts a list using the Quick Sort algorithm
    Returns a new sorted list without modifying the original, we dont want that :/
    """

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
