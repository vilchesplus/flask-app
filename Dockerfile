FROM python:3.7
COPY ./api.py /app/api.py
COPY ./static /app/static
COPY ./templates /app/templates
RUN pip install --no-cache-dir urllib3
RUN pip install --no-cache-dir python-time
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir python-decouple
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir gunicorn

WORKDIR /app
CMD [ "python", "./api.py" ]
