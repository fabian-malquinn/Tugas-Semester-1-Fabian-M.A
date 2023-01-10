print("==========ATM==========")

saldo1 = 1000000
print(f"Anda Memiliki Saldo Sebesar Rp. {saldo1:,}")

saldo2 = int(input("Masukkan Jumlah Saldo Yang Akan Ditarik : "))

if saldo2 <= 1000000:
    print(f"\nAnda Telah Menarik Saldo Sebesar Rp. {saldo2:,}")
    print(f"Total Saldo Anda Sebesar Rp. {saldo1 - saldo2:,}")
else:
    print("Saldo Anda Tidak Cukup")


