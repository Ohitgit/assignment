FROM python:3.9-slim
WORKDIR / forex_crm
COPY requirements.txt  requirements.txt
RUN pip install -r requirements.txt
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV NAME  myworld
RUN pip3 install --upgrade pip
COPY . .
CMD [ "python", "manage.py", "runserver", "0.0.1:8000" ]


# RUN  export DEBIAN_FRONTEND=noninteractive
# ENV  DEBIAN_FRONTEND noninteractive
# RUN apt-get update && apt-get -y install vim
# RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
# RUN apt-get -y update && apt-get -y install nodejs
# RUN apt-get -y update && apt-get install -y build-essential
# COPY docker_files/req.txt req.txt
# RUN pip3 install --no-cache-dir -r req.txt
# RUN pip3 install --upgrade pip
