#!/usr/bin/python3

import os
import argparse
import time
from subprocess import PIPE, Popen
from tqdm import tqdm

from modules.ipscan import ipscan
from modules.search import getToolList


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


def isTool(command):
    isCommand = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    isCommandOut, isCommandErr = isCommand.communicate()

    if isCommandOut:
        return True
    else:
        return False


def notFoundTool(command):
    os.system("clear")
    
    print("{} is not found..".format(command))
    time.sleep(2)
    return


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
                os.system("gnome-terminal -- sh -c \"nmap -A -p 1-65535 {}; exec sh\"".format(args.IP))
            elif n2 == '2':
                os.system("gnome-terminal -- sh -c \"nmap -sT {}; exec sh\"".format(args.IP))
            elif n2 == '3':
                os.system("gnome-terminal -- sh -c \"nmap -sUV -T4 -F --version-intensity 0 {}; exec sh\"".format(args.IP))
            else:
                return
        else:
            notFoundTool("Nmap")
            return
    elif n == '2':
        if (isTool("nikto")):
            os.system("gnome-terminal -- sh -c \"nikto -h {}; exec sh\"".format(args.IP))
        else:
            notFoundTool("Nikto")
            return
    elif n == '3':
        if (isTool("dirb")):
            os.system("clear")
            
            print(" 1. http ")
            print(" 2. https ")
            print()
            n2 = input("R4mbb >> ")
            if n2 == '1':
                os.system("gnome-terminal -- sh -c \"dirb http://{}; exec sh\"".format(args.IP))
            elif n2 == '2':
                os.system("gnome-terminal -- sh -c \"dirb https://{}; exec sh\"".format(args.IP))
            else:
                return
        else:
            notFoundTool("Dirb")
            return
    elif n == '4':
        if (isTool("dirsearch")):
            os.system("gnome-terminal -- sh -c \"dirsearch -u {}; exec sh\"".format(args.IP))
        else:
            notFoundTool("Dirsearch")
    elif n == '5':
        if (isTool("msfconsole")):
            os.system("gnome-terminal -- sh -c \"msfconsole; exec sh\"".format(args.IP))
        else:
            notFoundTool("Metasploit")
    elif n == '6':
        print("{}".format(ipscan(args.IP)))
        print(1)
        time.sleep(2)
             
    elif n == 'q':
        exitToken += 1
    else:
        return


def init():
    pass
#   osSearch()


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
    try:
        while True:
            main()
            if exitToken > 1:
                break
    except:
        pass

