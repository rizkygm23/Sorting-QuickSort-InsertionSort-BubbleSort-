def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

        # Cetak array setelah setiap langkah
        print(f"Iterasi {i}: {arr}")
        
    return arr


