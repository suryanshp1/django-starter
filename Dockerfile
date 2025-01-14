FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements_dev.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements_dev.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh && chmod +x /app/entrypoint.sh

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]