FROM registry.gitlab.com/thelabnyc/python:py311

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN poetry install

RUN mkdir /tox
ENV TOX_WORK_DIR='/tox'
