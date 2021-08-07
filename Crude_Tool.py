#!/usr/bin/python3

import os
import argparse

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

token = 0

def main():
    os.system("clear")
    print(disp)
    print("Select Mode plz..")
    print(" q. Quit ")
    print(" 1. Nmap ")
    print(" 2. Nikto ")
    print(" 3. Dirb ")
    print(" 4. Dirsearch ")
    print(" 5. Metasploit ")
    print()
    n = input("\u0332".join("R4m ") + ">> ")

    parser = argparse.ArgumentParser(description='R4mbb\'s Poor Tool..!')
    parser.add_argument('-i', '--IP', help='Target IP input here..!')
    args = parser.parse_args()

    if n == '1':
        os.system("clear")
        print(disp)
        print("Select Scan Nmap..!")
        print(" 1. ALL ")
        print(" 2. TCP ")
        print(" 3. UDP ")
        print()
        n2 = input("\u0332".join("R4m ") + ">> ")
        if n2 == '1':
            os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -A -p 1-65535 {};bash\"".format(args.IP))
        elif n2 == '2':
            os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -sT {};bash\"".format(args.IP))
        elif n2 == '3':
            os.system("gnome-terminal --tab -- /bin/bash -c \"nmap -sUV -T4 -F --version-intensity 0 {};bash\"".format(args.IP))
        else:
            return
    elif n == '2':
        os.system("gnome-terminal --tab -- /bin/bash -c \"nikto -h {};bash\"".format(args.IP))
    elif n == '3':
        os.system("gnome-terminal --tab -- /bin/bash -c \"dirb http://{};bash\"".format(args.IP))
    elif n == '4':
        os.system("gnome-terminal --tab -- /bin/bash -c \"dirsearch -u {};bash\"".format(args.IP))
    elif n == '5':
        os.system("gnome-terminal --tab -- /bin/bash -c \"msfconsole;bash\"")
    else:
        token += 1


if __name__ == '__main__':
    try:
        while True:
            main()
            if token > 0:
                break
    except:
        print()
        print("Bye~")

