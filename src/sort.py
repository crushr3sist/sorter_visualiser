# make a array with random numbers
import random, timeit

# make a sorter class
class Sorter:
    def __init__(self, arr: list):
        self.arr = arr

    def bubble_sort(self) -> list:
        for i in range(len(self.arr)):
            for j in range(len(self.arr) - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    yield self.arr

    def selection_sort(self) -> list:
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            yield self.arr

    def insertion_sort(self) -> list:
        for i in range(1, len(self.arr)):
            j = i
            while j > 0 and self.arr[j] < self.arr[j - 1]:
                self.swap(j, j - 1)
                j -= 1
            yield self.arr

    # merge sort with yield
    def merge_sort(self) -> list:
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left = self.arr[:mid]
            right = self.arr[mid:]
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.arr[k] = left[i]
                    i += 1
                else:
                    self.arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self.arr[k] = right[j]
                j += 1
                k += 1
            yield self.arr

    # quick sort with yield
    def quick_sort(self) -> list:
        self.quick_sort_helper(0, len(self.arr) - 1)
        yield self.arr

    def quick_sort_helper(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort_helper(low, pivot_index - 1)
            self.quick_sort_helper(pivot_index + 1, high)

    # quick sort with yield
    def quick_sort_with_pivot(self) -> list:
        self.quick_sort_with_pivot_helper(0, len(self.arr) - 1)
        yield self.arr

    def quick_sort_with_pivot_helper(self, low, high):
        if low < high:
            pivot_index = self.partition_with_pivot(low, high)
            self.quick_sort_with_pivot_helper(low, pivot_index - 1)
            self.quick_sort_with_pivot_helper(pivot_index + 1, high)

    def partition_with_pivot(self, low, high):
        pivot = self.arr[high]
        i = low
        for j in range(low, high):
            if self.arr[j] <= pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low
        for j in range(low, high):
            if self.arr[j] <= pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i

    def counting_sort(self) -> list:
        m = max(self.arr)
        count = [0] * (m + 1)
        for i in self.arr:
            count[i] += 1
        i = 0
        for j in range(m + 1):
            for k in range(count[j]):
                self.arr[i] = j
                i += 1
        return self.arr

    def radix_sort(self) -> list:
        m = max(self.arr)
        exp = 1
        while m / exp > 0:
            count = [0] * 10
            for i in self.arr:
                count[i // exp % 10] += 1
            i = 0
            for j in range(1, 10):
                count[j] += count[j - 1]
            for j in range(len(self.arr) - 1, -1, -1):
                self.arr[count[self.arr[j] // exp % 10] - 1] = self.arr[j]
                count[self.arr[j] // exp % 10] -= 1
            exp *= 10
            yield self.arr

    def shell_sort(self) -> list:
        gap = len(self.arr) // 2
        while gap > 0:
            for i in range(gap, len(self.arr)):
                tmp = self.arr[i]
                j = i
                while j >= gap and self.arr[j - gap] > tmp:
                    self.arr[j] = self.arr[j - gap]
                    j -= gap
                self.arr[j] = tmp
            gap //= 2
            yield self.arr

    def cocktail_sort(self) -> list:
        swapped = True
        start = 0
        end = len(self.arr) - 1
        while start < end and swapped:
            swapped = False
            for i in range(start, end):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in reversed(range(start, end)):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
            start += 1
            yield self.arr

    def is_sorted(self):
        return all(self.arr[i] <= self.arr[i + 1] for i in range(len(self.arr) - 1))

    def gnome_sort(self) -> list:
        i = 0
        while i < len(self.arr):
            if i == 0 or self.arr[i - 1] <= self.arr[i]:
                i += 1
            else:
                self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                i -= 1
            yield self.arr

    def pancake_sort(self) -> list:
        for i in range(len(self.arr)):
            max_index = self.find_max_index(i)
            if max_index != i:
                self.arr[i], self.arr[max_index] = self.arr[max_index], self.arr[i]
                self.reverse_array(i)
                yield self.arr
            yield self.arr

    def find_max_index(self, i):
        max_index = i
        for j in range(i + 1, len(self.arr)):
            if self.arr[j] > self.arr[max_index]:
                max_index = j
        return max_index

    def reverse_array(self, i):
        start = i
        end = len(self.arr) - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1

    def cycle_sort(self) -> list:
        for cycle_size in range(len(self.arr), 0, -1):
            for start in range(0, len(self.arr) - cycle_size):
                if self.arr[start] > self.arr[start + cycle_size]:
                    self.swap(start, start + cycle_size)
                    yield self.arr
        yield self.arr

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def comb_sort(self) -> list:
        shrink_factor = 1.247330950103979
        gap = len(self.arr)
        swapped = True
        while gap > 1 or swapped:
            gap = int(gap / shrink_factor)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(len(self.arr) - gap):
                if self.arr[i] > self.arr[i + gap]:
                    self.arr[i], self.arr[i + gap] = self.arr[i + gap], self.arr[i]
                    swapped = True
            yield self.arr

    def odd_even_sort(self) -> list:
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(self.arr), 2):
                if self.arr[i] < self.arr[i - 1]:
                    self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                    swapped = True
            for i in range(0, len(self.arr), 2):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
            yield self.arr

    def heap_sort(self) -> list:
        self.build_heap()
        for i in range(len(self.arr) - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(0, i - 1)
            yield self.arr

    def build_heap(self):
        for i in range(len(self.arr) // 2, -1, -1):
            self.heapify(i, len(self.arr) - 1)

    def heapify(self, index, end):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left <= end and self.arr[left] > self.arr[largest]:
            largest = left
        if right <= end and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.heapify(largest, end)


# main program
if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(100)]
    print(arr)
    print()
    sorter = Sorter(arr)
    print("Bubble sort:")
    print(sorter.bubble_sort())
