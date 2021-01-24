
class person:
    def __init__(self,name,age,nama_lawan):
        self.name = name
        self.age = age
        self.nama_lawan = nama_lawan
        
    def sapa(self):
        print("halo namaku: "+self.name)
        print("namamu siapa?")
        
    def salamkenal(self):
        print("halo namaku: "+self.nama_lawan)
        print("senang bertemu denganmu. sampai jumpa kebali")
