FROM python:3.13.1
LABEL authors="TheGreenMoray"
WORKDIR /app

ADD *.py .

CMD ["python","./testgo.py"]
