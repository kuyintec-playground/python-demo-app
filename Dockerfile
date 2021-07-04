FROM python:3.9.1
COPY . /app
WORKDIR /app
RUN pip install  --no-cache-dir  -r requirements.txt
CMD ["python3", "app.py"]