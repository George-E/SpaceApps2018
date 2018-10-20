import ftplib
import urllib2
import csv

URL_ROOT = 'ftp.asc-csa.gc.ca'
COMMON_DIR = 'users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV'

def get_sample_chem_data_for_date(year, month, day):
    ftp = _get_new_root_ftp()

    year_month = str(year) + '-' + str(month).zfill(2)
    year_month_day = year_month + '-' + str(day).zfill(2)

    try:
        ftp.cwd(year_month)  
    except:
        print 'Data not found for ' + year_month
        return {}

    ss_dirs = ftp.nlst()
    for ss_dir in ss_dirs:
        meta_data_url = _get_full_url(ftp, ss_dir + '/' + ss_dir + '_InfoMetadata%20.txt')
        meta_data_file = urllib2.urlopen(meta_data_url).read()

        if ('date = ') not in meta_data_file:
            continue

        ftp.cwd(ss_dir + '/Data-L2_1km_grid')

        response_dict = {}

        chem_files = ftp.nlst()
        for chem_file_name in chem_files:
            if '_err' in chem_file_name:
                continue;

            chem_formula = chem_file_name.split(".")[0]

            url = _get_full_url(ftp, chem_file_name)
            chem_file = urllib2.urlopen(url)
            chem_file_reader = csv.reader(chem_file)

            sum = 0
            count = 0
            for row_list in chem_file_reader:
                val = float(row_list[0])
                if (val == -999 or val == -888):
                    continue
                sum += val
                count += 1

            if count != 0 :
                average = sum/count
                response_dict[chem_formula] = average

            chem_file.close()

        return response_dict

    print 'Data not found for ' + year_month_day
    return {}

def _get_new_root_ftp():
    ftp = ftplib.FTP(URL_ROOT)
    ftp.login()  
    ftp.cwd(COMMON_DIR)  
    return ftp

def _get_full_url(ftp, file_name):
    return 'ftp://' + URL_ROOT + ftp.pwd() + '/' + file_name
