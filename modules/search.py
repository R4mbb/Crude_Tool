import os
import time
from subprocess import PIPE, Popen
import tqdm

class Search:
    def __init__(self, tools, os):
        self.tools = tools
        self.os = os
        self.enableList = []


    def getToolList(self):
        for i in tqdm(self.tools):
            if '[package]' in i:
                i = i.replace(' [package]', '')
            apt_list = Popen('dpkg -l {}'.format(i), shell=True, stdout=PIPE, stdErr=PIPE)
            found, foundErr = apt_list.communicate()
            time.sleep(0.1)

            if b'<none>' in found or b'no packages' in foundErr:
                self.enableList.append(0)
            else:
                self.enableList.append(1)

        os.system("clear")
        
        for num, tool in enumerate(tools):
            installed = ''
            if '[package]' in tool:
                tool = tool.replace(' [package]', '')

            if self.enableList[num]:
                installed = "Installed!!"
            else:
                installed = "Not Installed!!"

            print(" {0:<15} [{1}] ".format(tool, installed))
    
    def toolSearch(self):





    def osSearch(self):
        pass

