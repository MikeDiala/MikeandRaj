import usaddress
import re

def parse_address(s):
    s = s.strip('\n')
    try:
        address = usaddress.tag(s)
        addr = address[0].get("AddressNumber") + " " + address[0].get("StreetNamePreDirectional", '') \
               + " " + address[0].get("StreetName", '') \
               + " " + address[0].get("StreetNamePostType", '') \
               + " " + address[0].get("OccupancyType", '') \
               + " " + address[0].get("OccupancyIdentifier", '')
        addr = re.sub(' +', ' ', addr)
        addr = addr.rstrip()

        city = address[0].get("PlaceName")
        state = address[0].get("StateName")
        zip = address[0].get('ZipCode')
    except:
        addr = s
        city = ''
        state = ''
        zip = ''

    return addr, city, state, zip