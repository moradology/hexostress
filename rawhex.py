#!/usr/bin/env python
"""
modified example script for the hexoskin's API v2.0
"""

__author__ = 'antoine'

import sys, HxApi2_0
from config import CONFIG
from os.path import expanduser

def main(rec_list, config):
    '''Here is a sample script to get started. Enter your info below, and the
    recordId you want to download.'''

    # Credentials are entered here, directly in the code, and a session
    # authentication token is created
    username = config["uname"]
    password = config["pass"]
    public_key = config["pubkey"]
    private_key = config["privkey"]
    auth = HxApi2_0.SessionInfo(publicKey=public_key, privateKey=private_key,\
            username=username, password=password, base_url='api')

    # Enter the ID of the required record in an array, and
    # HxApi.getRecord will try to download the data associated
    # with it. If it manages to do so, HxApi.saveTxt will save it in the
    # desired path with an adequate filename.
    try:
        if rec_list == []:
            print('a list of records')
        else:
            for rec in rec_list:
                print 'Downloading record %s'%rec
                data = HxApi2_0.getRecordData(auth, recordID=rec)
                HxApi2_0.saveTxt(data, expanduser('~')+\
                        '/Downloads/HexoskinData/')
    except:
        print "Problem loading record : " + str(rec_list)


if __name__ == "__main__":
    main(sys.argv[1:], CONFIG)
