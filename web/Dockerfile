FROM python:3.12.3-slim

RUN apt-get update -qq \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "app:app"]
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]