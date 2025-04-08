# Paciente
class Paciente:
    def __init__(self, nombre, edad, sexo, presion_arterial, frecuencia_cardiaca, peso, altura, diabetes, hipertension):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__presion_arterial = presion_arterial
        self.__frecuencia_cardiaca = frecuencia_cardiaca
        self.__peso = peso
        self.__altura = altura
        self.__diabetes = diabetes
        self.__hipertension = hipertension
        
        # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_presion_arterial(self, presion_arterial):
        self.__presion_arterial = presion_arterial

    def set_frecuencia_cardiaca(self, frecuencia_cardiaca):
        self.__frecuencia_cardiaca = frecuencia_cardiaca

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def set_diabetes(self, diabetes):
        self.__diabetes = diabetes

    def set_hipertension(self, hipertension):
        self.__hipertension = hipertension

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_presion_arterial(self):
        return self.__presion_arterial

    def get_frecuencia_cardiaca(self):
        return self.__frecuencia_cardiaca

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_diabetes(self):
        return self.__diabetes

    def get_hipertension(self):
        return self.__hipertension
    
    def __str__(self):
        return (f"Paciente: {self.__nombre}, Edad: {self.__edad} años, Sexo: {self.__sexo}, "
                f"Presión Arterial: {self.__presion_arterial}, Frecuencia Cardíaca: {self.__frecuencia_cardiaca} bpm, "
                f"Peso: {self.__peso} kg, Altura: {self.__altura} m, "
                f"Diabetes: {'Sí' if self.__diabetes else 'No'}, Hipertensión: {'Sí' if self.__hipertension else 'No'}")
        

datos_pacientes = [{'Nombre': 'Maria', 'Edad': 58, 'Sexo': 'M', 'Presion Arterial': '107/82 mmHg', 'Frecuencia Cardiaca': 67, 'Peso': 59.5, 'Altura': 1.51, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Juan', 'Edad': 72, 'Sexo': 'H', 'Presion Arterial': '130/88 mmHg', 'Frecuencia Cardiaca': 78, 'Peso': 75.2, 'Altura': 1.73, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Ana', 'Edad': 45, 'Sexo': 'M', 'Presion Arterial': '110/75 mmHg', 'Frecuencia Cardiaca': 55, 'Peso': 50.8, 'Altura': 1.6, 'Diabetes': False, 'Hipertension': True},
 {'Nombre': 'Pedro', 'Edad': 65, 'Sexo': 'H', 'Presion Arterial': '145/95 mmHg', 'Frecuencia Cardiaca': 85, 'Peso': 82.1, 'Altura': 1.85, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Laura', 'Edad': 38, 'Sexo': 'M', 'Presion Arterial': '120/80 mmHg', 'Frecuencia Cardiaca': 60, 'Peso': 55.3, 'Altura': 1.68, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Carlos', 'Edad': 80, 'Sexo': 'H', 'Presion Arterial': '150/90 mmHg', 'Frecuencia Cardiaca': 92, 'Peso': 88.7, 'Altura': 1.78, 'Diabetes': True, 'Hipertension': True},
 {'Nombre': 'Sofia', 'Edad': 25, 'Sexo': 'M', 'Presion Arterial': '115/78 mmHg', 'Frecuencia Cardiaca': 50, 'Peso': 48.5, 'Altura': 1.55, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Luis', 'Edad': 52, 'Sexo': 'H', 'Presion Arterial': '135/85 mmHg', 'Frecuencia Cardiaca': 70, 'Peso': 68.9, 'Altura': 1.7, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Elena', 'Edad': 68, 'Sexo': 'M', 'Presion Arterial': '125/82 mmHg', 'Frecuencia Cardiaca': 75, 'Peso': 70.1, 'Altura': 1.65, 'Diabetes': False, 'Hipertension': True},
 {'Nombre': 'Miguel', 'Edad': 40, 'Sexo': 'H', 'Presion Arterial': '118/76 mmHg', 'Frecuencia Cardiaca': 62, 'Peso': 60.5, 'Altura': 1.75, 'Diabetes': False, 'Hipertension': False}]


for dato_paciente in datos_pacientes:
    paciente = Paciente(*dato_paciente)
    print(paciente)