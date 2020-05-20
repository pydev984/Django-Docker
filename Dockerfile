FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/test_project
WORKDIR /home/test_project
COPY requirements.txt /home/test_project
RUN pip install -r requirements.txt
COPY test_project /home/test_projects