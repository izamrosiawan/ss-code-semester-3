import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv("penjualan.csv")

# Total penjualan
total = data["jumlah"].sum()
print("Total penjualan:", total)

# Rata-rata penjualan
rata_rata = data["jumlah"].mean()
print("Rata-rata penjualan:", rata_rata)

# Penjualan maksimum
maksimum = data["jumlah"].max()
print("Penjualan maksimum:", maksimum)