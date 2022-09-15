
from Ds_Style import *
from time import sleep as timeout
import time
import base64
import os
os.system ('clear')
###################################
def banner():
    os.system('clear')
    ban='''
\033[1;31m _____   _____        _   _       ___   _____   _   _
\033[1;32m|  _  \ /  ___/      | | | |     /   | /  ___/ | | | |
\033[1;33m| |_| | | |___       | |_| |    / /| | | |___  | |_| |
\033[1;31m|  _  { \___  \      |  _  |   / / | | \___  \ |  _  |
\033[1;32m| |_| |  ___| |      | | | |  / /  | |  ___| | | | | |
\033[1;33m|_____/ /_____/      |_| |_| /_/   |_| /_____/ |_| |_|

\033[1;31m-\033[1;37m BLACK\033[1;31m_\033[1;37mSTORM TEAM\033[1;31m -
'''
    Animation(ban).SlowText(Time=0.01)
    print ()
    main ()
##############################################

def Encode():
    ss=str(input ('\n\033[1;33mEnter Your Txt Encode : \033[1;31m'))
    bshash=base64.b64encode (ss.encode ('ascii'))
    if ss=='':
        banner()
    else:
        txt='\033[1;32mEncrypted Successfully....'
        Animation(txt).SlowText(Time=0.01)
        print (' ')
        print ('\033[1;33m-'*38)
        print ('\033[1;31mDark_Storm : \033[1;31m[\033[1;32m',bshash,'\033[1;31m]')
        print ('\033[1;33m-'*38)
        time.sleep (0.1)
        print (' ')
        input ('\033[1;32m==>> \033[1;31m')
        banner()
################################################
def Decode():
    try:
       ssw=str(input ('\n\033[1;33mEnter Your Hash Decode : \033[1;31m'))
       bshash=base64.b64decode(ssw)
       if ssw=='':
           banner ()
       txt='\033[1;32mDecrypted successfully....'
       Animation(txt).SlowText(Time=0.01)
       print (' ')
       print ('\033[1;33m-'*38)
       print ('\033[1;31mDark_Storm : \033[1;31m[\033[1;32m',bshash,'\033[1;31m]')
       print ('\033[1;33m-'*38)
       time.sleep (0.1)
       print (' ')
       input ('\033[1;32m==>> \033[1;31m')
       banner()
    except ValueError:
         timeout (0.01)
         input ('\033[1;32mPlease Enter Your Hash To Decoding ...? ')
         banner()

############################

def main():
    mylist=['[1] Encode Txt ','[2] Decode Hash','[99] Exit']
    Ds_Style(mylist).Center(cols=2)
    print ()
    txt='\033[1;32mChoose Number To Start...?'
    Animation(txt).SlowText(Time=0.01)
    print ()
    main=input('''\033[1;31m╭────(\033[1;37mDark\033[1;31m_\033[1;37mStorm\033[1;31m)\033[1;37m#\033[1;31m(\033[1;37mHash\033[1;31m)──────\033[1;37m$
\033[1;31m│
\033[1;31m╰──\033[1;37m>>>$\033[1;33m ''')
    if main =='1':
        Encode()
    elif main =="2":
        Decode()
    elif main =='99':
        timeout (1)
        os.system ('clear')
    else:
        banner()
################################
banner ()

###################
## The Dark Storm :
#------------------
