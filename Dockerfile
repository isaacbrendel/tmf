# Dockerfile for TMF Django App
FROM python:3.10

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=tmf
ENV POSTGRES_USER=tmf_admin
ENV POSTGRES_PASSWORD=Alexander1377

# Install PostgreSQL client and dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set the working directory
WORKDIR /app

# Copy the entire backend directory
COPY backend/ .

# Install dependencies
RUN pip install -r requirements.txt

# Run Django with Gunicorn in production
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]