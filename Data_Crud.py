# Koneksi Database
import mysql.connector
import os
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'tugas_alpro'
)
print("Database Berhasil Terkoneksi")

def insert_data(conn):
    count = 0
    while True:
        id = input("Massukan id Barang : ")
        nama_barang = input("Massukan Nama Barang : ")
        jumlah = int(input("Massukan Jumlah Barang : "))
        satuan = input("Massukan Satuan Barang : ")
        harga = int(input("Massukan Harga Barang Rp. : "))
        cursor = conn.cursor()
        sql = "INSERT INTO alpro (id, nama_barang, jumlah, satuan, harga) VALUES (%s, %s, %s, %s, %s)"
        value = (id, nama_barang, jumlah, satuan, harga)
        cursor.execute(sql, value)
        conn.commit()
        count += 1

        os.system('cls')
        lagi = input("Apakah Ingin Menambah Data Lagi ? [Y/T] : ")
        if lagi != "y" and lagi != 'Y':
            print("{} Data berhasil disimpan".format(count))
            print("")
            show_menu(conn)
            break

def update_data(conn):
    count = 0
    while True:
        cursor = conn.cursor()
        show_data(conn)
        id = input("Pilih id yang ingin diubah : ")
        cursor.execute("SELECT * FROM alpro WHERE id="+id)
        result = cursor.fetchall()
        for value in result:
            nama_barang = input("Nama barang : "+value[1]+ " -> ") or value[1]
            jumlah = input("Jumlah : "+str(value[2])+ " -> ") or str(value[2])
            satuan = input("Satuan : "+value[3]+ " -> ") or value[3]
            harga = input("Harga barang Rp.  : "+str(value[4])+ " -> ") or str(value[4])
        sql = "UPDATE alpro SET nama_barang=%s, jumlah=%s, satuan=%s, harga=%s WHERE id=%s"
        val = (nama_barang, jumlah, satuan, harga, id)
        cursor.execute(sql, val)
        conn.commit()
        count += 1

        os.system('cls')
        lagi = input("Apakah ingin mengubah data lagi [Y/T] : ")
        if lagi != 'y' and lagi != 'Y':
            print("{} Data berhasil diubah".format(count))
            print("")
            show_menu(conn)
            break

def delete_data(conn):
    count = 0
    while True:
        cursor = conn.cursor()
        show_data(conn)
        id = input("Pilih id yang ingin dihapus : ")
        yakin = input("Apakah yakin menghapus data ini [Y/T] : ")
        if yakin == 'y' or yakin =='Y':
            sql = "DELETE FROM alpro WHERE id=%s"
            val = (id,)
            cursor.execute(sql, val)
            conn.commit()
        count += 1

        os.system('cls')
        lagi = input("Apakah ingin menghapus data lagi [Y/T] : ")
        if lagi != 'y' and lagi != 'Y':
            print("{} Data berhasil dihapus".format(count))
            print("")
            show_menu(conn)
            break

def show_data(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM alpro"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:
        print("-"*85)
        print("{:<10}{:<20}{:<20}{:<20}{:<20}".format("ID", "Nama Barang ", "Jumlah", "Satuan", "Harga"))
        print("-"*85)
        for value in results:
            harga = "{:,}".format(value[4]).replace(",", ".")
            print("{:<10}{:<20}{:<20}{:<20}{:>10}".format(value[0], value[1], value[2], value[3], harga))
        print("="*85)
        print("")
    else:
        print("Tidak ada data yang tersedia!")
        print("")

def show_menu(conn):
    while True:
        print("*"*10, "APLIKASI DATABASE PYTHON", "*"*10)
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("x. Keluar")
        print("-"*20)
        menu = input("Pilih menu >> ")
        os.system('cls')
        if menu == "1":
            insert_data(conn)
        elif menu == "2":
            update_data(conn)
        elif menu == "3":
            delete_data(conn)
        elif menu == "4":
            show_data(conn)
        elif menu == "x":
            print("*"*10, "TERIMA KASIH", "*"*10)
            exit()
        else:
            os.system('cls')
            print("Maaf, Pilihan Menu tidak tersedia!")
            coba_lagi = input("Pilih Menu lagi [Y/T] : ")
            print("-"*30, "\n")
            if coba_lagi == 't' or coba_lagi =="T":
                break
show_menu(conn)
