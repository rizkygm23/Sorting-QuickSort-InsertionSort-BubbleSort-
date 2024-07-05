


def quicksort(data):
    def quicksort_KEDUA(data, iteration):
        print(f"Iterasi {iteration}:")
        if len(data) <= 1:
            print(f"Mengembalikan array dengan satu elemen atau kosong: {data}\n")
            return data
        pivot = data[0]
        left = []    # BAGIAN KIRI
        middle = []  # BAGIAN TENGAH
        right = []   # BAGIAN KANAN
        # PERBANDINGAN TIAP NILAI PADA ARRAY
        for i in data:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
        print(f"NILAI PERBANDINGAN  :{pivot}")
        print(f"BAGIAN KIRI         :{left}")
        print(f"BAGIAN KANAN        :{right}")
        print()
        # Urutkan bagian kiri
        sorted_left = quicksort_KEDUA(left, iteration + 1)
        sorted_right = quicksort_KEDUA(right, iteration + 1)
        
        sorted_arr = sorted_left + middle + sorted_right
        
        
        return sorted_arr
    
    return quicksort_KEDUA(data, 1)


