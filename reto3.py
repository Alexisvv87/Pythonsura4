#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA

edad= int (input ("Digite su edad")) 


#PROCESO

if(edad>= 0 and  edad < 14):
    print (f'la etapa es Niño')
elif(edad>= 14 and  edad < 28):
    print (f'la etapa es Joven')
elif(edad>= 28 and  edad <= 60):
   print (f'Adulto')
elif(edad>= 60 and  edad < 150):
   print (f'Adulto mayor ')

else:
    print ("La edad ingresada es invalida")
