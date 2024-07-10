data_mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    data_mahasiswa.append({"NIM": nim, "Nama": nama})
    maulagi = input("Apakah ingin menambahkan data lagi? (yes/no): ").lower()

    if maulagi == "no":
        break
print("\nData Mahasiswa:")

for data in data_mahasiswa:
    print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")