    #valide e incorpore el codigo a la opcion 3 del menu        
   
    
    
numeros = (2, 4, 6,8,10,12,14,16)
print('Cantidad de elementos de la tupla:', len(numeros))
print(f'Contenido: {numeros}')

def printMaterias():
    repetido = []
    unico = []
    print('Operaciones o métodos que provee la clase `tuple`:')
    materias = ('Matemáticas', 'Matemáticas', 'Ofimática', 'Programación', 'Redes', 'Contabilidad', 'Redes')
    print(materias.count('Matemáticas'))
    print(materias)
    for x in materias:
        if x not in unico:
            unico.append(x)
        else:
            if x not in repetido:
                repetido.append(x)
    
        
    print (f'Materias Repetidas: {repetido}')
           
           