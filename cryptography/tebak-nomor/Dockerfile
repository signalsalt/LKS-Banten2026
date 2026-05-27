FROM python:3.11-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY chall.py .

EXPOSE 9000

CMD ["socat", "TCP-LISTEN:9000,reuseaddr,fork", "EXEC:python3 /app/chall.py"]
