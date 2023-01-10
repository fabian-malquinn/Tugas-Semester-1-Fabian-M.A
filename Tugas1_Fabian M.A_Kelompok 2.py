#JUDUL
print ("="*10,"PROGRAM KASIR","="*10)

#DEKLARASI
barang1 = input ("Barang ke-1 : ")
harga1 = int(input ("Harga : "))
barang2 = input ("Barang ke-2 : ")
harga2 = int(input ("Harga : "))
barang3 = input ("Barang ke-3 : ")
harga3 = int(input ("Harga : "))
total1 = harga1 + harga2 + harga3
total2 = total1-(total1*20/100)

#PROSES / OUTPUT
print (f"\nPelanggan Membeli : \n1. {barang1} Rp. {harga1:,} \n2. {barang2} Rp. {harga2:,} \n3. {barang3} Rp. {harga3:,}")
print (f"Total : Rp. {total1:,}\n")
print (f"Dapat Diskon 20%!")
print (f"Total Yang Harus Dibayar Pelanggan : Rp. {int (total2):,}")
uang1 = int (input("Uang Pelanggan : "))
print (f"Kembalian : {uang1 - int (total2):,}")
print ("\nTerima Kasih!")





