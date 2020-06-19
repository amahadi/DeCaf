FROM python:3.6.10

MAINTAINER Alvi Mahadi "alvi.utsab@gmail.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "src/api.py" ]