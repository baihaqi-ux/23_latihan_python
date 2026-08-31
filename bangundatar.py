import math


def persegi():
    sisi = float(input("Sisi: "))
    print(f"Luas = {sisi * sisi}")
    print(f"Keliling = {4 * sisi}")


def persegi_panjang():
    p = float(input("Panjang: "))
    l = float(input("Lebar: "))
    print(f"Luas = {p * l}")
    print(f"Keliling = {2 * (p + l)}")


def lingkaran():
    jari = float(input("Jari-jari: "))
    print(f"Luas = {math.pi * jari * jari:.2f}")
    print(f"Keliling = {2 * math.pi * jari:.2f}")


def hitung_bangun_datar():
    print("\n1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    pilihan = input("Pilih bangun datar: ").strip()

    if pilihan == "1":
        persegi()
    elif pilihan == "2":
        persegi_panjang()
    elif pilihan == "3":
        lingkaran()
    else:
        print("Pilihan tidak valid.")