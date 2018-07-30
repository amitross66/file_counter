import os
import sys
from filelister_function import *
##basedir = '/home/pi/'
##lister = dircheck(basedir)
currentpath = (os.getcwd())
if len(sys.argv) == 2:
    startpath = (sys.argv[1])
    if startpath.endswith('/') == False:
        startpath = (startpath+'/')
    allist = [startpath]
        
elif len(sys.argv) == 1:
    if currentpath.endswith('/') == False:
        allist = [currentpath+'/']
    else:
        allist = [currentpath]
    
else:
    print("Error! unacceptable ammount of parameters!")
print(allist)
totalfilecount = 0
totaldircount = 0


while (allist != []):
    base = allist.pop()
    try:
        lister, filecount, dircount, allcount = dircheck(base)
        allist = allist + lister
        totalfilecount = totalfilecount+filecount
        totaldircount = totaldircount+dircount
        
    
    except IOError as e:
        print(e.errno)
        print(e)
    except OSError as e:
        print(e.errno)
        print(e)
    
print ('Number of directories:', totaldircount)
print ('Number of files:', totalfilecount)    
print ('Number of all files:', totalfilecount+totaldircount)