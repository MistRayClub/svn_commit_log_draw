# -*- coding: GBK -*-
import os
name='test'
logs=os.system('G: && cd gjyWorkSpace/SMFdev/SMF && svn log --search '+name+' >c:/temp.txt')

log=open("c:/temp.txt")
lines=log.readlines()
numer=1
unit=1
for line in lines:
    if numer%4==0:
         print("".format(numer)+line)
    if(line.startswith("Merged")):
        continue
    numer = numer + unit