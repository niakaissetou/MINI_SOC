import os
import re

# Aller à la racine
os.chdir("/")
file_path = os.path.join("var", "log", "auth.log") #crée le chemin depuis la racine
failed_count = 0
ip_list = []

with open(file_path, "r") as file:

    logs = file.readlines()  # liste de lignes des logs

    for line in logs:

        #{1,3} = entre 1 et 3 chiffres, \b -> pas de combinaisons bizarres et \. pour la forme d'un ip

        if ("Failed password") in line:
            ip_list.append(re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)) #\d = un chiffre (0–9)

            #print(line.strip())
            failed_count += 1

if failed_count == 0:
    print("All is okk")

else :

    for ip in ip_list :
    
        if len(ip) != 0 :
            print(f"ip that failed to connect is ->{ip}")


#Pour tester -> fakeusr@localhost ou l'adresse de loopback a la place de localhost