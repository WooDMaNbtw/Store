FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y gcc libc-dev build-essential libpq-dev

# Удаление ненужных пакетов
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set the working directory
WORKDIR /app

RUN pip install --upgrade pip

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY ./entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

COPY . /app

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
