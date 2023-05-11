FROM python:latest
MAINTAINER barmansuperman@gmail.com
COPY . /SimpleProject
WORKDIR /SimpleProject
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
RUN ["pytest", "-v"]
CMD tail -f /dev/null