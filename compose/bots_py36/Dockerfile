FROM python:3.6-alpine
LABEL maintainer="janne.spijkervet@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./etc /requirements

RUN pip install --upgrade pip
RUN pip install -r /requirements/requirements.txt

COPY . /bots
WORKDIR /bots

RUN pip install /bots
RUN mkdir /usr/local/lib/python3.6/site-packages/bots/botssys
RUN mkdir /usr/local/lib/python3.6/site-packages/bots/botssys/sqlitedb
COPY ./src/bots/install/bots.ini /usr/local/lib/python3.6/site-packages/bots/config/
COPY ./src/bots/install/settings.py /usr/local/lib/python3.6/site-packages/bots/config/
COPY ./src/bots/install/botsdb /usr/local/lib/python3.6/site-packages/bots/botssys/sqlitedb/

# COPY ./compose/bots_py36/postinstall.py /bots
# RUN python /bots/postinstall.py

# Install supervisord
RUN pip install supervisor
# Copy Supervisord.conf file
COPY ./compose/bots_py36/supervisord.conf /etc/supervisor/supervisord.conf

# Add Crontab file
COPY ./compose/bots_complete/crontab /usr/local/lib/python2.7/dist-packages/bots/config/

CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

EXPOSE 8080
