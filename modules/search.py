#!/usr/bin/python3

import os
import time
from subprocess import PIPE, Popen
from tqdm import tqdm


def getToolList(tools):
    enableList = {}

    for i in tqdm(tools):
        if '[package]' in i:
            i = i.replace(' [package]', '')
        apt_list = Popen('dpkg -l {}'.format(i), shell=True, stdout=PIPE, stderr=PIPE)
        found, foundErr = apt_list.communicate()
        time.sleep(0.1)

        if b'<none>' in found or b'no packages' in foundErr:
            enableList[i] = "Not Installed..!!"
        else:
            enableList[i] = "Installed!!!"

    os.system('clear')
    return enableList


def toolSearch():
    pass



def osSearch():
    pass

