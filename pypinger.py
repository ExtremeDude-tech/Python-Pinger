import os, threading, subprocess, random;from colorama import Fore, init
colors = (Fore.RED, Fore.BLUE, Fore.LIGHTWHITE_EX, Fore.GREEN, Fore.MAGENTA)
init()
title = """
       ▄███████▄  ▄█  ███▄▄▄▄      ▄██████▄     ▄████████    ▄████████ 
      ███    ███ ███  ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ 
      ███    ███ ███▌ ███   ███   ███    █▀    ███    █▀    ███    ███ 
      ███    ███ ███▌ ███   ███  ▄███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀█████████▀  ███▌ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
      ███        ███  ███   ███   ███    ███   ███    █▄  ▀███████████ 
      ███        ███  ███   ███   ███    ███   ███    ███   ███    ███ 
     ▄████▀      █▀    ▀█   █▀    ████████▀    ██████████   ███    ███ 
                                                            ███    ███ """

os.system('title Pinger - by ExtremeDev')
print(title)

def ping(ip):
    f = os.popen('ping {} -n 1'.format(ip))
    if 'Request timed out.' in f.read():
        print(random.choice(colors) + '    Request timed out' + Fore.WHITE)
    else:
        print(random.choice(colors) + '    Pinging {} with 32 bytes of data'.format(ip) + Fore.WHITE)

print('    Enter the victim ip address.')
ip_ad  = input('    > ')
print()

while True:
    if threading.active_count() < 2:
        threading.Thread(target=ping, args=(ip_ad,)).start()
