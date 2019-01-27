FROM ubuntu:18.04

WORKDIR /storage_domain

COPY . /storage_domain

EXPOSE 8000

RUN apt-get update -y
RUN apt-get install postgresql -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install -r requirements.txt


CMD ["docker-entrypoint.sh"]

CMD ["python", "run.py"]
