#! /bin/bash
exit_code=0

for i in `find . -name "TEST-*.xml" -type f`; do
    python extractReport.py "$i"
    echo "python"
    echo $?
    if [ $? -ne 0 ]; then
        exit_code=1
        echo "check"
        echo $exit_code
    fi
done
echo "echo code final:"
echo $exit_code
exit $exit_code