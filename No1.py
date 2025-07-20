# Mengambil input dari user dan menyimpannya dalam variabel input_kata
input_kata = input("Masukkan String:")

# Menggunakan metode split() untuk memecah string menjadi list berdasarkan spasi.
# Ini akan menghasilkan list di mana setiap elemen adalah kata dalam string asli.
kata = input_kata.split()

# Menggunakan fungsi len() untuk menghitung jumlah elemen dalam list kata.
# untuk memberikan jumlah kata dalam string asli.
kalimat = len(kata)

# Menggunakan pernyataa if untuk mengecek apakah jumlah kata lebih dari 1.
# Jika ya, maka string tersebut dianggap sebagai kalimat.
if kalimat > 1:
    # Mencetak pesan yang menunjukkan bahwa string tersebut adalah kalimat.
    print(f"'{input_kata}'merupakan KALIMAT")
    # Mencetak jumlah kata dalam string tersebut.
    print(f"Jumlah kata: {kalimat}")
else:
    # Jika jumlah kata tidak lebih dari 1, maka string tersebut dianggap sebagai kata.
    print(f"'{input_kata}'merupakan KATA")
    # Mencetak jumlah kata dalam string tersebut.
    print(f"Jumlah kata: {kalimat}")