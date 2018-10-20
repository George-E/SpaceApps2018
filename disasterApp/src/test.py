import urllib 

file =  urllib.urlretrieve('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV/2010-08/sr37522/Data-L2_1km_grid/C2H2.csv')
print file[1].content
print file[1].read()