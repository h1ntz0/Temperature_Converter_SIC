# main.py
# Program utama untuk konversi suhu
from temperature_utils import konversi_suhu

print("=== KONVERSI SUHU ===")

# Minta input dari user
try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ")
    ke = input("Ke satuan (C/F/K): ")

    # Panggil fungsi dari utils.py
    hasil = konversi_suhu(nilai, dari, ke)
    print(hasil)

except ValueError:
    print("Error: Input harus berupa angka untuk nilai suhu!")
