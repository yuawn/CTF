import os , zipfile

name = ''
an = ''
ap = ''

for i in range(500):
    print i
    for file in os.listdir("./"):
        if file.endswith('.zip'):
            name = file

    pw = open('unZipkey').readline()[:-1]

    z = zipfile.ZipFile(name)
    uz = z.extractall(pwd = pw)
    an += name[:-4]
    ap += pw
    os.system('rm -rf '+name)

    print 'all_name ->' , an
    print 'all_pwd ->' , ap