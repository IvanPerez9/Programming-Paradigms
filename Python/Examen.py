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

class Certificado (object):

    def __init__(self, profesor , alumno, fecha):
        self.profesor = profesor
        self.alumno = alumno
        self.fecha = fecha

    def mensaje (self , profesor , alumno, fecha):
        pass

    def imprimir (self , certificado):
        print("Nombre Alumno: " + certificado.alumno.nombre)
        print("Nombre TFG: " + certificado.alumno.tfg)
        print("Profesor responsable: " + certificado.profesor.nombre)

    def esValido (self):
        if len(self.alumno.asignaturas) == 0 or self.alumno.tfg == "" or len(self.profesor.impartir) == 0 or len(self.profesor.tfg)== 0 or not self.tieneTFG() :
            print("Certificado no valido")
        else:
            print("Certificado valido")

    def tieneTFG (self): #Para el Valido, si no tienen el mismo TFG
        if self.alumno.tfg not in self.profesor.tfg:
            return False
        return True


class Alumno (object):

    def __init__(self, nombre , apellidos,trabajo, asignaturas = []  ):
        self.nombre = nombre
        self.apellidos = apellidos
        self.asignaturas = asignaturas
        self.tfg = trabajo

class Profesor (object):

    def __init__(self, nombre , apellidos,tfg = [], impartir = []):
        self.nombre = nombre
        self.apellidos = apellidos
        self.tfg = tfg
        self.impartir = impartir

class CertificadoAsistencia (Certificado):

    def mensaje(self):
        print("El profesor " + self.profesor.nombre + " responsable de la asignatura " +
              str(self.alumno.asignaturas) +" certifica la asistencia de " +
              self.alumno.nombre + " al examen celebrado el día " + self.fecha + " .")

class CertificadoTFG (Certificado):

    def mensaje(self):
        print("El profesor " + self.profesor.nombre + " director del trabajo final de carrera " +
              self.alumno.tfg +" certifica la defensa por parte de " +
              self.alumno.nombre + " a fecha de " + self.fecha + " .")


if __name__ == '__main__':
    prof = Profesor ("David" , "Concha" , ["TFG1" , "TFG2"] , ["PP" , "ED"])
    prof2 = Profesor("David", "Concha", ["TFG2"], ["PP", "ED"])
    alum = Alumno ("Ivan" , "Perez" , "TFG1" , ["PP"])
    alum2 = Alumno("Ivan", "Perez", "TFG1", [])
    cer = Certificado (prof , alum , "10/01")
    cer2 = Certificado(prof, alum2, "10/01")
    print(cer.alumno.nombre)

    cer.esValido()

    cerAsis = CertificadoAsistencia(prof, alum, "10/01")
    cerAsis2 = CertificadoAsistencia(prof, alum2, "10/01")
    cerAsis3 = CertificadoTFG(prof2, alum, "10/01")
    cerAsis.mensaje()

    cerAsis.esValido()
    cerAsis2.esValido()
    cerAsis3.esValido()
