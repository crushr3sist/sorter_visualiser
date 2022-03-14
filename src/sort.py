#make a array with random numbers
import random, timeit

# make a sorter class
class Sorter:
    def __init__(self, arr: list):
        self.arr = arr
    
    def bubble_sort(self) -> list:
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    yield self.arr

    def quick_bubble_sort(self) -> list:
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr

    def selection_sort(self) -> list:
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i+1,len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr

    def insertion_sort(self) -> list:
        for i in range(1,len(self.arr)):
            x = self.arr[i]
            j = i
            while j > 0 and self.arr[j-1] > x:
                self.arr[j] = self.arr[j-1]
                j -= 1
            self.arr[j] = x
        return self.arr

    def merge_sort(self) -> list:
        if len(self.arr) > 1:
            mid = len(self.arr)//2
            left = self.arr[:mid]
            right = self.arr[mid:]

            left_sorter = Sorter(left)
            right_sorter = Sorter(right)

            left_sorter.merge_sort()
            right_sorter.merge_sort()

            i = 0
            j = 0
            k = 0
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
        return self.arr

    def quick_sort(self) -> list:
        if len(self.arr) > 1:
            self.quick_sort_helper(0, len(self.arr)-1)
        return self.arr

    def quick_sort_helper(self, low, high):
        if low < high:
            pivot_location = self.partition(low, high)
            self.quick_sort_helper(low, pivot_location-1)
            self.quick_sort_helper(pivot_location+1, high)

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low
        for j in range(low, high):
            if self.arr[j] <= pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i

    def heap_sort(self) -> list:
        for i in range(len(self.arr)):
            self.heapify(len(self.arr)-1-i, len(self.arr)-1-i)
        for i in range(len(self.arr)):
            self.arr[0], self.arr[len(self.arr)-1-i] = self.arr[len(self.arr)-1-i], self.arr[0]
            self.heapify(0, len(self.arr)-2-i)
        return self.arr

    def heapify(self, index, end):
        largest = index
        left = 2*index + 1
        right = 2*index + 2
        if left <= end and self.arr[left] > self.arr[largest]:
            largest = left
        if right <= end and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.heapify(largest, end)

    def counting_sort(self) -> list:
        m = max(self.arr)
        count = [0]*(m+1)
        for i in self.arr:
            count[i] += 1
        i = 0
        for j in range(m+1):
            for k in range(count[j]):
                self.arr[i] = j
                i += 1
        return self.arr

    def radix_sort(self) -> list:
        max_length = False
        tmp = -1
        while not max_length:
            max_length = True
            buckets = [list() for _ in range(10)]
            for i in self.arr:
                tmp = i // (10**len(str(tmp)))
                buckets[i%(10**len(str(tmp)))].append(i)
                if max_length and i > 0:
                    max_length = False
            del self.arr[:]
            for i in buckets:
                self.arr.extend(i)
        return self.arr

    def shell_sort(self) -> list:
        gap = len(self.arr)//2
        while gap > 0:
            for i in range(gap, len(self.arr)):
                tmp = self.arr[i]
                j = i
                while j >= gap and self.arr[j-gap] > tmp:
                    self.arr[j] = self.arr[j-gap]
                    j -= gap
                self.arr[j] = tmp
            gap //= 2
        return self.arr
    
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
        return self.arr
    
    def bogo_sort(self) -> list:
        while not self.is_sorted():
            random.shuffle(self.arr)
        return self.arr

    def is_sorted(self):
        return all(self.arr[i] <= self.arr[i+1] for i in range(len(self.arr)-1))

# main program
if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(100)]
    print(arr)
    print()
    sorter = Sorter(arr)
    print("Bubble sort:")
    print(sorter.bubble_sort())
