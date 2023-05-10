FROM debian

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY * /home
# RUN cd /home && pip install -r re.txt && python manage.py migrate

