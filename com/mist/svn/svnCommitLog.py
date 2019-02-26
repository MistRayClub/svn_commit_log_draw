# -*- coding: GBK -*-
import os


def getSvnLog(command):

    # logs = os.system('G: && cd gjyWorkSpace/SMFdev/SMF && svn log --search ' + name + ' >c:/temp.txt')
    # log = open("c:/temp.txt")
    # lines = log.readlines()
    log = os.popen(command)
    numer = 1
    unit = 1
    lines = log.readlines()
    list = []
    for line in lines:
        if len(list) > 8:
            return  list
        if numer % 4 == 0:
            # print("{}".format(numer) + line)
            list.append(line)
        if (line.startswith("Merged")):
            continue
        numer = numer + unit



