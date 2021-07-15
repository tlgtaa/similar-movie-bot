FROM python:3.8-slim

RUN apt-get update && apt-get install -y gcc git gettext && apt clean && rm -rf /var/cache/apt/*
RUN pip install --upgrade pip

COPY requirements/ /tmp/requirements

#================================================
# PIP packages
#================================================
RUN pip install --no-cache-dir -r /tmp/requirements/prod.txt


#================================================
# Migrations tool
#================================================
ADD https://github.com/amacneil/dbmate/releases/download/v1.6.0/dbmate-linux-musl-amd64 /usr/local/bin/dbmate
RUN chmod +x /usr/local/bin/dbmate

#================================================
# Cleanup
#================================================
RUN pip uninstall -y uvloop

#================================================
# Code
#================================================
RUN useradd -m -d /proj -s /bin/bash app
COPY . /proj
WORKDIR /proj
RUN chown -R app:app /proj/*
RUN chmod +x /proj/bin/*
ENV PATH "$PATH:/proj/bin"
USER app
