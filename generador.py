# password generator with base64 in encoding
# author: jhosmar
# date: 2026-04-02
# password_generator.py - Secure password manager with Base64 encoding
#
# What it does:
# - Generates secure passwords using two user words + symbol + random number
# - Saves passwords encoded in Base64
# - Allows viewing and deleting saved passwords
# - Passwords persist between sessions using a text file
#
# How to use:
# Run: python generador.py
# Then choose from menu:
#   1. Generate new password
#   2. View saved passwords
#   3. Delete password
#   4. Exit



import random
import base64
import time
try:
    with open("passwords.txt", "r") as f:
        passwords = {}
        for line in f:
            line = line.strip()
            if ":" in line:
                # Buscar el primer ":"
                pos = line.find(":")
                username = line[:pos]
                contra = line[pos+1:]
                passwords[username] = contra
except:
    passwords = {}

# password generator using user words  
def generar_contraseña():
    word_1 = input("Enter one word here: ")
    word_2 = input("enter the second word here: ")
    simbolos = ["!", "@", "#", "$", "%", "&", "*"]
    simbolo = random.choice(simbolos)
    number = str(random.randint(10, 999))
    password = word_1 + word_2 + simbolo + number
    while len(password) < 6:
        extra = random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
        password = password + extra
    return password
#deje aqui un espacio para que se vea bonito el codigo

# loop for menu of the script
while True:
    print ("\n=======Generador de contraseñas=======")
    print ("1 Generate password")
    print ("2 view saved password")
    print ("3 delete password")
    print ("4 exit")
    option = input("Enter your  option here: ")

# condicion para la option 1 que pide las palabras al usuario para crear la contraseña
# condition for option 1 that asks the user for the words to create the password

    if option == "1":
        username = input("enter your name here: ")
        if username in passwords:
            print (f"Your user already has a saved password. Choose another option.")
            time.sleep(3)
        else:
            nueva = generar_contraseña()
            codificada = base64.b64encode(nueva.encode()).decode()
            passwords[username] = codificada
            print ("generating password....")
            time.sleep(4)
            print (f"your password has been generated: {nueva}")
            print ("(saved in base64)")
            time.sleep(3)


        with open("passwords.txt", "w") as f:
            for u, c in passwords.items():
                f.write(f"{u}:{c}\n")

        #print ("generating password....")
        #time.sleep(4)
        #print (f"your password has been generated: {nueva}")
        #print ("(saved in base64)")
        #time.sleep(3)

# segunda condicion para ver las contraseñas guardadas con el codigo de mas arriba
# Second condition to view saved passwords with the code above

    elif option == "2":
        if len(passwords) == 0:
            print ("no saved password")
            time.sleep(2)
        else:
            print ("\n=======Saved passwords =======")
            for username, codificada in passwords.items():
                decodificada = base64.b64decode(codificada.encode()).decode()
                print (f"{username}, {decodificada}")
                time.sleep(5)
#dejar espacion entre funciones para que se vea bien el codigo


# tercera condicion para eliminar las contraseñas guardadas
# third condition for deleting saved passwords
    elif option == "3":
        eliminar = input("Enter the user to be deleted :")
        if eliminar in passwords:
            del passwords[eliminar]
            with open("passwords.txt", "w") as f:
                for u, c in passwords.items():
                    f.write(f"{u}:{c}\n")
            print (f"Removing password from {eliminar}....")
            time.sleep(3)
            print ("password removed")
            time.sleep(2)
        else:
            print (f"{eliminar}'s password not found ")
            time.sleep(2)
#espacios entre funciones


# cuarta condicion para salir del loop y detener la script
    elif option == "4":
        print ("see you later")
        break


    else:
        print ("Invalid option, I tried again ")
