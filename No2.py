# Mengambil input dari user dengan tipe data integer.
input_angka = int(input("Masukkan bilangan: "))

# Membuat list kosong yang akan digunakan untuk menyimpan bilangan ganjil berkelipatan 3.
bilangan_ganjil_kelipatan_3 = []

# Menggunakan looping for untuk mengiterasi dari kelipatan 3 hingga input_angka yang dimasukkan oleh user.
for i in range(3, input_angka + 1, 3):
    # Menggunakan metode append() untuk menambahkan bilangan ke dalam list bilangan_ganjil_kelipatan_3.
    bilangan_ganjil_kelipatan_3.append(i)

# Mencetak pesan yang menunjukkan bahwa berikut adalah bilangan ganjil berkelipatan 3 dari input_angka.
print("Bilangan ganjil berkelipatan 3 dari", input_angka, "adalah:")

# Menggunakan looping for untuk mengiterasi setiap angka dalam list bilangan_ganjil_kelipatan_3.
for angka in bilangan_ganjil_kelipatan_3:
    # Mencetak setiap angka, dengan end=" " untuk menambahkan spasi setelah setiap angka.
    print(angka, end=" ")