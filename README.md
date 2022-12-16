project_coder
Alumno: Gonzalo Irusta.
Comision: 45020.
Tutor: Enzo Martin Zotti.

Para dar inicio al funcionamiento del programa tenes que seguir los siguientes pasos:

1- Abrir Visual Studio Code.

2- Seleccionar Clone git repository y agregar la URL de este proyecto (https://github.com/gonzairusta/project_coder.git)

3- Crear o seleccionar una carpeta para el programa.

4- En la terminal ejecutar los comandos: "python manage.py migrate" y luego "python manage.py runserver".

5- Luego de escribir python manage.py runserver te aparecera el siguiente link al final de la terminal: http://127.0.0.1:8000/

6- Para tener algunos datos precargados en la terminal puedes ejecuta los comandos: python manage.py shell import seed_data, sino podes cargar tus propios datos.

Hay 3 tipos de modelos dsiponibles: mi-familia, mascotas y automoviles:

http://127.0.0.1:8000/mi-familia : Con este link podras ver el listado de familiares.

http://127.0.0.1:8000/mi-familia/alta Con este link podras agregar familiares al listado.

http://127.0.0.1:8000/mi-familia/buscar Por ultimo con este link vas a poder buscar en el listado si existe el nombre que ingresaste.

Podes reemplazar "mi-familia" por mascotas o automoviles para hacer el mismo proceso.
