#Modified Code- Ardit Sulce's Udemy Python Mega Course 

import time 
from datetime import datetime as dt
#hosts_temp="hosts" #used for debugging 
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.instagram.com", "www.pinterest.com", "www.facebook.com", "www.youtube.com", "www.netflix.com", "www.twitter.com", "www.tiktok.com", "www.yahoo.com"]

while True: #Work is from 8am-3pm 
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print("PROCESSING: Work/School Hours")
        with open(hosts_path, "r+") as file: #r+ allows for read and write 
            content=file.read() #entire text of hosts file
            for website in website_list:
                if website in content:
                    pass 
                else: #add website to hosts file
                    file.write(redirect+ " "+ website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines() #list with all lines of hostfile 
            file.seek(0) #replace pointer to first line of host file 
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()    
        print("PROCESSING: Free Time")
    time.sleep(5) #debugging
