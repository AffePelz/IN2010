def sort(A):
    for i in range(len(A)-1):
        k = i
        for j in range(i+1,len(A)-1):
            if A[j] < A[k]:
                k = j
        if i != k:
            A.swap(i, k)
    return A
