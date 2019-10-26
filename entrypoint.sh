#! /bin/bash
exit_code=0
for i in `find . -name "TEST-*.xml" -type f`; do
    python extractReport.py "$i"
    echo $?
    #result=$(cat android_test_report_action.txt)
    #if [ $result -ne 0 ]; then
    #    exit_code=$result
    #fi
done
exit 1