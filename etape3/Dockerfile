# etape 3 Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY creation_db.py .
COPY import_data_url.py .
COPY analyse_sql.py .
COPY main.py .
COPY requirements.txt .

# Install any needed packages specified in requirements.txt, in this case requests
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

