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

