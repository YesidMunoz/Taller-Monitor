class Veterinaria:
    def __init__(self):
        self.mascotas= {}
        self.historias= {}
    
    def agregar_mascota(self):
        id_mascota=input("Ingrese el ID de la mascota")
        nombre=input("Nombre: ")
        tipo=input("Tipo: ")
        raza=input("Raza: ")
        edad=input("Edad: ")
        propietario=input("Propietario: ")
        telefono=input("Teléfono: ")
        
        mascota=Mascota(id_mascota,nombre,tipo,raza,edad,propietario,telefono)
        self.mascotas[id_mascota]=mascota
        print(f"Mascota {nombre} fue agregada")
        
    def mostrar_mascota(self, id_mascota):
        mascota = self.mascotas.get(id_mascota)
        if mascota:
            print(f"ID: {mascota.get_id_mascota()}, Nombre: {mascota.get_nombre()}, Tipo: {mascota.get_tipo()}, Raza: {mascota.get_raza()}, Edad: {mascota.get_edad()}, Propietario: {mascota.get_propietario()}, Teléfono: {mascota.get_telefono()}")
            return True
        else:
            print("Mascota no encontrada.")
            return False
    
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
        