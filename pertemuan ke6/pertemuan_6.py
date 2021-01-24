class perkalian:
    def __init__(self,angka1,angka2):
        self.angka1= angka1
        self.angka2= angka2 

    def mate(self):
        hasilkali = self.angka1*self.angka
        hasiltambah = self.angka1+self.angka2
        return hasilkali, hasiltambah
    
per = perkalian(200,100)
print("perkalian: ",per.mate()[0])
print("hasil tambah: ",per.mate()[1])

def masukan():
    nama= "michale"
    umur = 10
    gender = "male"
    return nama, umur, gender

a = masukan()
x = print(f"nama {a[0]}, umur{a[1]}, gender {a[2]}")
x
