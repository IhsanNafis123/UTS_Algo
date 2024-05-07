
def penjumlahan(a,b) :
    return a + b
def pengurangan(a,b) :
    return a - b
def sisa_bagi(a,b) :
    return a % b

def eksekusi_operasi():
    print("Pilihan operasi matematika:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Modulus")


    pilihan = int(input("Masukkan pilihan Anda: "))
    bilangan1 = float(input("Masukkan bilangan pertama: "))
    bilangan2 = float(input("Masukkan bilangan kedua: "))

  
    if pilihan == 1:
        hasil = penjumlahan (bilangan1, bilangan2)
        operasi = "penjumlahan"
    elif pilihan == 2:
        hasil = pengurangan(bilangan1, bilangan2)
        operasi = "pengurangan"
    elif pilihan == 3:
        hasil = sisa_bagi(bilangan1, bilangan2)
        operasi = "Modulus"
    else:
        print("Pilihan tidak valid")
        return

    print(f"Hasil {operasi}: {hasil}")

if __name__ == "__main__":
    while True:
        eksekusi_operasi()
        ulangi = input("Apakah Anda ingin melanjutkan (y/n)? ")
        if ulangi.lower() != 'y':
            break