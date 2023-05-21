FROM python:3.11.3-slim

# temporary dockerfile for development

ENV FLASK_APP=server.py
ENV FLASK_DEBUG=true

EXPOSE 9222
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9222"]