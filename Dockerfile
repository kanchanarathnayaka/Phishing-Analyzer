FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group with a specific UID and GID
RUN groupadd -g 10001 appuser && useradd -u 10001 -g appuser -s /bin/sh appuser

# Set the appropriate permissions for the /app directory
RUN chown -R appuser:appuser /app

# Copy the FastAPI application code
COPY . .

# Change ownership of the copied files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER 10001

# Expose the port FastAPI is running on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
