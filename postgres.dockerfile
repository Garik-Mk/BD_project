FROM postgres:latest

LABEL author="V1king"
LABEL description="Zoo postgres database image."
LABEL version="1.0"

COPY *.sql /docker-entrypoint-initdb.d/

