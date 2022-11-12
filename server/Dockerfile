# https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.10

WORKDIR /container-server

# https://github.com/ufoscout/docker-compose-wait
## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY * /container-server/

RUN /wait

CMD ["uvicorn", "main:app" , "--host", "0.0.0.0", "--reload"]
