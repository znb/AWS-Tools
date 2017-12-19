#!/usr/bin/python
# Disables or deletes a users AWS access keys

import sys
import os
try:
    import boto3
except Exception as err:
    print "[ERROR] " + str(err)
import json
import datetime


def keyinfo(credentials, USERNAME):
    """Get our users from IAM"""
    iam = boto3.resource('iam', region_name='us-west-1', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    try:
        dateformat = '%Y-%m-%d'
        userdata = iam.User(USERNAME)
        for key in userdata.access_keys.all():
            # This is fairly dirty
            tmptoday = datetime.datetime.now()
            today = tmptoday.strftime(dateformat)
            key_created = key.create_date.strftime(dateformat)
            # Adjust here for your desired warning time
            tmpwarning = tmptoday - datetime.timedelta(days=89)
            warning = tmpwarning.strftime(dateformat)
            # Adjust here for your desired time - Key delete
            tmpninetyago = tmptoday - datetime.timedelta(days=90)
            ninetyago = tmpninetyago.strftime(dateformat)
            if key_created < warning:
                returned = key.id + ".WARN"
            elif key_created < ninetyago:
                returned = key.id + ".FAIL"
            else:
                returned = key.id + ".OK"
            return returned
    except Exception as err:
        print "[ERROR] " + str(err)


def disablekey(credentials, USERNAME, KEYID):
    """Get our users from IAM"""
    iam = boto3.resource('iam', region_name='us-west-1', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    try:
        print "Deactivating access key: " + KEYID,
        # accesskey = iam.AccessKey(USERNAME, KEYID)
        # resp = accesskey.deactivate()
        # status_code = resp['ResponseMetadata']['HTTPStatusCode']
        # if status_code == 200:
        #     print " OK"
        # else:
        #     print " FAIL"
    except Exception as err:
        print "[ERROR] " + str(err)


def deletekey(credentials, USERNAME, KEYID):
    """Get our users from IAM"""
    iam = boto3.resource('iam', region_name='us-west-1', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    try:
        print "Deleting access key: " + KEYID,
        # accesskey = iam.AccessKey(USERNAME, KEYID)
        # resp = accesskey.delete()
        # status_code = resp['ResponseMetadata']['HTTPStatusCode']
        # if status_code == 200:
        #     print " OK"
        # else:
        #     print " FAIL"
    except Exception as err:
        print "[ERROR] " + str(err)
