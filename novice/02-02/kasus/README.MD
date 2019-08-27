# PENGERTIAN UNIT TESTING
Dalam pemrograman komputer, unit testing adalah metode dimana unit individu dari kode sumber, menetapkan satu atau lebih modul program komputer bersama-sama dengan data kontrol terkait, prosedur penggunaan, dan prosedur operasi diuji untuk menentukan apakah mereka layak digunakan. Secara intuitif, kita dapat melihat unit sebagai bagian diuji terkecil dari sebuah aplikasi. Dalam pemrograman prosedural unit bisa menjadi modul seluruh tetapi lebih umum fungsi individu atau prosedur. Dalam pemrograman berorientasi obyek unit sering merupakan seluruh antarmuka, seperti kelas, tetapi bisa menjadi metode individu. Unit test yang dibuat oleh programmer atau kadang-kadang oleh penguji kotak putih selama proses pembangunan
##EXAMPLE
def kurang(x, y):
    return x - y


class TestCalc(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(10, 5), 15) #membandingkan dengan operasi tambah, apakah 10+5 = 15
        self.assertEqual(tambah(-1, 1), 0)
        self.assertEqual(tambah(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()