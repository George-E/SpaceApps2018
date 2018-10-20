import query as q
import json

year = 2008
month = 3
day = 5

data = q.get_sample_chem_data_for_date(year, month, day)
print json.dumps(data, indent=2)