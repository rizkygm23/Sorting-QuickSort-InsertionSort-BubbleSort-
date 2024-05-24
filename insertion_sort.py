def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # Cetak array setelah setiap langkah
        print(f"Iterasi {i}: {arr}")

# input_array = input("Masukan Array : ")
# arr = list(map(int, input_array.split()))
# print("Iterasi awal:", arr)
# insertion_sort(arr)
# print("Iterasi Hasil:", arr)
