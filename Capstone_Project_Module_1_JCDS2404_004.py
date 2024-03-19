from tabulate import tabulate

stokProduk=[
     {'Kode Produk' : 'LAP-001', 
     'Nama Produk' : 'Laptop Acer', 
     'Jumlah Awal' : 200, 
     'Pemasukan' : 60,
     'Pengeluaran' : 40, 
     'Harga Satuan' : 5000000},
    {'Kode Produk' : 'PHO-002',
     'Nama Produk' : 'Smartphone Samsung',
     'Jumlah Awal' : 100,
     'Pemasukan': 60,
     'Pengeluaran' : 50,
     'Harga Satuan' : 2000000},
    {'Kode Produk' : 'REF-003',
     'Nama Produk' : 'Kulkas LG',
     'Jumlah Awal' : 80,
     'Pemasukan' : 50,
     'Pengeluaran' : 20,
     'Harga Satuan' : 3000000},
    {'Kode Produk' : 'BLE-004',
     'Nama Produk' : 'Belender Philips',
     'Jumlah Awal' : 70,
     'Pemasukan' : 40,
     'Pengeluaran' : 30,
     'Harga Satuan' : 500000}
]

for kolom in stokProduk:
    kolom['Jumlah Akhir'] = kolom['Jumlah Awal'] + kolom['Pemasukan'] - kolom['Pengeluaran'] #Jumlah Akhir
    kolom['Nilai Akhir Stok'] = kolom['Jumlah Akhir'] * kolom['Harga Satuan'] #Nilai Akhir Stok

def fiturUtama():
     while True:
        pilihanFitur=input('''
                Aplikasi Laporan Stok Barang
                Gudang PT Eramaju
                            
                Silahkan Pilih Fitur Di bawah ini:
                1. Menampilkan Laporan Stok Gudang
                2. Memperbarui Stok Barang
                3. Menambah Produk
                4. Menghapus Produk
                5. Keluar Aplikasi
                Masukkan Nomor Fitur yang ingin dijalankan :   ''')
        print("\n")
        if pilihanFitur=='1':
             subFitur1()
        elif pilihanFitur=='2':
             subFitur2()
        elif pilihanFitur=='3':
             subFitur3()
        elif pilihanFitur=='4':
             subFitur4()
        elif pilihanFitur== '5':
            print('Aplikasi telah mati!')
            break
        else:
            print("Masukan angka 1/2/3/4/5!")
    

#Menampilkan / Read
def subFitur1():
     while(True):
          subFitur1=input('''
                          -----------Menampilkan Data Stok Produk-----------
                          1. Tampilkan Seluruh Data Stok Produk
                          2. Tampilkan Data Produk Berdasarkan Kode Produk
                          3. Balik ke Fitur Utama
                          Masukkan angka subFitur1 yang ingin dijalankan [1-3]: ''')
          print("\n")
          if subFitur1 == '1':
               menampilkanLaporanSeluruh()
          elif subFitur1 == '2':
               if menampilkanKodeProduk():
                    menampilkanLaporanParsial()
          elif subFitur1 =='3':
               break
          else:
               print("Masukkan Angka 1-3!")

def menampilkanLaporanSeluruh():
    if len(stokProduk) <= 0:
         print('--DATABASE KOSONG, DATA TIDAK TERSEDIA--')
    else:
          headers = ['Kode Produk', 'Nama Produk', 'Jumlah\nAwal\n(Unit)', 'Pemasukan\n(Unit)', 'Pengeluaran\n(Unit)', 'Jumlah\nAkhir\n(Unit)', 'Harga\nSatuan\n(Rp)','Nilai Akhir\nStok (Rp)']
          isi_kolom = [[kolom['Kode Produk'], kolom['Nama Produk'], kolom['Jumlah Awal'], kolom['Pemasukan'], kolom['Pengeluaran'], kolom['Jumlah Akhir'], kolom['Harga Satuan'], kolom['Nilai Akhir Stok']] for kolom in stokProduk]
          print('\n')
          print('LAPORAN STOK GUDANG PT ERAMAJU'.center(115,'-'))
          print(tabulate(isi_kolom, headers=headers, tablefmt='fancy_grid'))
def menampilkanKodeProduk():
    if len(stokProduk) <= 0:
         print('--DATABASE KOSONG, DATA TIDAK TERSEDIA--')
         return False
    else:
         kode_produk = [[kolom['Kode Produk'], kolom['Nama Produk']] for kolom in stokProduk]
         print('\n')
         print("-----Daftar Kode Produk-----")
         print(tabulate(kode_produk, headers=['Kode Produk', 'Nama Produk'], tablefmt='fancy_grid'))
         return True
