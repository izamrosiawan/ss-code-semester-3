class Mahasiswa:
    # Konstruktor
    def __init__(self):
        self.nim = ""          # menggantikan char nim[10]
        self.nilai1 = 0        # menggantikan int nilai1
        self.nilai2 = 0        # menggantikan int nilai2

    # Primitif: Prosedur input (menggantikan procedure inputMhs)
    def input_mhs(self):
        """Prosedur untuk input data mahasiswa"""
        self.nim = input("input nama = ")
        self.nilai1 = int(input("input nilai1 = "))
        self.nilai2 = int(input("input nilai2 = "))

    # Primitif: Fungsi rata-rata (menggantikan function rata2)
    def rata2(self):
        """Fungsi untuk menghitung rata-rata nilai"""
        return (self.nilai1 + self.nilai2) / 2

# Program utama
def main():
    # Membuat objek mahasiswa (menggantikan mahasiswa mhs;)
    mhs = Mahasiswa()

    # Memanggil prosedur input
    mhs.input_mhs()

    # Memanggil fungsi rata-rata dan menampilkan hasil
    print(f"rata-rata = {mhs.rata2()}")

if __name__ == "__main__":
    main()
