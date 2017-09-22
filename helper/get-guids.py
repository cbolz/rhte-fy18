#!/usr/bin/python2
#
# # Copyright (C) 2016, Christian Jung
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# get the list of GUID's used in Ravello


import sys
import getopt
import getpass
import os
import requests

def usage():
    """ print usage information
    """
    print "Usage:"
    print "-u username"
    print "-p password"

try:
    opts, args = getopt.getopt(sys.argv[1:], "u:p:")
except getopt.GetoptError as err:
    # print help information and exit:
    print str("Unknon option")  # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

username = None
password = None

for o, a in opts:
    if o == "-u":
        username = a
    elif o == "-p":
        password  = a
    else:
        print "unhandled option"
        usage()
        sys.exit(2)

if username == None:
    username = raw_input("Enter Ravello Username: ")

if password == None:
    password = getpass.getpass("Enter Password: ")

# retrieve Authentication Token
session=requests.Session()
headers={ 'Content-Type': 'application/json', 'Accept': 'application/json'}
token=session.get('https://rhpds.redhat.com/api/auth', auth=(username, password))
content = token.json()
authtoken = content['auth_token']
headers={ 'X-Auth-Token': authtoken}

# query list of services
services=session.get('https://rhpds.redhat.com/api/services/', headers = headers)
servicelist = services.json()
resources = servicelist['resources']
for resource in resources: 
    # for each service, print out the name
    href = resource['href']
    myservice = session.get(href, auth=(username, password))
    name=myservice.json()['name']
    print name