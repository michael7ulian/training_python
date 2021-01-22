import os
clear = lambda: os.system('clear')
option = 0
i = 0
contacts = {}

def confimation():
    print("\n"*2)
    confirm = input("Anda yakin ingin keluar?(y/n) ")
    while confirm.lower() != "y" and confirm.lower() != "n":
        confirm = input("Anda yakin ingin keluar?(y/n) ")
    if(confirm.lower() == "n"):
        main()
    else:
        clear()
        print("Program selesai, sampai jumpa!")
        return

def back():
    print("\n")
    backToHome = input("Kembali ke Menu?(y/n) ")
    while backToHome.lower() != "y" and backToHome.lower() != "n":
        backToHome = input("Kembali ke Menu?(y/n) ")
    if(backToHome.lower() == "y"):
        main()
    else:
        clear()
        print("Program selesai, sampai jumpa!\n")
        return

def home():
    print("Selamat Datang\n--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def contactList():
    clear()
    if(len(contacts) > 0 ):
        print("Daftar Kontak:")
        print("-"*30)
        print()
        for a, b in contacts.items():
            for x in b:
                print(x, b[x], sep=': ')
        back()
    else:
        print("-"*30)
        print("Anda belum memiliki list Kontak")
        print("-"*30)
        back()
        
def validNumber(phone_number):
    if len(phone_number) < 10 or len(phone_number) > 12:
        return False
    for n in range(len(phone_number)):
        if phone_number[n].isalpha():
            return False
    return True

def addContact():
    clear()
    print("Tambah Kontak")
    print("-"*30)
    print()
    Name = input("Nama: ")
    Telp = input("No Telepon: ")
    while validNumber(Telp) == False:
        print("No telpon tidak Valid, no telpon harus berupa numeric dan panjang angka adalah 10 - 12 angka\n"+"-"*100)
        Telp = input("No Telepon: ")
    else:
        global i
        i += 1
        contacts[i] = {
            "Nama": Name,
            "No Telepon": Telp
        }
        print()
        print("Contact successfully added!")
        back()

def main():
    clear()
    home()
    while True:
        try:
            option = int(input("Pilih menu: "))
            break
        except ValueError:
            print("menu tidak tersedia")
    print()
    if(option == 1):
        contactList()
    elif(option == 2):
        addContact()
    elif(option == 3):
        confimation()
    else:
        clear()
        print("Menu tidak tersedia")
        back()

main()