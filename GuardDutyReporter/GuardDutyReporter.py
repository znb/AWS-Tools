#!/usr/bin/python
# Script to grab the latest findings for GuardDuty and report to Slack

import sys
import argparse
try:
    import boto3
except Exception as err:
    print "[ERROR] " + str(err)
# Custom modules
import configuration
import slack
import checks


def __main__():
    """Get this party started"""
    parser = argparse.ArgumentParser(description='Amazon GuardDuty Report Script of Doom')
    parser.add_argument('--configuration-file', '-c', dest='configfile', default='configuration.json', help='Configuration file')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()
    configfile = args.configfile

    print "\nAmazon AWS GuardDuty Report Script of Doom"
    if not args.configfile:
        sys.exit(parser.print_help())
    else:
        slackchannel = configuration.parse_config(configfile, config="slackchannel")
        slack_token = configuration.parse_config(configfile, config="slacktoken")
        credentials = configuration.parse_config(configfile, config="accounts")
        detector_id = configuration.parse_config(configfile, config="detector_id")

        for account, credentials in credentials.iteritems():
            print "\n[ACCOUNT] " + account
            checks.get_findings(slack_token, slackchannel, credentials, detector_id)
        print "[DONE]"


if __name__ == '__main__':
    __main__()
