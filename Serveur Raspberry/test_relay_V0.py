import RPi.GPIO as GPIO
import socket
import time

GPIO.setmode(GPIO.BCM)

hote = ''
port = 12800

GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) #attention relai actif a l'état bas( initialisation à état haut)
GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(14, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)

import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != "fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    var =msg_recu.decode("ASCII").strip()
    print(var)
     
    if "O" in var and var == "O": 
        GPIO.output(2,GPIO.LOW)
    elif "F" in var and var == "F":
        GPIO.output(2,GPIO.HIGH)
 
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()

#while True:
    #GPIO.input(2)
    #GPIO.output(2, not GPIO.input(2))
    #time.sleep(1)
