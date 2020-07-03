FROM python:3.8.3-alpine

WORKDIR /usr/src/app


RUN pip install --upgrade pip
COPY ./requrements.txt .
RUN pip install -r requrements.txt

RUN echo Hello
COPY ./entrypoint.sh .
COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]