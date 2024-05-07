# def hitung_bmi(berat, tinggi):
#     bmi = berat / (tinggi ** 2)
#     return bmi

# def menentukan_kategori(bmi):
#    if 18.5 <= bmi < 25:
#         return "Berat badan normal"
#    elif 25 <= bmi < 30:
#         return "Kelebihan berat badan"
#    else:
#         return "Obesitas"

# def main():
#     berat = float(input("Masukkan berat badan Anda (kg): "))
#     tinggi = float(input("Masukkan tinggi badan Anda (cm): "))

#     bmi = hitung_bmi(berat, tinggi)

#     print(f"Berat Badan : {berat}")

#     print(f"Tinggi Badan : {tinggi}")

#     print("Nilai BMI Anda adalah:", bmi)

#     if menentukan_kategori(bmi):
#         print("Kategori BMI : Berat Badan Normal.")
#     else:
#         print("Kategori BMI : Berat Badan Tidak Normal.")

# if __name__ == "__main__":
#     main()

def hitung_bmi(berat, tinggi):
    bmi = berat / ((tinggi / 100) ** 2)
    return bmi

def menentukan_kategori(bmi):
    if  bmi < 18.5:
        return "Berat badan tidak normal"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def main():
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (cm): "))

    bmi = hitung_bmi(berat, tinggi)

    print(f"Berat Badan : {berat} kg")
    print(f"Tinggi Badan : {tinggi} cm")
    print("Nilai BMI Anda adalah:", bmi)

    kategori = menentukan_kategori(bmi)
    print("Kategori BMI :", kategori)

if __name__ == "__main__":
    main()
