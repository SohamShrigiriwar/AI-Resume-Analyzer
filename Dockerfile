
FROM python:3.11-slim

WORKDIR /app

COPY resume_analyzer.py .

CMD ["python", "resume_analyzer.py"]
