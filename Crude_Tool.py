#!/usr/bin/python3

import os
import argparse
import time
from subprocess import PIPE, Popen

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

tool_list = ["nmap", "nikto", "dirb", "dirsearch", "msfconsole"]
exit_token = 0


def osSearch():
    pass


def toolSearch():
    # Tool presence
    pass


def menu():
    os.system("clear")
    print(disp)
    print("Select Mode plz..")
    print(" q. Quit ")
    for num, tool in enumerate(tool_list):
        print(" {}. {} ".format(num+1, tool))
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


def exploit(n, args):
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
                os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -A -p 1-65535 {};bash\"".format(args.IP))
            elif n2 == '2':
                os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -sT {};bash\"".format(args.IP))
            elif n2 == '3':
                os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -sUV -T4 -F --version-intensity 0 {};bash\"".format(args.IP))
            else:
                return
        else:
            notFoundTool("Nmap")
            return
    elif n == '2':
        if (isTool("nikto")):
            os.system("gnome-terminal --tab -- /bin/bash -c \"nikto -h {};bash\"".format(args.IP))
        else:
            notFoundTool("Nikto")
            return
    elif n == '3':
        if (isTool("dirb")):
            os.system("gnome-terminal --tab -- /bin/bash -c \"dirb http://{};bash\"".format(args.IP))
        else:
            notFoundTool("Dirb")
            return
    elif n == '4':
        if (isTool("dirsearch")):
            os.system("gnome-terminal --tab -- /bin/bash -c \"dirsearch -u {};bash\"".format(args.IP))
        else:
            notFoundTool("Dirsearch")
    elif n == '5':
        if (isTool("msfconsole")):
            os.system("gnome-terminal --tab -- /bin/bash -c \"msfconsole;bash\"")
        else:
            notFoundTool("Metasploit")
    elif n == 'q':
        exit_token += 1
    else:
        return


def main():
    n = menu()
    parser = argparse.ArgumentParser(description='R4mbb\'s Poor Tool..!')
    parser.add_argument('-i', '--IP', help='Target IP input here..!')
    args = parser.parse_args()

    exploit(n, args)




if __name__ == '__main__':
    try:
        while True:
            main()
            if exit_token > 0:
                break
    except:
        os.system("clear")
        print()
        print("Bye~")

