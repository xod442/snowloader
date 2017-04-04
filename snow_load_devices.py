'''
 Copyright 2016 Hewlett Packard Enterprise Development LP.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
__author__ = "@netmanchris"
__copyright__ = "Copyright 2016, Hewlett Packard Enterprise Development LP."
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Function; copies IMC devices into service now
04042017 - Initial release - RAK
'''

#GET SERVICE NOW
 #Need to install requests package for python
 #sudo easy_install requests
import requests
import json
from snowloader import *
from datetime import datetime
from pyhpeimc.auth import *
from pyhpeimc.plat.device import *
import time


# Set the request parameters
imc_user = "admin"
imc_passwd = "admin"
imc_host = "10.132.0.15"

snow_user = 'admin'
snow_passwd = 'Grape123!'
instance = "dev32384"
snow_url = 'https://'+instance+'.service-now.com/api/now/table/u_imcdevices'

# Configuring a connection to the VSD API

auth = IMCAuth("http://", imc_host, "8080", imc_user, imc_passwd)

dev_list = get_all_devs(auth.creds,auth.url,network_address=None)
c = 0

for i in dev_list:
    print "processing device %i: " % c
    snowObject = post_snow(dev_list[c], snow_url, snow_user, snow_passwd)
    print '.......'
    c = c + 1
    time.sleep(2)
