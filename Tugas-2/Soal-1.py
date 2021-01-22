import os
clear = lambda: os.system('cls')

option = 0
cntContact = 0
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
        print("\n"*2)
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
        print("\n"*2)
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
        print("Daftar Kontak")
        print("-"*30)
        print()
        for a, b in contacts.items():
            for x, y in b.items():
                if(x == "Name"):
                    print(f"Nama: {y}")
                else:
                     print(f"No. Telepon: {y}")
        back()
    else:
        print("-"*30)
        print("Anda belum memiliki list Kontak")
        print("-"*30)
        back()
        
def validNumber(phone_number):
    if len(phone_number) < 10 and len(phone_number) > 12:
        return False
    for i in range(len(phone_number)):
        if phone_number[i].isalnum():
            return False
    return True

def contactAdd():
    clear()
    print("Tambah Kontak")
    print("-"*30)
    print()
    Name = input("Nama: ")
    Telp = input("No. Telepon: ")
    print(validNumber(Telp))
    while validNumber(Telp) == False:
        print("No telpon tidak Valid, no telpon harus berupa numeric dan panjang angka adalah 10 - 12 angka\n"+"-"*100)
        Name = input("Nama: ")
        Telp = input("No. Telepon: ")
    else:
        global cntContact
        cntContact += 1
        contacts[cntContact] = {
            "Name": Name,
            "Telp": Telp
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
        contactAdd()
    elif(option == 3):
        confimation()
    else:
        clear()
        print("Menu tidak tersedia")
        back()

main()