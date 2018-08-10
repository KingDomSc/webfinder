#!/usr/bin/python

import requests, socket, ssl, sys
HOST       = ''
Host_path  = ''
COOKIES    = ''
https      = 443
headers_inf = ''
mmethond = 'http://'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0'
AcceptHeader = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
useTypes = True
Folders = [
    'admin', 'administrator', 'adminpanel', 'cpanel', 'login', 'admins', 'logins', 'adm', 'adminitem', 'adminitems',
    'manager', 'superuser', 'access', 'sysadm', 'supervisor', 'member', 'members', 'user', 'cp', 'management', 'signin',
    'log-in', 'sign_in', 'log_in', 'users', 'account', 'accounts', 'relogin', 'check', 'isadmin', 'moderator',
    'admincontrol', 'controlpanel', 'fileadmin', 'myadmin', 'ur-admin', 'server', 'wp-admin', 'wp-login', 'wp-users',
    'wp-user', 'admincp', 'logincp', 'administrators', 'administratorscp', 'root', 'secret', 'auth', 'admin_auth',
    'admin_login', 'login_admin', 'upload', 'uploader'
]
types = [
    '.php', '.html', '.htm', '.asp', '.aspx', 'cgi', 'txt' # just for fun
]
def scanFolders(fold):
    header = "GET " + Host_path + fold + " HTTP/1.1\r\nHost: " + HOST + "\r\nUser-Agent: " + userAgent + "\r\n" + COOKIES + headers_inf + "Accept: " + AcceptHeader + "\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: close\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if https == 443:
        while True:
            try:
                cc = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                ss = cc.wrap_socket(s, server_hostname = HOST)
                ss.connect((HOST, https))
                ss.send(header.encode())
                result = ss.recv(1000)
                ss.close()
                break
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("\033[1m\033[91m'-------------> There's some errors, wait to try again\033[0m")
    else:
        while True:
            try:
                s.connect((HOST, https))
                s.send(header.encode())
                result = s.recv(1000)
                s.close()
                break
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("\033[1m\033[91m'-------------> There's some errors, wait to try again\033[0m")
    return result
print("""


\033[35m
        __      __      ___.   ___________.__            .___            
       /  \\    /  \\ ____\\_ |__ \\_   _____/|__| ____    __| _/___________ 
       \\   \\/\\/   // __ \\| __ \\ |    __)  |  |/    \\  / __ |/ __ \\_  __ \\
        \\        /\\  ___/| \\_\\ \\|     \\   |  |   |  \\/ /_/ \\  ___/|  | \\/
         \\__/\\  /  \\___  >___  /\\___  /   |__|___|  /\\____ |\\___  >__|   
              \\/       \\/    \\/     \\/            \\/      \\/    \\/       

         ---===[\033[0m   \033[1;34mWebsite admin finder v.1 - by KingDomSc\033[0m   \033[35m]===---    \033[0m  


""")
inputUrl = input("""\033[94m- Write website \'HOST\' here ( example : www.google.com ) : \033[0m""")
HOST = str(inputUrl)
useSSL = input("""\033[94m- Did you wnat to use SSL/HTTPS Connection? [Y/N] : \033[0m""")
if ((useSSL == 'y') or (useSSL == 'Y')):
    https = 443
    mmethond = 'https://'
else:
    https = 80
    mmethond = 'http://'
itui = input("""\033[94m- Use files type scanner ? [Y/N] : \033[0m""")
if ((itui == 'y') or (itui == 'Y')) :
    useTypes = True
else:
    useTypes = False
while 1:
    hrdINF = input("\033[94m- Is there any Headers Info you want add ? [Y/N] : \033[0m")
    if ((hrdINF == 'y') or (hrdINF == 'Y')):
        headervalue = input("\033[30m'----------> Write header info with value ,example ! Refere : google.com : \033[0m")
        headervalue = str(headervalue)
        if not headervalue == None:
            headers_inf += headervalue + '\r\n'
        else:
            break
    else:
        break
iui = input("""\033[94m- Is there a special ' User-Agent ' ? [Y/N] : \033[0m""")
if ((iui == 'y') or (iui == 'Y')) :
    userA = input("""\033[94m'----------> Write User-Agent here : \033[0m""")
    if not str(userA) == None:
        userAgent = str(userA)
iaci = input("""\033[94m- Is there a special ' Accept Header ' ? [Y/N] : \033[0m""")
if ((iaci == 'y') or (iaci == 'Y')) :
    acceptA = input("""\033[94m'----------> Write Accept Header here : \033[0m""")
    if not str(acceptA) == None:
        AcceptHeader = str(acceptA)
iai = input("""\033[94m- Is there any path's need to write it ? [Y/N] : \033[0m""")
if ((iai == 'y') or (iai == 'Y')):
    inputVari = input("""\033[30m'----------> Write Path Here , ( example in RED : \033[31m/website/paragraph\033[30m ) : \033[0m""")
    Host_path = str(inputVari)
    if not Host_path == None:
        if not Host_path.endswith('/'):
            Host_path += '/'
        if not Host_path.startswith('/'):
            Host_path = '/' + Host_path
    else:
        Host_path = '/'
else:
    Host_path = '/'
ici = input("""\033[94m- Is there any COOKIES values? [Y/N] : \033[0m""")
if ((ici == 'y') or (ici == 'Y')):
    ccs = input("""\033[30m'----------> Write COOKIES values here : \033[0m""")
    if not str(ccs).strip():
        COOKIES = ''
    else:
        COOKIES = 'Cookie: ' + ccs + '\r\n'
print("""
""")
if useTypes == True:
    for x in Folders:
        result1 = str(scanFolders(x))
        if "HTTP/1.1 200 " in result1:
            print('[   \033[92m200\033[0m     ]  =  ' + mmethond + HOST + Host_path + x)
        elif "HTTP/1.1 301 " in result1:
            print('[   \033[93mMoved\033[0m   ]  =  ' + mmethond + HOST + Host_path + x)
        else:
            print('[   \033[31mFail\033[0m    ]  =  ' + mmethond + HOST + Host_path + x)
        for xx in types:
            result2 = str(scanFolders(x + xx))
            if "HTTP/1.1 200 " in result1:
                print('[   \033[92m200\033[0m     ]  =  ' + mmethond + HOST + Host_path + x + xx)
            elif "HTTP/1.1 301 " in result1:
                print('[   \033[93mMoved\033[0m   ]  =  ' + mmethond + HOST + Host_path + x + xx)
            else:
                print('[   \033[31mFail\033[0m    ]  =  ' + mmethond + HOST + Host_path + x + xx)
else:
    for x in Folders:
        result1 = str(scanFolders(x))
        if "HTTP/1.1 200 " in result1:
            print('[   \033[92m200\033[0m     ]  =  ' + mmethond + HOST + Host_path + x)
        elif "HTTP/1.1 301 " in result1:
            print('[   \033[93mMoved\033[0m   ]  =  ' + mmethond + HOST + Host_path + x)
        else:
            print('[   \033[31mFail\033[0m    ]  =  ' + mmethond + HOST + Host_path + x)

print("\r\n")
