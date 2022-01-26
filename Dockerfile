# parent image
FROM python:3.10-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get install nano

# pip command without proxy setting
RUN pip install --upgrade pip && pip install -r requirements.txt

# init the app
#ENTRYPOINT uvicorn --host 0.0.0.0 --port 8000 main:app --reload

CMD ["/bin/bash"]