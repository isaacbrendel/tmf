FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV PYTHONPATH=/opt/render/project/src/backend

# Set working directory
WORKDIR /opt/render/project/src/backend

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy requirements first (assuming it's in the project root)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade --force-reinstall -r requirements.txt

RUN ls -R /opt/render/project/src/backend


# Copy the entire project into the container
COPY . .

# Command to run
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:$PORT"]
