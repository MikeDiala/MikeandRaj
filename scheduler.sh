#!/bin/bash
echo "Starting FMCSA"
cd /home/ubuntu/TruckAutomation && /usr/bin/python3 /home/ubuntu/TruckAutomation/main.py --fmcsa
echo "emailing records"
/usr/bin/python3 /home/ubuntu/TruckAutomation/main.py --email_records 1 anhdy@acecic.com
