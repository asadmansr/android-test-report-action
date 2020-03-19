#! /bin/bash

status_code=0
log_file='extractReport_status.log'
status_message='Android Test Report Action executed successfully.'

echo ''
echo '------------------------------------------------'
echo '---        Android Test Report Action        ---'
echo '------------------------------------------------'
echo ''
echo ''

touch $log_file

for i in `find . -name "TEST-*.xml" -type f`; do
    python /usr/bin/extractReport.py "$i"
    echo ''
done

if grep -q 'error' "$log_file"; then
  status_code=1
  status_message='There were failing tests. Android Test Report Action failed the job.'
fi

rm $log_file

echo $status_message
echo ''
exit $status_code
