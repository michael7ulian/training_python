# define a function
# def main():
    # print("Say something ..")

# Memanggil fungsi
# main()

# Fungsi dengan Argumen an Parameter
# def perkalian(n, z):
#     print(n*z)

# perkalian(40, 56)

# Return nilai
# def prima(n):
#     if n <= 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     else:
#         return True

# def daftar_prima():
#     for n in range(100):
#         if prima(n):
#             print(n, end="-")
#     print()

# daftar_prima()
# n = 5
# if prima(n):
#     print(f"{n} adalah bilangan prima")
# else:
#     print(f"{n} bukan bilangan prima")

# def tambah(w, v):
#     return w+v
# print(tambah(4, 5))

# Default Parameter
def greeting(ucapan, jam):
    print(f"Sekarang pukul {jam}, {ucapan}")

greeting(jam = 6, ucapan = "Selamat Pagi")

