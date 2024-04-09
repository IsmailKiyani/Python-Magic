import phonenumbers
from phonenumbers import geocoder

a=input('Enter your Number: ')
phonenumber=phonenumbers.parse(a)

print(geocoder.description_for_number(phonenumber,'en'))