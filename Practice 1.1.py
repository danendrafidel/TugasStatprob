# %% [markdown]
# 1.Diketahui tinggi badan siswa kelas A adalah 100.5, 99.7, 101.0, 101.3, 99.9, 98.9, 165.0, 102.2, 98.7, 102.9, dan 100.0 . Menggunakan Mean, Median, dan Modus, coba gambarkan pusat distribusi data berikut. Manakah yang paling bagus?

# %% [markdown]
# A.Mean

# %%
# Inisialisasi dataset
data = [100.5, 99.7, 101.0, 101.3, 99.9, 98.9, 165.0, 102.2, 98.7, 102.9, 100.0]
print(f"Data: {data}")

# Jumlah nilai dalam dataset 
jumlah_nilai = sum(data)
print(f"Jumlah semua nilai: {jumlah_nilai}")

# Jumlah total data dalam dataset 
jumlah_total_data = len(data)
print(f"Jumlah total data: {jumlah_total_data}")

# Jumlah semua nilai dalam dataset 
mean_value = jumlah_nilai / jumlah_total_data
print(f"Mean: {mean_value}")

import matplotlib.pyplot as plt

# Create a histogram
plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='green')

# Add a vertical line at the mean
plt.axvline(x=mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Mean = {mean_value:.2f}')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Mean')

# Add legend
plt.legend()

# Show the plot
plt.show()

# %% [markdown]
# B.Median

# %%
# Inisialisasi dataset
data = [100.5, 99.7, 101.0, 101.3, 99.9, 98.9, 165.0, 102.2, 98.7, 102.9, 100.0]
print(f"Data: {data}")

# Mengurutkan data dari terkecil hingga terbesar
sorted_data = sorted(data)
print(f"Data berurut: {sorted_data}")

# Jumlah total data dalam dataset 
n = len(sorted_data)
print(f"Jumlah total data: {n}")

index_tengah = n//2 # double slash // is used for floor division

# Jika jumlah data genap, median adalah rata-rata dari dua nilai tengah 
if n % 2 == 0:
    print(f"Jumlah total data Genap")
    median1 = sorted_data[index_tengah]
    median2 = sorted_data[index_tengah - 1]
    print(f"Nilai tengah: {median1} {median2}")
    median_value = (median1 + median2) / 2
    
# Jika jumlah data ganjil, median adalah nilai tengah
else:
    print(f"Jumlah total data Ganjil")
    median_value = sorted_data[index_tengah]
    print(f"Nilai tengah: {median_value}")

print(f"Median: {median_value}")

import matplotlib.pyplot as plt

# Membuat histogram dengan warna biru
plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='blue')

# Menambahkan garis vertikal pada median dengan warna merah
plt.axvline(x=median_value, color='red', linestyle='dashed', linewidth=1, label=f'Median = {median_value:.2f}')

# Menambahkan label dan judul
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Median')

# Menambahkan legenda
plt.legend()

# Menampilkan plot
plt.show()


# %% [markdown]
# C.Modus

# %%
import matplotlib.pyplot as plt
from collections import Counter

# Data tinggi badan siswa
data = [100.5, 99.7, 101, 101.3, 99.9, 98.9, 165, 102.2, 98.7, 102.9, 100]

# Menghitung frekuensi setiap tinggi badan
frekuensi = Counter(data)

# Mengambil tinggi badan dan frekuensi sebagai list terpisah
tinggi_badan = list(frekuensi.keys())
jumlah_siswa = list(frekuensi.values())

# Mencari modus (tinggi badan dengan frekuensi tertinggi)
modus = [tinggi for tinggi, frek in frekuensi.items() if frek == max(jumlah_siswa)]

print(f"Modus: {modus}")

# Membuat grafik batang
plt.bar(tinggi_badan, jumlah_siswa, color='magenta')

# Menambahkan label dan judul
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Jumlah Siswa')
plt.title('Grafik Batang Pusat Distribusi Tinggi Badan Siswa')

