from datetime import date
from django.core.exceptions import ValidationError

START_DATE = date(2020, 1, 1)
    

def date_validator(form_date):
    """Validate that entered date is on or after Jan 1, 2020"""
    # form.to_python() has already converted the date field to a date object
    if form_date < START_DATE:
        raise ValidationError(f"Date must be on or after {START_DATE:%x}")
