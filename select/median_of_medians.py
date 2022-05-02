def quick_select(arr : list, k : int) -> int:
    p = arr[0]
    A, B, M = [], [], []
    for x in arr:
        if x < p:
            A.append(x)
        elif p < x:
            B.append(x)
        else:
            M.append(x)

    if k < len(A):
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k - len(A) - len(M))
    else:
        return p

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    print(quick_select(arr, len(arr) // 2))