#!usr/python
#!encoding: UTF-8
print "Introduzca el nombre del fichero donde se encuentran los resultados"
nombre_fichero = raw_input ():
try:
  fichero = open (nombre_fichero)
  linea = fichero.readline()
  while (linea != ""):
    aproximaciones = int (linea.split()[3])
    print ("numero de intervalos %d" % (aproximaciones))
    for i in range (5):
      linea = fichero.readline()
      porcentaje = linea.split()[0]
      umbral = float (linea.split()[0])
      print ("%d de fallos para el umbral %2.5f" % (porcentaje,umbral))
    linea = fichero.readline()
except:
  print "El noombre del fichero introducido es incorrecto"
      