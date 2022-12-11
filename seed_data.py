from ejemplo.models import Familiar
Familiar(nombre="Gonzalo", direccion="Duarte Quiros 651", nacimiento="1997-12-24").save()
Familiar(nombre="Cristina", direccion="Chacabuco 1304", nacimiento="1950-10-07").save()
Familiar(nombre="Denise", direccion="Figueroa Alcorta 285", nacimiento="1998-07-10").save()

print("Se cargo con éxito los usuarios de pruebas")