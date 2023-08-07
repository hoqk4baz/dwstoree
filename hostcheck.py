#TG CHANNEL : @dwstoree

import requests
import os



def enza_logo():
    os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizlemek için
    print("\033[38;2;0;153;255m")
    print("""
    ________              ______              
    ___  __ \_____ __________  /__ 
    __  / / /  __ `/_  ___/_  //_/ 
    _  /_/ // /_/ /_  /   _  ,<   
    /_____/ \__,_/ /_/    /_/|_|""")
    print("")
    print("\033[38;2;255;128;0m")
    print("                        ENZA")
    print("\033[38;2;255;0;255m")
    print("    Gemiler battı diye")
    print("\033[38;2;153;0;204m")
    print("     Acırmı denizin canı..")
    print("")
    print("\033[0m")

def detaylar(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        response = requests.get(url, verify=True)
    except requests.exceptions.SSLError:
        print("\033[91mSSL hatası alındı, HTTP olarak denenecek.\033[0m")
        url = url.replace('https://', 'http://')
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"URL: {url}, Hata: {e}")
            return
    enza_logo()

    print("")
    print("---"*12)
    print(f"\033[93mURL: {url}\033[0m")
    print("---"*12)
    print("\033[92mSunucu: {server}\033[0m".format(server=response.headers.get('server', 'Bilinmiyor')))
    print("")
    print("\033[92mVia: {via}\033[0m".format(via=response.headers.get('Via', 'Bilinmiyor')))
    print("")
    print("\033[92mBağlantı Türü: {conn}\033[0m".format(conn=response.headers.get('connection', 'Bilinmiyor')))
    print("")
    print("\033[0mİçerik Uzunluğu: {length}".format(length=len(response.text)))
    print("")
    print("\033[0mİçerik Türü: {ctype}".format(ctype=response.headers.get('content-type', 'Bilinmiyor')))
    print("---"*12)
    print("")

while True:
    user_url = input("\033[93mURL GİR(Çıkmak İçin 'c': \033[0m")
    if user_url.lower() == 'c':
        break
    detaylar(user_url)
