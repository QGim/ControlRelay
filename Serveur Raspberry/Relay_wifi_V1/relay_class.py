import socket
import RPi.GPIO as GPIO

class GESTION_RELAY:

     def __init__(self):
         GPIO.setmode(GPIO.BCM)
         
         GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) #attention relai actif a l'état bas( initialisation à état haut)
         GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
         GPIO.setup(14, GPIO.OUT, initial=GPIO.HIGH)
         GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)



class WIFI:

    wifi = socket.socket()

    def __init__(self):
        # Define the socket
        self.wifi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connexion(self, hote, port):
       
        self.wifi.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.wifi.bind((hote, port))
        self.wifi.listen(5)
        connexion_avec_client, infos_connexion = self.wifi.accept()
        msg = "Le serveur écoute à présent sur le port:" + str(port)+ "\n"
        connexion_avec_client.send(msg.encode("UTF-8"))
        return connexion_avec_client
       

    def close(self,connex_client): 
        connex_client.close()
        self.wifi.close()

