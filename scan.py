"""

Author: DR4G0N5
Version: 0.2.0

"""
import sys,platform
import re
from os import system as STES
from time import sleep as TIMER
from var import banner
from var import *

def clear():
    if sys.platform.startswith('darwin'):
        STES('clear')
    elif sys.platform.startswith('linux'):
        STES('clear')
    elif sys.platform.startswith('freebsd'):
        STES('clear')
    else:
        STES('cls')
class target:
    def __init__(self):
        clear()
        banner()
        try:
            while True:
                import socket
                htts = ['https://']
                htt = ['http://']
                ht = ['www.']
                u = input(f'{BrightCyan}[+] Url target:{BrightGreen} ')
                host = socket.gethostbyname(u)
                print(f'{Reset}')
                htt.append(host)
                htts.append(u)
                ht.append(u)
                TargetNOTFOUND=(f'{Bold}{BrightRed}[!] Put your target without [https/http].\n[+] Try again...\n{Reset}')
                if '://' in u:
                    print(''.join(TargetNOTFOUND))
                    TIMER(0.1)
                elif 'https' in u:
                    print(''.join(TargetNOTFOUND))
                    TIMER(0.2)
                elif 'http' in u:
                    print(''.join(TargetNOTFOUND))
                    TIMER(0.3)
                elif '.' not in u:
                    print(''.join(TargetNOTFOUND))
                    TIMER(0.3)
                else:
                    print(f'{Bold}{Yellow}[1] HTTP\n[2] HTTPS\n{Reset}')
                    while True:
                        check_ht = input(''.join(promt))
                        if len(check_ht) > 2:
                            print(f'{Bold}{BrightRed}[!] Choice not found. {Reset}')
                        elif '://' in check_ht:
                            print(f'{Bold}{BrightRed}[!] Choice not found. {Reset}')
                        else:
                            if check_ht == '1':

                                x = '{TARGET}'.format(TARGET=htt[1])

                                y = '{TARGET}'.format(TARGET=htts[1])

                                z = '{TARGET}'.format(TARGET=ht[1])
                                self.main_target(x,y,z)
                            elif check_ht == '2':
                                w = '{HTTP}{TARGET}{SPLI}'.format(
                                    HTTP=htts[0],
                                    TARGET=htts[1],
                                    SPLI=htts[0][7])

                                x = '{TARGET}'.format(TARGET=htt[1])

                                y = '{TARGET}'.format(TARGET=htts[1])

                                z = '{WW}{TARGET}'.format(WW=ht[0],TARGET=ht[1])
                                self.main_target(w,x,y,z)
        except KeyboardInterrupt:
            sys.exit(f'\n{Bold}{BrightRed}[+] Aborted.{Reset}')
        finally:
            try:
                pass
            except:
                sys.exit(1)
    def main_target(self, main_url, host, url, urls):
        global list_tools
        clear()
        banner()
        target_main = main_url
        target_host = host
        target_url = url
        target_urls = urls
        print(f'{Bold}{BrightBlue}[+] Target URL : {BrightMagenta}'+main_url+f'{Reset}')
        print(f'{Bold}{BrightBlue}[+] Target Host: {BrightMagenta}'+target_host+f'{Reset}')
        print(
            list_tools['TOOLS'],
            list_tools['01'],
            list_tools['02'],
            list_tools['03'],
            list_tools['04'],
            list_tools['05'],
            list_tools['06'],
            list_tools['07'],
            list_tools['08'],
            list_tools['09'],
            list_tools['10'],
            list_tools['EXIT'])
        while True:
            BAD_CHOICE = f'{Bold}{Red} [!] Choice not found.{Reset}'
            choice = input(''.join(promt))
            if len(choice) == 3:
                print(''.join(BAD_CHOICE))
                TIMER(0.3)
            else:
                NAME_SAVED=f'{Bold}{Green}[+] Result Saved at '
                try:
                    import requests
                    import os.path
                    from os import path
                    def c_b(choice, respon):
                        file = choice
                        res = respon
                        NAME_DIR = f'.result'
                        try:
                            print(f'{Bold}{Blue}[-] Checking...{Reset}')
                            if path.exists(f'{NAME_DIR}') == False:
                                print(f'{Bold}{Red}[+] Dir Not Found .. [✘]{Reset}')
                                TIMER(1.2)
                                print(f'{Bold}{Blue}[-] Creating...{Reset}')
                                TIMER(1.7)
                                STES('mkdir .result')
                                print(f'{Bold}{Green}[+] Dir Created .. [✔]{Reset}')
                                TIMER(1.8)
                            else:
                                try:
                                    pass
                                except:
                                    sys.exit(1)
                        except KeyboardInterrupt:
                            sys.exit(f'\n{Bold}{Red} Aborted.{Reset}')
                        finally:
                            clear()
                            banner()
                            try:
                                NAME_PATH = f'.result/{file}-{target_host}.txt'
                                file = open(f'{NAME_PATH}', 'w')
                                file.write(res)
                                print(res)
                                print(''.join(NAME_SAVED) + f'{NAME_PATH}')
                            finally:
                                sys.exit(1)
                    if choice in ['01', '1']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/mtr/?q={}'.format(target_host))
                            res = req.text
                            c_b('mtr-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['02', '2']:
                        try:
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/nping/?q={}'.format(target_host))
                            res = req.text
                            c_b('nping-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['03', '3']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/dnslookup/?q={}'.format(target_url))
                            res = req.text
                            c_b('dns-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['04', '4']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/reversedns/?q={}'.format(target_host))
                            res = req.text
                            c_b('reverse-dns-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['05', '5']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/whois/?q={}'.format(target_host))
                            res = req.text
                            c_b('whois-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['06', '6']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/geoip/?q={}'.format(target_host))
                            res = req.text
                            c_b('geoip-lookup', res)

                        finally:
                            sys.exit(1)
                    elif choice in ['07', '7']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/reverseiplookup/?q={}'.format(target_host))
                            res = req.text
                            c_b('reverseip-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['08', '8']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/httpheaders/?q={}'.format(target_urls))
                            res = req.json()
                            c_b('httpheaders-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['09', '9']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/pagelinks/?q={}'.format(target_urls))
                            res = req.text
                            c_b('pagelinks-lookup', res)
                        finally:
                            sys.exit(1)
                    elif choice in ['10', '10']:
                        try:
                            print(f'{Bold}{Blue}[+] Lookingup...{Reset}')
                            TIMER(2)
                            clear()
                            banner()
                            print(f'{Bold}{Green}[+] Scanning...{Reset}')
                            req = requests.get('https://api.hackertarget.com/aslookup/?q={}'.format(target_host))
                            res = req.text
                            c_b('as-lookup', res)
                        finally:
                            sys.exit(1)
                    else:
                        raise ValueError(f'{Bold}{Red} [!] Not Found')
                except ValueError:
                    pass
target()
#choice = input(''.join(promt))
#if choice in ['1', '01']:
#    target()
