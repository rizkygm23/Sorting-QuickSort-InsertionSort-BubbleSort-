
import quick_sort as quick
import insertion_sort as insert
default = [23,4,5,8,1,7,9]
array = []


def pilih_Sort():
    inputSort = input("Pilih Metode Sorting (1/2/3):\n1.Quick Sort\n2.Insertion Sort\n3.Bubble Sort\nSilahkan masukan pilihan anda  :")
    if inputSort == "1":
        print("Array asli:", array)
        # Urutkan array menggunakan quicksort
        sorted_array = quick.quicksort(array)
        # Tampilkan array yang sudah diurutkan
        print("Array yang sudah diurutkan:", sorted_array)
    elif inputSort == "2" :
        sorted_array = insert.insertion_sort(array)     
        
    
    # elif:
    # else:
    








print("="*48)
print("SELAMAT DATANG DI PROGRAM SORTING DARI KELOMPOK 1")
print("="*48)


while True:
    print("Pilih data yang mau anda gunakan ?\n 1. Data Default [23,4,5,8,1,7,9]\n 2. Data Inputan ")
    pilihan = input("Masukan pilihan anda ( 1/2 ) : ")
    if pilihan == "1":
        array = default
        print("Data yang terinput", array)
        pilih_Sort()
        break
    elif pilihan == "2":
        Jumlah = int(input("masukan berapa index array :"))
        for i in range(Jumlah):
            inputArray = int(input(f"Masukkan array index ke-{i}: "))
            array.append(inputArray)
            print("Data yang terinput", array)
            pilih_Sort()
    else: 
        print("Pilihan anda tidak valid" )
        








    
    






# Buat array dengan 6 elemen acak




