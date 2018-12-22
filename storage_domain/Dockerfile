FROM bkulenko/memegen:python-postgres-base

WORKDIR /storage_domain

COPY . /storage_domain

EXPOSE 8000
EXPOSE 5432

RUN service postgresql restart

CMD ["python", "run.py"]
