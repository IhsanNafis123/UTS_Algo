tahun = int(input("Masukkan tahun: "))

def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

if tahun_kabisat(tahun):
    print(f"{tahun} merupakan tahun kabisat.")
else:
    print(f"{tahun} merupakan bukan tahun kabisat.")