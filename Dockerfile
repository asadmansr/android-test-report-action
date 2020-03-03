FROM ubuntu:18.04

RUN apt-get update && apt-get install -qy python

COPY entrypoint.sh /entrypoint.sh
COPY extractReport.py /extractReport.py

ENTRYPOINT ["/entrypoint.sh"]