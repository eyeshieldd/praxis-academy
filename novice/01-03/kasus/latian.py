class AnggotaSekolah:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

        print ('membuat anggota sekolah baru: %s' % self.nama)

    def info(self):
        "cetak info"
        print ('Nama: %s, Umur: %s' % (self.nama, self.umur))


class Guru(AnggotaSekolah):
    "representasi guru"
    def __init__(self, nama, umur, gaji):
        AnggotaSekolah.__init__(self, nama, umur)
        self.gaji = gaji

        print ('membuat guru: %s' % self.nama)

    def info(self):
        AnggotaSekolah.info(self)
        print ('Gaji: %s' % self.gaji)


class Siswa(AnggotaSekolah):
    "representasi siswa"
    def __init__(self, nama, umur, nilai):
        AnggotaSekolah.__init__(self, nama, umur)
        self.nilai = nilai

        print ('membuat siswa: %s' % self.nama)

    def info(self):
        AnggotaSekolah.info(self)
        print ('Nilai: %s' % self.nilai)


guru = Guru('Budi', 40, 3444444)
siswa = Siswa('Andi', 25, 75)


print()

anggota = [guru, siswa]

for orang in anggota:
    orang.info()