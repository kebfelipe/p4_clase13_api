FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install debugpy

COPY ./app /app

EXPOSE 5000 5678

CMD ["python3", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "app.py"]