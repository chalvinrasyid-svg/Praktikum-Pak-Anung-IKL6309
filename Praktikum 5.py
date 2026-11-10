'''
latihan 1 membuat fungsi yang mengembalikan peringkat dari nilai huruf.
'''
#LATIHAN PERTAMA
#Chalvin Azyzir Rasyid
#065002600005
def ord_nilai_huruf(huruf):
    if huruf == "A":
        peringkat = 9
    elif huruf == "A-":
        peringkat = 8
    elif huruf == "B+":
        peringkat = 7
    elif huruf == "B":
        peringkat = 6
    elif huruf == "B-":
        peringkat = 5
    elif huruf == "C":
        peringkat = 4
    elif huruf == "C-":
        peringkat = 3
    elif huruf == "D":
        peringkat = 2
    elif huruf == "E":
        peringkat = 1
    else:
        peringkat = None
        
    return peringkat

#Chalvin Azyzir Rasyid
#065002600005
total_nilai = 0
jumlah_data = 0

while True:
    input_huruf = input("Masukkan nilai huruf (atau ketik 'keluar' untuk berhenti): ")
    
    if input_huruf.lower() == "keluar":
        print("Program selesai. Terima kasih!")
        break
        
    hasil = ord_nilai_huruf(input_huruf)
    print(f"Peringkat untuk nilai {input_huruf} adalah: {hasil}\n")
    
    
    if hasil is not None:
        total_nilai += hasil
        jumlah_data += 1

#Chalvin Azyzir Rasyid
#065002600005
if jumlah_data > 0:
    rata_rata = total_nilai / jumlah_data
    print(f"Rata-rata peringkat: {rata_rata}")
    



'''Latihan 2 membuat program tiket bioskop dengan perulangan while.'''
#Chalvin Azyzir Rasyid
#065002600005
total_harga = 0.0

while True:
    umur_input = input("masukkan umur:")
    
    if umur_input == "":
        break
        
    umur = int(umur_input)
    
    if umur <= 2:
        harga = 0.0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14.0
        print("Harga $14.00")
    elif umur >= 65:
        harga = 18.0
        print("Harga $18.00")
    else:
        harga = 23.0
        print("Harga $23.00")
        
    total_harga += harga
    print(f"Running total: {total_harga:.2f}")
    
#Chalvin Azyzir Rasyid
#065002600005
uang_dibayar = float(input("masukkan jumlah uang: "))
kembalian = uang_dibayar - total_harga
print(f"Running kembalian: {kembalian:.2f}")