def menampilkanLaporanParsial():
    kodeProdukPK = input("Ketik Kode Produk Sesuai Data Di Atas: ")
    mengecek_PK = [kolom for kolom in stokProduk if kolom['Kode Produk'] == kodeProdukPK.upper()]
    if mengecek_PK:
        print('\n')
        print('Data Ditemukan')
        print('LAPORAN DETAIL PRODUK PT ERAMAJU'.center(125,'-'))
        headers = ['Kode Produk', 'Nama Produk', 'Jumlah\nAwal\n(Unit)', 'Pemasukan\n(Unit)', 'Pengeluaran\n(Unit)', 'Jumlah\nAkhir\n(Unit)', 'Harga\nSatuan\n(Rp)','Nilai Akhir\nStok (Rp)']
        data = [[kolom['Kode Produk'], kolom['Nama Produk'], kolom['Jumlah Awal'], kolom['Pemasukan'], kolom['Pengeluaran'], kolom['Jumlah Akhir'], kolom['Harga Satuan'], kolom['Nilai Akhir Stok']] for kolom in mengecek_PK]
        print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
    else:
        print('Data tidak ditemukan')

#Memperbarui / Update
def subFitur2():
     while(True):
          subFitur2=input ('''
                           -----------Memperbaharui Data Stok Produk-----------
                           1. Ubah Data Stok Produk
                           2. Balik ke Fitur Utama
                           Masukkan angka subfitur yang ingin dijalankan [1-2]: ''')
          print("\n")
          if subFitur2 == '1':
               memperbaruiLaporan()
          elif subFitur2 == '2':
               break
          else:
               print("Masukkan Angka 1-2!") 

def isDigit(angka):
    return angka.isdigit()
def masukanAngka(teks):
    userInput=input(teks)
    while not isDigit(userInput):
        print('Input harus Angka. Coba lagi!')
        userInput=input(teks)
    return userInput  
def memperbaruiLaporan():
    if menampilkanKodeProduk():
     kodeProdukPembaruan = input("Ketik Kode Produk yang ingin diubah: ")
     mengecek_PK = [produk for produk in stokProduk if produk['Kode Produk'] == kodeProdukPembaruan.upper()]
     if mengecek_PK:
          print('\n')
          print('Data Ditemukan')
          print('LAPORAN DETAIL PRODUK PT ERAMAJU'.center(125,'-'))
          headers = ['Kode Produk', 'Nama Produk', 'Jumlah\nAwal\n(Unit)', 'Pemasukan\n(Unit)', 'Pengeluaran\n(Unit)', 'Jumlah\nAkhir\n(Unit)', 'Harga\nSatuan\n(Rp)','Nilai Akhir\nStok (Rp)']
          data = [[kolom['Kode Produk'], kolom['Nama Produk'], kolom['Jumlah Awal'], kolom['Pemasukan'], kolom['Pengeluaran'], kolom['Jumlah Akhir'], kolom['Harga Satuan'], kolom['Nilai Akhir Stok']] for kolom in mengecek_PK]
          print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
          while True:
               melanjutkan_pembaruan = input("Ketik Y jika ingin melanjutkan Pembaruan Data, T Jika tidak: ")
               if melanjutkan_pembaruan.upper() == 'Y':
                    isi_kolom_pembaruan = input('Ketik Nama Kolom yang ingin diubah [Nama Produk/Jumlah Awal/Pemasukan/Pengeluaran/Harga Satuan]: ').lower()
                    if isi_kolom_pembaruan not in ['nama produk', 'jumlah awal', 'pemasukan', 'pengeluaran', 'harga satuan']:
                         print("Nama Kolom Tidak Ada!")
                    else:
                         if isi_kolom_pembaruan == 'nama produk':
                            data_pembaruan = input(f"Masukkan {isi_kolom_pembaruan} baru: ").title()
                         else:
                              data_pembaruan = masukanAngka(f"Masukkan {isi_kolom_pembaruan} baru: ")
                              
                         for produk in mengecek_PK:  # Perulangan untuk mengupdate semua produk dengan kode yang sama
                              if isi_kolom_pembaruan.lower() in ['jumlah awal', 'pemasukan', 'pengeluaran']:
                                   produk[isi_kolom_pembaruan.title()] = int(data_pembaruan)
                                   produk['Jumlah Akhir'] = produk['Jumlah Awal'] + produk['Pemasukan'] - produk['Pengeluaran']
                                   produk['Nilai Akhir Stok'] = produk['Jumlah Akhir'] * produk['Harga Satuan']
                              else:
                                   produk[isi_kolom_pembaruan.title()] = data_pembaruan
                         print("\nData sudah diperbarui!\n")
                         print(tabulate([list(produk.values()) for produk in mengecek_PK], headers=headers, tablefmt='fancy_grid'))
               elif melanjutkan_pembaruan.upper() == 'T':
                    break
               else:
                    print("Masukan huruf Y atau T!")
     else:
          print("\n")
          print("Data tidak ditemukan!")

