#LATIHAN PERTAMA
def cek_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

#Chalvin Azyzir Rasyid
#065002600005

def jumlah_hari(bulan, tahun=0):
    bulan_31 = [1, 3, 5, 7, 8, 10, 12]
    bulan_30 = [4, 6, 9, 11]
    
    if bulan in bulan_31:
        return 31
    elif bulan in bulan_30:
        return 30
    elif bulan == 2:
        
        if cek_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return 0
    
#Chalvin Azyzir Rasyid
#065002600005
#LATIHAN KEDUA
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan_input = int(input("masukkan bulan (1-12): "))
    
    
    if bulan_input == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break
        
    
    if bulan_input == 2:
        tahun_input = int(input("masukkan tahun (e.g., 2021): "))
        hari = jumlah_hari(bulan_input, tahun_input)
    else:
        hari = jumlah_hari(bulan_input)
        
    print(f"{hari} hari dalam sebulan")
