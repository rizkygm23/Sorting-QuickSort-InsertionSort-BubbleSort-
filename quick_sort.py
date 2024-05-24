


def quicksort(arr):
    def quicksort_helper(arr, iteration):
        print(f"Iterasi {iteration}:")
        print("Array saat ini:", arr)
        
        if len(arr) <= 1:
            print(f"Mengembalikan array dengan satu elemen atau kosong: {arr}\n")
            return arr
        
        pivot = arr[0]
        left = []    # Partisi untuk elemen yang lebih kecil dari pivot
        middle = []  # Partisi untuk elemen yang sama dengan pivot
        right = []   # Partisi untuk elemen yang lebih besar dari pivot
        
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
        
        print("Pivot dipilih:", pivot)
        print("Partisi kiri:", left)
        print("Partisi tengah (pivot):", middle)
        print("Partisi kanan:", right)
        print()
        
        # Urutkan bagian kiri terlebih dahulu
        sorted_left = quicksort_helper(left, iteration + 1)
        sorted_right = quicksort_helper(right, iteration + 1)
        
        sorted_arr = sorted_left + middle + sorted_right
        print(f"Iterasi {iteration} - Hasil penggabungan: {sorted_arr}\n")
        
        return sorted_arr
    
    return quicksort_helper(arr, 1)


