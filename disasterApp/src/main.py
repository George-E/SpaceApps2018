import query as q
import json

data = q.get_sample_chem_data_for_date(year=2008, month=3, day=5)
print json.dumps(data, indent=2)