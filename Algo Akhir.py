
# import webbrowser
# import os

# file_path = os.path.abspath("peta.html")
# webbrowser.open(f"file://{file_path}")

# # masuk gak guys? hah
# # haloo \

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="nama_database",  
    user="postgres",           
    password="password"       
)
cur = conn.cursor()

def selection_sort_by_stok(data, ascending=True):
    n = len(data)
    for i in range(n):
        idx_extreme = i
        for j in range(i + 1, n):
            if ascending:
                if data[j][2] < data[idx_extreme][2]:  
                    idx_extreme = j
            else:
                if data[j][2] > data[idx_extreme][2]:
                    idx_extreme = j
        data[i], data[idx_extreme] = data[idx_extreme], data[i]
    return data


def ambil_semua_data():
    cur.execute("SELECT * FROM sayur")
    return cur.fetchall()

def tampilkan_data(data):
    print("\nData Sayur:")
    for row in data:
        print(f"ID: {row[0]}, Nama: {row[1]}, Stok: {row[2]}, Harga: {row[3]}")

def cari_sayur_berdasarkan_nama(nama_sayur):
    cur.execute("SELECT * FROM sayur WHERE LOWER(nama_sayur) LIKE %s", ('%' + nama_sayur.lower() + '%',))
    hasil = cur.fetchall()
    print(f"\nHasil Pencarian untuk '{nama_sayur}':")
    if hasil:
        tampilkan_data(hasil)
    else:
        print("Tidak ditemukan.")


def menu():
    while True:
        print("\n==== Menu Pengelolaan Stok Sayur ====")
        print("1. Tampilkan sayur dengan stok paling sedikit (Selection Sort)")
        print("2. Cari sayur berdasarkan nama")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            data = ambil_semua_data()
            data_sorted = selection_sort_by_stok(data, ascending=True)
            tampilkan_data(data_sorted)
        elif pilihan == '2':
            nama = input("Masukkan nama sayur yang ingin dicari: ")
            cari_sayur_berdasarkan_nama(nama)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

menu()

cur.close()
conn.close()

print ("hellow wolrd")

import psycopg2
import webbrowser
import os

file_path = os.path.abspath("peta.html")
webbrowser.open(f"file://{file_path}")


# mhaloo