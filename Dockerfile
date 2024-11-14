FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set working directory to Render's expected path
WORKDIR /opt/render/project/src
ENV PYTHONPATH="${PYTHONPATH}:/opt/render/project/src"


# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project directory
COPY . .

# Command to run
CMD ["gunicorn", "backend.backend.wsgi:application", "--bind", "0.0.0.0:$PORT"]
