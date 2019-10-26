# Container image that runs your code
FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -qy python

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY extractReport.py /extractReport.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python","extractReport.py"]