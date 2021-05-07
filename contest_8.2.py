# creating merge sort programm
def merge(L,R):
        i,j = 0,0
        n, m = len(L), len(R)
        c = [0] * (n+m)
        k = 0
        while i < n and j < m:
            if L[i] < R[j]:
                c[k] = L[i]
                i += 1
                k += 1
            else:
                c[k] = R[j]
                j += 1
                k += 1
        if i == n:
            while k < n+m and j < m:
                c[k] = R[j]
                k += 1
                j += 1
        else:
            while k < n+m and i < n:
                c[k] = L[i]
                k += 1
                i += 1
        return c




def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)
    if len(A) == 1:
        return A
    l = merge_sort(A[:len(A)//2], depth + 1, part = "left")
    r = merge_sort(A[len(A)//2:len(A)+1], depth + 1, part = "right")
    A = merge(l,r)
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)
    return A
    
merge_sort([2,4,1])
        
