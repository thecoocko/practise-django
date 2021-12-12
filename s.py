import re

t = 'http://127.0.0.1:8000/vehicles/set_driver/1/'
driver_id_from_request = re.search(r'\/\d\/',t)
print(t)
print(int(driver_id_from_request.group(0).split('/')[1]))