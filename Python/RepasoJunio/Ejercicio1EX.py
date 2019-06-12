"""
Se desea crear un aplicación para la gestión de certificados.
Existen 2 tipos de certificados, los de asistencia a un examen y los certificados del
tribunal de TFG. Ambos certificados tienen un profesor responsable, un alumno beneficiario
y la fecha de expedición. Tanto alumnos como profesores tienen nombre y apellidos.
Los alumnos tienen una serie de asignaturas identificadas por su nombre y un TFG
identificado por su titulo. Por su parte los profesores imparten una serie de asignaturas
 y pueden dirigir varios TFG.

Los certificados de asistencia tendrán el siguiente mensaje:

"El profesor (nombre del responsable) responsable de la asignatura (nombre asignatura)
 certifica la asistencia de (nombre del alumno) al examen celebrado el día  (fecha).

Por su parte, los certificados de TFG tendrán el siguiente mensaje:

"El profesor (nombre del responsable) director del trabajo final de carrera (titulo del TFG) certifica la defensa por parte de (nombre del alumno) a fecha de (fecha).

No todos los certificados que se generen tienen por que se validos. Se considerarán invalidos todos los certificados que beneficien a un alumno que no tiene la asignatura o TFG que se certifica, o que el responsable de ese certificado (el profesor) no imparte la asignatura o el TFG.

Definir las clases necesarias para gestionar los certificados. (0.5 puntos)
Implementar todos los métodos necesarios para poder crear e imprimir por pantalla nuevos certificados, esto incluye la creación de alumnos y profesores añadiendoles asignaturas y TFG. (2 puntos)
Crear una función que recibe un certificado y devuelve si es un certificado valido o no. (1.5 puntos)
En este ejercicio no será necesario documentar las clases, métodos o funciones.
"""


class Certificado():

    # Falta añadir asignaturas y TFG profesores y alumnos

    def __init__(self, profesor, alumno, fecha):
        self.profesor = profesor
        self.alumno = alumno
        self.fecha = fecha

    def mensaje(self, profesor, alumno, fecha):
        pass

    def imprimirPantalla(self, certificado):
        print("Nombre alumno: " + certificado.alumno.nombre)
        print("Nombre profesor: " + certificado.alumno.nombre)
        print("Nombre TFG: " + certificado.alumno.TFG)

    # Se considerarán invalidos todos los certificados que beneficien a un alumno que no tiene la
    # asignatura o TFG que se certifica, o que el responsable de ese certificado (el profesor) no
    # imparte la asignatura o el TFG.
    def esValido(self):
        pass

    #Solo si el alumno solo tiene 1 TFG
    def mismoTFG(self):
        if self.alumno.TFG not in self.profesor.TFG:
            return False
        return True


class Alumno():

    # Falta añadir asignaturas y TFG profesores y alumnos

    def __init__(self, nombre, apellido,TFG, asignaturas=set()):
        self.nombre = nombre;
        self.apellido = apellido
        self.TFG = TFG
        self.asignaturas = asignaturas

    def asignarTFG(self, TFG, profesor):
        if self.TFG != None:
            print("Ya tiene un TFG asignado")
        else:
            self.TFG = TFG
            profesor.TFGs.append(TFG)

    def anadirAsignatura(self, asignatura):
        if asignatura not in self.asignatura:
            self.asignatura.add(asignatura)
        else:
            print("Ya cursa esa asignatura")

    def imprimirAlumno(self):
        print("Nombre: " + self.nombre);
        print("Apellido: " + self.apellido)
        if self.TFG != None:
            print("El TFG asignado es: " + self.TFG)
        else:
            print("No tiene TFG asignado")

        if len(self.asignaturas) != 0:
            print("Asignatuas asignadas: ", end="");
            for i in self.asignaturas:
                print(i)
        else:
            print("No tiene asignaturas asignadas")


class Profesor():

    # Falta añadir asignaturas y TFG profesores

    def __init__(self, nombre, apellido, TFGs=[], asignaturas=set()):
        self.nombre = nombre
        self.apellido = apellido
        self.TFGs = TFGs
        self.asignaturas = asignaturas

    def asignarTFG(self, TFG, alumno):
        if len(self.TFGs) < 10:
            print("Puede asignarle TFG " + TFG + " a " + alumno.nombre + " como responsable " + self.nombre)
            self.TFGs.apprend(TFG)
        else:
            print("No puede dirigir más TFGs")

    def anadirAsignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.add(asignatura)
        else:
            print("Ya imparte esa asignatura")

    def imprimirProfesor(self):
        print("Nombre: " + self.nombre);
        print("Apellido: " + self.apellido)
        if len(self.TFGs) != 0:
            for i in self.TFG:
                print("Tiene: " + i + " TFGs")
        else:
            print("No tiene TFGs asignados")

        if len(self.asignaturas) != 0:
            for i in self.asignaturas:
                print("Imparte: " + i + " asignatura")
        else:
            print("No tiene asignaturas asignadas")


class CertificadoAsistencia(Certificado):

    def mensaje(self, asignatura):
        if self.esValido(asignatura) == True:
            print("El profesor " + self.profesor.nombre + " responsable de la asignatura " +
                  asignatura + " certifica la asistencia de " +
                  self.alumno.nombre + " al examen celebrado el día " + self.fecha + " .")
        else:
            print("Certificado no valido para " + asignatura)

    def esValido(self, asignatura):
        if (len(self.profesor.asignaturas) == 0):
            return False
        elif (asignatura not in self.alumno.asignaturas or asignatura not in self.profesor.asignaturas):
            return False
        else:
            return True

class CertificadoTFG(Certificado):

    def mensaje(self, TFG):
        if self.esValido(TFG) == True:
            print("El profesor " + self.profesor.nombre + " director del trabajo final de carrera " +
                  TFG + " certifica la defensa por parte de " +
                  self.alumno.nombre + " a fecha de " + self.fecha + " .")
        else:
            print("Certificado no valido para TFG: " + TFG)

    def esValido(self, TFG):
        if (len(self.profesor.asignaturas) == 0):
            return False
        elif (TFG not in self.alumno.TFG or TFG not in self.profesor.TFGs):
            return False
        else:
            return True


if __name__ == '__main__':
    prof1 = Profesor("David" , "Concha" , ["TFG1" , "TFG2"] , ["PP" , "ED"])
    prof2 = Profesor("Jesus" , "Sanchez" , ["TFG1"] , ["Concurrente"] )
    alum1 = Alumno("Ivan" , "Perez" , "TFG1" , ["PP" , "Concurrente"])
    alum2 = Alumno("Pepe" , "Muñoz" , "TFG2" , [])
    cer = Certificado(prof1 , alum1 , "10/02")
    cerTFG = CertificadoTFG(prof1, alum1, "12/06")
    cerAsis = CertificadoAsistencia(prof1 , alum2, "03/02")

    print(cer.alumno.nombre) # Prueba
    cerTFG.mensaje("TFG1")
    cerAsis.esValido("PP")
    cerAsis.mensaje("PP")