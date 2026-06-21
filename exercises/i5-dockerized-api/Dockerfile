FROM python:3.12-slim

WORKDIR /app
COPY b4-balance-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY b4-balance-api/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
