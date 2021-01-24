class biodata:
    def __init__(self):
        nama = input("nama anda: ")
        alamat = input("alamat anda: ")
        umur = int(input("umur anda: "))
        self.name = nama
        self.age = umur
        self.alamat = alamat
        
    def bio(self):
        print("nama: ",self.name)
        print("alamat: ",self.alamat)
        print("umur: ", self.age)

p1 = biodata()
p1.bio