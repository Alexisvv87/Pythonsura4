#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA

mesDigitado=input ("Digite el mes del año")
mes = mesDigitado.lower()

#PROCESO

if(mes == "enero" or mes == "febrero" or mes == "marzo" ):
    print (f'El mes  {mes} invirno: ')
elif(mes == "abril" or mes == "mayo" or  mes == "junio" ):
    print (f'El mes  {mes} primavera: ')
elif(mes == "julio" or mes == "agosto" or mes == "septiembre" ):
   print (f'El mes  {mes} verano: ')
else:
    print ("el mes es invalido")


