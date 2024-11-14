# Dockerfile for TMF Django App

# Use Python 3.10 as the base image
FROM python:3.10

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=tmf
ENV POSTGRES_USER=tmf_admin
ENV POSTGRES_PASSWORD=Alexander1377

# Install PostgreSQL client and dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set the working directory
WORKDIR /app/backend

# Copy requirements file and install dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Collect static files and apply migrations
RUN python manage.py collectstatic --noinput && \
    python manage.py migrate

# Run Django with Gunicorn in production
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000
