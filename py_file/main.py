import os
import re

os.chdir("/")
file_path = os.path.join("var", "log", "auth.log")
failed_count = 0
ip_list = []

with open(file_path, "r") as file:

    logs = file.readlines()

    for line in logs:

        if ("Failed password") in line:
            ip_list.append(re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)) #\d = un chiffre entre 0 et 9

            failed_count += 1

if failed_count == 0:
    print("All is okk")

else :

    for ip in ip_list :
    
        if len(ip) != 0 :
            print(f"ip that failed to connect is ->{ip}")


#Pour tester --> fakeusr@localhost ou l'adresse de loopback a la place de localhost
