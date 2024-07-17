#!/usr/bin/python3

import os
import argparse
import time
from subprocess import PIPE, Popen
from tqdm import tqdm

disp = '''

   Made by                                                                                                    
                                                                                                    
                                                              ```             ````                  
      .yhhhhhhys+-           .yhh:                           `dNNo            sNNd                  
      :NMMdhhhmMMNy`        -dMMM+                           .mMMs            yMMm                  
      :NMM:  `.sMMM/       :mMMMM+                           .mMMs            yMMm                  
      :NMM-    oMMM:     `+NN+dMM+    oddy./yddh+.`/yddhs-   .mMMs-ohddho-    yMMm.+yddhs:`         
      :NMMo//+yNMm+`    .yNd:`hMM+    yMMNdhyhNMMdddyymMMm-  .mMMmdhyydMMN+   yMMNdhyyhNMNy`        
      :NMMNNNMMm+.    `/mNh. `hMM+    yMMN:  `oMMMy`  -NMMs  .mMMd-   `sMMN-  yMMN:`  `/NMM+        
      :NMM/.-sNMm+   `sMMh+///mMMy/-  yMMd`   :NMM:    mMMy  .mMMo     :MMM:  yMMd     `mMMs        
      :NMM-   +NMMs` `dNNNNNNNMMMNNy  yMMd`   :NMM:    mMMy  .mMMy`   `oMMm-  yMMm`    /NMM/        
      :NMM-    :mMMh. .......-dMMo..  yMMd`   :NMM:    mMMy  .mMMNh+/+yMMN+   yMMMdo//sNMMy`        
      -mNN-     -dNNh.       `hNN+    sNNh`   :mNN:    dNNs  `dNNysmNNNmy-    yNNdodNNNmh/`         
      `...`      `...`        ...`    ....    `...`    ....   ...` `...`      ....  ...`            
                                                                                                    
                                                                                                    
    
'''

enableList = []
exitToken = 0

def osSearch():
    pass


def toolSearch():
    # Tool presence
    global tools

    tool_list = Popen('cat ./tool_list.txt', shell=True, stdout=PIPE, stderr=PIPE)
    tools, toolsErr = tool_list.communicate()
    tools = tools.decode().split('\n')[:-1]


    os.system("clear")
    print(disp)
    print("[**] Installed require tool/package searching... [**]")
    print()

    for i in tqdm(tools):
        if '[package]' in i:
            i = i.replace(' [package]', '')
        apt_list = Popen('dpkg -l {}'.format(i), shell=True, stdout=PIPE, stderr=PIPE)
        found, foundErr = apt_list.communicate()
        time.sleep(0.05)

        if b'<none>' in found or b'no packages' in foundErr:
            enableList.append(0)
        else:
            enableList.append(1)

    os.system("clear")
    print(disp)
    print('-'*35)
    print()
    print("[**] Installed require tool/package search [**]")
    print()
    print('-'*35)
    print()

    for num, tool in enumerate(tools):
        installed = ''
        if '[package]' in tool:
            tool = tool.replace(' [package]', '')

        if enableList[num]:
            installed = 'Installed!!'
        else:
            installed = 'Not Installed!!'
        print(" {0:<15} [{1}] ".format(tool, installed))

    print()
    print("Enter to Restart Search!!")
    print()
    print('-'*35)
    print()


def menu(args):
    init()
    print("[Target IP] ==> {}".format(args.IP))
    print()
    print("Select Mode plz..")
    print(" q. Quit ")

    num = 0
    for tool in tools:
        if '[package]' in tool:
            continue
        num += 1
        print(" {}. {}".format(num, tool))

    print()
    n = input("R4mbb >> ")
    return n


def isTool(command):
    isCommand = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    isCommandOut, isCommandErr = isCommand.communicate()

    if (isCommandOut):
        return True
    else:
        return False


def notFoundTool(command):
    os.system("clear")
    print(disp)
    print("{} is not found..".format(command))
    time.sleep(2)
    return


def executeTool(n, args):
    if n == '1':
        if (isTool("nmap")):
            os.system("clear")
            print(disp)
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
            print(disp)
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
    elif n == 'q':
        exitToken += 1
    else:
        return


def init():
    toolSearch()
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
    """
    except:
        os.system("clear")
        print()
        print("Bye~")
    """
