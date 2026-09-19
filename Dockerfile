FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends rclone gosu \
  && rm -rf /var/lib/apt/lists/* \
  && adduser --disabled-password --gecos "" --uid 1000 appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x docker-entrypoint.sh && mkdir -p /app/downloads && chown -R appuser:appuser /app
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "userbot_drive.py"]
