import os


def dircheck(basedir):
    lister = []
    directory = os.listdir(basedir)
    filecount = 0
    dircount = 0
    allcount = 0
    for item in directory:
        fullpath = basedir+item
         #print (fullpath)
        if os.path.isdir(fullpath) == True:
            if os.path.islink(fullpath) == False:
                #print (fullpath, 'is a directory')
                lister.append(fullpath+'/')
                dircount = dircount+1
        elif os.path.isfile(fullpath) == True:
            #print (fullpath, 'is a file')
            filecount = filecount+1
        #else:
            #print (fullpath, 'File type error!')
            
    return lister, filecount, dircount, allcount
