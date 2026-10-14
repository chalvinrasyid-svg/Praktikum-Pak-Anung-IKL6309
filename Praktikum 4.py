print("Program Perulangan Angka Menurun")
#Chalvin Azyzir Rasyid 
#065002600005 
for i in range(7, 0, -1):
    print(str(i) * i)
    
print("--- Program Penentu Jumlah Hari dalam Bulan (While Loop) ---")
status = "y"
while status.lower() == "y":
    
    tahun = int(input("\nMasukkan Tahun (contoh: 2026): "))
    bulan = int(input("Masukkan Bulan (1-12): "))
    
    if 1 <= bulan <= 12:
        
        if bulan == 2:
            
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                jumlah_hari = 29
                keterangan = "Tahun Kabisat"
            else:
                jumlah_hari = 28
                keterangan = "Bukan Tahun Kabisat"
            print(f"Bulan 2 (Februari) tahun {tahun} ({keterangan}) memiliki {jumlah_hari} hari.")
            
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            print(f"Bulan ke-{bulan} pada tahun {tahun} memiliki 31 hari.")
            
        else:
            print(f"Bulan ke-{bulan} pada tahun {tahun} memiliki 30 hari.")
    else:
        print("!- Error: Masukkan angka bulan antara 1 sampai 12 dengan benar -! ")
        
    status = input("\nApakah Anda ingin menghitung lagi? (y/n): ")

print("\nTerima kasih telah menggunakan program ini!")
