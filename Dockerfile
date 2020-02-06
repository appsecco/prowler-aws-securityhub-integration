FROM python:latest

# Declar Env Vars
ENV MY_DYANMODB_TABLE=MY_DYANMODB_TABLE
ENV AWS_REGION=AWS_REGION

# Install Dependencies
RUN \
    apt update && \
    apt upgrade -y && \
    pip install awscli && \
    apt install -y python3-pip jq

# Place scripts
ADD converter.py /root
ADD loader.py /root
ADD script.sh /root

# Installs prowler, moves scripts into prowler directory
RUN \
    git clone https://github.com/toniblyx/prowler && \
    mv root/converter.py /prowler && \
    mv root/loader.py /prowler && \
    mv root/script.sh /prowler

# Runs prowler, ETLs ouput with converter and loads DynamoDB with loader
WORKDIR /prowler
RUN pip3 install boto3
CMD bash script.sh
