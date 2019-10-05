#! /bin/bash

for i in `find . -name "TEST-*.xml" -type f`; do
    python extractReport.py "$i"
done