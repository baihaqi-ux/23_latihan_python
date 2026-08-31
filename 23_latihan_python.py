#!/usr/bin/env python3
"""
Program Perkalian dan Pembagian
Menghitung hasil perkalian dan pembagian dua bilangan.
"""


def perkalian(a, b):
    return a * b


def pembagian(a, b):
    if b == 0:
        return None
    return a / b


def tabel_perkalian(angka):
    print(f"\nTabel Perkalian {angka}:")
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")


def show_menu():
    print("\n=== PERKALIAN & PEMBAGIAN ===")
    print("1. Perkalian dua bilangan")
    print("2. Pembagian dua bilangan")
    print("3. Tabel perkalian 1-10")
    print("4. Keluar")


def main():
    while True:
        show_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            try:
                a = float(input("Bilangan pertama: "))
                b = float(input("Bilangan kedua: "))
                print(f"Hasil = {perkalian(a, b)}")
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "2":
            try:
                a = float(input("Bilangan yang dibagi: "))
                b = float(input("Pembagi: "))
                hasil = pembagian(a, b)
                if hasil is None:
                    print("Tidak bisa membagi dengan nol.")
                else:
                    print(f"Hasil = {hasil}")
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "3":
            try:
                angka = int(input("Masukkan angka: "))
                tabel_perkalian(angka)
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "4":
            print("Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
