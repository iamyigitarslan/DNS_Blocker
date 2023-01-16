import time, os
from datetime import datetime as dt

host_path = ""
redirect = "127.0.0.1"

def detectOS():
    if os.name == "nt":
        return "C:\Windows\System32\drivers\etc\hosts"
    else:
        return "/etc/hosts"

host_path = detectOS()
	

    
website_list = open('DNS_Blocker/url-list.txt','r')

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 9):

        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
            
        print("All the listed website are blocked!!")
        break
    else:

        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
        print("Websites are unblocked!")
        break

