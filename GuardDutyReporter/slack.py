#!/usr/bin/python
# Send out notifications via Slack

from slackclient import SlackClient


def notifystatus(slack_token, slackchannel, status):
    """Notify the admin that we're starting the audit"""
    if status == "running":
        message = "Starting GuardDuty Report"
    elif status == "complete":
        message = "GuardGuty Reporting Complete"
    sc = SlackClient(slack_token)
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)


def notifyerror(slack_token, slackchannel):
    """"Send a notification that keys have been disabled"""
    sc = SlackClient(slack_token)
    message = "Something has gone wrong with the " + account + " AWS account. Please investigate"
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)


def notification(slack_token, slackchannel, message):
    """Send a notification to the AWS Admin"""
    sc = SlackClient(slack_token)
    sc.api_call("chat.postMessage", channel=slackchannel, as_user=True, text=message)
