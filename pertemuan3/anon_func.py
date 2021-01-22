# Anonymous Function

# a = lambda x,y:x*y
# print(a(8,9))



# Scope
x = "Halo"
def greet():
    global x
    x = "Hola"
    print(x)
greet()
print(x)