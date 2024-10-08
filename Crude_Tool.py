#!/usr/bin/python3

import os
import argparse
import time
from subprocess import PIPE, Popen
from tqdm import tqdm

from modules.ipscan import ipscan
from modules.search import getToolList, isTool
from modules.tools import Tools


enableList = []
exitToken = 0

def osSearch():
    pass


def toolSearch():
    # Tool presence
    global tools

    tool_list = Popen('cat ./require/tool_list.txt', shell=True, stdout=PIPE, stderr=PIPE)
    tools, toolsErr = tool_list.communicate()
    tools = tools.decode().split('\n')[:-1]

    os.system("clear")
    
    return getToolList(tools)


def menu(args):
    enableList = toolSearch()

    print("[Target IP] ==> {}".format(args.IP))
    print()
    print("Select Mode plz..")
    print(" {:>2}. {:<15} ".format("q", "Quit"))

    for num,tool in enumerate(enableList):
        if 'Not' in enableList[tool]:
            print(" {:>2}. {:<15} [{:<15}]".format(num+1, tool, enableList[tool]))
            continue
        print(" {:>2}. {:<15}".format(num+1, tool))

    print()
    n = input("Select >> ")
    return n

def executeTool(n, args):
    if n == '1':
        if (isTool("nmap")):
            os.system("clear")
            
            print("Select Scan Nmap..!")
            print(" 1. ALL ")
            print(" 2. TCP ")
            print(" 3. UDP ")
            print()
            n2 = input("R4mbb >> ")
            if n2 == '1':
                os.system("nmap -sV -T5 -p 1-65535 {}; sleep 2s".format(args.IP))
            elif n2 == '2':
                os.system("nmap -sTV -T5 {}".format(args.IP))
            elif n2 == '3':
                os.system("nmap -sUV -T5 {}".format(args.IP))
            else:
                return
    elif n == '2':
        if (isTool("nikto")):
            os.system("nikto -h {}".format(args.IP))
    elif n == '3':
        if (isTool("dirb")):
            os.system("clear")
            
            print(" 1. http ")
            print(" 2. https ")
            print()
            n2 = input("R4mbb >> ")
            if n2 == '1':
                os.system("dirb http://{}".format(args.IP))
            elif n2 == '2':
                os.system("dirb https://{}".format(args.IP))
            else:
                return
    elif n == '4':
        if (isTool("dirsearch")):
            os.system("dirsearch -u {}".format(args.IP))
    elif n == '5':
        if (isTool("msfconsole")):
            os.system("msfconsole".format(args.IP))
    elif n == '6':
        print("{}".format(ipscan(args.IP)))
        print(1)
        time.sleep(2)
             
    elif n == 'q':
        exitToken += 1
    else:
        return


def init():
    initial = Tools()
    initial.ip = args.IP


def main():
    parser = argparse.ArgumentParser(description='R4mbb\'s Poor Tool..!')
    parser.add_argument('-i', '--IP', required=True, help='Target IP input here..!')
    args = parser.parse_args()
    if args.IP == None:
        exitToken += 1
        return

    n = menu(args)
    executeTool(n, args)




if __name__ == '__main__':
    init()
    try:
        while True:
            main()
            if exitToken > 1:
                break
    except:
        pass

