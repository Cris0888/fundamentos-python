#los sets en python son cajas donde podemos almacenar valores pero no pueden estar repetidos parecidos alas listas pero no se pueden repetir los datos ay dos maneras de crear un sets con el atributo set y creandolo entre llaves {}

#con el modulo set 
mi_set=set([9,8,7,6,5,4,3,2,1,])

#tambien podemos crearlo usando {}
set2={9,8,7,7,6,5,4,3,2,1}


print(set2)

# si queremos imprimirlo sin comas ni corchetes debemos usar " ".join(map(str, mi_set))

print(" ".join(map(str,mi_set)))
