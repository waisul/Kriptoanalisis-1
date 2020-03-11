import os
#Nama Kelompok
#Gede Agus Surya Atmaja (1708561025)
#Kadek Dwi Oka Mahendra (1708561034)
class Tugas3:

    def loop(self):
        for i in range(65, 90):
            for j in range(65, 90):
                for k in range(65, 90):
                    for z in range(65, 90):
                        #karena di console tidak cukup untuk output dari looping ini maka digunakan write file
                        f = open("D:\hasil.txt", "a")
                        f.write(chr(i) + chr(j) + chr(k) + chr(z) + '\n')

        f.close()
        print("File telah Selesai di tulis")
    def replace(self):
        #input kalimat
        words = input("Inputkan kalimat:")
        #tampilkan
        print(words)
        #huruf yang ingin diganti
        huruf_awal = input("Huruf yang akan diganti:")
        #huruf pengganti
        huruf_ganti = input("Diganti dengan huruf apa:")
        #menggunakan list
        new_save = list(map(lambda st:str.replace(st,huruf_awal,huruf_ganti), words))
        #mencetak hasil
        print("setelah direplace:"+str(new_save))

if __name__ == '__main__':
    t3 =Tugas3()
    pil = input("1. Looping Alphabet\n2. Replace\npilihan:")
    if pil == '1':
        t3.loop()
        os.system("pause")
    else:
        t3.replace()
        os.system("pause")