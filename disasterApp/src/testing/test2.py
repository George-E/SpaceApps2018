import csv
import urllib2

url = 'ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV/2010-08/sr37522/Data-L2_1km_grid/C2H2.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row