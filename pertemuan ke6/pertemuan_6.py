import module

class perkalian(self,angka1,angka2):
    def __init__(self,angka1,angka2):
        self.angka1= angka1
        self.angka2= angka2 

    def mate(self):
        hasilkali = self.angka1*self.angka2
        hasiltambah = self.angka1+self.angka2
        return hasilkali, hasiltambah
    
per = perkalian(1,3)
print(per.mate())
        
p3 = module.person("michael",23,"dodi")
p3.sapa()
p3.salamkenal()