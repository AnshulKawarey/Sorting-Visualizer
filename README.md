# Sorting Visualizer

A Python-based Sorting Visualizer using `matplotlib` and `numpy`.

## Supported Sorting Algorithms:

- **Bubble Sort**
- **Insertion Sort**
- **Merge Sort**
- **Quick Sort**

---

## Prerequisites

Ensure you have the following installed:

1. [Python](https://www.python.org/downloads/)
2. [Matplotlib](https://matplotlib.org/stable/install/index.html)
3. [NumPy](https://numpy.org/install/)

Install missing dependencies using:
```bash
pip install matplotlib numpy
```

---

## About the Sorting Algorithms

### 1. Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

- The algorithm traverses from left to right, comparing adjacent elements and moving the larger one to the right.
- This process continues, moving the largest element to its correct position at each iteration.
- The algorithm repeats until all elements are sorted.

**Time Complexity:**
- Worst-case: `O(n²)`
- Average-case: `O(n²)`
- Best-case (already sorted list): `O(n)`

### 2. Insertion Sort

Insertion Sort builds the sorted array one item at a time by taking an element and inserting it into its correct position.

- It maintains a sorted and an unsorted portion.
- Elements from the unsorted portion are picked and placed in the correct position in the sorted portion.
- It is a stable sorting algorithm, meaning elements with equal values retain their relative order.

**Time Complexity:**
- Worst-case: `O(n²)`
- Average-case: `O(n²)`
- Best-case (already sorted list): `O(n)`

### 3. Merge Sort

Merge Sort follows the **divide-and-conquer** approach to sorting.

- The array is recursively divided into two halves.
- Each half is sorted individually.
- The sorted halves are merged back together.
- This process repeats until the entire array is sorted.

**Time Complexity:**
- Worst-case: `O(n log n)`
- Average-case: `O(n log n)`
- Best-case: `O(n log n)`

### 4. Quick Sort

QuickSort is another **divide-and-conquer** sorting algorithm that selects a **pivot** element and partitions the array around it.

- It picks an element as a pivot and partitions the array into two halves: elements less than the pivot and elements greater than the pivot.
- The process is repeated recursively for each partition until the array is fully sorted.

**Time Complexity:**
- Worst-case: `O(n²)` (when the pivot is the smallest or largest element)
- Average-case: `O(n log n)`
- Best-case: `O(n log n)`

---
