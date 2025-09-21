.SILENT:

# ➤ 📄 Экспорт зависимостей poetry в requirements.txt
req:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

# 🐍 Проверка кода по flake8
lint:
	flake8 app --max-line-length=79 && \
	echo "Lint: SUCCESS" || (echo "Lint: FAIL" && exit 1)

# 🧪 Запуск тестов
test:
	pytest app

# 🧪 ✚ 🐍 Запуск тестов и проверка кода по flake8 
lt:
	pytest app --disable-warnings -q --tb=no app && make lint