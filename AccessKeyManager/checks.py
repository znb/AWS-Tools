# Gets information on an AWS IAM Access keys

try:
    import boto3
except Exception as err:
    print "[ERROR] " + str(err)
# Custom modules
import slack
import keymanagement


def get_service_account_owner(service_accounts, user):
    """Check who owns a service account"""
    owner = "None"
    for k, v in service_accounts.iteritems():
        if user in k:
            owner = v
            break
        else:
            pass

    return owner


def get_users(slack_token, slackers, slackchannel, service_accounts, account, credentials):
    """Get our users from IAM"""
    iam = boto3.client('iam', region_name='us-west-1', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    response = iam.get_paginator('list_users')
    try:
        for item in response.paginate():
            awsdata = item
    except Exception as err:
        slack.notifyerror(slack_token, account, slackchannel)
        print "[ERROR] " + str(err)
        return False

    for k, v in enumerate(awsdata['Users']):
        iamuser = v['UserName']
        print iamuser + " - ",
        keycheck = keymanagement.keyinfo(credentials, iamuser)
        if keycheck is None:
            print "No Access Keys attached to account"
        else:
            keyid = keycheck.split(".")[0]
            if keycheck.split(".")[1] == "OK":
                print "OK"
            elif keycheck.split(".")[1] == "WARN":
                print "WARNING - ",
                slack_id = slack.slack_lookup(slackers, iamuser)
                status = "Warning"
                if slack_id == "None":
                    print " No Slack ID",
                    owner = get_service_account_owner(service_accounts, iamuser)
                    print " - Service account owner: " + owner
                    slack_id = slack.slack_lookup(slackers, owner)
                    slack.notifyadmin(slack_token, account, owner, keyid, status, slackchannel, iamuser)
                    slack.notifyuser(slack_token, account, keyid, status, slack_id, iamuser)
                else:
                    print " - Sending Slack notification"
                    owner = "None"
                    slack.notifyadmin(slack_token, account, owner, keyid, status, slackchannel, iamuser)
                    slack.notifyuser(slack_token, account, keyid, status, slack_id, iamuser)
            elif keycheck.split(".")[1] == "FAIL":
                print "FAILURE - ",
                slack_id = slack.slack_lookup(slackers, iamuser)
                status = "Fail"
                if slack_id == "None":
                    print " No Slack ID",
                    owner = get_service_account_owner(service_accounts, iamuser)
                    print " - Service account owner: " + owner
                    slack_id = slack.slack_lookup(slackers, owner)
                    slack.notifyadmin(slack_token, account, owner, keyid, status, slackchannel, iamuser)
                    slack.notifyuser(slack_token, account, keyid, status, slack_id, iamuser)
                else:
                    print " - Sending Slack notification"
                    owner = "None"
                    slack.notifyadmin(slack_token, account, owner, keyid, status, slackchannel, iamuser)
                    slack.notifyuser(slack_token, account, keyid, status, slack_id, iamuser)
