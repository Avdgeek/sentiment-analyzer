from flask import Flask, request, jsonify, render_template  # <-- Добавил render_templat
from transformers import pipeline

# Инициализируем приложение Flask и модель
app = Flask(__name__)
# Загружаем готовую модель для анализа тональности
classifier = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")

@app.route('/')
def home():
       return render_template('index.html')

# Создаем endpoint (API точку) для анализа
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем JSON данные из запроса
        data = request.get_json()
        # Извлекаем текст из поля 'text'
        text = data['text']
        # Передаем текст модели для предсказания
        result = classifier(text)
        # Возвращаем результат в формате JSON
        return jsonify(result[0])
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
