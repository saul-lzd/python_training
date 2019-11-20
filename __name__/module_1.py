import module_2
from module_3 import add, multi

print ("Module 1")

# Call functions from module_2
module_2.main()

print 'sum: ', add(2,3)
print 'multi: ', multi(2,3)

def add():
    print add(4,8)





def Lista():
    lista = [0,1,2,3,4,5,6,7,8,9]
    return lista

s = len(Lista())
print 'size ', s
print len(Lista())

