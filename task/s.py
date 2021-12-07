import re
value = 'AA 2342 23'
print(re.search(r'^[A-Z]{2}\s\d{4}\s[A-Z]{2}$',value))