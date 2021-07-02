import phonenumbers
num=input()

from phonenumbers import geocoder
ch_num=phonenumbers.parse(num, "CH")
print(geocoder.description_for_number(ch_num, "en")) #To print the lopcation or simply the country name of the phone_number

from phonenumbers import carrier
service_name=phonenumbers.parse(num,"RO")
print(carrier.name_for_number(service_name,"en"))  #To print the service provider name for ex: Airtel,Reliance Jio,...

