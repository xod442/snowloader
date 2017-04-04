#!/usr/bin/env python
'''
  2017 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__copyright__ = "2017, wookieware.."
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Functions to interact with Sevice Now and snowBridge local database
03212017 Initial release.


'''

import time
import json
import requests
from datetime import datetime
from pyhpeimc.auth import *
from pyhpeimc.plat.alarms import *

#
# Get record by number from snow

def get_snow(snow_url, snow_user, snow_passwd):
    """
    function takes the IMC-XXXX incident number and gets record from Snow
    :param snow_url: The URL for the Service Now instance with a single record number
    :param snow_user: Username for the Service Now instance
    :param snow_pass: Password for the Service Now instance
    :return:dictionary fields from Service Now
    :rtype: dict
    >>> from snowbridge import *
    >>> snowObject = get_snow(https://'devXXXXX.service-now.com/api/now/table/incident?IMC0000-31','admin','admin')
    >>> assert snowObject['number'] in snowObject
    """
    # Set proper headers
    headers = {"Accept":"application/json"}

    # Do the HTTP request
    response = requests.get(snow_url, auth=(snow_user, snow_passwd), headers=headers )

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print response.status_code
    # Decode the JSON response into a dictionary and use the data
    data = json.loads(response.text)
    return data



def post_snow(device, snow_url, snow_user, snow_passwd):
    """
    function takes alarm which is a python list and builds record for new snow incident
    :param device: a python dict
    :param snow_url: A URL for the service now table
    :param snow_user: A str for the Service Now instance
    :param snow_passwd: A str for the Service Now instance
    :return: response.status_code for Service Now
    :rtype: int or string value of the return code
    >>> from snowbridge import *
    >>> snowObject = post_snow({device},'https://'devXXXXX.service-now.com/api/now/table/incident','admin','admin')
    >>> assert response.status_code == 201
    """
    data = {}           # A dictionary to build post information
    varz = []           # A list for errors

    # Build dictionary for Service Now incedent report
    data['u_imc_id'] = device['id'].encode('utf-8')
    data['u_label'] = device['label'].encode('utf-8')
    data['u_ip'] = device['ip'].encode('utf-8')
    data['u_mask'] = device['mask'].encode('utf-8')
    data['u_contact'] = device['contact'].encode('utf-8')
    data['u_location'] = device['location'].encode('utf-8')
    data['u_sysoid'] = device['sysOid'].encode('utf-8')
    data['u_typename'] = device['typeName'].encode('utf-8')
    # Convert dict to a string for post
    data = str(data)

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP POST to Snow
    response = requests.post(snow_url, auth=(snow_user, snow_passwd), headers=headers ,data=data)
    if response.status_code != 201:
        #print "This is the response code for snow %s for device %s" % (response.status_code, data['ip'])
        print response.status_code
    return data
