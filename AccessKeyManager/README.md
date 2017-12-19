Access Key Manager
==================

Check a users access key. If they are older than 3 months, warn the user
via Slack. Delete after one warning


Scripts
-------


 * AccessKeyManager.py - Master script that gets our user list
 * configuration.py - Pulls configuration stuff from file
 * slack.py - Checks if the user is on Slack and sends a notification if true
 * checks.py - Performs checks on the AWS keys
 * keymanagement.py - Work with users access keys
