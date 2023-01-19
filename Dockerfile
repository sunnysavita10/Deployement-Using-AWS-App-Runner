FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8082
ENTRYPOINT [ "python3", "main.py" ]
