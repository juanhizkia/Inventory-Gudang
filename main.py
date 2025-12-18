# Inventory sederhana menggunakan pyhton
inventory = {}

def tampilkan_inventory():
    if not inventory:
        print("Inventory kosong.")
    else:
        print("\nDaftar Barang:")
        for nama, jumlah in inventory.items():
            print(f"- {nama}: {jumlah}")

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah: "))
    
    if nama in inventory:
        inventory[nama] += jumlah
    else:
        inventory[nama] = jumlah
    
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    
    if nama in inventory:
        del inventory[nama]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== MENU INVENTORY ===")
    print("1. Lihat Inventory")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tampilkan_inventory()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
