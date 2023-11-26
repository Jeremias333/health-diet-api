#Só uma base, não está implementado da forma que precisa ser

FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "start.py"]
