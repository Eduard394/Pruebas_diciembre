
import sys
import os




my_list = [{'id': 3, 'status':'ok', 'name':'legarda',},
{'id': 2, 'status':'no', 'name':'na',},
{'id': 4, 'status':'ok', 'name':'arenas',},
{'id': 6, 'status':'ok', 'name':'hoyos',},
]
a = 5;
salida = []
for f in my_list:
	aux = {'name': f['name'], 'total': f['id']}
	salida.append(aux)
	#print aux
print salida
print "hola mundo";
print a
a = 10
print a


print "hola señor Pablo"


lista = [[1,2],[3,4],[5,6]]
print lista[0]