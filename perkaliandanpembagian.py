def perkalian(a, b):
    return a * b


def pembagian(a, b):
    if b == 0:
        return None
    return a / b


def hitung():
    print("\n1. Perkalian")
    print("2. Pembagian")
    pilihan = input("Pilih operasi: ").strip()

    try:
        a = float(input("Bilangan pertama: "))
        b = float(input("Bilangan kedua: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pilihan == "1":
        print(f"Hasil = {perkalian(a, b)}")
    elif pilihan == "2":
        hasil = pembagian(a, b)
        if hasil is None:
            print("Tidak bisa membagi dengan nol.")
        else:
            print(f"Hasil = {hasil}")
    else:
        print("Pilihan tidak valid.")