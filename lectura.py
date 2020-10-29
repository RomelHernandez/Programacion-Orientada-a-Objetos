def escritura (datoa, datob, datoc):
    prueba = open('C:/cosascurso','w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print("/nEscritura/n")
    prueba.close

escritura('Hola',
          'Mundo',
          'Bonito')

def lectura():
    prueba = open('C:/cosascurso','r')
    print(prueba.read())
    prueba.close()
lectura() 