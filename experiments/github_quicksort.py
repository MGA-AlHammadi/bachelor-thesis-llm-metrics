"""
Beispiel aus Open Source Repository:
https://github.com/calebmadrigal/algorithms-in-python/blob/master/quicksort.py

Dieses Skript implementiert den QuickSort-Algorithmus in Python.
QuickSort ist ein effizienter, rekursiver Sortieralgorithmus mit einer durchschnittlichen Zeitkomplexität von O(n log n).
"""

def quicksort(arr):
    """Sortiert eine Liste mit dem QuickSort-Algorithmus."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Wähle das mittlere Element als Pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def main():
    """Testet den QuickSort-Algorithmus mit einer Beispiel-Liste."""
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    print("Unsortierte Liste:", unsorted_list)
    sorted_list = quicksort(unsorted_list)
    print("Sortierte Liste:", sorted_list)


if __name__ == "__main__":
    main()
