from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

x = int(input("Input Batas Perulangan: "))

def cetak(i):
  if i%2 == 0:
    print(f"{i+1} Ganjil", "- ID proses", getpid())
  elif i%2 !=0:
    print(f"{i+1} Genap", "- ID proses", getpid())
  else:
    print("selesai")
    sleep(1)

print("\nSekuensial")

#  waktu sebelum eksekusi
sekuensial_awal = time()

# Proses
for i in range(x):
    cetak(i)

# waktu setelah eksekusi
sekuensial_akhir = time()

print("\nKelas Process")

# kumpulan proses
kumpulan_proses = []

# proses awal
process_awal = time()

# proses berlangsung
for i in range(x):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

# untuk menggabungkan setiap proses agar tidak loncat ke step berikutnya
for i in kumpulan_proses:
    p.join()
    
# proses akhir
process_akhir = time()

print("\nKelas Pool")

# proses awal
pool_awal = time()

# proses berlangsung
pool = Pool()
pool.map(cetak, range(x))
pool.close()

# proses akhir
pool_akhir = time()

print("\nSekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool :", pool_akhir - pool_awal, "detik")
