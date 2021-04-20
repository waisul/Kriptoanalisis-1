#hasil dari program ini kami buatkan file dikarenakan hasil dari console tidak cukup
for a in range(65,91):
    for b in range(65,91):
        for c in range(65,91):
            for d in range(65,91):
                file = open("D:\hasil.txt", "a")
                file.write(chr(a) + chr(b) + chr(c) + chr(d) + "\n")
file.close()