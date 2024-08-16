#!/usr/bin/python3

import os
import time
from subprocess import PIPE, Popen
from tqdm import tqdm


def getToolList(tools):
    enableList = {}

    for i in tqdm(tools):
        tmp = 0
        if '[package]' in i:
            i = i.replace(' [package]', '')
            tmp += 1
        apt_list = Popen('dpkg -l {}'.format(i), shell=True, stdout=PIPE, stderr=PIPE)
        found, foundErr = apt_list.communicate()
        time.sleep(0.1)

        if b'<none>' in found or b'no packages' in foundErr:
            if tmp:
                enableList[i] = "This package is Not Installed!!!"
                continue
            enableList[i] = "This tool is Not Installed..!!"
        else:
            if tmp:
                continue
            enableList[i] = "Installed!!!"

    os.system('clear')
    return enableList


def isTool(command):
    isCommand = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    isCommandout, _ = isCommand.communicate()

    if isCommandout:
        return True
    else:
        os.system("clear")
        print("{} is not found...".format(command))
        time.sleep(2)
        return


def osSearch():
    pass

def osSearch():
    pass

