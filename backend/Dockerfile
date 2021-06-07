FROM ubuntu:20.04

RUN apt update && apt install python3.9 python3-pip -y && pip3 install pipenv
RUN apt install python3-dev libpq-dev -y
WORKDIR /app
COPY Pipfile* ./
RUN alias python=python3 && alias pip3=pip && python3 -m pipenv install
COPY . .
EXPOSE 5000
CMD ["python3", "-m", "pipenv", "run", "python3", "main.py"]
#CMD "pipenv run python3 main.py"
#CMD 'ls'