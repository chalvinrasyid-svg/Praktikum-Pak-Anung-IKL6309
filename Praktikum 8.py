#LATIHAN PERTAMA
def penjumlahan_rekursif(batas, iterasi=1):
    if iterasi > batas:
        return 0
    
    return int(input(f"Masukkan bilangan ke-{iterasi}: ")) + penjumlahan_rekursif(batas, iterasi + 1)

jumlah = int(input("Masukkan Jumlah: "))
print(f"Hasil dari penjumlahan adalah: {penjumlahan_rekursif(jumlah)}")
#Chalvin Azyzir Rasyid
#065002600005

#LATIHAN KEDUA
def pangkat_rekursif(base, power):
    if power == 0:
        return 1
    elif power > 0:
        return base * pangkat_rekursif(base, power - 1)
    else:
        return (1 / base) * pangkat_rekursif(base, power + 1)
    
#Chalvin Azyzir Rasyid
#065002600005
def jalankan_program():
    print("\nIni merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    base_input = input("Masukkan Angka: ")
    
    
    if base_input == "":
        print("Program Selesai")
        return 
        
    power_input = int(input("Masukkan Pangkatnya: "))
    base = float(base_input) 
    
    
    hasil = pangkat_rekursif(base, power_input)
    
    
    if isinstance(hasil, float) and hasil.is_integer():
        hasil = int(hasil)
        
    print(f"Hasilnya adalah: {hasil}")
    
    
    jalankan_program()


jalankan_program()