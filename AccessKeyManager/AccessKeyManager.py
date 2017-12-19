#!/usr/bin/python
# Script to audit AWS users access keys and report status to Slack

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
    parser = argparse.ArgumentParser(description='Amazon Access Key Audit Script of Doom')
    parser.add_argument('--configuration-file', '-c', dest='configfile', default='configuration.json', help='Configuration file')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()
    configfile = args.configfile

    print "\nAmazon AWS Access Key Audit Script of Doom"
    if not args.configfile:
        sys.exit(parser.print_help())
    else:
        slackchannel = configuration.parse_config(configfile, config="slackchannel")
        slack_token = configuration.parse_config(configfile, config="slacktoken")
        slack.notifystatus(slack_token, slackchannel, status="running")
        slackers = slack.get_slackers(slack_token)
        credentials = configuration.parse_config(configfile, config="accounts")
        service_accounts = configuration.parse_config(configfile, config="service_accounts")

        for account, credentials in credentials.iteritems():
            print "\n[ACCOUNT] " + account
            checks.get_users(slack_token, slackers, slackchannel, service_accounts, account, credentials)
        print "[DONE]"
        slack.notifystatus(slack_token, slackchannel, status="complete")


if __name__ == '__main__':
    __main__()
