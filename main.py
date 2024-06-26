
import quick_sort as quick
import insertion_sort as insert
import bubble_sort as bubble
import time
default = [23,4,5,8,1,7,9]

def pesan(msg):
    print("="*48)
    print(msg.center(48))
    print("="*48)
    print("\n"*2)
    
def pilih_Sort(array):
    pesan("PILIH METODE SORTING")
    inputSort = input("Pilih Metode Sorting (1/2/3):\n1.Quick Sort\n2.Insertion Sort\n3.Bubble Sort\nSilahkan masukan pilihan anda  :")
    arrayToSort = array.copy()
    if inputSort == "1":
        pesan("METODE YANG DIPILIH ADALAH QUICK SORT")
        print("Array Awal:", array)
        # Urutkan array menggunakan quicksort
        start_time = time.time()
        sorted_array = quick.quicksort(arrayToSort)
        pesan(f"HASIL SORTING :{sorted_array}")
        end_time = time.time()
        timeAkhir = (end_time - start_time)*1000
        print("Quick Sort time:", timeAkhir,"ms")
    elif inputSort == "2" :
        pesan("METODE YANG DIPILIH ADALAH INSERTION SORT")
        print("Array Awal:", array)
        start_time = time.time()
        sorted_array = insert.insertion_sort(arrayToSort)
        pesan(f"HASIL SORTING :{sorted_array}")
        end_time = time.time()
        timeAkhir = (end_time - start_time)*1000
        print("Insertion Sort time:", timeAkhir,"ms")
    elif inputSort == "3":
        pesan("METODE YANG DIPILIH ADALAH BUBBLE SORT")
        print("Array Awal:", array)
        start_time = time.time()
        sorted_array = bubble.BubbleSort(arrayToSort)
        pesan(f"HASIL SORTING :{sorted_array}")
        end_time = time.time()
        timeAkhir = (end_time - start_time)*1000
        print("Bubble Sort time:", timeAkhir,"ms")
        
    else: 
        print("Maaf inputan anda salah.... silahkan coba lagi :")
        pilih_Sort(array)

def inputData():
        print("Pilih data yang mau anda gunakan ?\n 1. Data Default [23,4,5,8,1,7,9]\n 2. Data Inputan ")
        pilihan = input("Masukan pilihan anda ( 1/2 ) : ")
        if pilihan == "1":
            array = default
            print("Data yang terinput", array)
            pilih_Sort(array)
            
        elif pilihan == "2":
            array = []
            Jumlah = int(input("masukan berapa index array :"))
            for i in range(Jumlah):
                inputArray = int(input(f"Masukkan array index ke-{i}: "))
                array.append(inputArray)
                print("Data yang terinput", array)
            pilih_Sort(array)    
        else: 
            print("Pilihan anda tidak valid" )
                
    
    

            

while True:
    print("="*48)
    print("SELAMAT DATANG DI PROGRAM SORTING DARI KELOMPOK 1")
    print("="*48)
    inputData()
    ulangi = input("Mau melakukan sorting lagi ?(Y/N)")
    print("\n"*3)
    if ulangi.lower() == "n":
        pesan("TERIMA KASIH")
        break
        











