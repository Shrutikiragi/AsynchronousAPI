FROM python:3.7.9

WORKDIR \AsynchronousAPI

COPY . .

RUN pip install -r requirement.txt

EXPOSE 5000

CMD python3 main1.py
