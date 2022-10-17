FROM python:3.7
COPY ./api-scraper.py /app/api-scraper.py
COPY ./static /app/static
COPY ./templates /app/templates
RUN pip install --no-cache-dir urllib3
RUN pip install --no-cache-dir python-time
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir python-decouple
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir selenium
RUN pip install --no-cache-dir psycopg2
WORKDIR /app
CMD [ "python", "./api-scraper.py" ]
