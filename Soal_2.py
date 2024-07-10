import pandas as pd
Nilai = [
    [90, 80],  
    [50, 60],  
    [65, 70]  
]

df = pd.DataFrame(Nilai, 
    columns=['algoritma dan struktur Data 2', 'matematika numerik'], 
    index=['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'])

total_algoritma = sum(df['algoritma dan struktur Data 2'])
total_matematika = sum(df['matematika numerik'])
algoritma = total_algoritma / len(df)
matematika = total_matematika / len(df)

print("\nRata-Rata Nilai Setiap Mata Kuliah:")
print(f"Algoritma dan Struktur Data 2: {algoritma}")
print(f"Matematika Numerik: {matematika}")

print("\nNilai Rata-Rata Setiap Mahasiswa:")
for i in df.index:
    total_mahasiswa = sum(df.loc[i])
    mahasiswa = total_mahasiswa / len(df.columns)
    print(f"{i}:{mahasiswa}")