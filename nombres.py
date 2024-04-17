
#cantidad de parametros indefinida 
def escribir_el_nombre(*args, **kwargs):
    print("     inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key ", key, "--value", value)
    

escribir_el_nombre("Ludmila",primer_nombre="Hernan", segundo_nombre="Herramienta", primer_apellido="Hernandez", segundo_apellido="Herrera")
escribir_el_nombre("Franco","Ramiro",primer_nombre="Jorge", segundo_nombre="Reynols", primer_apellido="Lopez")
escribir_el_nombre(primer_nombre="Cecilio", primer_apellido="Cesar")

