# quess.py - Guess the secret number game
# Author: jhosmar
# Date: 2026-04-05
#
# What it does:
# - The program thinks of a random number between 1 and 100
# - The player has 5 attempts to guess it
# - After each guess, gives hints: "too high" or "too low"
# - Tracks number of attempts
# - Shows the secret number if the player loses
#
# How to use:
# Run: python quess.py
# Then enter your guesses and try to find the secret number



# Author: jhosmar


import random
# Generate random secret number between 1 and 100
numero_secreto = random.randint(1, 100)
tried = ""
contador = 0
max_intentos = 5
access = False
print (f" Welcome to a number guessing game. The system will think of a number between")
print (f"the 1 and the 100, your job will be to try to guess the number but with a")
print (f"limited number of 5 attempts")
print ("Do you want to play? ?")
respuesta = input("Enter your answerº here (yes/no):")
if respuesta == "no":
    print ("Okay, we hope you'll want to play next time.")
elif respuesta == "yes":
     # Main game loop
    while access == False and contador < 5:
        intento = int(input("Enter your number here: "))
# Author: jhosmar
        if intento == numero_secreto:
            access = True
            print (f"¡Excellent! The number was {numero_secreto} You did it!")
            # Check if guess is correct
            # Check if guess is too high
            # Check if guess is too low
        elif intento > numero_secreto:
            # Track number of attempts
            contador = contador + 1
            print (f"The number is incorrect. Your number of attempts is {contador}")
            print (f" Hint: the number is lower than {intento}")
            # Check if guess is correct
            # Check if guess is too high
            # Check if guess is too low
        elif intento < numero_secreto:
            # Track number of attempts
            contador = contador + 1
            print (f"The number is incorrect. Your number of attempts is {contador}")
            print (f"Hint: the number is higher than {intento}")
    if access == False:
        print (f" You have reached the maximum number of attempts. The number was {numero_secreto}")
#elif respuesta == "no":
    #print ("ok esperaremos que la proxima quieras jugar")
#esto de arriba es codigo basura que no quise borrar
#por eso estan aqui como si fueran comentarios pero es codigo basura
# Author: jhosmar
