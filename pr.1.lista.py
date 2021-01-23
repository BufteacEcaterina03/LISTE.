lista1=[30,3,6,4,6,87,91,10,183]
print("lista initiala: ", lista1)
lista2=sorted(lista1)
print("lista sortata in ordine crescatoare:    ",lista2)
lista3=sorted(lista1,reverse=True)
print( "lista in ordine descrescatoare:    ",lista3)
print( "Numarul de elemente din lista: ",     len(lista1))
print( "Elementul MAX , elementul MIN:    "  ,max(lista1),min(lista1),sep="\n")
lista4=lista1+[111]
print( "Lista +111: " ,lista4)
lista5=lista1
lista5.insert(1, 222)
print(  "Lista cu nr 222 inserat pe pozitia 1: ", lista5)