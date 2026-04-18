# json_demo.py - Save and load data using JSON
# Author: Mariscal
# Date: 2026-04-18

import json
import time

# Datos de ejemplo
perfil = {
    "nombre": "Jhosmar",
    "dias_programando": 68,
    "scripts": ["generator", "tareas", "guess", "countdown", "unit_converter"],
    "objetivo": "Comprar laptop y trabajar freelance"
}

# Guardar en archivo JSON
with open("perfil.json", "w") as archivo:
    json.dump(perfil, archivo, indent=4)

print("✅ Datos guardados en perfil.json")
time.sleep(1)

# Leer desde archivo JSON
with open("perfil.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print("\n📖 Datos cargados:")
print(f"   Nombre: {datos_cargados['nombre']}")
print(f"   Días programando: {datos_cargados['dias_programando']}")
print(f"   Scripts: {len(datos_cargados['scripts'])} scripts")
print(f"   Objetivo: {datos_cargados['objetivo']}")
