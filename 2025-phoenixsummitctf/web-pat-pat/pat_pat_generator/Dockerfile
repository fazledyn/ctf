FROM python:3.13.3-bookworm

# Install system dependencies
RUN apt update -y; apt install -y curl supervisor ghostscript

# Install Python dependencies
RUN pip install flask Pillow

# Switch working environment
WORKDIR /tmp

# Setup app
RUN mkdir -p /app
WORKDIR /app

# Backup application
RUN mkdir -p /var/backups/app
COPY challenge /var/backups/app

# Add application
COPY challenge .
RUN chown -R www-data:www-data /app

COPY flag.txt /flag.txt

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# copy run.sh
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]
