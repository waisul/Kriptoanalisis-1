# fungsi untuk mengubah format kalimat inputan
def preprocess(kal):
    #ubah bentuk huruf dalam kalimat menjadi huruf kecil
    kal = kal.lower()
    #menghapus tanda baca dan spasi dalam kalimat
    bad_chars = ['!', ".", ",", "?", " "]
    for i in bad_chars:
        kal = kal.replace(i, '')
    return kal

# fungsi untuk menghitung munculnya huruf
def count(kalimat, huruf):
    # variabel untuk menghitung kemunculan huruf
    hitung = 0
    # pengulangan untuk setiap data pada kalimat
    for huruf1 in kalimat:
        # jika huruf terdapat pada kalimat
        # maka hitung ditambah 1
        if huruf1 == huruf:
            hitung += 1
    return hitung
# variabel untuk menyimpan nilai inputan kalimat
kal = str(input("Masukkan Kalimat: "))
# memberi nilai kal yang sudah di proses fungsi preprocess
kal = preprocess(kal)
# varibel untuk menyimpan alphabet
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# menampilkan jumlah huruf yang sudah di proses, hanya menampilkan huruf yang tidak bernilai 0
for huruf in alpabet:
    if count(kal, huruf)!=0:
        print("Munculnya Huruf ", huruf, "=", count(kal, huruf), " kali")