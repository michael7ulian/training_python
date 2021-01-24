# a = "Halo"
# b = 1

# try:
#     print(a+b)

# except ZeroDivisionError:
#     print("Error, tidak bisa membagi dengan angka NOL")
# except:
#     print("Ada Error")

# else:
#     print("tidak ada error")

# finally:
#     print("Next Code....")


# try:
#     f = open("list.txt", 'r')
#     f.write("Hai")
# except IOError:
#     print("IO Error")
# else:
#     print("Sukses!!")

try:
    f = open("list.txt", 'w')
    f.write("Hai")
except IOError:
    print("IO Error")
except:
    print("Ada yang error")
else:
    print("Sukses!!")
finally:
    print("Selamat, ada file baru")
    f.close()