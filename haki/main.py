from ganjilgenap import cek_ganjil_genap
from ifelse import cek_kelulusan
from perkaliandanpembagian import hitung
from bangundatar import hitung_bangun_datar


def main():
    print("=== PROGRAM UTAMA ===")
    print("1. Cek Ganjil/Genap")
    print("2. Cek Kelulusan")
    print("3. Perkalian & Pembagian")
    print("4. Bangun Datar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        cek_ganjil_genap()
    elif pilihan == "2":
        cek_kelulusan()
    elif pilihan == "3":
        hitung()
    elif pilihan == "4":
        hitung_bangun_datar()
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()