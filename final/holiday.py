# holiday.py
import requests

def get_holiday():
    url = 'https://date.nager.at/api/v3/NextPublicHolidaysWorldwide'
    response = requests.get(url)
    holidays = response.json()
    return holidays  # This will be a list of holidays
