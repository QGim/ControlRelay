from relay_class import * 
import time

hote = ''
port = 12800
start = 1

while (start == 1):

    init = GESTION_RELAY()
    co = WIFI()
    connex_client = co.connexion(hote, port)
    msg = "Serveur en attente d'une instrcution"+"\n"
    connex_client.send(msg.encode("UTF-8"))


    msg_recu = b""
    bit = 1
    start = 0
    while (bit == 1):
        msg_recu = connex_client.recv(1024)
        # L'instruction ci-dessous peut lever une exception si le message
        # Réceptionné comporte des accents
        var =msg_recu.decode("ASCII").strip()
        print(var)

        if "F" in var and var == "F":
            GPIO.output(2,GPIO.LOW)
            #GPIO.output(2, not GPIO.input(2))
        elif "f" in var and var == "f":
            GPIO.output(2,GPIO.HIGH)
        elif "S" in var and var == "S":
            GPIO.output(3,GPIO.LOW)
        elif "s" in var and var == "s":
            GPIO.output(3,GPIO.HIGH)
        elif "T" in var and var == "T":
            GPIO.output(14,GPIO.LOW)
        elif "t" in var and var == "t":
            GPIO.output(14,GPIO.HIGH)
        elif "E" in var and var == "E":
            GPIO.output(15,GPIO.LOW)
        elif "e" in var and var == "e":
            GPIO.output(15,GPIO.HIGH)
        elif "all" in var and var =="all":
            GPIO.output(2,GPIO.LOW)
            GPIO.output(3,GPIO.LOW)
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)
        elif "off" in var and var =="off":
            GPIO.output(2,GPIO.HIGH)
            GPIO.output(3,GPIO.HIGH)
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
        elif "fin" in var and var =="fin":
            bit = 0
            start = 1
        elif len(var) == 0:
            bit = 0
            start = 1 

    msg2 = "Fermeture de la connexion"
    connex_client.send(msg2.encode("UTF-8"))

    co.close(connex_client)
