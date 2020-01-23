while true
do 
 echo "Starting FMCSA"
 python3 main.py --fmcsa
 python3 main.py --email_records 1 anhdy@acecic.com 
 sleep 86400
done
