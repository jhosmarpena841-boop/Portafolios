import os
import shutil
import time

formatos = {
        ".pdf": "documentos_pdf",
        ".csv": "documentos_csv",
        ".mp3": "archivos_mp3"
            }



# 1. Creamos la carpeta de destino por si no existe

os.makedirs("documentos_pdf", exist_ok=True)
os.makedirs("documentos_csv", exist_ok=True)
os.makedirs("archivos_mp3", exist_ok=True)


# 2. Listamos todos los archivos donde está corriendo este script


todos_los_archivos = os.listdir(".")
contador = 0

# 3. Revisamos uno por uno con un ciclo 'for'
for archivo in todos_los_archivos:

    nombre, extencion = os.path.splitext(archivo)
    extencion = extencion.lower()
    try:
        if extencion in formatos:
            shutil.move(archivo, f"{formatos[extencion]}")
            contador += 1
            print (f"archivo '{archivo}' movido correctamente")
            time.sleep(1)
        else:
            print (f"el formato '{extencion}' de {nombre}  no es compatible")
            time.sleep(1)
    except KeyError:
        print (f"el formato {extencion} de  {nombre} no es compatible")
        time.sleep(1)
    except shutil.Error:
        print (f"archivo '{archivo}'  ya existe en la carpeta: {formato[extencion]} ")
        time.sleep(1)

print ("todos los archivos han sido organizados, revisa las subcarpetas")
print (f"archivos organizados correctamente: {contador}")

