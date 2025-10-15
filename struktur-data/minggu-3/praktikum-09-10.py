class Kelas:
    def __init__(self, NIM, nama):
        self.NIM = NIM
        self.nama = nama
    def tampilkan(self):
        print("NIM:", self.NIM)
        print("Nama:", self.nama)

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mahasiswa1 = Kelas("123456789", "Izam Rosiawan")
    mahasiswa2 = Kelas("987654321", "John Doe")
    
    # Menampilkan data mahasiswa
    print("Data Mahasiswa 1:")
    mahasiswa1.tampilkan()
    
    print("\nData Mahasiswa 2:")
    mahasiswa2.tampilkan()
