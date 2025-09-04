FROM python:3.11-slim

WORKDIR /app

# Установите системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Сначала установите setuptools и wheel
RUN pip install --upgrade pip setuptools==70.0.0 wheel==0.43.0

# Скопируйте requirements и установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы приложения
COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