# Menampilkan modus pada grafik dengan label
plt.text(modus[0], max(jumlah_siswa), f'Modus: {modus[0]} cm', ha='center', va='bottom', color='red')

# Menampilkan grafik
plt.show()


# %% [markdown]
# 2.Berikut adalah nilai UAS pada mata pelajaran matematika di kelas A: 95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75. Menggunakan Mean, Median, dan Modus, coba gambarkan pusat distribusi data berikut. Manakah yang paling bagus?

# %% [markdown]
# A.Mean

# %%
import numpy as np
import matplotlib.pyplot as plt

# Data nilai UAS matematika
nilai_uas = np.array([95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75])

# Menghitung mean
mean_nilai = np.mean(nilai_uas)

# Mencetak hasil
print(f"Mean: {mean_nilai:.2f}")

# Membuat histogram
plt.hist(nilai_uas, bins=10, edgecolor='black', alpha=0.7, color='blue')

# Menambahkan garis vertikal pada mean
plt.axvline(x=mean_nilai, color='red', linestyle='dashed', linewidth=1, label=f'Mean = {mean_nilai:.2f}')

# Menambahkan label dan judul
plt.xlabel('Nilai UAS')
plt.ylabel('Frekuensi')
plt.title('Grafik Distribusi Nilai UAS Matematika')

# Menampilkan legenda
plt.legend()

# Menampilkan grafik
plt.show()


# %% [markdown]
# B.Median

# %%
# Inisialisasi dataset
data = [95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75]
print(f"Data: {data}")

# Mengurutkan data dari terkecil hingga terbesar
sorted_data = sorted(data)
print(f"Data berurut: {sorted_data}")

# Jumlah total data dalam dataset 
n = len(sorted_data)
print(f"Jumlah total data: {n}")

index_tengah = n//2 # double slash // is used for floor division

# Jika jumlah data genap, median adalah rata-rata dari dua nilai tengah 
if n % 2 == 0:
    print(f"Jumlah total data Genap")
    median1 = sorted_data[index_tengah]
    median2 = sorted_data[index_tengah - 1]
    print(f"Nilai tengah: {median1} {median2}")
    median_value = (median1 + median2) / 2
    
# Jika jumlah data ganjil, median adalah nilai tengah
else:
    print(f"Jumlah total data Ganjil")
    median_value = sorted_data[index_tengah]
    print(f"Nilai tengah: {median_value}")

print(f"Median: {median_value}")

import matplotlib.pyplot as plt

# Create a histogram
plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='yellow')

# Add a vertical line at the mean
plt.axvline(x=median_value, color='red', linestyle='dashed', linewidth=1, label=f'Median = {median_value:.2f}')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Median')

# Add legend
plt.legend()

# Show the plot
plt.show()

# %% [markdown]
# C.Modus

# %%
# Import library Counter untuk menghitung modus
from collections import Counter

# Inisialisasi dataset
data = [95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75]
print(f"Data: {data}")

counter = Counter(data)
mode_data = dict(counter) # ubah ke tipe data dictionary
max_counter = max(list(counter.values())) # mencari data yang memiliki counter paling banyak
print(f"Max Counter: {max_counter}")

mode_value = []
for k, v in mode_data.items():
    print(f"{k} muncul {v} kali")
    if v == max(list(counter.values())):
        mode_value.append(k)
    
print(f"Mode: {mode_value}")

import matplotlib.pyplot as plt

# Create a histogram
plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='green')

# Add a vertical line at the mean
plt.axvline(x=mode_value[0], color='red', linestyle='dashed', linewidth=1, label=f'Modus 1 = {mode_value[0]:.2f}')
plt.axvline(x=mode_value[1], color='blue', linestyle='dashed', linewidth=1, label=f'Modus 2 = {mode_value[1]:.2f}')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Modes')

# Add legend
plt.legend()

# Show the plot
plt.show()

