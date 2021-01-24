# Membuat file baru
f = open("belajar.txt", "w+")
# Menambah value ke file text
f.write("baris pertama \r")

f.close()

# Append value baru
append = open("belajar.txt", "a")
append.write("Baris ke- dua")

append.close()

# Read file
fread = open("belajar.txt", 'r')
if fread.mode == 'r':
    contents = fread.read()
    print(contents)
    fread.close()