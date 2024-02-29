FROM python:3.9-slim

WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


ENV DB_NAME=user_database
ENV DB_USER=postgres
ENV DB_PASSWORD=mysecretpassword
ENV DB_HOST=postgres
ENV DB_PORT=5432


CMD ["python", "app.py"]
