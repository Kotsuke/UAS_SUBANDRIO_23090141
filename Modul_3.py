from collections import deque

antrian = deque()
def front():
    if len(antrian) < 1: 
        return 'Data Kosong'
    else:
        return antrian[0]
def second():
    if len(antrian) < 2: 
        return 'Data Kosong'
    else:
        return antrian[1]

def enqueue():
    print(f'Antrian Sekarang :{front()}')
    print(f'Antrian Selanjutnya :{second()}:')
    print(f'Jumlah Antrian :{len(antrian)}')
    print('pilihan :')
    print('1. Tambah Antrian')
    print('2. Antrian Selanjutnya')
    print('3. lihat Antrian')
    print('4. keluar')
    i = input('Masukan Pilihan :')
    if i  == ('1'):
        data = input('Tambahkan Antrian :')
        antrian.append(data)
        print('Berhasil ditambahkan Keantrian')
    if i == ('2'):
        antrian.popleft()
    if i == ('3'):
        print(f"Antrian yang tersisa {antrian}")
    if i == ('4'):
        quit