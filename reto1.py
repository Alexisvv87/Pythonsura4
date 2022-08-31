#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA

nivelAgua=None
nivelAgua=int (input ("Digite el nivel de agua: "))

#PROCESO

if (nivelAgua >= 0 and  nivelAgua < 20 ):
    print (f'El nivel de agua es {nivelAgua} bajo: ')
elif (nivelAgua >= 20 and  nivelAgua < 400):
    print (f'El nivel de agua es {nivelAgua} medio: ')
elif(nivelAgua>=400):
   print (f'El nivel de agua es {nivelAgua} Alto: ')
else:
    print ("El nivel de agua no es valido")

#SALIDAS