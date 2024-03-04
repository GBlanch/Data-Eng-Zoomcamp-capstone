FROM python:3.13.0a2-slim

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python" , "ingest_data.py"  ]


# FROM python:3.13.0a2-slim

# FROM python:3.9.1 