#Chalvin Azyzir Rasyid
#065002600005
#LATIHAN PERTAMA
def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

def tampilkan_hasil_prima(angka):
    if cek_prima(angka):
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")

angka_input = int(input("Masukkan angka: "))
tampilkan_hasil_prima(angka_input)


#LATIHAN KEDUA
def get_ordinal(angka):
    if angka == 0:
        return (0, 'th')
    
    akhiran_terakhir = angka % 10
    
    
    if akhiran_terakhir == 1 and angka != 11:
        suffix = 'st'
    elif akhiran_terakhir == 2 and angka != 12:
        suffix = 'nd'
    elif akhiran_terakhir == 3 and angka != 13:
        suffix = 'rd'
    else:
        suffix = 'th'
        
    return (angka, suffix)

#Chalvin Azyzir Rasyid
#065002600005

print("Ordinal Number")
print("ketik 0 untuk mengentikan program")

while True:
    angka_input = int(input("masukkan angka: "))
    hasil = get_ordinal(angka_input)
    print(hasil)
    
    if angka_input == 0:
        print("terima kasih telah menggunakan program saya")
        break








