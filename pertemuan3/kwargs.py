# Kwargs

def main():
    x = dict(pagi = 'Kentang Goreng', siang = 'Rendang', malam = 'Geprek')
    makanan(**x)

def makanan(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f"Sarapan {k} saya adalah {kwargs[k]}")
    else: pass

main()