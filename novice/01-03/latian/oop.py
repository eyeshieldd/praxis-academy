class Orang:
    total = 0
    def __init__(self, nama):
        self.nama = nama
        Orang.total += 1
        
    def katakanHalo(self):
        print ('Halo, nama saya %s, apa kabar' %self.nama)
    def __del__(self):
        Orang.total -=1
    def total_populasi(cls):
        print ('Total Orang %s' % cls.total)
        
    total_populasi = classmethod(total_populasi)

org = Orang('budi')
org.katakanHalo()
Orang.total_populasi()


org2 = Orang('joni')
org2.katakanHalo()
Orang.total_populasi()

print ('objek dihapus')
del org
del org2

Orang.total_populasi()
