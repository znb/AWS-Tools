#!/usr/bin/python
# Get a list of Guard Duty findings and their details for a specific detector
# Archive findings once we have sent out the Slack

try:
    import boto3
except Exception as err:
    print "[ERROR] " + str(err)
# Custom modules
import slack


def get_finding_details(credentials, slack_token, slackchannel, detector_id, finding_id):
    """Get the details on our finding"""
    gd = boto3.client('guardduty', region_name='eu-west-2', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    findings = gd.get_findings(DetectorId=detector_id, FindingIds=[finding_id])
    try:
        for k, v in enumerate(findings['Findings']):
            message = "(Sev: " + str(v['Severity']) + ") " + v['Resource']['ResourceType'] + " " + \
                v['Resource']['InstanceDetails']['InstanceId'] + \
                " -> " + str(v['Description'])
        return message
    except Exception as err:
        slack.notifyerror(slack_token, slackchannel)
        print "[ERROR] " + str(err)
        return False


def archive_finding(credentials, detector_id, finding_id):
    """Archive our finding after we have alerted on it"""
    print "Archiving finding: " + finding_id
    gd = boto3.client('guardduty', region_name='eu-west-2', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    archive = gd.archive_findings(DetectorId=detector_id, FindingIds=[finding_id])


def get_findings(slack_token, slackchannel, credentials, detector_id):
    """Get a list of members to our Guard Duty master account"""
    gd = boto3.client('guardduty', region_name='eu-west-2', aws_access_key_id=credentials['AccessKey'], aws_secret_access_key=credentials['Secret'])
    findings = gd.list_findings(DetectorId=detector_id, MaxResults=50)
    if len(findings['FindingIds']) == 0:
        message = "No GuardDuty Findings"
        slack.notification(slack_token, slackchannel, message)
    else:
        for k, v in enumerate(findings['FindingIds']):
            finding_id = v
            print "Sending notification"
            message = get_finding_details(credentials, slack_token, slackchannel, detector_id, finding_id)
            slack.notification(slack_token, slackchannel, message)
            print "Archiving finding"
            archive_finding(credentials, detector_id, finding_id)
