FROM mysql:latest

LABEL author="Alberto Franco"

COPY initialize_db.sql /docker-entrypoint-initdb.d