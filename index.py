import phonenumbers as ph
from numbers_listFile import desire_number
from phonenumbers import carrier
from phonenumbers import geocoder
var=ph.parse(desire_number,'CH')
print(geocoder.description_for_number(var,'en'))
# print(geocoder._region_display_name(57000,'en'))
var1=ph.parse(desire_number, 'RO')
print(carrier.name_for_number(var1 , 'en'))