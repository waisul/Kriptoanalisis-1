import hashlib

my_hash = hashlib.sha256()
my_string = b"Saya mahasiswa Informatika"

my_hash.update(my_string);
print("Hasil SHA256 dari: ")
print(my_string)
print("adalah")
print(my_hash.hexdigest())
