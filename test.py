import mysql.connector

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Baihaqi123321",
    database="db_login"
)

mycursor = mydb.cursor()


def register():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Registrasi berhasil! Silakan login.\n")
    except mysql.connector.Error as err:
        print("Registrasi gagal:", err, "\n")


def login():
    username = input("Username: ")
    password = input("Password: ")

    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        print(f"Login berhasil! Selamat datang, {username}.\n")
    else:
        print("Username atau password salah.\n")


def menu():
    while True:
        print("=== MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")


menu()