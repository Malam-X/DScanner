
Bold='\u001b[1m'
Underline='\u001b[4m'
Reversed='\u001b[7m'
Black='\u001b[30m'
Red='\u001b[31m'
Green='\u001b[32m'
Yellow='\u001b[33m'
Blue='\u001b[34m'
Magenta='\u001b[35m'
Cyan='\u001b[36m'
White='\u001b[37m'
Reset='\u001b[0m'
BrightBlack='\u001b[30;1m'
BrightRed='\u001b[31;1m'
BrightGreen='\u001b[32;1m'
BrightYellow='\u001b[33;1m'
BrightBlue='\u001b[34;1m'
BrightMagenta='\u001b[35;1m'
BrightCyan='\u001b[36;1m'
BrightWhite='\u001b[37;1m'
promt = f'{Bold}{BrightBlue}[+] Choice:{BrightGreen} ',f'{Reset}'

x = {
    "__version__": '0.2.0',
    "__author__": "DR4G0N5",
    "__github__": "https://github.com/Malam-X"
}
def banner():
    print(r'''{BOLD}{COLOR}

    {BLUE}_____{COLOR}   _____
   {BLUE}|  __ \{COLOR} / ____| GitHub: {GREEN}{GITHUB}{COLOR}
   {BLUE}| |  | |{COLOR} (___   ___ __ _ _ __  _ __   ___ _ __
   {BLUE}| |  | |{COLOR}\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
   {BLUE}| |__| |{COLOR}____) | (_| (_| | | | | | | |  __/ |
   {BLUE}|_____/{COLOR}|_____/ \___\__,_|_| |_|_| |_|\___|_|

     Coded By {BLUE}{author}{COLOR} | {YELLOW_COLOR}Version: [ {VERSION} ]{RESET}

'''.format(BOLD=Bold,
    COLOR=BrightRed,
    author=x['__author__'],
    YELLOW_COLOR=BrightYellow,
    VERSION=x['__version__'],
    RESET=Reset,
    GITHUB=x['__github__'],
    GREEN=BrightGreen,
    BLUE=BrightBlue,
    MAGENTA=BrightMagenta))

list_tools = {
    'TOOLS': f'\n\n\n{Bold}{Green}[+] LIST SCANNER TOOLS [+] {Reset}\n\n',
    '01': f'{Bold}{BrightYellow}   [01] MTR LOOKUP\n',
    '02': '   [02] NPING LOOKUP\n',
    '03': '   [03] DNS LOOKUP\n',
    '04': '   [04] REVERSE DNS LOOKUP\n',
    '05': '   [05] WHOIS LOOKUP\n',
    '06': '   [06] GEOIP LOOKUP\n',
    '07': '   [07] REVERSE IP LOOKUP\n',
    '08': '   [08] HTTP HEADER LOOKUP\n',
    '09': '   [09] PAGE LINK LOOKUP\n',
    '10': f'   [10] ASLOOKUP{Reset}\n',
    'EXIT': f'{Bold}{Red}   [CTRL+C] EXIT{Reset}\n\n'
}
