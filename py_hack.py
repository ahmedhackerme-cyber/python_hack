import colorama as c
import os
import subprocess as s
import time
import webbrowser as wb

time.sleep(1)
s.run("clear.bat")
c.init()

f = c.Fore
print(f.RED   +"██   ██  "+f.YELLOW+" █████ "+f.BLUE+"  █████  "+f.WHITE+"  ██   ██  "+f.GREEN+"  █████"+f.YELLOW+"   ██   ██")
print(f.RED   +"██   ██  "+f.YELLOW+" █   █ "+f.BLUE+"  █   █  "+f.WHITE+"  ██   ██  "+f.GREEN+"  ██ ██"+f.YELLOW+"   ██   ██")
print(f.RED   +"███████  "+f.YELLOW+"██   ██"+f.BLUE+" ██      "+f.WHITE+"  ███████  "+f.GREEN+"  █████"+f.YELLOW+"   ██   ██")
print(f.RED   +"██   ██  "+f.YELLOW+"███████"+f.BLUE+" ██   █  "+f.WHITE+"  ██   ██  "+f.GREEN+"  █    "+f.YELLOW+"    ████  ")
print(f.RED   +"██   ██  "+f.YELLOW+"██   ██"+f.BLUE+" ██   █  "+f.WHITE+"  ██   ██  "+f.GREEN+"  █    "+f.YELLOW+"    ██    ")
print(f.RED   +"██   ██  "+f.YELLOW+"██   ██"+f.BLUE+"  █████  "+f.WHITE+"  ██   ██  "+f.GREEN+"  █    "+f.YELLOW+"      ███ ")
   
   



print(f.YELLOW+"["+f.RED+"1"+f.YELLOW+"]"+f.WHITE+" hacker web")
print(" ")
print(f.YELLOW+"["+f.RED+"0"+f.YELLOW+"]"+f.RED+" exit")

print("")
i = input(" > ")

if i == "0":
    exit()
elif i == "1":
    time.sleep(1)
    s.run("clear.bat")
    c.init()

    f = c.Fore
    print(f.YELLOW+"["+f.RED+"1"+f.YELLOW+"]"+f.WHITE+" open web")
    print(" ")
    print(f.YELLOW+"["+f.RED+"2"+f.YELLOW+"]"+f.WHITE+" search page web")
    print(" ")
    print(f.YELLOW+"["+f.RED+"0"+f.YELLOW+"]"+f.RED+" exit")
    print(" ")
    i = input(" > hacker web > ")
    if i == "1":
        s.run("clear.bat")
        c.init()
        while True:
            print(f.RED)
            w = input(" > hacker web > open web > web is : ")
            if w == "exit":
                print("exit")
                print(f.WHITE+" ------------------------- "+f.RED+"Stop"+f.WHITE+" -------------------------------")
                exit()
            wb.open("https://"+w+"/")
            print(" url = "+f.GREEN+"https://"+w+"/"+f.WHITE+"------------------------------")
    elif i == "2":
        import requests
        
        def e(url, timeout=5):
            try:
                r = requests.head(url, allow_redirects=True, timeout=timeout)
                print(f.RED+r.status_code < 400)
            except requests.RequestException:
                print(f.RED+"False")
        s.run("clear.bat")
        while True:
            i = input(" > hacker web > search page web > page is : ")
            if i == "exit":
                exit()
            print(" ")
            e("https://"+i+"/")
            
