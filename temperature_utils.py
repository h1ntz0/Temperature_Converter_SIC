# utils.py
# Fungsi untuk konversi suhu

def konversi_suhu(nilai, dari, ke):
    # Biar input ga case sensitive (huruf besar/kecil sama aja)
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid! Gunakan hanya C, F, atau K."

    # Validasi suhu (K ga boleh negatif)
    if dari == "k" and nilai < 0:
        return "Error: Nilai Kelvin tidak boleh negatif."

    # Kalau satuan asal == tujuan, langsung return
    if dari == ke:
        return f"Hasil: {nilai}°{dari.upper()}"

    hasil = None

    # Konversi berdasarkan satuan
    # Celsius -> Fahrenheit
    if dari == "c" and ke == "f":
        hasil = (nilai * 9/5) + 32
    # Celsius -> Kelvin
    elif dari == "c" and ke == "k":
        hasil = nilai + 273.15
    # Fahrenheit -> Celsius
    elif dari == "f" and ke == "c":
        hasil = (nilai - 32) * 5/9
    # Fahrenheit -> Kelvin
    elif dari == "f" and ke == "k":
        hasil = (nilai - 32) * 5/9 + 273.15
    # Kelvin -> Celsius
    elif dari == "k" and ke == "c":
        hasil = nilai - 273.15
    # Kelvin -> Fahrenheit
    elif dari == "k" and ke == "f":
        hasil = (nilai - 273.15) * 9/5 + 32

    return f"Hasil: {nilai}°{dari.upper()} = {hasil:.2f}°{ke.upper()}"
