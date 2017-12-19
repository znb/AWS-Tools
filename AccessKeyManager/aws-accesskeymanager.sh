#!/bin/bash
# Wrapper script for AccessKeyManager to be run from cron

SCRIPT="/home/user/AccessKeyManager/AccessKeyManager.py"
LOGFILE="/var/log/aws-accesskeymanager.log"
WORKDIR="/home/user/AccessKeyManager/"

# Run our script
echo -n "Running script..."
cd ${WORKDIR}
python ${SCRIPT} > ${LOGFILE}
echo " Done"
