FROM python:3.12-bookworm

WORKDIR /app

COPY README.md /app/
COPY pyproject.toml /app/
COPY .env /app/
COPY vanilla_steel/ /app/vanilla_steel/

RUN apt update
RUN apt install cmake -y
RUN apt install openjdk-17-jdk graphviz -y
RUN apt clean

RUN pip3 install poetry
RUN cd /app
RUN poetry install
RUN poetry run python -m vanilla_steel --docs --build
