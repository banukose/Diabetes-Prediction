FROM python:3.10-slim

WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]