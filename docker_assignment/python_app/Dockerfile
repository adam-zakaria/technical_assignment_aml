# ./python_app/Dockerfile
FROM python:3.9

RUN apt-get update && \
    apt-get install -y vim openssh-client iputils-ping && \
    pip install --no-cache-dir pymatgen

WORKDIR /usr/src/app

ENTRYPOINT ["python", "./main.py"]