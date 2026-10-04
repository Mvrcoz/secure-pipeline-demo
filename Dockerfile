FROM python:3.12-slim

WORKDIR /app

# Run as non-root (Trivy config scan checks for this)
RUN useradd --create-home appuser
USER appuser

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "-m", "flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "8080"]
