import pickle
class Vehiculo:
    def __init__(self,tipo,color,marca):
        self.tipo=tipo
        self.color=color
        self.marca=marca

    def __str__(self):
        return self.tipo+" "+self.color+" "+self.marca

class Fichero:
    datosGuardados=[]
#cargamos los datos de la clase Vehiculo y añadimos a una lista
#a continuacion escribimos en el fichero
    def cargarDatos(self,d):
        self.datosGuardados.append(d)
        self.escribir()
#creammos y escribimos en un fichero la lista, con los datos de la clase Vehiculo
    def escribir(self):
        f=open("datosVehiculos.bin",'wb')
        pickle.dump(self.datosGuardados,f)
        f.close()
#leemos el fichero y mostramos el total de vehículos incluidos
    def leerFichero(self):
        f = open('datosVehiculos.bin', 'ab+')
        f.seek(0)
        try:
            datos = pickle.load(f)
        except:
            print("El fichero está vacío")
        finally:
            f.close()
            print("Se han cargado {} vehículos".format(len(self.datosGuardados)))

    def mostrarDatos(self):
        if len(self.datosGuardados) ==0:
            print("Datos vacios")
            return
        for v in self.datosGuardados:
            print(v)


fichero=Fichero()
fichero.cargarDatos(Vehiculo('Moto','Negro','Yamaha'))
fichero.cargarDatos(Vehiculo('Coche','Rojo','BMW'))
fichero.cargarDatos(Vehiculo('Camion','Blanco','Volvo'))
fichero.mostrarDatos()
fichero.leerFichero()

