print("""==============================
=                            =
=        TARIF PARKIR        =
=                            =
============================== """)

jam = int(input("Jam Masuk : "))
jam2 = int(input("Jam Keluar : "))
hasil1 = jam2 - jam
tarif = 3500
jam_pertama = (hasil1-1)*2000+tarif
hasil2 = (hasil1+12)
berhasil = False

if hasil1 <= 1 or hasil1 <= 12:
    jam_pertama = (hasil1-1)*2000+tarif

    if hasil1 < 1:
        if hasil1+12 > 0 :
            jam_pertama = (hasil1-1+12)*2000 + tarif
            hasil2 = (hasil1+12)
            berhasil = True
        elif hasil1+12 <= 0:
            berhasil = False

    elif hasil1 <= 12:
        jam_pertama = (hasil1-1)*2000+tarif
        hasil2 = hasil1
        berhasil = True
    else:
        print("Jam Masuk / Keluar Harus Bernilai antara 1 - 12")
else:
    print("Jam Masuk / Keluar Harus Bernilai antara 1 - 12")

if berhasil == True :
    print(f"Tarif = {jam_pertama}")
    print(f"Jam = {hasil2}")
elif hasil1 <0 :
    print("Jam Masuk / Keluar Harus Bernilai antara 1 - 12")



