# Latihan OOP Dasar Python

# 1. Membuat class Mobil
class Mobil:
    def __init__(self, merk, warna):
        # atribut (data yang dimiliki oleh objek)
        self.merk = merk
        self.warna = warna

    def jalan(self):
        # method (aksi yang bisa dilakukan objek)
        print(f"Mobil {self.merk} sedang berjalan")

    def info(self):
        print(f"Merk: {self.merk}, Warna: {self.warna}")

# ========== LATIHAN ==========

# A. Buat objek dari class Mobil
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

# B. Panggil method jalan() dari masing-masing objek
mobil1.jalan()   # Output: Mobil Toyota sedang berjalan
mobil2.jalan()   # Output: Mobil Honda sedang berjalan

# C. Tampilkan info mobil
mobil1.info()    # Output: Merk: Toyota, Warna: Merah
mobil2.info()    # Output: Merk: Honda, Warna: Hitam

# ========== TUGAS MANDIRI ==========

# 1. Buat objek mobil lain dengan merk dan warna berbeda!
# 2. Tampilkan info dan panggil method jalan() dari mobil yang kamu buat!
# 3. Upload jawabanmu di Space untuk direview!