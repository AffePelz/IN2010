def sort(A):
    def BubbleDown(A,i,n):
        current = i
        left = 2*i + 1
        right = 2*i + 2
        if (left < n) and (A[current] < A[left]):
            current, left = left, current
        if right < n and A[current] < A[right]:
            current, right = right, current
        if i != current:
            A.swap(i,current)
            BubbleDown(A, current, n)

    def BuildMaxHeap(A,n):
        for i in range(n//2, -1, -1):
            BubbleDown(A,i,n)

    def Heapsort(A):
        n = len(A)
        BuildMaxHeap(A, n)
        for i in range(len(A)-1,0, -1):
            A.swap(0,i)
            BubbleDown(A,0,i)
        return A

    return Heapsort(A)
