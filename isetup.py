from __future__ import print_function
from fcoclient import (clients, api)
from resttypes import (cobjects, enums, endpoints)
from wrapper import *
import logging
from typed.builtins import (Dict, List)

logging.basicConfig(level=logging.DEBUG)


auth = {'api_uuid': '4d194318-778b-3059-85e6-5e4d33a03a9b',
        'password': 'api-test',
        'customer': 'e50bfd1b-253a-3290-85ff-95e218398b7e',
        'url': 'https://cp.diceproject.flexiant.net',
        'ca_cert': False}

a = api.REST(auth, logging)
fco_api = a
