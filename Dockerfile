FROM python:3.6-slim
MAINTAINER barmansuperman@gmail.com
COPY . /SimpleProject
WORKDIR /SimpleProject
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v"]
CMD tail -f /dev/null