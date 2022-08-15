FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --default-timeout=120 --no-cache-dir -r requirements.txt

COPY ./ ./

CMD ["python3", "main.py"]