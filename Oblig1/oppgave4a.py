import math
import sys

def PrintBinarySearchTree(A):
    k = len(A)

    def Mid(i, j):
        m = math.ceil((i+j)/2)

        print(A[m])

        if i == j:
            return
        elif j == m:
            Mid(i, m-1)
        else:
            Mid(m+1, j)
            Mid(i, m-1)

    Mid(0, k-1)

if __name__ == "__main__":
    sorted_array = []
    for line in  sys.stdin:
        sorted_array.append(int(line))

    PrintBinarySearchTree(sorted_array)
