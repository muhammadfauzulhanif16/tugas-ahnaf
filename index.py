# pegawai1 = {
#   nama: "Ahmad",
#   agama: "Islam",
#   gajiPokok: 4000000,
#   anak: 2
# }

# pegawai2 = {
#   nama: "Alex",
#   agama: "Kristen Protestan",
#   gajiPokok: 6000000,
#   anak: 5
# }

print("Masukan nama:")
nama = input()
print("Masukan agama:")
agama = input()
print("Masukan jumlah gaji pokok:")
gajiPokok = input()
print("Masukan jumlah anak:")
anak = input()

print("SLIP GAJI PT. XXX")
print("-----------------")
print("- Nama Pegawai       :", nama)
print("- Agama              :", agama)
print("- Jumlah Anak        :", anak)
print("- Gaji pokok         : Rp.", gajiPokok)


# tunjangan jabatan
tunjanganJabatan = int(gajiPokok) * 20 / 100
print("- Tunjangan Jabatan  : Rp.", int(tunjanganJabatan))

# tunjangan keluarga
if int(anak) <= 2:
    tunjanganKeluarga = int(gajiPokok) * 10 / 100
    print("- Tunjangan Keluarga : Rp.", int(tunjanganKeluarga))
else:
    tunjanganKeluarga = int(gajiPokok) * 20 / 100
    print("- Tunjangan Keluarga : Rp.", int(tunjanganKeluarga))

# gaji kotor
gajiKotor = int(gajiPokok) + tunjanganJabatan + tunjanganKeluarga
print("- Gaji Kotor         : Rp.", int(gajiKotor))

# zakat profesi
# if agama == "Islam" and gajiKotor >= 6000000:
#     zakatProfesi = gajiKotor * 2.5 / 100
#     print("- Zakat Profesi      : Rp.", int(zakatProfesi))
# else:
#     zakatProfesi = 0
#     print("- Zakat Profesi      : Rp.", int(zakatProfesi))

zakatProfesi = (0, 0.025)[
    agama == "Islam" and gajiKotor >= 6000000] * gajiKotor
print("- Zakat Profesi      : Rp.", int(zakatProfesi))

# gaji bersih
if zakatProfesi:
    gajiBersih = gajiKotor - zakatProfesi
    print("- Take Home Pay      : Rp.", int(gajiBersih))
else:
    gajiBersih = gajiKotor
    print("- Take Home Pay      : Rp.", int(gajiBersih))
