FROM python:3.11-slim

WORKDIR /app

# Установите системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Сначала установите setuptools и wheel
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы
COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