#Menambah / Create
def subFitur3():
     while(True):
          subFitur3=input ('''
                           ------Memperbaharui Data Stok Produk------
                           1. Menambah Stok Produk
                           2. Balik ke Fitur Utama
                           Masukkan angka subfitur yang ingin dijalankan [1-2]: ''')
          print("\n")
          if subFitur3 == '1':
               menambahProduk()
          elif subFitur3 == '2':     
               break
          else:
               print("Masukkan Angka 1-2!")
            
def update_table():
    for kolom in stokProduk:
        kolom['Jumlah Akhir'] = kolom['Jumlah Awal'] + kolom['Pemasukan'] - kolom['Pengeluaran']
        kolom['Nilai Akhir Stok'] = kolom['Jumlah Akhir'] * kolom['Harga Satuan']
def print_table():
    headers = ['Kode Produk', 'Nama Produk', 'Jumlah\nAwal\n(Unit)', 'Pemasukan\n(Unit)', 'Pengeluaran\n(Unit)', 'Jumlah\nAkhir\n(Unit)', 'Harga\nSatuan\n(Rp)','Nilai Akhir\nStok (Rp)']
    data = [[kolom['Kode Produk'], kolom['Nama Produk'], kolom['Jumlah Awal'], kolom['Pemasukan'], kolom['Pengeluaran'], kolom['Jumlah Akhir'], kolom['Harga Satuan'], kolom['Nilai Akhir Stok']] for kolom in stokProduk]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
def menambahProduk():
    namaProduk = input('Masukkan Nama Barang: ')
    # Memastikan kode produk yang dimasukkan tidak ada dalam stokProduk
    while True:
        kodeProduk = input('Masukkan Kode Barang: ')
        if not any(kodeProduk == barang['Kode Produk'] for barang in stokProduk):
            break
        else:
            print("Kode produk sudah ada, mohon masukkan kode yang berbeda.")
    # Menginput data
    stokAwal = int(masukanAngka('Masukkan Stok Awal Barang: '))
    pemasukan = int(masukanAngka('Masukkan Jumlah Pemasukan Barang: '))
    pengeluaran = int(masukanAngka('Masukkan Jumlah Pengeluaran Barang: '))
    hargaProdukSatuan = int(masukanAngka('Masukkan Harga Satuan Barang: '))
    # Menambahkan data produk ke stokProduk dengan struktur yang sesuai
    stokProduk.append({
        'Kode Produk': kodeProduk,
        'Nama Produk': namaProduk,
        'Jumlah Awal': stokAwal,
        'Pemasukan': pemasukan,
        'Pengeluaran': pengeluaran,
        'Harga Satuan': hargaProdukSatuan
    })
    
    print('Produk baru telah ditambahkan!')
    update_table()  


#Menghapus / Delete
def subFitur4():
     while(True):
          subFitur3=input ('''
                           ----------Menghapus Data Stok Produk----------
                           1. Menghapus Data Produk
                           2. Balik ke Fitur Utama
                           Masukkan angka subfitur yang ingin dijalankan [1-2]: ''')
          print("\n")
          if subFitur3 == '1':
               menghapusProduk()
          elif subFitur3 == '2':     
               break
          else:
               print("Masukkan Angka 1-2!")

def menghapusProduk():
     if menampilkanKodeProduk():
          kodeProduk = input("Masukkan Kode Produk yang ingin dihapus: ")
          produk_found = False
          for i, produk in enumerate(stokProduk):
               if produk['Kode Produk'] == kodeProduk.upper():
                    produk_found = True
                    break
          if not produk_found:
               print("Produk tidak ditemukan!")
          else:
               while True:
                    delete = input("Hapus data tersebut? [y/t]: ")
                    if delete.lower() != 'y' and delete.lower() != 't':
                         print("Masukkan y/t")
                    elif delete.lower() == 'y':
                         del stokProduk[i]
                         print("\nData telah dihapus!\n")
                         update_table()  # Memperbarui tabel setelah penghapusan
                         break
                    elif delete.lower() == 't':
                         print("\nData tidak terhapus!\n")
                         break
fiturUtama()