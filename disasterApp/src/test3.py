import ftplib
import urllib2
import csv

#Open ftp connection
ftp = ftplib.FTP('ftp.asc-csa.gc.ca')
ftp.login()    
ftp.cwd('users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV/2010-08')  

#List the files in the current directory
ssDirs = ftp.nlst()

for ssDir in ssDirs:
    print ssDir
    ftp.cwd(ssDir)
    ftp.cwd('Data-L2_1km_grid')

    chemCSVfiles = ftp.nlst()
    for chemCSVfileName in chemCSVfiles:

        url = 'ftp://ftp.asc-csa.gc.ca' + ftp.pwd() + '/' + chemCSVfileName
        print url
        chemCSVfile = urllib2.urlopen(url)
        fileReader = csv.reader(chemCSVfile)

        for row in fileReader:
            print row

        chemCSVfile.close()

    ftp.cwd('../..')
