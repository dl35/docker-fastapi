FROM ubuntu:20.04





WORKDIR /code

COPY ./app /code/app

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt-get update && apt-get install -y python3.8  python3.8-dev python3-pip python3-venv

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential 




ENV CONTAINER_NAME="fastapi"

ADD ./docker/prompt.sh /root/.bash_aliases

COPY ./docker/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN . $VIRTUAL_ENV/bin/activate

COPY ./docker/run.sh /code/run.sh
RUN chmod +x /code/run.sh


CMD ["bash"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]