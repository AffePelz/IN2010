import random

def sort(A):
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
    def ChoosePivot(A,low,high):
        return random.randint(low,high)

    def Partition(A,low,high):
        p = ChoosePivot(A,low,high)
        A.swap(p,high)
        pivot = A[high]
        
        left = low
        right = high - 1
        while left <= right:
            while left <= right and A[left] <= pivot:
                left += 1
            while right >= left and pivot <= A[right]:
                right -= 1
            if left < right:
                A.swap(left,right)
        A.swap(left,right)
        return left


    def QuickSort(A,low,high):
        if low >= high:
            return A
        p = Partition(A,low,high)
        QuickSort(A,low,p-1)
        QuickSort(A,p+1,high)
        return A

    return QuickSort(A, 0, len(A)-1)
