FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV PYTHONPATH=/opt/render/project/src/backend

# Set working directory to where manage.py is located
WORKDIR /opt/render/project/src/backend

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade --force-reinstall -r requirements.txt

# Copy the entire project into the container
COPY . .

# Command to run the application
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:$PORT"]
