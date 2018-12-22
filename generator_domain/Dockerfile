FROM python:3.7.1-stretch

WORKDIR /generator_domain

COPY . /generator_domain

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "run.py"]