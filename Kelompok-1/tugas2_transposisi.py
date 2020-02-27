# fungsi untuk menentukan banyak baris
def baris(perulangan):
    # variabel perulangan bertipe float
    # variabel perulangan1 untuk menyimpan nilai dari perulangan berupa integer
    perulangan1 = int(perulangan)
    #variabel menyimpan nilai baris
    n = perulangan1
    #jika hasil float - int lebih dari 0 maka ditambah 1
    if perulangan-perulangan1 > 0:
        n = n+1
    return n
# variabel untuk menyimpan inputan berupa string
kal = str(input("Masukkan Kalimat: "))
# variabel untuk meyimpan panjang kalimat
panjang = len(kal)
# memberi nilai awal perulangan 2
start = 2
# akan mengulang sebanyak panjang kalimat
while start<=panjang:
    print("\tPerulangan dengan", start, "index:")
    j=0
    a=0
    s=start
    # nilai variabel perulangan didapat berupa float untuk mencari banyaknya baris yang akan diperlukan
    perulangan = panjang / start
    # perulangan untuk mencetak nilai baris
    while j<baris(perulangan):
        print(kal[a:s])
        a += start
        s += start
        j += 1
    start += 1