#texto = open("C:\\Users\\Yola\\Desktop\\PythonYolanda\\dani.txt")
#print(texto.read())

#Agenda = open("dani.txt",'w')
#Agenda.truncate()
#Agenda.write(" hola mundo, ya estoy escribiendo en Phyton")
#Agenda.close()
#agenda = open("dani.txt")

#print (agenda)

agenda = open("agenda.csv",'a')
nombre = input("Introduce tu nombre de contacto > ")
telefono = input("Introduce tu telefono > ")
edad = input("Edad > ")
print("Seha guardado en la agenda el cotacto: ", nombre, "con el numero de telefono ",telefono, "tienes ", edad, "anos")
agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write(edad)
agenda.write(",")
agenda.write("\n")
agenda.close()
