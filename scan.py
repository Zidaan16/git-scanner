import requests, os, time, sys, re, platform

class main:
	def __init__(self, f):
		self.file = f
		self.merah = '\033[1;31m'
		self.ijo = '\033[1;32m'
		self.kuning = '\033[1;33m'
		self.aqua = '\033[1;36m'
		self.normal = '\033[0m'
		self.head = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
		}

	def resp(self, url): # Respon
		r = requests.get(url, headers=self.head)

		if r.status_code == 200:
			c = self.ijo
		elif r.status_code == 403:
			c = self.kuning
		else:
			c = self.merah

		if r.is_redirect == False:
			a = self.merah
		else:
			a = self.aqua

		print(c+"[URL]"+self.normal,url,"<<"+c,r.status_code, self.normal+"<<"+a,r.is_redirect, self.normal)
		time.sleep(0.5)

	def reg(self):	# Fungsi regex
		f = open(self.file, "r").read().splitlines()
		a = list(set(re.findall("(http[s]?://[a-zA-Z0-9._+-]+)", str(f))))
		print("List Loaded:",len(a))
		print("-----------------------")
		return a

def clean():
	if platform.system() == "Linux":
		os.system("clear")
	if platform.system() == "Windows":
		os.system("cls")

clean()
try:
	kelas = main(sys.argv[1])
	for i in kelas.reg():
		kelas.resp(i+"/.git/HEAD")
except (IndexError, FileNotFoundError) as e:
	print("File tidak ditemukan")
else:
	print("-----------------------")