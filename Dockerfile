# Dockerfile for TMF Django App
FROM python:3.10

# Set environment variables
ENV POSTGRES_DB=tmf
ENV POSTGRES_USER=tmf_admin
ENV POSTGRES_PASSWORD=Alexander1377
ENV PYTHONUNBUFFERED=1

# Install PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set working directory in Render
WORKDIR /opt/render/project/src

# Copy backend directory contents
COPY backend/ .

# Install dependencies
# Make sure requirements.txt is present in the backend directory
RUN pip install --no-cache-dir -r requirements.txt

# Run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]