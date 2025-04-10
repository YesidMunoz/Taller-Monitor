import random
class Veterinaria:
    def __init__(self):
        self.__mascotas = {}
        self.__historias = {}
        self.__contador_historias =0
        
    def pedir_entero(self,mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Por favor, ingrese un número válido.")
    def get_mascotas(self):
        return self.__mascotas

    def get_historias(self):
        return self.__historias
    
    def generar_id_mascota(self): # se genera un número y se llena de ceros a la izquiera hasta completar 5 dígitos
        numero = random.randint(0, 99999)
        return "M" + str(numero).zfill(5)

    def generar_id_historia(self):
        self.__contador_historias += 1
        return f"H{self.__contador_historias:05d}" #Toma el número de historia, lo convierte a 5 dígitos con ceros delante y le pone una H al inicio

    def agregar_mascota(self):
        id_mascota = self.generar_id_mascota()
        nombre=input("Nombre: ")
        tipo=input("Tipo: ")
        raza=input("Raza: ")
        edad = self.pedir_entero("Edad: ")
        propietario=input("Propietario: ")
        telefono = self.pedir_entero("Teléfono: ")
        
        mascota=Mascota(id_mascota,nombre,tipo,raza,edad,propietario,telefono)
        self.__mascotas[id_mascota]=mascota
        print(f"Mascota {nombre} fue agregada")
        
    def mostrar_mascota(self, id_mascota):
        mascota = self.__mascotas.get(id_mascota)
        if mascota:
            print(f"ID: {mascota.get_id_mascota()}, Nombre: {mascota.get_nombre()}, Tipo: {mascota.get_tipo()}, Raza: {mascota.get_raza()}, Edad: {mascota.get_edad()}, Propietario: {mascota.get_propietario()}, Teléfono: {mascota.get_telefono()}")
            return True
        else:
            print("Mascota no encontrada.")
            return False
        
    def eliminar_mascota(self):
        id_mascota = input("Ingrese el ID de la mascota a eliminar: ")
        
        if id_mascota in self.__mascotas:
            # Primero buscamos todas las historias médicas asociadas a la mascota
            historias_a_eliminar = []
            for id_historia, historia_medica in self.__historias.items():
                if historia_medica.get_id_mascota() == id_mascota:
                    historias_a_eliminar.append(id_historia)
            
            # Eliminamos cada historia médica
            for id_historia in historias_a_eliminar:
                del self.__historias[id_historia]
            
            # Ahora eliminamos la mascota
            del self.__mascotas[id_mascota]
            print(f"Mascota {id_mascota} y sus historias médicas fueron eliminadas exitosamente.")
        else:
            print("Mascota no encontrada.")
    
    #------------------------Historia Médica---------------------------------------------------------------------------------
    def agregar_historia_medica(self):
        id_mascota = input("Ingrese el ID de la mascota: ")

        if id_mascota in self.__mascotas:
            fecha = input("Fecha de la consulta: ")
            descripcion = input("Descripción de la consulta: ")
            veterinario = input("Nombre del veterinario: ")

            id_historia = self.generar_id_historia()

            historia = HistoriaMedica(id_historia, id_mascota, fecha, descripcion, veterinario)
            self.__historias[id_historia] = historia

            print(f"Historia médica {id_historia} agregada correctamente para la mascota {self.__mascotas[id_mascota].get_nombre()}.")
        else:
            print("Mascota no encontrada. No se puede agregar la historia médica.")
            
    def mostrar_historias_medicas(self, id_mascota):
        encontro = False
        for historia in self.__historias.values():
            if historia.get_id_mascota() == id_mascota:
                print(f"ID Historia: {historia.get_id_historia()}, Fecha: {historia.get_fecha()}, Descripción: {historia.get_descripcion()}, Veterinario: {historia.get_veterinario()}")
                encontro = True
        if not encontro:
            print("No hay historias médicas registradas para esta mascota.")
            
    def eliminar_historia_medica(self):
        id_historia = input("Ingrese el ID de la historia médica a eliminar: ")
        
        if id_historia in self.__historias:
            del self.__historias[id_historia]
            print(f"Historia médica {id_historia} eliminada exitosamente.")
        else:
            print("Historia médica no encontrada.")
            
        
class Mascota:
    def __init__(self, id_mascota,nombre,tipo,raza,edad,propietario,telefono):
        self.__id_mascota=id_mascota
        self.__nombre=nombre
        self.__tipo=tipo
        self.__raza=raza
        self.__edad=edad
        self.__propietario=propietario
        self.__telefono=telefono
        
    
    def get_id_mascota(self):
        return self.__id_mascota

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_propietario(self):
        return self.__propietario

    def get_telefono(self):
        return self.__telefono

    def set_id_mascota(self, id_mascota):
        self.__id_mascota = id_mascota

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def set_propietario(self, propietario):
        self.__propietario = propietario

    def set_telefono(self, telefono):
        self.__telefono = telefono
        
        
class HistoriaMedica:
    def __init__(self, id_historia, id_mascota,fecha,descripcion,veterinario):
        self.__id_historia=id_historia
        self.__id_mascota=id_mascota
        self.__fecha=fecha
        self.__descripcion=descripcion
        self.__veterinario = veterinario
        
    def get_id_historia(self):
        return self.__id_historia

    def get_id_mascota(self):
        return self.__id_mascota

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion

    def get_veterinario(self):
        return self.__veterinario

    def set_id_historia(self, id_historia):
        self.__id_historia = id_historia

    def set_id_mascota(self, id_mascota):
        self.__id_mascota = id_mascota

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_veterinario(self, veterinario):
        self.__veterinario = veterinario
        
        
def main():
    veterinaria = Veterinaria()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar mascota")
        print("2. Mostrar mascota")
        print("3. Agregar historia médica")
        print("4. Mostrar historias médicas")
        print("5. Eliminar mascota")
        print("6. Eliminar historia médica")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            veterinaria.agregar_mascota()
        elif opcion == "2":
            id_mascota = input("Ingrese el ID de la mascota a mostrar: ")
            veterinaria.mostrar_mascota(id_mascota)
        elif opcion == "3":
            veterinaria.agregar_historia_medica()
        elif opcion == "4":
            id_mascota = input("Ingrese el ID de la mascota: ")
            veterinaria.mostrar_historias_medicas(id_mascota)
        elif opcion == "5":
            veterinaria.eliminar_mascota()
        elif opcion == "6":
            veterinaria.eliminar_historia_medica()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()