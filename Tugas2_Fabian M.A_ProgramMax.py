print(">>>>> Program Menentukan Max <<<<<")
print("Nama : Fabian Malquinn Andrian")
print("Kelas : X-PPLG\n")

bilangan1 = int(input("Masukkan Bilangan 1 : "))
bilangan2 = int(input("Masukkan Bilangan 2 : "))
bilangan3 = int(input("Masukkan Bilangan 3 : "))

if bilangan1 > bilangan2 and bilangan1 > bilangan3:
    hasil = bilangan1
else:
    if bilangan2 > bilangan3:
        hasil = bilangan2
    else:
        hasil = bilangan3

print("\nBilangan Terbesar Adalah", hasil)
print("\nPROGRAM SELESAI @FABIAN")
