FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir .

COPY sensei_service /app/sensei_service

EXPOSE 8000
CMD ["uvicorn", "sensei_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
