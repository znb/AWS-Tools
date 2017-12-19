#!/usr/bin/python
# Parse our configuration file for accounts and checks

import json
import sys


def parse_config(configfile, config):
    """Pull account information from our config file"""
    try:
        with open(configfile, 'r') as fh:
            jsondata = json.load(fh)
    except Exception as err:
        print err
        sys.exit("[ERROR] Unable to open config file")

    if config == "accounts":
        return jsondata['accounts']
    if config == "slackchannel":
        return jsondata['slack']['channel']['key']
    if config == "slackadmin":
        return jsondata['slack']['admin']['key']
    if config == "slacktoken":
        return jsondata['slack']['token']['key']
    if config == "service_accounts":
        return jsondata['service_accounts']
