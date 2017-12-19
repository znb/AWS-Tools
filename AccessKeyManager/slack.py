#!/usr/bin/python
# Check if a user is on Slack and sends a notification


import os
import json
from slackclient import SlackClient
import sys


def get_slackers(slack_token):
    """Get a list of Slack users"""
    sc = SlackClient(slack_token)

    slack_users = []
    data = sc.api_call("users.list")

    # TODO: Make this less hacky
    for k, v in enumerate(data['members']):
        slack_id = v['id']
        try:
            slack_email = v['profile']['email']
            domain = slack_email.split("@")[1]
            if "example.com" in domain:
                slackdata = slack_id + "," + slack_email
                slack_users.append(slackdata)
            else:
                pass
        except Exception as err:
            slack_email = "nope@nope.nope"

    return slack_users


def slack_lookup(slackers, user):
    """Get our Slack ID for the user"""
    slack_id = "None"
    for slacker in slackers:
        if user in slacker:
            slack_id = slacker.split(",")[0]
            break
        else:
            pass

    return slack_id


def notifystatus(slack_token, slackchannel, status):
    """Notify the admin that we're starting the audit"""
    if status == "running":
        message = "Starting Access Key Audit"
    elif status == "complete":
        message = "Access Key Audit Complete"
    sc = SlackClient(slack_token)
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)


def notifyuser(slack_token, account, keyid, status, slack_id, iamuser):
    """"Send a notification that keys have been disabled"""
    sc = SlackClient(slack_token)
    message = "Expired AWS access key " + keyid + "/" + account + "/" + iamuser + ". Please rotate out today."
    sc.api_call("chat.postMessage", channel=slack_id, as_user=True, text=message)


def notifyerror(slack_token, account, slackchannel):
    """"Send a notification that keys have been disabled"""
    sc = SlackClient(slack_token)
    message = "Something has gone wrong with the " + account + " AWS account. Please investigate"
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)


def notifyadmin(slack_token, account, owner, keyid, status, slackchannel, iamuser):
    """Send a notification to the AWS Admin"""
    if status == "Warning":
        if owner == "None":
            message = "Expired Access Key: " + keyid + "/" + account + "/" + iamuser + " -> Rotate tomorrow"
        else:
            message = "Expired Access Key: " + keyid + "/" + account + "/" + iamuser + " Owner: " + owner + " -> Rotate tomorrow"
    elif status == "Fail":
        if owner == "None":
            message = "Expired Access Key: " + keyid + "/" + account + "/" + iamuser + " -> Rotate today"
        else:
            message = "Expired Access Key: " + keyid + "/" + account + " Owner: " + owner + " -> Rotate today."

    sc = SlackClient(slack_token)
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)
