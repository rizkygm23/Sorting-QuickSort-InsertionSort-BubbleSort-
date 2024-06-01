def BubbleSort(Z):
    for i in range(len(Z) - 1, 0, -1):
        Max = 0
        for l in range(1, i + 1):
            if Z[l] > Z[Max]:
                Max = l
        # Melakukan pertukaran elemen
        tukar = Z[i]
        Z[i] = Z[Max]
        Z[Max] = tukar
        # Mencetak array setelah setiap iterasi
        print(f"Iterasi {len(Z) - i}: {Z}")
    return Z


