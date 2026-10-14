FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Django collectstatic ishlatish uchun
RUN python manage.py collectstatic --noinput

# port
EXPOSE 8010

# Production WSGI server
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8010", "--workers", "4"]