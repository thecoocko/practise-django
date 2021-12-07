from django.core.exceptions import ValidationError
import re


def validate_plate_numberLATIN(value):
    if re.search(r"^[A-Z]{2}\s\d{4}\s[A-Z]{2}$",value) == None:
        raise ValidationError("Validation Error", params={'value':value})
    
         
    

def validate_plate_numberCYRYLLIC(value):
    if re.search(r'^[A-Z]{2}\s\d{4}\s[A-Z]{2}$',value) == None:
        raise ValidationError("Validation Error", params={'value':value})
        